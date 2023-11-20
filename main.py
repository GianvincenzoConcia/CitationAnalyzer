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
            first_result = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'result-list')))
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
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@class="title"]')))

                # Ottenere il nuovo HTML dopo il clic
                new_page_source = driver.page_source

                # Utilizza BeautifulSoup per analizzare il nuovo HTML
                soup = BeautifulSoup(new_page_source, 'html.parser')

                block_elements = soup.find_all("cite", attrs={"class": "data tts-content"})

                article_titles_list = []
                article_data_list = []

                for i in range(1, len(block_elements)):
                    authors = block_elements[i].find_all("span", attrs={"itemprop": "author"})
                    author_list = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
                    article_title = block_elements[i].find("span", attrs={"class": "title"}).text.strip()
                    numero_citazioni = get_citations(article_title)

                    article_titles_list.append(article_title)
                    article_data_list.append((article_title, author_list, numero_citazioni))

                return article_data_list

                # Trova i titoli degli articoli utilizzando Beautiful Soup
                # article_titles = [title.text.strip() for title in soup.find_all('span', class_='title')]
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


# Avvio applicazione Flask usando il server web Waitress
if __name__ == '__main__':
    from waitress import serve

    serve(app, host="0.0.0.0", port=8080)