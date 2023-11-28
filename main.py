from flask import Flask, render_template, request, flash, redirect, url_for
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

app = Flask(__name__, template_folder='templates')

SCOPUS_API_KEY = "ce1da58cc35b89014c26ff7de31cca85"


# Inizializza un'istanza del driver Chrome con opzione headless
def init_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    return webdriver.Chrome(options=options)


# Cerca una conferenza su DBLP utilizzando Selenium
# Restituisce il contenuto della pagina della conferenza
def search_conference(conference_title, driver):
    try:
        search_url = f"https://dblp.org/search?q={conference_title}"
        driver.get(search_url)

        first_result = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'result-list')))
        first_result.click()

        return driver.page_source
    except TimeoutException:
        flash(f"Conferenza {conference_title} non trovata", "error")
        return None


# Trova l'anno della conferenza
# Restituisce l'elemento dell'anno o None se non trovato
def get_year_element(soup, conference_year):
    year_element = soup.find('span', {'itemprop': 'datePublished'},
                             string=lambda text: str(conference_year) in text)

    if not year_element:
        flash(f"Anno della conferenza {conference_year} non trovato.", 'error')
        return None

    return year_element


# Entra nella pagina contents della conferenza che contiene gli articoli citati
# Restituisce il contenuto della pagina contents
def get_contents_link(year_element, driver):
    contents_line = year_element.find_next('a', {'class': 'toc-link'})
    if contents_line:
        try:
            driver.get(contents_line['href'])
            return driver.page_source
        except TimeoutException:
            flash("Timeout durante il caricamento della pagina dei contenuti", 'error')
            return None
    else:
        flash("Nessun articolo trovato", 'error')
        return None


def get_block_elements(page_source):
    soup = BeautifulSoup(page_source, 'html.parser')
    return soup.find_all("cite", attrs={"class": "data tts-content"})


# Restituisce i dati degli articoli con titolo, autori e numero di citazioni in ordine di numero
def get_article_data_list(block_elements):
    article_data_list = []

    for i in range(1, len(block_elements)):
        authors = block_elements[i].find_all("span", attrs={"itemprop": "author"})
        author_list = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
        article_title = block_elements[i].find("span", attrs={"class": "title"}).text.strip()
        numero_citazioni = get_citations(article_title)

        article_data_list.append((article_title, author_list, int(numero_citazioni)))

    article_data_list.sort(reverse=True, key=lambda x: x[2])
    return article_data_list


# Ottiene il numero di citazioni da Scopus per un determinato titolo dell'articolo.
def get_citations(article_title):
    try:
        # Esegui una ricerca su Scopus utilizzando la chiave API
        url = f'https://api.elsevier.com/content/search/scopus?query=TITLE("{article_title}")&apiKey={SCOPUS_API_KEY}'
        response = requests.get(url)
        data = response.json()

        # Estrai il numero di citazioni dall'output della ricerca
        if 'search-results' in data and 'entry' in data['search-results']:
            entry = data['search-results']['entry'][0]
            if 'citedby-count' in entry:
                return entry['citedby-count']
        return 0
    except Exception as e:
        print(f"Errore nel recuperare citazioni per '{article_title}' da Scopus: {str(e)}")
        return 0


@app.route('/')
def index():
    return render_template('interfaccia_web.html', result=None)


# Pagina iniziale con il form di ricerca per la conferenza specifica

@app.route('/search_classifica', methods=['GET'])
def show_classifica():
    return render_template('classifica.html', result=None)


@app.route('/classifica', methods=['POST'])
def handle_classifica():
    conference_title = request.form.get('conference_title')
    conference_year = request.form.get('conference_year')

    if conference_title and conference_year:
        driver = init_driver()

        try:
            page_source = search_conference(conference_title, driver)

            if page_source is not None:
                soup = BeautifulSoup(page_source, 'html.parser')
                year_element = get_year_element(soup, conference_year)

                if year_element is not None:
                    contents_page_source = get_contents_link(year_element, driver)

                    if contents_page_source is not None:
                        block_elements = get_block_elements(contents_page_source)
                        article_titles = get_article_data_list(block_elements)

                        if article_titles is not None:
                            return render_template('classifica.html', result=article_titles)
        finally:
            driver.quit()

    # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
    return redirect(url_for('show_classifica'))


# Avvio applicazione Flask usando il server web Waitress
if __name__ == '__main__':
    from waitress import serve

    serve(app, host="0.0.0.0", port=8080)
