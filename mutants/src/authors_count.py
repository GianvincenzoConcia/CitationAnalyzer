
from inspect import signature as _mutmut_signature

def _mutmut_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result


from inspect import signature as _mutmut_signature

def _mutmut_yield_from_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result



from bs4 import BeautifulSoup
from flask import render_template, request, redirect, url_for

from src.conf_hindex import validate_years
from src.ranking_articles import search_conference, get_year_element, get_contents_link, init_driver

def x_get_block_elements__mutmut_orig(contents_page_source):
    soup = BeautifulSoup(contents_page_source, "html.parser")
    blocks = soup.find_all("cite", attrs={"class": "data tts-content"})
    blocks = blocks[1:]
    return blocks

def x_get_block_elements__mutmut_1(contents_page_source):
    soup = BeautifulSoup(None, "html.parser")
    blocks = soup.find_all("cite", attrs={"class": "data tts-content"})
    blocks = blocks[1:]
    return blocks

def x_get_block_elements__mutmut_2(contents_page_source):
    soup = BeautifulSoup(contents_page_source, "XXhtml.parserXX")
    blocks = soup.find_all("cite", attrs={"class": "data tts-content"})
    blocks = blocks[1:]
    return blocks

def x_get_block_elements__mutmut_3(contents_page_source):
    soup = BeautifulSoup( "html.parser")
    blocks = soup.find_all("cite", attrs={"class": "data tts-content"})
    blocks = blocks[1:]
    return blocks

def x_get_block_elements__mutmut_4(contents_page_source):
    soup = None
    blocks = soup.find_all("cite", attrs={"class": "data tts-content"})
    blocks = blocks[1:]
    return blocks

def x_get_block_elements__mutmut_5(contents_page_source):
    soup = BeautifulSoup(contents_page_source, "html.parser")
    blocks = soup.find_all("XXciteXX", attrs={"class": "data tts-content"})
    blocks = blocks[1:]
    return blocks

def x_get_block_elements__mutmut_6(contents_page_source):
    soup = BeautifulSoup(contents_page_source, "html.parser")
    blocks = soup.find_all("cite", attrs={"XXclassXX": "data tts-content"})
    blocks = blocks[1:]
    return blocks

def x_get_block_elements__mutmut_7(contents_page_source):
    soup = BeautifulSoup(contents_page_source, "html.parser")
    blocks = soup.find_all("cite", attrs={"class": "XXdata tts-contentXX"})
    blocks = blocks[1:]
    return blocks

def x_get_block_elements__mutmut_8(contents_page_source):
    soup = BeautifulSoup(contents_page_source, "html.parser")
    blocks = soup.find_all("cite",)
    blocks = blocks[1:]
    return blocks

def x_get_block_elements__mutmut_9(contents_page_source):
    soup = BeautifulSoup(contents_page_source, "html.parser")
    blocks = None
    blocks = blocks[1:]
    return blocks

def x_get_block_elements__mutmut_10(contents_page_source):
    soup = BeautifulSoup(contents_page_source, "html.parser")
    blocks = soup.find_all("cite", attrs={"class": "data tts-content"})
    blocks = blocks[2:]
    return blocks

def x_get_block_elements__mutmut_11(contents_page_source):
    soup = BeautifulSoup(contents_page_source, "html.parser")
    blocks = soup.find_all("cite", attrs={"class": "data tts-content"})
    blocks = blocks[None]
    return blocks

def x_get_block_elements__mutmut_12(contents_page_source):
    soup = BeautifulSoup(contents_page_source, "html.parser")
    blocks = soup.find_all("cite", attrs={"class": "data tts-content"})
    blocks = None
    return blocks

x_get_block_elements__mutmut_mutants = {
'x_get_block_elements__mutmut_1': x_get_block_elements__mutmut_1, 
    'x_get_block_elements__mutmut_2': x_get_block_elements__mutmut_2, 
    'x_get_block_elements__mutmut_3': x_get_block_elements__mutmut_3, 
    'x_get_block_elements__mutmut_4': x_get_block_elements__mutmut_4, 
    'x_get_block_elements__mutmut_5': x_get_block_elements__mutmut_5, 
    'x_get_block_elements__mutmut_6': x_get_block_elements__mutmut_6, 
    'x_get_block_elements__mutmut_7': x_get_block_elements__mutmut_7, 
    'x_get_block_elements__mutmut_8': x_get_block_elements__mutmut_8, 
    'x_get_block_elements__mutmut_9': x_get_block_elements__mutmut_9, 
    'x_get_block_elements__mutmut_10': x_get_block_elements__mutmut_10, 
    'x_get_block_elements__mutmut_11': x_get_block_elements__mutmut_11, 
    'x_get_block_elements__mutmut_12': x_get_block_elements__mutmut_12
}

def get_block_elements(*args, **kwargs):
    result = _mutmut_trampoline(x_get_block_elements__mutmut_orig, x_get_block_elements__mutmut_mutants, *args, **kwargs)
    return result 

get_block_elements.__signature__ = _mutmut_signature(x_get_block_elements__mutmut_orig)
x_get_block_elements__mutmut_orig.__name__ = 'x_get_block_elements'




def x_get_authors__mutmut_orig(block_elements_list):
    author_list = []

    for block_element in block_elements_list:
        authors = block_element.find_all("span", attrs={"itemprop": "author"})
        authors = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
        author_list.append(authors)

    return author_list


def x_get_authors__mutmut_1(block_elements_list):
    author_list = None

    for block_element in block_elements_list:
        authors = block_element.find_all("span", attrs={"itemprop": "author"})
        authors = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
        author_list.append(authors)

    return author_list


def x_get_authors__mutmut_2(block_elements_list):
    author_list = []

    for block_element in block_elements_list:
        authors = block_element.find_all("XXspanXX", attrs={"itemprop": "author"})
        authors = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
        author_list.append(authors)

    return author_list


def x_get_authors__mutmut_3(block_elements_list):
    author_list = []

    for block_element in block_elements_list:
        authors = block_element.find_all("span", attrs={"XXitempropXX": "author"})
        authors = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
        author_list.append(authors)

    return author_list


def x_get_authors__mutmut_4(block_elements_list):
    author_list = []

    for block_element in block_elements_list:
        authors = block_element.find_all("span", attrs={"itemprop": "XXauthorXX"})
        authors = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
        author_list.append(authors)

    return author_list


def x_get_authors__mutmut_5(block_elements_list):
    author_list = []

    for block_element in block_elements_list:
        authors = block_element.find_all("span",)
        authors = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
        author_list.append(authors)

    return author_list


def x_get_authors__mutmut_6(block_elements_list):
    author_list = []

    for block_element in block_elements_list:
        authors = None
        authors = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
        author_list.append(authors)

    return author_list


def x_get_authors__mutmut_7(block_elements_list):
    author_list = []

    for block_element in block_elements_list:
        authors = block_element.find_all("span", attrs={"itemprop": "author"})
        authors = [author.find("XXspanXX", attrs={"itemprop": "name"}).text.strip() for author in authors]
        author_list.append(authors)

    return author_list


