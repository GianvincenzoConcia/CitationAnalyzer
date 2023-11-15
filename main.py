import flask
from flask import Flask, render_template, request, flash, redirect, url_for
import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

app = Flask(__name__, template_folder='templates')
app.secret_key = 'il_tuo_segreto'  # Sostituisci con una chiave segreta più sicura


# La funzione ricerca la conferenza su DBLP e filtra per anno
def get_article_titles(conference_title, conference_year):
    # Utilizza Selenium per navigare su DBLP e ottenere il contenuto della pagina
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    try:
        search_url = f"https://dblp.org/search?q={conference_title}"
        driver.get(search_url)
        try:
            # Utilizza Selenium per navigare alla pagina della conferenza e ottenere il contenuto della pagina
            first_result = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'result-list')))
            first_result.click()
        except TimeoutException:
            flash(f"Conferenza {conference_title} non trovata", "error")
            return None

        # Ottieni il contenuto della pagina
        page_content = driver.page_source

        # Utilizza Beautiful Soup per analizzare il contenuto HTML
        soup = BeautifulSoup(page_content, 'html.parser')

        year_element = soup.find('span', {'itemprop': 'datePublished'},
                                 string=lambda text: str(conference_year) in text)

        if year_element:

            # Attende il caricamento della pagina
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@class="title"]')))

            # Trova il link contents dell'anno scelto
            contents_line = year_element.find_next('a', {'class': 'toc-link'})

            if contents_line:

                # Accede a contents
                driver.get(contents_line['href'])

                # Attendere che la pagina successiva si carichi completamente
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@class="title"]')))

                # Ottenere il nuovo HTML dopo il clic
                new_page_source = driver.page_source

                # Utilizza BeautifulSoup per analizzare il nuovo HTML
                soup = BeautifulSoup(new_page_source, 'html.parser')

                # Trova i titoli degli articoli utilizzando Beautiful Soup
                article_titles = [title.text.strip() for title in soup.find_all('span', class_='title')]

                return article_titles

            else:
                flash("Nessun articolo trovato", 'error')
                return None
        else:
            flash(f"Anno della conferenza {conference_year} non trovato.", 'error')
            return None
    except Exception as e:
        flash("Si è verificato un errore: " + str(e), 'error')
        return None
    finally:
        driver.quit()


@app.route('/')
def index():
    return render_template('interfaccia_web.html', result=None)


# Pagina iniziale con il form di ricerca per la conferenza specifica
@app.route('/search', methods=['POST'])
def search():
    if request.method == 'POST':
        conference_title = request.form['conference_title']
        conference_year = request.form['conference_year']

        # Ottieni i titoli degli articoli utilizzando Selenium e Beautiful Soup
        article_titles = get_article_titles(conference_title, conference_year)

        if article_titles is not None:
            return render_template('interfaccia_web.html', result=article_titles)
        else:
            return redirect(url_for('index'))


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
