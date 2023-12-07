from bs4 import BeautifulSoup
from flask import render_template, request, redirect, url_for
from conf_hindex import validate_years

from ranking_articles import search_conference, get_year_element, get_contents_link, init_driver


def get_block_elements(contents_page_source):
    soup = BeautifulSoup(contents_page_source, "html.parser")
    blocks = soup.find_all("cite", attrs={"class": "data tts-content"})
    blocks = [blocks[i] for i in range(1, len(blocks))]
    return blocks


def get_authors(block_elements_list):
    author_list = []

    for block_element in block_elements_list:
        authors = block_element.find_all("span", attrs={"itemprop": "author"})
        authors = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
        author_list.append(authors)

    return author_list


def count_authors(author_list):
    authors = []
    for author in author_list:
        for a in author:
            authors.append(a)
    author_occurrences = {author: authors.count(author) for author in set(authors)}

    sorted_authors = sorted(author_occurrences.items(), key=lambda x: x[1], reverse=True)
    return sorted_authors


def get_author_usage(driver, start_year, end_year, conference_title):
    author_list = []

    page_conference = search_conference(conference_title, driver)
    if page_conference:
        for conference_year in range(int(start_year), int(end_year) + 1):
            soup = BeautifulSoup(page_conference, "html.parser")
            year_element = get_year_element(soup, conference_year)

            if year_element is not None:
                contents_page_source = get_contents_link(year_element, driver)

                if contents_page_source is not None:
                    block_elements = get_block_elements(contents_page_source)
                    for block_element in block_elements:
                        authors = block_element.find_all("span", attrs={"itemprop": "author"})
                        authors = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
                        author_list.append(authors)
    return count_authors(author_list)


def show_authcount():
    return render_template('authcount.html', result=None)

def handle_authcount():
    conference_title = request.form.get('conference_title')
    start_year = request.form.get('start_year')
    end_year = request.form.get('end_year')

    if conference_title and start_year and end_year:
        validate_years(start_year, end_year)
        driver = init_driver()
        try:
            authors_count = get_author_usage(driver, start_year, end_year, conference_title)
            if authors_count is not None:
                return render_template('authcount.html', result=authors_count,
                                       conference_title=conference_title, start_year=start_year, end_year=end_year)
        finally:
            driver.quit()
    return redirect(url_for('show_authcount'))

def setup_authcount_routes(app):
    @app.route('/search_authcount', methods=['GET'])
    def show_authcount_route():
        return show_authcount()

    @app.route('/authcount', methods=['POST'])
    def handle_authcount_route():
        return handle_authcount()