def x_get_authors__mutmut_8(block_elements_list):
    author_list = []

    for block_element in block_elements_list:
        authors = block_element.find_all("span", attrs={"itemprop": "author"})
        authors = [author.find("span", attrs={"XXitempropXX": "name"}).text.strip() for author in authors]
        author_list.append(authors)

    return author_list


def x_get_authors__mutmut_9(block_elements_list):
    author_list = []

    for block_element in block_elements_list:
        authors = block_element.find_all("span", attrs={"itemprop": "author"})
        authors = [author.find("span", attrs={"itemprop": "XXnameXX"}).text.strip() for author in authors]
        author_list.append(authors)

    return author_list


def x_get_authors__mutmut_10(block_elements_list):
    author_list = []

    for block_element in block_elements_list:
        authors = block_element.find_all("span", attrs={"itemprop": "author"})
        authors = [author.find("span",).text.strip() for author in authors]
        author_list.append(authors)

    return author_list


def x_get_authors__mutmut_11(block_elements_list):
    author_list = []

    for block_element in block_elements_list:
        authors = block_element.find_all("span", attrs={"itemprop": "author"})
        authors = None
        author_list.append(authors)

    return author_list


def x_get_authors__mutmut_12(block_elements_list):
    author_list = []

    for block_element in block_elements_list:
        authors = block_element.find_all("span", attrs={"itemprop": "author"})
        authors = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
        author_list.append(None)

    return author_list

x_get_authors__mutmut_mutants = {
'x_get_authors__mutmut_1': x_get_authors__mutmut_1, 
    'x_get_authors__mutmut_2': x_get_authors__mutmut_2, 
    'x_get_authors__mutmut_3': x_get_authors__mutmut_3, 
    'x_get_authors__mutmut_4': x_get_authors__mutmut_4, 
    'x_get_authors__mutmut_5': x_get_authors__mutmut_5, 
    'x_get_authors__mutmut_6': x_get_authors__mutmut_6, 
    'x_get_authors__mutmut_7': x_get_authors__mutmut_7, 
    'x_get_authors__mutmut_8': x_get_authors__mutmut_8, 
    'x_get_authors__mutmut_9': x_get_authors__mutmut_9, 
    'x_get_authors__mutmut_10': x_get_authors__mutmut_10, 
    'x_get_authors__mutmut_11': x_get_authors__mutmut_11, 
    'x_get_authors__mutmut_12': x_get_authors__mutmut_12
}

def get_authors(*args, **kwargs):
    result = _mutmut_trampoline(x_get_authors__mutmut_orig, x_get_authors__mutmut_mutants, *args, **kwargs)
    return result 

get_authors.__signature__ = _mutmut_signature(x_get_authors__mutmut_orig)
x_get_authors__mutmut_orig.__name__ = 'x_get_authors'




def x_count_authors__mutmut_orig(author_list):
    authors = []
    for author in author_list:
        for a in author:
            authors.append(a)
    author_occurrences = {author: authors.count(author) for author in set(authors)}

    sorted_authors = sorted(author_occurrences.items(), key=lambda x: x[1], reverse=True)
    return sorted_authors


def x_count_authors__mutmut_1(author_list):
    authors = None
    for author in author_list:
        for a in author:
            authors.append(a)
    author_occurrences = {author: authors.count(author) for author in set(authors)}

    sorted_authors = sorted(author_occurrences.items(), key=lambda x: x[1], reverse=True)
    return sorted_authors


def x_count_authors__mutmut_2(author_list):
    authors = []
    for author in author_list:
        for a in author:
            authors.append(None)
    author_occurrences = {author: authors.count(author) for author in set(authors)}

    sorted_authors = sorted(author_occurrences.items(), key=lambda x: x[1], reverse=True)
    return sorted_authors


def x_count_authors__mutmut_3(author_list):
    authors = []
    for author in author_list:
        for a in author:
            authors.append(a)
    author_occurrences = {author: authors.count(None) for author in set(authors)}

    sorted_authors = sorted(author_occurrences.items(), key=lambda x: x[1], reverse=True)
    return sorted_authors


def x_count_authors__mutmut_4(author_list):
    authors = []
    for author in author_list:
        for a in author:
            authors.append(a)
    author_occurrences = {author: authors.count(author) for author in set(None)}

    sorted_authors = sorted(author_occurrences.items(), key=lambda x: x[1], reverse=True)
    return sorted_authors


def x_count_authors__mutmut_5(author_list):
    authors = []
    for author in author_list:
        for a in author:
            authors.append(a)
    author_occurrences = None

    sorted_authors = sorted(author_occurrences.items(), key=lambda x: x[1], reverse=True)
    return sorted_authors


def x_count_authors__mutmut_6(author_list):
    authors = []
    for author in author_list:
        for a in author:
            authors.append(a)
    author_occurrences = {author: authors.count(author) for author in set(authors)}

    sorted_authors = sorted(author_occurrences.items(), key=lambda x: x[2], reverse=True)
    return sorted_authors


def x_count_authors__mutmut_7(author_list):
    authors = []
    for author in author_list:
        for a in author:
            authors.append(a)
    author_occurrences = {author: authors.count(author) for author in set(authors)}

    sorted_authors = sorted(author_occurrences.items(), key=lambda x: x[None], reverse=True)
    return sorted_authors


def x_count_authors__mutmut_8(author_list):
    authors = []
    for author in author_list:
        for a in author:
            authors.append(a)
    author_occurrences = {author: authors.count(author) for author in set(authors)}

    sorted_authors = sorted(author_occurrences.items(), key=lambda x: None, reverse=True)
    return sorted_authors


def x_count_authors__mutmut_9(author_list):
    authors = []
    for author in author_list:
        for a in author:
            authors.append(a)
    author_occurrences = {author: authors.count(author) for author in set(authors)}

    sorted_authors = sorted(author_occurrences.items(), key=lambda x: x[1], reverse=False)
    return sorted_authors


def x_count_authors__mutmut_10(author_list):
    authors = []
    for author in author_list:
        for a in author:
            authors.append(a)
    author_occurrences = {author: authors.count(author) for author in set(authors)}

    sorted_authors = sorted(author_occurrences.items(), reverse=True)
    return sorted_authors


def x_count_authors__mutmut_11(author_list):
    authors = []
    for author in author_list:
        for a in author:
            authors.append(a)
    author_occurrences = {author: authors.count(author) for author in set(authors)}

    sorted_authors = sorted(author_occurrences.items(), key=lambda x: x[1],)
    return sorted_authors


def x_count_authors__mutmut_12(author_list):
    authors = []
    for author in author_list:
        for a in author:
            authors.append(a)
    author_occurrences = {author: authors.count(author) for author in set(authors)}

    sorted_authors = None
    return sorted_authors

