from flask import render_template, request, flash, redirect, url_for

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import TimeoutException
from ranking_articles import get_block_elements, get_citations, get_year_element, search_conference, get_contents_link

SCOPUS_API_KEY = "ce1da58cc35b89014c26ff7de31cca85"


# Inizializza un'istanza del driver Chrome con opzione headless
def init_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    return webdriver.Chrome(options=options)


# Cerca una conferenza su DBLP utilizzando Selenium
# Restituisce il contenuto della pagina della conferenza
def search_year(conference_year, driver):
    try:
        search_url = f"https://dblp.org/search?q=type%3AEditorship%3A%20year%3A{conference_year}%3A"
        driver.get(search_url)
        page_conferences = driver.page_source
        return page_conferences
    except TimeoutException:
        flash(f"Anno {conference_year} non trovato", "error")
        return None


def get_conference_title(page_conferences):
    soup = BeautifulSoup(page_conferences, 'html.parser')
    block_conf = soup.find_all("cite", attrs={'class': 'data tts-content'})[:10]
    conf_title_list = []
    for i in block_conf:
        title = i.find("span", attrs={"class": "title"})
        contents_line = i.find("a", {'class': 'toc-link'})
        conf_title_list.append((title, contents_line))
    return conf_title_list


def get_conference_hindex(block_elements_list):
    num_citazioni_list = []

    for block_elements in block_elements_list:
        for i in block_elements:
            # Itera sugli elementi invece di chiamare find_all
            for title_element in i.find_all("span", attrs={"class": "title"}):
                article_title = title_element.text.strip()
                numero_citazioni = get_citations(article_title)
                num_citazioni_list.append(int(numero_citazioni))

    num_citazioni_list.sort(reverse=True)
    hindex = calcola_h_index(num_citazioni_list)

    return hindex



def calcola_h_index(citazioni_per_articolo):
    citazioni_per_articolo.sort(reverse=True)
    h_index = 0
    for i, citazione in enumerate(citazioni_per_articolo, start=1):
        if i <= citazione:
            h_index = i
        else:
            break
    return h_index


def all_conference_index(driver, start_year, end_year, conference_titles):
    conferences_list = []

    for conference_title in conference_titles:
        block_element_list = []
        # Cerca le conferenze per l'anno specificato
        page_conference = search_conference(conference_title, driver)

        if page_conference:
            for conference_year in range(int(start_year), int(end_year) + 1):
                soup = BeautifulSoup(page_conference, "html.parser")
                # Ottieni i titoli delle conferenze
                year_element = get_year_element(soup, conference_year)

                if year_element is not None:
                    contents_page_source = get_contents_link(year_element, driver)

                    if contents_page_source is not None:
                        block_elements = get_block_elements(contents_page_source)
                        # h_index = get_conference_hindex(block_elements)
                        block_element_list.append(block_elements)
                     #   conferences_list.append((conference_title, block_element_list))

        conf_index = get_conference_hindex(block_element_list)
        conferences_list.append((conference_title, conf_index))
    return conferences_list


def setup_hindex_routes(app):
    @app.route('/search_hindex', methods=['GET'])
    def show_hindex():
        return render_template('h_index.html', result=None)

    @app.route('/h_index', methods=['POST'])
    def handle_hindex():
        start_year = request.form.get('start_year')
        end_year = request.form.get('end_year')
        conference_list = request.form.getlist('conference_list')

        if start_year and end_year and conference_list:
            driver = init_driver()

            try:
                conferences_list = all_conference_index(driver, start_year, end_year, conference_list)
                if conferences_list is not None:
                    return render_template('h_index.html', result=conferences_list)
            finally:
                driver.quit()
    # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_hindex'))