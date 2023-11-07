from flask import Flask, render_template, request
import requests
import re
from bs4 import BeautifulSoup


#app = Flask(__name__)


# La funzione ricerca la conferenza su DBLP
def cerca_conferenza(conference_query):
    pass


# Pagina iniziale con il form di ricerca per la conferenza specifica
#@app.route('/', methods=['GET', 'POST'])
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


#if __name__ == '__main__':
#app.run(debug=True)
# Esempio di utilizzo
nome_articolo = "Babbo Natale, Gesù Adulto. In cosa crede chi crede?"  # Inserisci il nome del tuo articolo
citazioni = trova_numero_citazioni_su_google_scholar(nome_articolo)
print(f"L'articolo '{nome_articolo}' ha {citazioni} citazioni su Google Scholar.")