x_count_authors__mutmut_mutants = {
'x_count_authors__mutmut_1': x_count_authors__mutmut_1, 
    'x_count_authors__mutmut_2': x_count_authors__mutmut_2, 
    'x_count_authors__mutmut_3': x_count_authors__mutmut_3, 
    'x_count_authors__mutmut_4': x_count_authors__mutmut_4, 
    'x_count_authors__mutmut_5': x_count_authors__mutmut_5, 
    'x_count_authors__mutmut_6': x_count_authors__mutmut_6, 
    'x_count_authors__mutmut_7': x_count_authors__mutmut_7, 
    'x_count_authors__mutmut_8': x_count_authors__mutmut_8, 
    'x_count_authors__mutmut_9': x_count_authors__mutmut_9, 
    'x_count_authors__mutmut_10': x_count_authors__mutmut_10, 
    'x_count_authors__mutmut_11': x_count_authors__mutmut_11, 
    'x_count_authors__mutmut_12': x_count_authors__mutmut_12
}

def count_authors(*args, **kwargs):
    result = _mutmut_trampoline(x_count_authors__mutmut_orig, x_count_authors__mutmut_mutants, *args, **kwargs)
    return result 

count_authors.__signature__ = _mutmut_signature(x_count_authors__mutmut_orig)
x_count_authors__mutmut_orig.__name__ = 'x_count_authors'




def x_get_author_usage__mutmut_orig(driver, start_year, end_year, conference_title):
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


def x_get_author_usage__mutmut_1(driver, start_year, end_year, conference_title):
    author_list = None

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


def x_get_author_usage__mutmut_2(driver, start_year, end_year, conference_title):
    author_list = []

    page_conference = search_conference(None, driver)
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


def x_get_author_usage__mutmut_3(driver, start_year, end_year, conference_title):
    author_list = []

    page_conference = search_conference(conference_title, None)
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


def x_get_author_usage__mutmut_4(driver, start_year, end_year, conference_title):
    author_list = []

    page_conference = search_conference( driver)
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


def x_get_author_usage__mutmut_5(driver, start_year, end_year, conference_title):
    author_list = []

    page_conference = search_conference(conference_title,)
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


def x_get_author_usage__mutmut_6(driver, start_year, end_year, conference_title):
    author_list = []

    page_conference = None
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


def x_get_author_usage__mutmut_7(driver, start_year, end_year, conference_title):
    author_list = []

    page_conference = search_conference(conference_title, driver)
    if page_conference:
        for conference_year in range(int(None), int(end_year) + 1):
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


def x_get_author_usage__mutmut_8(driver, start_year, end_year, conference_title):
    author_list = []

    page_conference = search_conference(conference_title, driver)
    if page_conference:
        for conference_year in range(int(start_year), int(None) + 1):
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


def x_get_author_usage__mutmut_9(driver, start_year, end_year, conference_title):
    author_list = []

    page_conference = search_conference(conference_title, driver)
    if page_conference:
        for conference_year in range(int(start_year), int(end_year) - 1):
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


def x_get_author_usage__mutmut_10(driver, start_year, end_year, conference_title):
    author_list = []

    page_conference = search_conference(conference_title, driver)
    if page_conference:
        for conference_year in range(int(start_year), int(end_year) + 2):
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


def x_get_author_usage__mutmut_11(driver, start_year, end_year, conference_title):
    author_list = []

    page_conference = search_conference(conference_title, driver)
    if page_conference:
        for conference_year in range(int(start_year), int(end_year) + 1):
            soup = BeautifulSoup(None, "html.parser")
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


def x_get_author_usage__mutmut_12(driver, start_year, end_year, conference_title):
    author_list = []

    page_conference = search_conference(conference_title, driver)
    if page_conference:
        for conference_year in range(int(start_year), int(end_year) + 1):
            soup = BeautifulSoup(page_conference, "XXhtml.parserXX")
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


def x_get_author_usage__mutmut_13(driver, start_year, end_year, conference_title):
    author_list = []

    page_conference = search_conference(conference_title, driver)
    if page_conference:
        for conference_year in range(int(start_year), int(end_year) + 1):
            soup = BeautifulSoup( "html.parser")
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


def x_get_author_usage__mutmut_14(driver, start_year, end_year, conference_title):
    author_list = []

    page_conference = search_conference(conference_title, driver)
    if page_conference:
        for conference_year in range(int(start_year), int(end_year) + 1):
            soup = None
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


def x_get_author_usage__mutmut_15(driver, start_year, end_year, conference_title):
    author_list = []

    page_conference = search_conference(conference_title, driver)
    if page_conference:
        for conference_year in range(int(start_year), int(end_year) + 1):
            soup = BeautifulSoup(page_conference, "html.parser")
            year_element = get_year_element(None, conference_year)

            if year_element is not None:
                contents_page_source = get_contents_link(year_element, driver)

                if contents_page_source is not None:
                    block_elements = get_block_elements(contents_page_source)
                    for block_element in block_elements:
                        authors = block_element.find_all("span", attrs={"itemprop": "author"})
                        authors = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
                        author_list.append(authors)
    return count_authors(author_list)


def x_get_author_usage__mutmut_16(driver, start_year, end_year, conference_title):
    author_list = []

    page_conference = search_conference(conference_title, driver)
    if page_conference:
        for conference_year in range(int(start_year), int(end_year) + 1):
            soup = BeautifulSoup(page_conference, "html.parser")
            year_element = get_year_element(soup, None)

            if year_element is not None:
                contents_page_source = get_contents_link(year_element, driver)

                if contents_page_source is not None:
                    block_elements = get_block_elements(contents_page_source)
                    for block_element in block_elements:
                        authors = block_element.find_all("span", attrs={"itemprop": "author"})
                        authors = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
                        author_list.append(authors)
    return count_authors(author_list)


def x_get_author_usage__mutmut_17(driver, start_year, end_year, conference_title):
    author_list = []

    page_conference = search_conference(conference_title, driver)
    if page_conference:
        for conference_year in range(int(start_year), int(end_year) + 1):
            soup = BeautifulSoup(page_conference, "html.parser")
            year_element = get_year_element( conference_year)

            if year_element is not None:
                contents_page_source = get_contents_link(year_element, driver)

                if contents_page_source is not None:
                    block_elements = get_block_elements(contents_page_source)
                    for block_element in block_elements:
                        authors = block_element.find_all("span", attrs={"itemprop": "author"})
                        authors = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
                        author_list.append(authors)
    return count_authors(author_list)


def x_get_author_usage__mutmut_18(driver, start_year, end_year, conference_title):
    author_list = []

    page_conference = search_conference(conference_title, driver)
    if page_conference:
        for conference_year in range(int(start_year), int(end_year) + 1):
            soup = BeautifulSoup(page_conference, "html.parser")
            year_element = get_year_element(soup,)

            if year_element is not None:
                contents_page_source = get_contents_link(year_element, driver)

                if contents_page_source is not None:
                    block_elements = get_block_elements(contents_page_source)
                    for block_element in block_elements:
                        authors = block_element.find_all("span", attrs={"itemprop": "author"})
                        authors = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
                        author_list.append(authors)
    return count_authors(author_list)


