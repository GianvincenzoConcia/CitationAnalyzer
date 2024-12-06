from flask import render_template, request, redirect, url_for, flash

from bs4 import BeautifulSoup
from selenium import webdriver
from src.ranking_articles import get_block_elements, get_citations, search_conference, get_contents_link

# Inizializza un'istanza del driver Chrome con opzione headless
def init_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    return webdriver.Chrome(options=options)


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
                        block_element_list.append(block_elements)

        conf_index = get_conference_hindex(block_element_list)
        conferences_list.append((conference_title, conf_index))
    conferences_list.sort(reverse=True, key=lambda x: x[1])
    return conferences_list


def get_year_element(soup, conference_year):
    year_element = soup.find('span', {'itemprop': 'datePublished'},
                             string=lambda text: str(conference_year) in text)
    return year_element


def validate_years(start_year, end_year):
    if int(start_year) > int(end_year):
        flash(f"L'anno di inizio deve essere precedente all'anno di fine", 'error')
        return None


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
            validate_years(start_year, end_year)
            driver = init_driver()

            try:
                conferences_list = all_conference_index(driver, start_year, end_year, conference_list)
                if conferences_list is not None:
                    return render_template('h_index.html', result=conferences_list,
                                           start_year=start_year, end_year=end_year, conference_list=conference_list)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_hindex'))
