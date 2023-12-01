from bs4 import BeautifulSoup

from ranking_articles import search_conference, get_year_element, get_contents_link, get_block_elements, init_driver


def get_author_usage(driver, start_year, end_year, conference_title):
    block_element_list = []

    page_conference = search_conference(conference_title, driver)
    if page_conference:
        for conference_year in range(int(start_year), int(end_year) + 1):
            soup = BeautifulSoup(page_conference, "html.parser")
            year_element = get_year_element(soup, conference_year)

            if year_element is not None:
                contents_page_source = get_contents_link(year_element, driver)

                if contents_page_source is not None:
                    block_elements = get_block_elements(contents_page_source)
                    block_element_list.append(block_elements)

        author_list = get_authors(block_element_list)
        print(count_authors(author_list))


def get_authors(block_elements_list):
    authors_list = []

    for block_elements in block_elements_list:
        for i in range(1, len(block_elements)):
            print(block_elements[i])
            # Itera sugli elementi invece di chiamare find_all
            for j in block_elements[i].find_all("span", attrs={"itemprop": "author"}):

                author_article = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in j]
                for author in author_article:
                    authors_list.append(author)
            #print(authors_list)
    return authors_list


def count_authors(author_list):
    author_occurrences = {author: author_list.count(author) for author in set(author_list)}

    return author_occurrences


get_author_usage(init_driver(), 2012, 2012, "3D Data Processing Visualization and Transmission")