def x_get_author_usage__mutmut_19(driver, start_year, end_year, conference_title):
    author_list = []

    page_conference = search_conference(conference_title, driver)
    if page_conference:
        for conference_year in range(int(start_year), int(end_year) + 1):
            soup = BeautifulSoup(page_conference, "html.parser")
            year_element = None

            if year_element is not None:
                contents_page_source = get_contents_link(year_element, driver)

                if contents_page_source is not None:
                    block_elements = get_block_elements(contents_page_source)
                    for block_element in block_elements:
                        authors = block_element.find_all("span", attrs={"itemprop": "author"})
                        authors = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
                        author_list.append(authors)
    return count_authors(author_list)


def x_get_author_usage__mutmut_20(driver, start_year, end_year, conference_title):
    author_list = []

    page_conference = search_conference(conference_title, driver)
    if page_conference:
        for conference_year in range(int(start_year), int(end_year) + 1):
            soup = BeautifulSoup(page_conference, "html.parser")
            year_element = get_year_element(soup, conference_year)

            if year_element is  None:
                contents_page_source = get_contents_link(year_element, driver)

                if contents_page_source is not None:
                    block_elements = get_block_elements(contents_page_source)
                    for block_element in block_elements:
                        authors = block_element.find_all("span", attrs={"itemprop": "author"})
                        authors = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
                        author_list.append(authors)
    return count_authors(author_list)


def x_get_author_usage__mutmut_21(driver, start_year, end_year, conference_title):
    author_list = []

    page_conference = search_conference(conference_title, driver)
    if page_conference:
        for conference_year in range(int(start_year), int(end_year) + 1):
            soup = BeautifulSoup(page_conference, "html.parser")
            year_element = get_year_element(soup, conference_year)

            if year_element is not None:
                contents_page_source = get_contents_link(None, driver)

                if contents_page_source is not None:
                    block_elements = get_block_elements(contents_page_source)
                    for block_element in block_elements:
                        authors = block_element.find_all("span", attrs={"itemprop": "author"})
                        authors = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
                        author_list.append(authors)
    return count_authors(author_list)


def x_get_author_usage__mutmut_22(driver, start_year, end_year, conference_title):
    author_list = []

    page_conference = search_conference(conference_title, driver)
    if page_conference:
        for conference_year in range(int(start_year), int(end_year) + 1):
            soup = BeautifulSoup(page_conference, "html.parser")
            year_element = get_year_element(soup, conference_year)

            if year_element is not None:
                contents_page_source = get_contents_link(year_element, None)

                if contents_page_source is not None:
                    block_elements = get_block_elements(contents_page_source)
                    for block_element in block_elements:
                        authors = block_element.find_all("span", attrs={"itemprop": "author"})
                        authors = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
                        author_list.append(authors)
    return count_authors(author_list)


def x_get_author_usage__mutmut_23(driver, start_year, end_year, conference_title):
    author_list = []

    page_conference = search_conference(conference_title, driver)
    if page_conference:
        for conference_year in range(int(start_year), int(end_year) + 1):
            soup = BeautifulSoup(page_conference, "html.parser")
            year_element = get_year_element(soup, conference_year)

            if year_element is not None:
                contents_page_source = get_contents_link( driver)

                if contents_page_source is not None:
                    block_elements = get_block_elements(contents_page_source)
                    for block_element in block_elements:
                        authors = block_element.find_all("span", attrs={"itemprop": "author"})
                        authors = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
                        author_list.append(authors)
    return count_authors(author_list)


def x_get_author_usage__mutmut_24(driver, start_year, end_year, conference_title):
    author_list = []

    page_conference = search_conference(conference_title, driver)
    if page_conference:
        for conference_year in range(int(start_year), int(end_year) + 1):
            soup = BeautifulSoup(page_conference, "html.parser")
            year_element = get_year_element(soup, conference_year)

            if year_element is not None:
                contents_page_source = get_contents_link(year_element,)

                if contents_page_source is not None:
                    block_elements = get_block_elements(contents_page_source)
                    for block_element in block_elements:
                        authors = block_element.find_all("span", attrs={"itemprop": "author"})
                        authors = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
                        author_list.append(authors)
    return count_authors(author_list)


def x_get_author_usage__mutmut_25(driver, start_year, end_year, conference_title):
    author_list = []

    page_conference = search_conference(conference_title, driver)
    if page_conference:
        for conference_year in range(int(start_year), int(end_year) + 1):
            soup = BeautifulSoup(page_conference, "html.parser")
            year_element = get_year_element(soup, conference_year)

            if year_element is not None:
                contents_page_source = None

                if contents_page_source is not None:
                    block_elements = get_block_elements(contents_page_source)
                    for block_element in block_elements:
                        authors = block_element.find_all("span", attrs={"itemprop": "author"})
                        authors = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
                        author_list.append(authors)
    return count_authors(author_list)


def x_get_author_usage__mutmut_26(driver, start_year, end_year, conference_title):
    author_list = []

    page_conference = search_conference(conference_title, driver)
    if page_conference:
        for conference_year in range(int(start_year), int(end_year) + 1):
            soup = BeautifulSoup(page_conference, "html.parser")
            year_element = get_year_element(soup, conference_year)

            if year_element is not None:
                contents_page_source = get_contents_link(year_element, driver)

                if contents_page_source is  None:
                    block_elements = get_block_elements(contents_page_source)
                    for block_element in block_elements:
                        authors = block_element.find_all("span", attrs={"itemprop": "author"})
                        authors = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
                        author_list.append(authors)
    return count_authors(author_list)


def x_get_author_usage__mutmut_27(driver, start_year, end_year, conference_title):
    author_list = []

    page_conference = search_conference(conference_title, driver)
    if page_conference:
        for conference_year in range(int(start_year), int(end_year) + 1):
            soup = BeautifulSoup(page_conference, "html.parser")
            year_element = get_year_element(soup, conference_year)

            if year_element is not None:
                contents_page_source = get_contents_link(year_element, driver)

                if contents_page_source is not None:
                    block_elements = get_block_elements(None)
                    for block_element in block_elements:
                        authors = block_element.find_all("span", attrs={"itemprop": "author"})
                        authors = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
                        author_list.append(authors)
    return count_authors(author_list)


def x_get_author_usage__mutmut_28(driver, start_year, end_year, conference_title):
    author_list = []

    page_conference = search_conference(conference_title, driver)
    if page_conference:
        for conference_year in range(int(start_year), int(end_year) + 1):
            soup = BeautifulSoup(page_conference, "html.parser")
            year_element = get_year_element(soup, conference_year)

            if year_element is not None:
                contents_page_source = get_contents_link(year_element, driver)

                if contents_page_source is not None:
                    block_elements = None
                    for block_element in block_elements:
                        authors = block_element.find_all("span", attrs={"itemprop": "author"})
                        authors = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
                        author_list.append(authors)
    return count_authors(author_list)


