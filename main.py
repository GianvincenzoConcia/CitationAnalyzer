from flask import Flask, render_template, request
import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

app = Flask(__name__, template_folder='templates')


# La funzione ricerca la conferenza su DBLP
def cerca_conferenza(conference_query):
    driver = webdriver.Chrome()  # Assicurati di avere ChromeDriver installato e il path corretto qui
    driver.get(f"https://dblp.org/search?q={conference_query}")

    try:
        # Trova e clicca sul primo risultato della ricerca, dopo aver atteso la presenza di un elemento cliccabile
        first_result = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'result-list')))
        first_result.click()
        conference_query = first_result.text.strip()

        # Ottieni il titolo dalla pagina del risultato
       # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'headline')))
       # conference_query = driver.find_element(By.CLASS_NAME, 'headline').text.strip()

        driver.quit()
        return conference_query

    except:
        driver.quit()
        return "Errore durante la ricerca della conferenza su DBLP"


# Pagina iniziale con il form di ricerca per la conferenza specifica
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        conference_query = request.form['conference_query']
        results = cerca_conferenza(conference_query)
        if results:
            return render_template('results.html', results=results)
        else:
            return "Errore nella ricerca della conferenza."
    return render_template('interfaccia_web.html')


def trova_numero_citazioni_su_google_scholar(nome_articolo):
    try:
        # Costruisci l'URL di Google Scholar per la ricerca dell'articolo
        ricerca_url = f"https://scholar.google.com/scholar?hl=en&q={nome_articolo}"

        # Esegui una richiesta HTTP per ottenere la pagina dei risultati di Google Scholar
        pagina = requests.get(ricerca_url)

        # Verifica se la richiesta ha avuto successo
        if pagina.status_code == 200:
            # Utilizza BeautifulSoup per analizzare la pagina HTML
            soup = BeautifulSoup(pagina.text, 'html.parser')

            # Trova l'elemento che contiene il numero di citazioni
            citazioni_element = soup.find('div', {"class": "gs_fl gs_flb"})

            # Estrai il numero di citazioni dall'elemento
            if citazioni_element:
                numero_citazioni = re.search(r"\d{1,}", citazioni_element.text).group()
                return numero_citazioni
            else:
                return "Citazioni non trovate"
        else:
            return "Errore nella richiesta HTTP"
    except Exception as e:
        return f"Si è verificato un errore: {str(e)}"

# Avvio applicazione Flask usando il server web Waitress
if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)


# Esempio di utilizzo
nome_articolo = "Babbo Natale, Gesù Adulto. In cosa crede chi crede?"  # Inserisci il nome del tuo articolo
citazioni = trova_numero_citazioni_su_google_scholar(nome_articolo)
print(f"L'articolo '{nome_articolo}' ha {citazioni} citazioni su Google Scholar.")