def x_get_author_usage__mutmut_29(driver, start_year, end_year, conference_title):
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
                        authors = block_element.find_all("XXspanXX", attrs={"itemprop": "author"})
                        authors = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
                        author_list.append(authors)
    return count_authors(author_list)


def x_get_author_usage__mutmut_30(driver, start_year, end_year, conference_title):
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
                        authors = block_element.find_all("span", attrs={"XXitempropXX": "author"})
                        authors = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
                        author_list.append(authors)
    return count_authors(author_list)


def x_get_author_usage__mutmut_31(driver, start_year, end_year, conference_title):
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
                        authors = block_element.find_all("span", attrs={"itemprop": "XXauthorXX"})
                        authors = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
                        author_list.append(authors)
    return count_authors(author_list)


def x_get_author_usage__mutmut_32(driver, start_year, end_year, conference_title):
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
                        authors = block_element.find_all("span",)
                        authors = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
                        author_list.append(authors)
    return count_authors(author_list)


def x_get_author_usage__mutmut_33(driver, start_year, end_year, conference_title):
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
                        authors = None
                        authors = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
                        author_list.append(authors)
    return count_authors(author_list)


def x_get_author_usage__mutmut_34(driver, start_year, end_year, conference_title):
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
                        authors = [author.find("XXspanXX", attrs={"itemprop": "name"}).text.strip() for author in authors]
                        author_list.append(authors)
    return count_authors(author_list)


def x_get_author_usage__mutmut_35(driver, start_year, end_year, conference_title):
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
                        authors = [author.find("span", attrs={"XXitempropXX": "name"}).text.strip() for author in authors]
                        author_list.append(authors)
    return count_authors(author_list)


def x_get_author_usage__mutmut_36(driver, start_year, end_year, conference_title):
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
                        authors = [author.find("span", attrs={"itemprop": "XXnameXX"}).text.strip() for author in authors]
                        author_list.append(authors)
    return count_authors(author_list)


def x_get_author_usage__mutmut_37(driver, start_year, end_year, conference_title):
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
                        authors = [author.find("span",).text.strip() for author in authors]
                        author_list.append(authors)
    return count_authors(author_list)


def x_get_author_usage__mutmut_38(driver, start_year, end_year, conference_title):
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
                        authors = None
                        author_list.append(authors)
    return count_authors(author_list)


def x_get_author_usage__mutmut_39(driver, start_year, end_year, conference_title):
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
                        author_list.append(None)
    return count_authors(author_list)


def x_get_author_usage__mutmut_40(driver, start_year, end_year, conference_title):
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
    return count_authors(None)

x_get_author_usage__mutmut_mutants = {
'x_get_author_usage__mutmut_1': x_get_author_usage__mutmut_1, 
    'x_get_author_usage__mutmut_2': x_get_author_usage__mutmut_2, 
    'x_get_author_usage__mutmut_3': x_get_author_usage__mutmut_3, 
    'x_get_author_usage__mutmut_4': x_get_author_usage__mutmut_4, 
    'x_get_author_usage__mutmut_5': x_get_author_usage__mutmut_5, 
    'x_get_author_usage__mutmut_6': x_get_author_usage__mutmut_6, 
    'x_get_author_usage__mutmut_7': x_get_author_usage__mutmut_7, 
    'x_get_author_usage__mutmut_8': x_get_author_usage__mutmut_8, 
    'x_get_author_usage__mutmut_9': x_get_author_usage__mutmut_9, 
    'x_get_author_usage__mutmut_10': x_get_author_usage__mutmut_10, 
    'x_get_author_usage__mutmut_11': x_get_author_usage__mutmut_11, 
    'x_get_author_usage__mutmut_12': x_get_author_usage__mutmut_12, 
    'x_get_author_usage__mutmut_13': x_get_author_usage__mutmut_13, 
    'x_get_author_usage__mutmut_14': x_get_author_usage__mutmut_14, 
    'x_get_author_usage__mutmut_15': x_get_author_usage__mutmut_15, 
    'x_get_author_usage__mutmut_16': x_get_author_usage__mutmut_16, 
    'x_get_author_usage__mutmut_17': x_get_author_usage__mutmut_17, 
    'x_get_author_usage__mutmut_18': x_get_author_usage__mutmut_18, 
    'x_get_author_usage__mutmut_19': x_get_author_usage__mutmut_19, 
    'x_get_author_usage__mutmut_20': x_get_author_usage__mutmut_20, 
    'x_get_author_usage__mutmut_21': x_get_author_usage__mutmut_21, 
    'x_get_author_usage__mutmut_22': x_get_author_usage__mutmut_22, 
    'x_get_author_usage__mutmut_23': x_get_author_usage__mutmut_23, 
    'x_get_author_usage__mutmut_24': x_get_author_usage__mutmut_24, 
    'x_get_author_usage__mutmut_25': x_get_author_usage__mutmut_25, 
    'x_get_author_usage__mutmut_26': x_get_author_usage__mutmut_26, 
    'x_get_author_usage__mutmut_27': x_get_author_usage__mutmut_27, 
    'x_get_author_usage__mutmut_28': x_get_author_usage__mutmut_28, 
    'x_get_author_usage__mutmut_29': x_get_author_usage__mutmut_29, 
    'x_get_author_usage__mutmut_30': x_get_author_usage__mutmut_30, 
    'x_get_author_usage__mutmut_31': x_get_author_usage__mutmut_31, 
    'x_get_author_usage__mutmut_32': x_get_author_usage__mutmut_32, 
    'x_get_author_usage__mutmut_33': x_get_author_usage__mutmut_33, 
    'x_get_author_usage__mutmut_34': x_get_author_usage__mutmut_34, 
    'x_get_author_usage__mutmut_35': x_get_author_usage__mutmut_35, 
    'x_get_author_usage__mutmut_36': x_get_author_usage__mutmut_36, 
    'x_get_author_usage__mutmut_37': x_get_author_usage__mutmut_37, 
    'x_get_author_usage__mutmut_38': x_get_author_usage__mutmut_38, 
    'x_get_author_usage__mutmut_39': x_get_author_usage__mutmut_39, 
    'x_get_author_usage__mutmut_40': x_get_author_usage__mutmut_40
}

def get_author_usage(*args, **kwargs):
    result = _mutmut_trampoline(x_get_author_usage__mutmut_orig, x_get_author_usage__mutmut_mutants, *args, **kwargs)
    return result 

get_author_usage.__signature__ = _mutmut_signature(x_get_author_usage__mutmut_orig)
x_get_author_usage__mutmut_orig.__name__ = 'x_get_author_usage'




def x_show_authcount__mutmut_orig():
    return render_template('authcount.html', result=None)


def x_show_authcount__mutmut_1():
    return render_template('XXauthcount.htmlXX', result=None)


def x_show_authcount__mutmut_2():
    return render_template('authcount.html',)

x_show_authcount__mutmut_mutants = {
'x_show_authcount__mutmut_1': x_show_authcount__mutmut_1, 
    'x_show_authcount__mutmut_2': x_show_authcount__mutmut_2
}

def show_authcount(*args, **kwargs):
    result = _mutmut_trampoline(x_show_authcount__mutmut_orig, x_show_authcount__mutmut_mutants, *args, **kwargs)
    return result 

show_authcount.__signature__ = _mutmut_signature(x_show_authcount__mutmut_orig)
x_show_authcount__mutmut_orig.__name__ = 'x_show_authcount'




def x_handle_authcount__mutmut_orig():
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


def x_handle_authcount__mutmut_1():
    conference_title = request.form.get('XXconference_titleXX')
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


def x_handle_authcount__mutmut_2():
    conference_title = None
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


def x_handle_authcount__mutmut_3():
    conference_title = request.form.get('conference_title')
    start_year = request.form.get('XXstart_yearXX')
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


def x_handle_authcount__mutmut_4():
    conference_title = request.form.get('conference_title')
    start_year = None
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


def x_handle_authcount__mutmut_5():
    conference_title = request.form.get('conference_title')
    start_year = request.form.get('start_year')
    end_year = request.form.get('XXend_yearXX')

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


def x_handle_authcount__mutmut_6():
    conference_title = request.form.get('conference_title')
    start_year = request.form.get('start_year')
    end_year = None

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


def x_handle_authcount__mutmut_7():
    conference_title = request.form.get('conference_title')
    start_year = request.form.get('start_year')
    end_year = request.form.get('end_year')

    if conference_title or start_year and end_year:
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


def x_handle_authcount__mutmut_8():
    conference_title = request.form.get('conference_title')
    start_year = request.form.get('start_year')
    end_year = request.form.get('end_year')

    if conference_title and start_year and end_year:
        validate_years(None, end_year)
        driver = init_driver()
        try:
            authors_count = get_author_usage(driver, start_year, end_year, conference_title)
            if authors_count is not None:
                return render_template('authcount.html', result=authors_count,
                                       conference_title=conference_title, start_year=start_year, end_year=end_year)
        finally:
            driver.quit()
    return redirect(url_for('show_authcount'))


def x_handle_authcount__mutmut_9():
    conference_title = request.form.get('conference_title')
    start_year = request.form.get('start_year')
    end_year = request.form.get('end_year')

    if conference_title and start_year and end_year:
        validate_years(start_year, None)
        driver = init_driver()
        try:
            authors_count = get_author_usage(driver, start_year, end_year, conference_title)
            if authors_count is not None:
                return render_template('authcount.html', result=authors_count,
                                       conference_title=conference_title, start_year=start_year, end_year=end_year)
        finally:
            driver.quit()
    return redirect(url_for('show_authcount'))


def x_handle_authcount__mutmut_10():
    conference_title = request.form.get('conference_title')
    start_year = request.form.get('start_year')
    end_year = request.form.get('end_year')

    if conference_title and start_year and end_year:
        validate_years( end_year)
        driver = init_driver()
        try:
            authors_count = get_author_usage(driver, start_year, end_year, conference_title)
            if authors_count is not None:
                return render_template('authcount.html', result=authors_count,
                                       conference_title=conference_title, start_year=start_year, end_year=end_year)
        finally:
            driver.quit()
    return redirect(url_for('show_authcount'))


def x_handle_authcount__mutmut_11():
    conference_title = request.form.get('conference_title')
    start_year = request.form.get('start_year')
    end_year = request.form.get('end_year')

    if conference_title and start_year and end_year:
        validate_years(start_year,)
        driver = init_driver()
        try:
            authors_count = get_author_usage(driver, start_year, end_year, conference_title)
            if authors_count is not None:
                return render_template('authcount.html', result=authors_count,
                                       conference_title=conference_title, start_year=start_year, end_year=end_year)
        finally:
            driver.quit()
    return redirect(url_for('show_authcount'))


def x_handle_authcount__mutmut_12():
    conference_title = request.form.get('conference_title')
    start_year = request.form.get('start_year')
    end_year = request.form.get('end_year')

    if conference_title and start_year and end_year:
        validate_years(start_year, end_year)
        driver = None
        try:
            authors_count = get_author_usage(driver, start_year, end_year, conference_title)
            if authors_count is not None:
                return render_template('authcount.html', result=authors_count,
                                       conference_title=conference_title, start_year=start_year, end_year=end_year)
        finally:
            driver.quit()
    return redirect(url_for('show_authcount'))


def x_handle_authcount__mutmut_13():
    conference_title = request.form.get('conference_title')
    start_year = request.form.get('start_year')
    end_year = request.form.get('end_year')

    if conference_title and start_year and end_year:
        validate_years(start_year, end_year)
        driver = init_driver()
        try:
            authors_count = get_author_usage(None, start_year, end_year, conference_title)
            if authors_count is not None:
                return render_template('authcount.html', result=authors_count,
                                       conference_title=conference_title, start_year=start_year, end_year=end_year)
        finally:
            driver.quit()
    return redirect(url_for('show_authcount'))


def x_handle_authcount__mutmut_14():
    conference_title = request.form.get('conference_title')
    start_year = request.form.get('start_year')
    end_year = request.form.get('end_year')

    if conference_title and start_year and end_year:
        validate_years(start_year, end_year)
        driver = init_driver()
        try:
            authors_count = get_author_usage(driver, None, end_year, conference_title)
            if authors_count is not None:
                return render_template('authcount.html', result=authors_count,
                                       conference_title=conference_title, start_year=start_year, end_year=end_year)
        finally:
            driver.quit()
    return redirect(url_for('show_authcount'))


def x_handle_authcount__mutmut_15():
    conference_title = request.form.get('conference_title')
    start_year = request.form.get('start_year')
    end_year = request.form.get('end_year')

    if conference_title and start_year and end_year:
        validate_years(start_year, end_year)
        driver = init_driver()
        try:
            authors_count = get_author_usage(driver, start_year, None, conference_title)
            if authors_count is not None:
                return render_template('authcount.html', result=authors_count,
                                       conference_title=conference_title, start_year=start_year, end_year=end_year)
        finally:
            driver.quit()
    return redirect(url_for('show_authcount'))


def x_handle_authcount__mutmut_16():
    conference_title = request.form.get('conference_title')
    start_year = request.form.get('start_year')
    end_year = request.form.get('end_year')

    if conference_title and start_year and end_year:
        validate_years(start_year, end_year)
        driver = init_driver()
        try:
            authors_count = get_author_usage(driver, start_year, end_year, None)
            if authors_count is not None:
                return render_template('authcount.html', result=authors_count,
                                       conference_title=conference_title, start_year=start_year, end_year=end_year)
        finally:
            driver.quit()
    return redirect(url_for('show_authcount'))


def x_handle_authcount__mutmut_17():
    conference_title = request.form.get('conference_title')
    start_year = request.form.get('start_year')
    end_year = request.form.get('end_year')

    if conference_title and start_year and end_year:
        validate_years(start_year, end_year)
        driver = init_driver()
        try:
            authors_count = get_author_usage( start_year, end_year, conference_title)
            if authors_count is not None:
                return render_template('authcount.html', result=authors_count,
                                       conference_title=conference_title, start_year=start_year, end_year=end_year)
        finally:
            driver.quit()
    return redirect(url_for('show_authcount'))


def x_handle_authcount__mutmut_18():
    conference_title = request.form.get('conference_title')
    start_year = request.form.get('start_year')
    end_year = request.form.get('end_year')

    if conference_title and start_year and end_year:
        validate_years(start_year, end_year)
        driver = init_driver()
        try:
            authors_count = get_author_usage(driver, end_year, conference_title)
            if authors_count is not None:
                return render_template('authcount.html', result=authors_count,
                                       conference_title=conference_title, start_year=start_year, end_year=end_year)
        finally:
            driver.quit()
    return redirect(url_for('show_authcount'))


def x_handle_authcount__mutmut_19():
    conference_title = request.form.get('conference_title')
    start_year = request.form.get('start_year')
    end_year = request.form.get('end_year')

    if conference_title and start_year and end_year:
        validate_years(start_year, end_year)
        driver = init_driver()
        try:
            authors_count = get_author_usage(driver, start_year, conference_title)
            if authors_count is not None:
                return render_template('authcount.html', result=authors_count,
                                       conference_title=conference_title, start_year=start_year, end_year=end_year)
        finally:
            driver.quit()
    return redirect(url_for('show_authcount'))


def x_handle_authcount__mutmut_20():
    conference_title = request.form.get('conference_title')
    start_year = request.form.get('start_year')
    end_year = request.form.get('end_year')

    if conference_title and start_year and end_year:
        validate_years(start_year, end_year)
        driver = init_driver()
        try:
            authors_count = get_author_usage(driver, start_year, end_year,)
            if authors_count is not None:
                return render_template('authcount.html', result=authors_count,
                                       conference_title=conference_title, start_year=start_year, end_year=end_year)
        finally:
            driver.quit()
    return redirect(url_for('show_authcount'))


def x_handle_authcount__mutmut_21():
    conference_title = request.form.get('conference_title')
    start_year = request.form.get('start_year')
    end_year = request.form.get('end_year')

    if conference_title and start_year and end_year:
        validate_years(start_year, end_year)
        driver = init_driver()
        try:
            authors_count = None
            if authors_count is not None:
                return render_template('authcount.html', result=authors_count,
                                       conference_title=conference_title, start_year=start_year, end_year=end_year)
        finally:
            driver.quit()
    return redirect(url_for('show_authcount'))


def x_handle_authcount__mutmut_22():
    conference_title = request.form.get('conference_title')
    start_year = request.form.get('start_year')
    end_year = request.form.get('end_year')

    if conference_title and start_year and end_year:
        validate_years(start_year, end_year)
        driver = init_driver()
        try:
            authors_count = get_author_usage(driver, start_year, end_year, conference_title)
            if authors_count is  None:
                return render_template('authcount.html', result=authors_count,
                                       conference_title=conference_title, start_year=start_year, end_year=end_year)
        finally:
            driver.quit()
    return redirect(url_for('show_authcount'))


def x_handle_authcount__mutmut_23():
    conference_title = request.form.get('conference_title')
    start_year = request.form.get('start_year')
    end_year = request.form.get('end_year')

    if conference_title and start_year and end_year:
        validate_years(start_year, end_year)
        driver = init_driver()
        try:
            authors_count = get_author_usage(driver, start_year, end_year, conference_title)
            if authors_count is not None:
                return render_template('XXauthcount.htmlXX', result=authors_count,
                                       conference_title=conference_title, start_year=start_year, end_year=end_year)
        finally:
            driver.quit()
    return redirect(url_for('show_authcount'))


def x_handle_authcount__mutmut_24():
    conference_title = request.form.get('conference_title')
    start_year = request.form.get('start_year')
    end_year = request.form.get('end_year')

    if conference_title and start_year and end_year:
        validate_years(start_year, end_year)
        driver = init_driver()
        try:
            authors_count = get_author_usage(driver, start_year, end_year, conference_title)
            if authors_count is not None:
                return render_template('authcount.html', result=None,
                                       conference_title=conference_title, start_year=start_year, end_year=end_year)
        finally:
            driver.quit()
    return redirect(url_for('show_authcount'))


def x_handle_authcount__mutmut_25():
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
                                       conference_title=None, start_year=start_year, end_year=end_year)
        finally:
            driver.quit()
    return redirect(url_for('show_authcount'))


def x_handle_authcount__mutmut_26():
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
                                       conference_title=conference_title, start_year=None, end_year=end_year)
        finally:
            driver.quit()
    return redirect(url_for('show_authcount'))


def x_handle_authcount__mutmut_27():
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
                                       conference_title=conference_title, start_year=start_year, end_year=None)
        finally:
            driver.quit()
    return redirect(url_for('show_authcount'))


def x_handle_authcount__mutmut_28():
    conference_title = request.form.get('conference_title')
    start_year = request.form.get('start_year')
    end_year = request.form.get('end_year')

    if conference_title and start_year and end_year:
        validate_years(start_year, end_year)
        driver = init_driver()
        try:
            authors_count = get_author_usage(driver, start_year, end_year, conference_title)
            if authors_count is not None:
                return render_template('authcount.html',
                                       conference_title=conference_title, start_year=start_year, end_year=end_year)
        finally:
            driver.quit()
    return redirect(url_for('show_authcount'))


def x_handle_authcount__mutmut_29():
    conference_title = request.form.get('conference_title')
    start_year = request.form.get('start_year')
    end_year = request.form.get('end_year')

    if conference_title and start_year and end_year:
        validate_years(start_year, end_year)
        driver = init_driver()
        try:
            authors_count = get_author_usage(driver, start_year, end_year, conference_title)
            if authors_count is not None:
                return render_template('authcount.html', result=authors_count, start_year=start_year, end_year=end_year)
        finally:
            driver.quit()
    return redirect(url_for('show_authcount'))


def x_handle_authcount__mutmut_30():
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
                                       conference_title=conference_title, end_year=end_year)
        finally:
            driver.quit()
    return redirect(url_for('show_authcount'))


def x_handle_authcount__mutmut_31():
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
                                       conference_title=conference_title, start_year=start_year,)
        finally:
            driver.quit()
    return redirect(url_for('show_authcount'))


def x_handle_authcount__mutmut_32():
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
    return redirect(url_for('XXshow_authcountXX'))

x_handle_authcount__mutmut_mutants = {
'x_handle_authcount__mutmut_1': x_handle_authcount__mutmut_1, 
    'x_handle_authcount__mutmut_2': x_handle_authcount__mutmut_2, 
    'x_handle_authcount__mutmut_3': x_handle_authcount__mutmut_3, 
    'x_handle_authcount__mutmut_4': x_handle_authcount__mutmut_4, 
    'x_handle_authcount__mutmut_5': x_handle_authcount__mutmut_5, 
    'x_handle_authcount__mutmut_6': x_handle_authcount__mutmut_6, 
    'x_handle_authcount__mutmut_7': x_handle_authcount__mutmut_7, 
    'x_handle_authcount__mutmut_8': x_handle_authcount__mutmut_8, 
    'x_handle_authcount__mutmut_9': x_handle_authcount__mutmut_9, 
    'x_handle_authcount__mutmut_10': x_handle_authcount__mutmut_10, 
    'x_handle_authcount__mutmut_11': x_handle_authcount__mutmut_11, 
    'x_handle_authcount__mutmut_12': x_handle_authcount__mutmut_12, 
    'x_handle_authcount__mutmut_13': x_handle_authcount__mutmut_13, 
    'x_handle_authcount__mutmut_14': x_handle_authcount__mutmut_14, 
    'x_handle_authcount__mutmut_15': x_handle_authcount__mutmut_15, 
    'x_handle_authcount__mutmut_16': x_handle_authcount__mutmut_16, 
    'x_handle_authcount__mutmut_17': x_handle_authcount__mutmut_17, 
    'x_handle_authcount__mutmut_18': x_handle_authcount__mutmut_18, 
    'x_handle_authcount__mutmut_19': x_handle_authcount__mutmut_19, 
    'x_handle_authcount__mutmut_20': x_handle_authcount__mutmut_20, 
    'x_handle_authcount__mutmut_21': x_handle_authcount__mutmut_21, 
    'x_handle_authcount__mutmut_22': x_handle_authcount__mutmut_22, 
    'x_handle_authcount__mutmut_23': x_handle_authcount__mutmut_23, 
    'x_handle_authcount__mutmut_24': x_handle_authcount__mutmut_24, 
    'x_handle_authcount__mutmut_25': x_handle_authcount__mutmut_25, 
    'x_handle_authcount__mutmut_26': x_handle_authcount__mutmut_26, 
    'x_handle_authcount__mutmut_27': x_handle_authcount__mutmut_27, 
    'x_handle_authcount__mutmut_28': x_handle_authcount__mutmut_28, 
    'x_handle_authcount__mutmut_29': x_handle_authcount__mutmut_29, 
    'x_handle_authcount__mutmut_30': x_handle_authcount__mutmut_30, 
    'x_handle_authcount__mutmut_31': x_handle_authcount__mutmut_31, 
    'x_handle_authcount__mutmut_32': x_handle_authcount__mutmut_32
}

def handle_authcount(*args, **kwargs):
    result = _mutmut_trampoline(x_handle_authcount__mutmut_orig, x_handle_authcount__mutmut_mutants, *args, **kwargs)
    return result 

handle_authcount.__signature__ = _mutmut_signature(x_handle_authcount__mutmut_orig)
x_handle_authcount__mutmut_orig.__name__ = 'x_handle_authcount'




def x_setup_authcount_routes__mutmut_orig(app):
    @app.route('/search_authcount', methods=['GET'])
    def show_authcount_route():
        return show_authcount()

    @app.route('/authcount', methods=['POST'])
    def handle_authcount_route():
        return handle_authcount()


def x_setup_authcount_routes__mutmut_1(app):
    @app.route('XX/search_authcountXX', methods=['GET'])
    def show_authcount_route():
        return show_authcount()

    @app.route('/authcount', methods=['POST'])
    def handle_authcount_route():
        return handle_authcount()


def x_setup_authcount_routes__mutmut_2(app):
    @app.route('/search_authcount', methods=['XXGETXX'])
    def show_authcount_route():
        return show_authcount()

    @app.route('/authcount', methods=['POST'])
    def handle_authcount_route():
        return handle_authcount()


def x_setup_authcount_routes__mutmut_3(app):
    @app.route('/search_authcount',)
    def show_authcount_route():
        return show_authcount()

    @app.route('/authcount', methods=['POST'])
    def handle_authcount_route():
        return handle_authcount()


def x_setup_authcount_routes__mutmut_4(app):

    def show_authcount_route():
        return show_authcount()

    @app.route('/authcount', methods=['POST'])
    def handle_authcount_route():
        return handle_authcount()


def x_setup_authcount_routes__mutmut_5(app):
    @app.route('/search_authcount', methods=['GET'])
    def show_authcount_route():
        return show_authcount()

    @app.route('XX/authcountXX', methods=['POST'])
    def handle_authcount_route():
        return handle_authcount()


def x_setup_authcount_routes__mutmut_6(app):
    @app.route('/search_authcount', methods=['GET'])
    def show_authcount_route():
        return show_authcount()

    @app.route('/authcount', methods=['XXPOSTXX'])
    def handle_authcount_route():
        return handle_authcount()


def x_setup_authcount_routes__mutmut_7(app):
    @app.route('/search_authcount', methods=['GET'])
    def show_authcount_route():
        return show_authcount()

    @app.route('/authcount',)
    def handle_authcount_route():
        return handle_authcount()


def x_setup_authcount_routes__mutmut_8(app):
    @app.route('/search_authcount', methods=['GET'])
    def show_authcount_route():
        return show_authcount()

    def handle_authcount_route():
        return handle_authcount()

x_setup_authcount_routes__mutmut_mutants = {
'x_setup_authcount_routes__mutmut_1': x_setup_authcount_routes__mutmut_1, 
    'x_setup_authcount_routes__mutmut_2': x_setup_authcount_routes__mutmut_2, 
    'x_setup_authcount_routes__mutmut_3': x_setup_authcount_routes__mutmut_3, 
    'x_setup_authcount_routes__mutmut_4': x_setup_authcount_routes__mutmut_4, 
    'x_setup_authcount_routes__mutmut_5': x_setup_authcount_routes__mutmut_5, 
    'x_setup_authcount_routes__mutmut_6': x_setup_authcount_routes__mutmut_6, 
    'x_setup_authcount_routes__mutmut_7': x_setup_authcount_routes__mutmut_7, 
    'x_setup_authcount_routes__mutmut_8': x_setup_authcount_routes__mutmut_8
}

def setup_authcount_routes(*args, **kwargs):
    result = _mutmut_trampoline(x_setup_authcount_routes__mutmut_orig, x_setup_authcount_routes__mutmut_mutants, *args, **kwargs)
    return result 

setup_authcount_routes.__signature__ = _mutmut_signature(x_setup_authcount_routes__mutmut_orig)
x_setup_authcount_routes__mutmut_orig.__name__ = 'x_setup_authcount_routes'


