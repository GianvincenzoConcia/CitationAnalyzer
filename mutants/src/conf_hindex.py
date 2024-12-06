
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


from flask import render_template, request, redirect, url_for, flash

from bs4 import BeautifulSoup
from selenium import webdriver
from src.ranking_articles import get_block_elements, get_citations, search_conference, get_contents_link

# Inizializza un'istanza del driver Chrome con opzione headless
def x_init_driver__mutmut_orig():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    return webdriver.Chrome(options=options)

# Inizializza un'istanza del driver Chrome con opzione headless
def x_init_driver__mutmut_1():
    options = None
    options.add_argument('--headless')
    return webdriver.Chrome(options=options)

# Inizializza un'istanza del driver Chrome con opzione headless
def x_init_driver__mutmut_2():
    options = webdriver.ChromeOptions()
    options.add_argument('XX--headlessXX')
    return webdriver.Chrome(options=options)

# Inizializza un'istanza del driver Chrome con opzione headless
def x_init_driver__mutmut_3():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    return webdriver.Chrome(options=None)

x_init_driver__mutmut_mutants = {
'x_init_driver__mutmut_1': x_init_driver__mutmut_1, 
    'x_init_driver__mutmut_2': x_init_driver__mutmut_2, 
    'x_init_driver__mutmut_3': x_init_driver__mutmut_3
}

def init_driver(*args, **kwargs):
    result = _mutmut_trampoline(x_init_driver__mutmut_orig, x_init_driver__mutmut_mutants, *args, **kwargs)
    return result 

init_driver.__signature__ = _mutmut_signature(x_init_driver__mutmut_orig)
x_init_driver__mutmut_orig.__name__ = 'x_init_driver'




def x_get_conference_hindex__mutmut_orig(block_elements_list):
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


def x_get_conference_hindex__mutmut_1(block_elements_list):
    num_citazioni_list = None

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


def x_get_conference_hindex__mutmut_2(block_elements_list):
    num_citazioni_list = []

    for block_elements in block_elements_list:
        for i in block_elements:
            # Itera sugli elementi invece di chiamare find_all
            for title_element in i.find_all("XXspanXX", attrs={"class": "title"}):
                article_title = title_element.text.strip()
                numero_citazioni = get_citations(article_title)
                num_citazioni_list.append(int(numero_citazioni))

    num_citazioni_list.sort(reverse=True)
    hindex = calcola_h_index(num_citazioni_list)

    return hindex


def x_get_conference_hindex__mutmut_3(block_elements_list):
    num_citazioni_list = []

    for block_elements in block_elements_list:
        for i in block_elements:
            # Itera sugli elementi invece di chiamare find_all
            for title_element in i.find_all("span", attrs={"XXclassXX": "title"}):
                article_title = title_element.text.strip()
                numero_citazioni = get_citations(article_title)
                num_citazioni_list.append(int(numero_citazioni))

    num_citazioni_list.sort(reverse=True)
    hindex = calcola_h_index(num_citazioni_list)

    return hindex


def x_get_conference_hindex__mutmut_4(block_elements_list):
    num_citazioni_list = []

    for block_elements in block_elements_list:
        for i in block_elements:
            # Itera sugli elementi invece di chiamare find_all
            for title_element in i.find_all("span", attrs={"class": "XXtitleXX"}):
                article_title = title_element.text.strip()
                numero_citazioni = get_citations(article_title)
                num_citazioni_list.append(int(numero_citazioni))

    num_citazioni_list.sort(reverse=True)
    hindex = calcola_h_index(num_citazioni_list)

    return hindex


def x_get_conference_hindex__mutmut_5(block_elements_list):
    num_citazioni_list = []

    for block_elements in block_elements_list:
        for i in block_elements:
            # Itera sugli elementi invece di chiamare find_all
            for title_element in i.find_all("span",):
                article_title = title_element.text.strip()
                numero_citazioni = get_citations(article_title)
                num_citazioni_list.append(int(numero_citazioni))

    num_citazioni_list.sort(reverse=True)
    hindex = calcola_h_index(num_citazioni_list)

    return hindex


def x_get_conference_hindex__mutmut_6(block_elements_list):
    num_citazioni_list = []

    for block_elements in block_elements_list:
        for i in block_elements:
            # Itera sugli elementi invece di chiamare find_all
            for title_element in i.find_all("span", attrs={"class": "title"}):
                article_title = None
                numero_citazioni = get_citations(article_title)
                num_citazioni_list.append(int(numero_citazioni))

    num_citazioni_list.sort(reverse=True)
    hindex = calcola_h_index(num_citazioni_list)

    return hindex


def x_get_conference_hindex__mutmut_7(block_elements_list):
    num_citazioni_list = []

    for block_elements in block_elements_list:
        for i in block_elements:
            # Itera sugli elementi invece di chiamare find_all
            for title_element in i.find_all("span", attrs={"class": "title"}):
                article_title = title_element.text.strip()
                numero_citazioni = get_citations(None)
                num_citazioni_list.append(int(numero_citazioni))

    num_citazioni_list.sort(reverse=True)
    hindex = calcola_h_index(num_citazioni_list)

    return hindex


def x_get_conference_hindex__mutmut_8(block_elements_list):
    num_citazioni_list = []

    for block_elements in block_elements_list:
        for i in block_elements:
            # Itera sugli elementi invece di chiamare find_all
            for title_element in i.find_all("span", attrs={"class": "title"}):
                article_title = title_element.text.strip()
                numero_citazioni = None
                num_citazioni_list.append(int(numero_citazioni))

    num_citazioni_list.sort(reverse=True)
    hindex = calcola_h_index(num_citazioni_list)

    return hindex


def x_get_conference_hindex__mutmut_9(block_elements_list):
    num_citazioni_list = []

    for block_elements in block_elements_list:
        for i in block_elements:
            # Itera sugli elementi invece di chiamare find_all
            for title_element in i.find_all("span", attrs={"class": "title"}):
                article_title = title_element.text.strip()
                numero_citazioni = get_citations(article_title)
                num_citazioni_list.append(int(None))

    num_citazioni_list.sort(reverse=True)
    hindex = calcola_h_index(num_citazioni_list)

    return hindex


def x_get_conference_hindex__mutmut_10(block_elements_list):
    num_citazioni_list = []

    for block_elements in block_elements_list:
        for i in block_elements:
            # Itera sugli elementi invece di chiamare find_all
            for title_element in i.find_all("span", attrs={"class": "title"}):
                article_title = title_element.text.strip()
                numero_citazioni = get_citations(article_title)
                num_citazioni_list.append(int(numero_citazioni))

    num_citazioni_list.sort(reverse=False)
    hindex = calcola_h_index(num_citazioni_list)

    return hindex


def x_get_conference_hindex__mutmut_11(block_elements_list):
    num_citazioni_list = []

    for block_elements in block_elements_list:
        for i in block_elements:
            # Itera sugli elementi invece di chiamare find_all
            for title_element in i.find_all("span", attrs={"class": "title"}):
                article_title = title_element.text.strip()
                numero_citazioni = get_citations(article_title)
                num_citazioni_list.append(int(numero_citazioni))

    num_citazioni_list.sort(reverse=True)
    hindex = calcola_h_index(None)

    return hindex


def x_get_conference_hindex__mutmut_12(block_elements_list):
    num_citazioni_list = []

    for block_elements in block_elements_list:
        for i in block_elements:
            # Itera sugli elementi invece di chiamare find_all
            for title_element in i.find_all("span", attrs={"class": "title"}):
                article_title = title_element.text.strip()
                numero_citazioni = get_citations(article_title)
                num_citazioni_list.append(int(numero_citazioni))

    num_citazioni_list.sort(reverse=True)
    hindex = None

    return hindex

x_get_conference_hindex__mutmut_mutants = {
'x_get_conference_hindex__mutmut_1': x_get_conference_hindex__mutmut_1, 
    'x_get_conference_hindex__mutmut_2': x_get_conference_hindex__mutmut_2, 
    'x_get_conference_hindex__mutmut_3': x_get_conference_hindex__mutmut_3, 
    'x_get_conference_hindex__mutmut_4': x_get_conference_hindex__mutmut_4, 
    'x_get_conference_hindex__mutmut_5': x_get_conference_hindex__mutmut_5, 
    'x_get_conference_hindex__mutmut_6': x_get_conference_hindex__mutmut_6, 
    'x_get_conference_hindex__mutmut_7': x_get_conference_hindex__mutmut_7, 
    'x_get_conference_hindex__mutmut_8': x_get_conference_hindex__mutmut_8, 
    'x_get_conference_hindex__mutmut_9': x_get_conference_hindex__mutmut_9, 
    'x_get_conference_hindex__mutmut_10': x_get_conference_hindex__mutmut_10, 
    'x_get_conference_hindex__mutmut_11': x_get_conference_hindex__mutmut_11, 
    'x_get_conference_hindex__mutmut_12': x_get_conference_hindex__mutmut_12
}

def get_conference_hindex(*args, **kwargs):
    result = _mutmut_trampoline(x_get_conference_hindex__mutmut_orig, x_get_conference_hindex__mutmut_mutants, *args, **kwargs)
    return result 

get_conference_hindex.__signature__ = _mutmut_signature(x_get_conference_hindex__mutmut_orig)
x_get_conference_hindex__mutmut_orig.__name__ = 'x_get_conference_hindex'




def x_calcola_h_index__mutmut_orig(citazioni_per_articolo):
    citazioni_per_articolo.sort(reverse=True)
    h_index = 0
    for i, citazione in enumerate(citazioni_per_articolo, start=1):
        if i <= citazione:
            h_index = i
        else:
            break
    return h_index


def x_calcola_h_index__mutmut_1(citazioni_per_articolo):
    citazioni_per_articolo.sort(reverse=False)
    h_index = 0
    for i, citazione in enumerate(citazioni_per_articolo, start=1):
        if i <= citazione:
            h_index = i
        else:
            break
    return h_index


def x_calcola_h_index__mutmut_2(citazioni_per_articolo):
    citazioni_per_articolo.sort(reverse=True)
    h_index = 1
    for i, citazione in enumerate(citazioni_per_articolo, start=1):
        if i <= citazione:
            h_index = i
        else:
            break
    return h_index


def x_calcola_h_index__mutmut_3(citazioni_per_articolo):
    citazioni_per_articolo.sort(reverse=True)
    h_index = None
    for i, citazione in enumerate(citazioni_per_articolo, start=1):
        if i <= citazione:
            h_index = i
        else:
            break
    return h_index


def x_calcola_h_index__mutmut_4(citazioni_per_articolo):
    citazioni_per_articolo.sort(reverse=True)
    h_index = 0
    for i, citazione in enumerate(None, start=1):
        if i <= citazione:
            h_index = i
        else:
            break
    return h_index


def x_calcola_h_index__mutmut_5(citazioni_per_articolo):
    citazioni_per_articolo.sort(reverse=True)
    h_index = 0
    for i, citazione in enumerate(citazioni_per_articolo, start=2):
        if i <= citazione:
            h_index = i
        else:
            break
    return h_index


def x_calcola_h_index__mutmut_6(citazioni_per_articolo):
    citazioni_per_articolo.sort(reverse=True)
    h_index = 0
    for i, citazione in enumerate( start=1):
        if i <= citazione:
            h_index = i
        else:
            break
    return h_index


def x_calcola_h_index__mutmut_7(citazioni_per_articolo):
    citazioni_per_articolo.sort(reverse=True)
    h_index = 0
    for i, citazione in enumerate(citazioni_per_articolo,):
        if i <= citazione:
            h_index = i
        else:
            break
    return h_index


def x_calcola_h_index__mutmut_8(citazioni_per_articolo):
    citazioni_per_articolo.sort(reverse=True)
    h_index = 0
    for i, citazione in enumerate(citazioni_per_articolo, start=1):
        if i < citazione:
            h_index = i
        else:
            break
    return h_index


def x_calcola_h_index__mutmut_9(citazioni_per_articolo):
    citazioni_per_articolo.sort(reverse=True)
    h_index = 0
    for i, citazione in enumerate(citazioni_per_articolo, start=1):
        if i <= citazione:
            h_index = None
        else:
            break
    return h_index


def x_calcola_h_index__mutmut_10(citazioni_per_articolo):
    citazioni_per_articolo.sort(reverse=True)
    h_index = 0
    for i, citazione in enumerate(citazioni_per_articolo, start=1):
        if i <= citazione:
            h_index = i
        else:
            return
    return h_index

x_calcola_h_index__mutmut_mutants = {
'x_calcola_h_index__mutmut_1': x_calcola_h_index__mutmut_1, 
    'x_calcola_h_index__mutmut_2': x_calcola_h_index__mutmut_2, 
    'x_calcola_h_index__mutmut_3': x_calcola_h_index__mutmut_3, 
    'x_calcola_h_index__mutmut_4': x_calcola_h_index__mutmut_4, 
    'x_calcola_h_index__mutmut_5': x_calcola_h_index__mutmut_5, 
    'x_calcola_h_index__mutmut_6': x_calcola_h_index__mutmut_6, 
    'x_calcola_h_index__mutmut_7': x_calcola_h_index__mutmut_7, 
    'x_calcola_h_index__mutmut_8': x_calcola_h_index__mutmut_8, 
    'x_calcola_h_index__mutmut_9': x_calcola_h_index__mutmut_9, 
    'x_calcola_h_index__mutmut_10': x_calcola_h_index__mutmut_10
}

def calcola_h_index(*args, **kwargs):
    result = _mutmut_trampoline(x_calcola_h_index__mutmut_orig, x_calcola_h_index__mutmut_mutants, *args, **kwargs)
    return result 

calcola_h_index.__signature__ = _mutmut_signature(x_calcola_h_index__mutmut_orig)
x_calcola_h_index__mutmut_orig.__name__ = 'x_calcola_h_index'




def x_all_conference_index__mutmut_orig(driver, start_year, end_year, conference_titles):
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


def x_all_conference_index__mutmut_1(driver, start_year, end_year, conference_titles):
    conferences_list = None

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


def x_all_conference_index__mutmut_2(driver, start_year, end_year, conference_titles):
    conferences_list = []

    for conference_title in conference_titles:
        block_element_list = None
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


def x_all_conference_index__mutmut_3(driver, start_year, end_year, conference_titles):
    conferences_list = []

    for conference_title in conference_titles:
        block_element_list = []
        # Cerca le conferenze per l'anno specificato
        page_conference = search_conference(None, driver)

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


def x_all_conference_index__mutmut_4(driver, start_year, end_year, conference_titles):
    conferences_list = []

    for conference_title in conference_titles:
        block_element_list = []
        # Cerca le conferenze per l'anno specificato
        page_conference = search_conference(conference_title, None)

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


def x_all_conference_index__mutmut_5(driver, start_year, end_year, conference_titles):
    conferences_list = []

    for conference_title in conference_titles:
        block_element_list = []
        # Cerca le conferenze per l'anno specificato
        page_conference = search_conference( driver)

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


def x_all_conference_index__mutmut_6(driver, start_year, end_year, conference_titles):
    conferences_list = []

    for conference_title in conference_titles:
        block_element_list = []
        # Cerca le conferenze per l'anno specificato
        page_conference = search_conference(conference_title,)

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


def x_all_conference_index__mutmut_7(driver, start_year, end_year, conference_titles):
    conferences_list = []

    for conference_title in conference_titles:
        block_element_list = []
        # Cerca le conferenze per l'anno specificato
        page_conference = None

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


def x_all_conference_index__mutmut_8(driver, start_year, end_year, conference_titles):
    conferences_list = []

    for conference_title in conference_titles:
        block_element_list = []
        # Cerca le conferenze per l'anno specificato
        page_conference = search_conference(conference_title, driver)

        if page_conference:
            for conference_year in range(int(None), int(end_year) + 1):
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


def x_all_conference_index__mutmut_9(driver, start_year, end_year, conference_titles):
    conferences_list = []

    for conference_title in conference_titles:
        block_element_list = []
        # Cerca le conferenze per l'anno specificato
        page_conference = search_conference(conference_title, driver)

        if page_conference:
            for conference_year in range(int(start_year), int(None) + 1):
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


def x_all_conference_index__mutmut_10(driver, start_year, end_year, conference_titles):
    conferences_list = []

    for conference_title in conference_titles:
        block_element_list = []
        # Cerca le conferenze per l'anno specificato
        page_conference = search_conference(conference_title, driver)

        if page_conference:
            for conference_year in range(int(start_year), int(end_year) - 1):
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


def x_all_conference_index__mutmut_11(driver, start_year, end_year, conference_titles):
    conferences_list = []

    for conference_title in conference_titles:
        block_element_list = []
        # Cerca le conferenze per l'anno specificato
        page_conference = search_conference(conference_title, driver)

        if page_conference:
            for conference_year in range(int(start_year), int(end_year) + 2):
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


def x_all_conference_index__mutmut_12(driver, start_year, end_year, conference_titles):
    conferences_list = []

    for conference_title in conference_titles:
        block_element_list = []
        # Cerca le conferenze per l'anno specificato
        page_conference = search_conference(conference_title, driver)

        if page_conference:
            for conference_year in range(int(start_year), int(end_year) + 1):
                soup = BeautifulSoup(None, "html.parser")
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


def x_all_conference_index__mutmut_13(driver, start_year, end_year, conference_titles):
    conferences_list = []

    for conference_title in conference_titles:
        block_element_list = []
        # Cerca le conferenze per l'anno specificato
        page_conference = search_conference(conference_title, driver)

        if page_conference:
            for conference_year in range(int(start_year), int(end_year) + 1):
                soup = BeautifulSoup(page_conference, "XXhtml.parserXX")
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


def x_all_conference_index__mutmut_14(driver, start_year, end_year, conference_titles):
    conferences_list = []

    for conference_title in conference_titles:
        block_element_list = []
        # Cerca le conferenze per l'anno specificato
        page_conference = search_conference(conference_title, driver)

        if page_conference:
            for conference_year in range(int(start_year), int(end_year) + 1):
                soup = BeautifulSoup( "html.parser")
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


def x_all_conference_index__mutmut_15(driver, start_year, end_year, conference_titles):
    conferences_list = []

    for conference_title in conference_titles:
        block_element_list = []
        # Cerca le conferenze per l'anno specificato
        page_conference = search_conference(conference_title, driver)

        if page_conference:
            for conference_year in range(int(start_year), int(end_year) + 1):
                soup = None
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


def x_all_conference_index__mutmut_16(driver, start_year, end_year, conference_titles):
    conferences_list = []

    for conference_title in conference_titles:
        block_element_list = []
        # Cerca le conferenze per l'anno specificato
        page_conference = search_conference(conference_title, driver)

        if page_conference:
            for conference_year in range(int(start_year), int(end_year) + 1):
                soup = BeautifulSoup(page_conference, "html.parser")
                # Ottieni i titoli delle conferenze
                year_element = get_year_element(None, conference_year)

                if year_element is not None:
                    contents_page_source = get_contents_link(year_element, driver)

                    if contents_page_source is not None:
                        block_elements = get_block_elements(contents_page_source)
                        block_element_list.append(block_elements)

        conf_index = get_conference_hindex(block_element_list)
        conferences_list.append((conference_title, conf_index))
    conferences_list.sort(reverse=True, key=lambda x: x[1])
    return conferences_list


def x_all_conference_index__mutmut_17(driver, start_year, end_year, conference_titles):
    conferences_list = []

    for conference_title in conference_titles:
        block_element_list = []
        # Cerca le conferenze per l'anno specificato
        page_conference = search_conference(conference_title, driver)

        if page_conference:
            for conference_year in range(int(start_year), int(end_year) + 1):
                soup = BeautifulSoup(page_conference, "html.parser")
                # Ottieni i titoli delle conferenze
                year_element = get_year_element(soup, None)

                if year_element is not None:
                    contents_page_source = get_contents_link(year_element, driver)

                    if contents_page_source is not None:
                        block_elements = get_block_elements(contents_page_source)
                        block_element_list.append(block_elements)

        conf_index = get_conference_hindex(block_element_list)
        conferences_list.append((conference_title, conf_index))
    conferences_list.sort(reverse=True, key=lambda x: x[1])
    return conferences_list


def x_all_conference_index__mutmut_18(driver, start_year, end_year, conference_titles):
    conferences_list = []

    for conference_title in conference_titles:
        block_element_list = []
        # Cerca le conferenze per l'anno specificato
        page_conference = search_conference(conference_title, driver)

        if page_conference:
            for conference_year in range(int(start_year), int(end_year) + 1):
                soup = BeautifulSoup(page_conference, "html.parser")
                # Ottieni i titoli delle conferenze
                year_element = get_year_element( conference_year)

                if year_element is not None:
                    contents_page_source = get_contents_link(year_element, driver)

                    if contents_page_source is not None:
                        block_elements = get_block_elements(contents_page_source)
                        block_element_list.append(block_elements)

        conf_index = get_conference_hindex(block_element_list)
        conferences_list.append((conference_title, conf_index))
    conferences_list.sort(reverse=True, key=lambda x: x[1])
    return conferences_list


def x_all_conference_index__mutmut_19(driver, start_year, end_year, conference_titles):
    conferences_list = []

    for conference_title in conference_titles:
        block_element_list = []
        # Cerca le conferenze per l'anno specificato
        page_conference = search_conference(conference_title, driver)

        if page_conference:
            for conference_year in range(int(start_year), int(end_year) + 1):
                soup = BeautifulSoup(page_conference, "html.parser")
                # Ottieni i titoli delle conferenze
                year_element = get_year_element(soup,)

                if year_element is not None:
                    contents_page_source = get_contents_link(year_element, driver)

                    if contents_page_source is not None:
                        block_elements = get_block_elements(contents_page_source)
                        block_element_list.append(block_elements)

        conf_index = get_conference_hindex(block_element_list)
        conferences_list.append((conference_title, conf_index))
    conferences_list.sort(reverse=True, key=lambda x: x[1])
    return conferences_list


def x_all_conference_index__mutmut_20(driver, start_year, end_year, conference_titles):
    conferences_list = []

    for conference_title in conference_titles:
        block_element_list = []
        # Cerca le conferenze per l'anno specificato
        page_conference = search_conference(conference_title, driver)

        if page_conference:
            for conference_year in range(int(start_year), int(end_year) + 1):
                soup = BeautifulSoup(page_conference, "html.parser")
                # Ottieni i titoli delle conferenze
                year_element = None

                if year_element is not None:
                    contents_page_source = get_contents_link(year_element, driver)

                    if contents_page_source is not None:
                        block_elements = get_block_elements(contents_page_source)
                        block_element_list.append(block_elements)

        conf_index = get_conference_hindex(block_element_list)
        conferences_list.append((conference_title, conf_index))
    conferences_list.sort(reverse=True, key=lambda x: x[1])
    return conferences_list


def x_all_conference_index__mutmut_21(driver, start_year, end_year, conference_titles):
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

                if year_element is  None:
                    contents_page_source = get_contents_link(year_element, driver)

                    if contents_page_source is not None:
                        block_elements = get_block_elements(contents_page_source)
                        block_element_list.append(block_elements)

        conf_index = get_conference_hindex(block_element_list)
        conferences_list.append((conference_title, conf_index))
    conferences_list.sort(reverse=True, key=lambda x: x[1])
    return conferences_list


def x_all_conference_index__mutmut_22(driver, start_year, end_year, conference_titles):
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
                    contents_page_source = get_contents_link(None, driver)

                    if contents_page_source is not None:
                        block_elements = get_block_elements(contents_page_source)
                        block_element_list.append(block_elements)

        conf_index = get_conference_hindex(block_element_list)
        conferences_list.append((conference_title, conf_index))
    conferences_list.sort(reverse=True, key=lambda x: x[1])
    return conferences_list


def x_all_conference_index__mutmut_23(driver, start_year, end_year, conference_titles):
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
                    contents_page_source = get_contents_link(year_element, None)

                    if contents_page_source is not None:
                        block_elements = get_block_elements(contents_page_source)
                        block_element_list.append(block_elements)

        conf_index = get_conference_hindex(block_element_list)
        conferences_list.append((conference_title, conf_index))
    conferences_list.sort(reverse=True, key=lambda x: x[1])
    return conferences_list


def x_all_conference_index__mutmut_24(driver, start_year, end_year, conference_titles):
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
                    contents_page_source = get_contents_link( driver)

                    if contents_page_source is not None:
                        block_elements = get_block_elements(contents_page_source)
                        block_element_list.append(block_elements)

        conf_index = get_conference_hindex(block_element_list)
        conferences_list.append((conference_title, conf_index))
    conferences_list.sort(reverse=True, key=lambda x: x[1])
    return conferences_list


def x_all_conference_index__mutmut_25(driver, start_year, end_year, conference_titles):
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
                    contents_page_source = get_contents_link(year_element,)

                    if contents_page_source is not None:
                        block_elements = get_block_elements(contents_page_source)
                        block_element_list.append(block_elements)

        conf_index = get_conference_hindex(block_element_list)
        conferences_list.append((conference_title, conf_index))
    conferences_list.sort(reverse=True, key=lambda x: x[1])
    return conferences_list


def x_all_conference_index__mutmut_26(driver, start_year, end_year, conference_titles):
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
                    contents_page_source = None

                    if contents_page_source is not None:
                        block_elements = get_block_elements(contents_page_source)
                        block_element_list.append(block_elements)

        conf_index = get_conference_hindex(block_element_list)
        conferences_list.append((conference_title, conf_index))
    conferences_list.sort(reverse=True, key=lambda x: x[1])
    return conferences_list


def x_all_conference_index__mutmut_27(driver, start_year, end_year, conference_titles):
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

                    if contents_page_source is  None:
                        block_elements = get_block_elements(contents_page_source)
                        block_element_list.append(block_elements)

        conf_index = get_conference_hindex(block_element_list)
        conferences_list.append((conference_title, conf_index))
    conferences_list.sort(reverse=True, key=lambda x: x[1])
    return conferences_list


def x_all_conference_index__mutmut_28(driver, start_year, end_year, conference_titles):
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
                        block_elements = get_block_elements(None)
                        block_element_list.append(block_elements)

        conf_index = get_conference_hindex(block_element_list)
        conferences_list.append((conference_title, conf_index))
    conferences_list.sort(reverse=True, key=lambda x: x[1])
    return conferences_list


def x_all_conference_index__mutmut_29(driver, start_year, end_year, conference_titles):
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
                        block_elements = None
                        block_element_list.append(block_elements)

        conf_index = get_conference_hindex(block_element_list)
        conferences_list.append((conference_title, conf_index))
    conferences_list.sort(reverse=True, key=lambda x: x[1])
    return conferences_list


def x_all_conference_index__mutmut_30(driver, start_year, end_year, conference_titles):
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
                        block_element_list.append(None)

        conf_index = get_conference_hindex(block_element_list)
        conferences_list.append((conference_title, conf_index))
    conferences_list.sort(reverse=True, key=lambda x: x[1])
    return conferences_list


def x_all_conference_index__mutmut_31(driver, start_year, end_year, conference_titles):
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

        conf_index = get_conference_hindex(None)
        conferences_list.append((conference_title, conf_index))
    conferences_list.sort(reverse=True, key=lambda x: x[1])
    return conferences_list


def x_all_conference_index__mutmut_32(driver, start_year, end_year, conference_titles):
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

        conf_index = None
        conferences_list.append((conference_title, conf_index))
    conferences_list.sort(reverse=True, key=lambda x: x[1])
    return conferences_list


def x_all_conference_index__mutmut_33(driver, start_year, end_year, conference_titles):
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
    conferences_list.sort(reverse=False, key=lambda x: x[1])
    return conferences_list


def x_all_conference_index__mutmut_34(driver, start_year, end_year, conference_titles):
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
    conferences_list.sort(reverse=True, key=lambda x: x[2])
    return conferences_list


def x_all_conference_index__mutmut_35(driver, start_year, end_year, conference_titles):
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
    conferences_list.sort(reverse=True, key=lambda x: x[None])
    return conferences_list


def x_all_conference_index__mutmut_36(driver, start_year, end_year, conference_titles):
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
    conferences_list.sort(reverse=True, key=lambda x: None)
    return conferences_list


def x_all_conference_index__mutmut_37(driver, start_year, end_year, conference_titles):
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
    conferences_list.sort( key=lambda x: x[1])
    return conferences_list


def x_all_conference_index__mutmut_38(driver, start_year, end_year, conference_titles):
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
    conferences_list.sort(reverse=True,)
    return conferences_list

x_all_conference_index__mutmut_mutants = {
'x_all_conference_index__mutmut_1': x_all_conference_index__mutmut_1, 
    'x_all_conference_index__mutmut_2': x_all_conference_index__mutmut_2, 
    'x_all_conference_index__mutmut_3': x_all_conference_index__mutmut_3, 
    'x_all_conference_index__mutmut_4': x_all_conference_index__mutmut_4, 
    'x_all_conference_index__mutmut_5': x_all_conference_index__mutmut_5, 
    'x_all_conference_index__mutmut_6': x_all_conference_index__mutmut_6, 
    'x_all_conference_index__mutmut_7': x_all_conference_index__mutmut_7, 
    'x_all_conference_index__mutmut_8': x_all_conference_index__mutmut_8, 
    'x_all_conference_index__mutmut_9': x_all_conference_index__mutmut_9, 
    'x_all_conference_index__mutmut_10': x_all_conference_index__mutmut_10, 
    'x_all_conference_index__mutmut_11': x_all_conference_index__mutmut_11, 
    'x_all_conference_index__mutmut_12': x_all_conference_index__mutmut_12, 
    'x_all_conference_index__mutmut_13': x_all_conference_index__mutmut_13, 
    'x_all_conference_index__mutmut_14': x_all_conference_index__mutmut_14, 
    'x_all_conference_index__mutmut_15': x_all_conference_index__mutmut_15, 
    'x_all_conference_index__mutmut_16': x_all_conference_index__mutmut_16, 
    'x_all_conference_index__mutmut_17': x_all_conference_index__mutmut_17, 
    'x_all_conference_index__mutmut_18': x_all_conference_index__mutmut_18, 
    'x_all_conference_index__mutmut_19': x_all_conference_index__mutmut_19, 
    'x_all_conference_index__mutmut_20': x_all_conference_index__mutmut_20, 
    'x_all_conference_index__mutmut_21': x_all_conference_index__mutmut_21, 
    'x_all_conference_index__mutmut_22': x_all_conference_index__mutmut_22, 
    'x_all_conference_index__mutmut_23': x_all_conference_index__mutmut_23, 
    'x_all_conference_index__mutmut_24': x_all_conference_index__mutmut_24, 
    'x_all_conference_index__mutmut_25': x_all_conference_index__mutmut_25, 
    'x_all_conference_index__mutmut_26': x_all_conference_index__mutmut_26, 
    'x_all_conference_index__mutmut_27': x_all_conference_index__mutmut_27, 
    'x_all_conference_index__mutmut_28': x_all_conference_index__mutmut_28, 
    'x_all_conference_index__mutmut_29': x_all_conference_index__mutmut_29, 
    'x_all_conference_index__mutmut_30': x_all_conference_index__mutmut_30, 
    'x_all_conference_index__mutmut_31': x_all_conference_index__mutmut_31, 
    'x_all_conference_index__mutmut_32': x_all_conference_index__mutmut_32, 
    'x_all_conference_index__mutmut_33': x_all_conference_index__mutmut_33, 
    'x_all_conference_index__mutmut_34': x_all_conference_index__mutmut_34, 
    'x_all_conference_index__mutmut_35': x_all_conference_index__mutmut_35, 
    'x_all_conference_index__mutmut_36': x_all_conference_index__mutmut_36, 
    'x_all_conference_index__mutmut_37': x_all_conference_index__mutmut_37, 
    'x_all_conference_index__mutmut_38': x_all_conference_index__mutmut_38
}

def all_conference_index(*args, **kwargs):
    result = _mutmut_trampoline(x_all_conference_index__mutmut_orig, x_all_conference_index__mutmut_mutants, *args, **kwargs)
    return result 

all_conference_index.__signature__ = _mutmut_signature(x_all_conference_index__mutmut_orig)
x_all_conference_index__mutmut_orig.__name__ = 'x_all_conference_index'




def x_get_year_element__mutmut_orig(soup, conference_year):
    year_element = soup.find('span', {'itemprop': 'datePublished'},
                             string=lambda text: str(conference_year) in text)
    return year_element


def x_get_year_element__mutmut_1(soup, conference_year):
    year_element = soup.find('XXspanXX', {'itemprop': 'datePublished'},
                             string=lambda text: str(conference_year) in text)
    return year_element


def x_get_year_element__mutmut_2(soup, conference_year):
    year_element = soup.find('span', {'XXitempropXX': 'datePublished'},
                             string=lambda text: str(conference_year) in text)
    return year_element


def x_get_year_element__mutmut_3(soup, conference_year):
    year_element = soup.find('span', {'itemprop': 'XXdatePublishedXX'},
                             string=lambda text: str(conference_year) in text)
    return year_element


def x_get_year_element__mutmut_4(soup, conference_year):
    year_element = soup.find('span', {'itemprop': 'datePublished'},
                             string=lambda text: str(None) in text)
    return year_element


def x_get_year_element__mutmut_5(soup, conference_year):
    year_element = soup.find('span', {'itemprop': 'datePublished'},
                             string=lambda text: str(conference_year) not in text)
    return year_element


def x_get_year_element__mutmut_6(soup, conference_year):
    year_element = soup.find('span', {'itemprop': 'datePublished'},
                             string=lambda text: None)
    return year_element


def x_get_year_element__mutmut_7(soup, conference_year):
    year_element = soup.find('span', {'itemprop': 'datePublished'},)
    return year_element


def x_get_year_element__mutmut_8(soup, conference_year):
    year_element = None
    return year_element

x_get_year_element__mutmut_mutants = {
'x_get_year_element__mutmut_1': x_get_year_element__mutmut_1, 
    'x_get_year_element__mutmut_2': x_get_year_element__mutmut_2, 
    'x_get_year_element__mutmut_3': x_get_year_element__mutmut_3, 
    'x_get_year_element__mutmut_4': x_get_year_element__mutmut_4, 
    'x_get_year_element__mutmut_5': x_get_year_element__mutmut_5, 
    'x_get_year_element__mutmut_6': x_get_year_element__mutmut_6, 
    'x_get_year_element__mutmut_7': x_get_year_element__mutmut_7, 
    'x_get_year_element__mutmut_8': x_get_year_element__mutmut_8
}

def get_year_element(*args, **kwargs):
    result = _mutmut_trampoline(x_get_year_element__mutmut_orig, x_get_year_element__mutmut_mutants, *args, **kwargs)
    return result 

get_year_element.__signature__ = _mutmut_signature(x_get_year_element__mutmut_orig)
x_get_year_element__mutmut_orig.__name__ = 'x_get_year_element'




def x_validate_years__mutmut_orig(start_year, end_year):
    if int(start_year) > int(end_year):
        flash(f"L'anno di inizio deve essere precedente all'anno di fine", 'error')
        return None


def x_validate_years__mutmut_1(start_year, end_year):
    if int(None) > int(end_year):
        flash(f"L'anno di inizio deve essere precedente all'anno di fine", 'error')
        return None


def x_validate_years__mutmut_2(start_year, end_year):
    if int(start_year) >= int(end_year):
        flash(f"L'anno di inizio deve essere precedente all'anno di fine", 'error')
        return None


def x_validate_years__mutmut_3(start_year, end_year):
    if int(start_year) > int(None):
        flash(f"L'anno di inizio deve essere precedente all'anno di fine", 'error')
        return None


def x_validate_years__mutmut_4(start_year, end_year):
    if int(start_year) > int(end_year):
        flash(f"L'anno di inizio deve essere precedente all'anno di fine", 'XXerrorXX')
        return None

x_validate_years__mutmut_mutants = {
'x_validate_years__mutmut_1': x_validate_years__mutmut_1, 
    'x_validate_years__mutmut_2': x_validate_years__mutmut_2, 
    'x_validate_years__mutmut_3': x_validate_years__mutmut_3, 
    'x_validate_years__mutmut_4': x_validate_years__mutmut_4
}

def validate_years(*args, **kwargs):
    result = _mutmut_trampoline(x_validate_years__mutmut_orig, x_validate_years__mutmut_mutants, *args, **kwargs)
    return result 

validate_years.__signature__ = _mutmut_signature(x_validate_years__mutmut_orig)
x_validate_years__mutmut_orig.__name__ = 'x_validate_years'




def x_setup_hindex_routes__mutmut_orig(app):
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


def x_setup_hindex_routes__mutmut_1(app):
    @app.route('XX/search_hindexXX', methods=['GET'])
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


def x_setup_hindex_routes__mutmut_2(app):
    @app.route('/search_hindex', methods=['XXGETXX'])
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


def x_setup_hindex_routes__mutmut_3(app):
    @app.route('/search_hindex',)
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


def x_setup_hindex_routes__mutmut_4(app):

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


def x_setup_hindex_routes__mutmut_5(app):
    @app.route('/search_hindex', methods=['GET'])
    def show_hindex():
        return render_template('XXh_index.htmlXX', result=None)

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


def x_setup_hindex_routes__mutmut_6(app):
    @app.route('/search_hindex', methods=['GET'])
    def show_hindex():
        return render_template('h_index.html',)

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


def x_setup_hindex_routes__mutmut_7(app):
    @app.route('/search_hindex', methods=['GET'])
    def show_hindex():
        return render_template('h_index.html', result=None)

    @app.route('XX/h_indexXX', methods=['POST'])
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


def x_setup_hindex_routes__mutmut_8(app):
    @app.route('/search_hindex', methods=['GET'])
    def show_hindex():
        return render_template('h_index.html', result=None)

    @app.route('/h_index', methods=['XXPOSTXX'])
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


def x_setup_hindex_routes__mutmut_9(app):
    @app.route('/search_hindex', methods=['GET'])
    def show_hindex():
        return render_template('h_index.html', result=None)

    @app.route('/h_index',)
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


def x_setup_hindex_routes__mutmut_10(app):
    @app.route('/search_hindex', methods=['GET'])
    def show_hindex():
        return render_template('h_index.html', result=None)

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


def x_setup_hindex_routes__mutmut_11(app):
    @app.route('/search_hindex', methods=['GET'])
    def show_hindex():
        return render_template('h_index.html', result=None)

    @app.route('/h_index', methods=['POST'])
    def handle_hindex():
        start_year = request.form.get('XXstart_yearXX')
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


def x_setup_hindex_routes__mutmut_12(app):
    @app.route('/search_hindex', methods=['GET'])
    def show_hindex():
        return render_template('h_index.html', result=None)

    @app.route('/h_index', methods=['POST'])
    def handle_hindex():
        start_year = None
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


def x_setup_hindex_routes__mutmut_13(app):
    @app.route('/search_hindex', methods=['GET'])
    def show_hindex():
        return render_template('h_index.html', result=None)

    @app.route('/h_index', methods=['POST'])
    def handle_hindex():
        start_year = request.form.get('start_year')
        end_year = request.form.get('XXend_yearXX')
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


def x_setup_hindex_routes__mutmut_14(app):
    @app.route('/search_hindex', methods=['GET'])
    def show_hindex():
        return render_template('h_index.html', result=None)

    @app.route('/h_index', methods=['POST'])
    def handle_hindex():
        start_year = request.form.get('start_year')
        end_year = None
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


def x_setup_hindex_routes__mutmut_15(app):
    @app.route('/search_hindex', methods=['GET'])
    def show_hindex():
        return render_template('h_index.html', result=None)

    @app.route('/h_index', methods=['POST'])
    def handle_hindex():
        start_year = request.form.get('start_year')
        end_year = request.form.get('end_year')
        conference_list = request.form.getlist('XXconference_listXX')

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


def x_setup_hindex_routes__mutmut_16(app):
    @app.route('/search_hindex', methods=['GET'])
    def show_hindex():
        return render_template('h_index.html', result=None)

    @app.route('/h_index', methods=['POST'])
    def handle_hindex():
        start_year = request.form.get('start_year')
        end_year = request.form.get('end_year')
        conference_list = None

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


def x_setup_hindex_routes__mutmut_17(app):
    @app.route('/search_hindex', methods=['GET'])
    def show_hindex():
        return render_template('h_index.html', result=None)

    @app.route('/h_index', methods=['POST'])
    def handle_hindex():
        start_year = request.form.get('start_year')
        end_year = request.form.get('end_year')
        conference_list = request.form.getlist('conference_list')

        if start_year or end_year and conference_list:
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


def x_setup_hindex_routes__mutmut_18(app):
    @app.route('/search_hindex', methods=['GET'])
    def show_hindex():
        return render_template('h_index.html', result=None)

    @app.route('/h_index', methods=['POST'])
    def handle_hindex():
        start_year = request.form.get('start_year')
        end_year = request.form.get('end_year')
        conference_list = request.form.getlist('conference_list')

        if start_year and end_year and conference_list:
            validate_years(None, end_year)
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


def x_setup_hindex_routes__mutmut_19(app):
    @app.route('/search_hindex', methods=['GET'])
    def show_hindex():
        return render_template('h_index.html', result=None)

    @app.route('/h_index', methods=['POST'])
    def handle_hindex():
        start_year = request.form.get('start_year')
        end_year = request.form.get('end_year')
        conference_list = request.form.getlist('conference_list')

        if start_year and end_year and conference_list:
            validate_years(start_year, None)
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


def x_setup_hindex_routes__mutmut_20(app):
    @app.route('/search_hindex', methods=['GET'])
    def show_hindex():
        return render_template('h_index.html', result=None)

    @app.route('/h_index', methods=['POST'])
    def handle_hindex():
        start_year = request.form.get('start_year')
        end_year = request.form.get('end_year')
        conference_list = request.form.getlist('conference_list')

        if start_year and end_year and conference_list:
            validate_years( end_year)
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


def x_setup_hindex_routes__mutmut_21(app):
    @app.route('/search_hindex', methods=['GET'])
    def show_hindex():
        return render_template('h_index.html', result=None)

    @app.route('/h_index', methods=['POST'])
    def handle_hindex():
        start_year = request.form.get('start_year')
        end_year = request.form.get('end_year')
        conference_list = request.form.getlist('conference_list')

        if start_year and end_year and conference_list:
            validate_years(start_year,)
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


def x_setup_hindex_routes__mutmut_22(app):
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
            driver = None

            try:
                conferences_list = all_conference_index(driver, start_year, end_year, conference_list)
                if conferences_list is not None:
                    return render_template('h_index.html', result=conferences_list,
                                           start_year=start_year, end_year=end_year, conference_list=conference_list)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_hindex'))


def x_setup_hindex_routes__mutmut_23(app):
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
                conferences_list = all_conference_index(None, start_year, end_year, conference_list)
                if conferences_list is not None:
                    return render_template('h_index.html', result=conferences_list,
                                           start_year=start_year, end_year=end_year, conference_list=conference_list)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_hindex'))


def x_setup_hindex_routes__mutmut_24(app):
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
                conferences_list = all_conference_index(driver, None, end_year, conference_list)
                if conferences_list is not None:
                    return render_template('h_index.html', result=conferences_list,
                                           start_year=start_year, end_year=end_year, conference_list=conference_list)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_hindex'))


def x_setup_hindex_routes__mutmut_25(app):
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
                conferences_list = all_conference_index(driver, start_year, None, conference_list)
                if conferences_list is not None:
                    return render_template('h_index.html', result=conferences_list,
                                           start_year=start_year, end_year=end_year, conference_list=conference_list)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_hindex'))


def x_setup_hindex_routes__mutmut_26(app):
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
                conferences_list = all_conference_index(driver, start_year, end_year, None)
                if conferences_list is not None:
                    return render_template('h_index.html', result=conferences_list,
                                           start_year=start_year, end_year=end_year, conference_list=conference_list)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_hindex'))


def x_setup_hindex_routes__mutmut_27(app):
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
                conferences_list = all_conference_index( start_year, end_year, conference_list)
                if conferences_list is not None:
                    return render_template('h_index.html', result=conferences_list,
                                           start_year=start_year, end_year=end_year, conference_list=conference_list)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_hindex'))


def x_setup_hindex_routes__mutmut_28(app):
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
                conferences_list = all_conference_index(driver, end_year, conference_list)
                if conferences_list is not None:
                    return render_template('h_index.html', result=conferences_list,
                                           start_year=start_year, end_year=end_year, conference_list=conference_list)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_hindex'))


def x_setup_hindex_routes__mutmut_29(app):
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
                conferences_list = all_conference_index(driver, start_year, conference_list)
                if conferences_list is not None:
                    return render_template('h_index.html', result=conferences_list,
                                           start_year=start_year, end_year=end_year, conference_list=conference_list)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_hindex'))


def x_setup_hindex_routes__mutmut_30(app):
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
                conferences_list = all_conference_index(driver, start_year, end_year,)
                if conferences_list is not None:
                    return render_template('h_index.html', result=conferences_list,
                                           start_year=start_year, end_year=end_year, conference_list=conference_list)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_hindex'))


def x_setup_hindex_routes__mutmut_31(app):
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
                conferences_list = None
                if conferences_list is not None:
                    return render_template('h_index.html', result=conferences_list,
                                           start_year=start_year, end_year=end_year, conference_list=conference_list)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_hindex'))


def x_setup_hindex_routes__mutmut_32(app):
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
                if conferences_list is  None:
                    return render_template('h_index.html', result=conferences_list,
                                           start_year=start_year, end_year=end_year, conference_list=conference_list)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_hindex'))


def x_setup_hindex_routes__mutmut_33(app):
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
                    return render_template('XXh_index.htmlXX', result=conferences_list,
                                           start_year=start_year, end_year=end_year, conference_list=conference_list)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_hindex'))


def x_setup_hindex_routes__mutmut_34(app):
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
                    return render_template('h_index.html', result=None,
                                           start_year=start_year, end_year=end_year, conference_list=conference_list)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_hindex'))


def x_setup_hindex_routes__mutmut_35(app):
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
                                           start_year=None, end_year=end_year, conference_list=conference_list)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_hindex'))


def x_setup_hindex_routes__mutmut_36(app):
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
                                           start_year=start_year, end_year=None, conference_list=conference_list)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_hindex'))


def x_setup_hindex_routes__mutmut_37(app):
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
                                           start_year=start_year, end_year=end_year, conference_list=None)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_hindex'))


def x_setup_hindex_routes__mutmut_38(app):
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
                    return render_template('h_index.html',
                                           start_year=start_year, end_year=end_year, conference_list=conference_list)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_hindex'))


def x_setup_hindex_routes__mutmut_39(app):
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
                    return render_template('h_index.html', result=conferences_list, end_year=end_year, conference_list=conference_list)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_hindex'))


def x_setup_hindex_routes__mutmut_40(app):
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
                                           start_year=start_year, conference_list=conference_list)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_hindex'))


def x_setup_hindex_routes__mutmut_41(app):
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
                                           start_year=start_year, end_year=end_year,)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_hindex'))


def x_setup_hindex_routes__mutmut_42(app):
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
        return redirect(url_for('XXshow_hindexXX'))

x_setup_hindex_routes__mutmut_mutants = {
'x_setup_hindex_routes__mutmut_1': x_setup_hindex_routes__mutmut_1, 
    'x_setup_hindex_routes__mutmut_2': x_setup_hindex_routes__mutmut_2, 
    'x_setup_hindex_routes__mutmut_3': x_setup_hindex_routes__mutmut_3, 
    'x_setup_hindex_routes__mutmut_4': x_setup_hindex_routes__mutmut_4, 
    'x_setup_hindex_routes__mutmut_5': x_setup_hindex_routes__mutmut_5, 
    'x_setup_hindex_routes__mutmut_6': x_setup_hindex_routes__mutmut_6, 
    'x_setup_hindex_routes__mutmut_7': x_setup_hindex_routes__mutmut_7, 
    'x_setup_hindex_routes__mutmut_8': x_setup_hindex_routes__mutmut_8, 
    'x_setup_hindex_routes__mutmut_9': x_setup_hindex_routes__mutmut_9, 
    'x_setup_hindex_routes__mutmut_10': x_setup_hindex_routes__mutmut_10, 
    'x_setup_hindex_routes__mutmut_11': x_setup_hindex_routes__mutmut_11, 
    'x_setup_hindex_routes__mutmut_12': x_setup_hindex_routes__mutmut_12, 
    'x_setup_hindex_routes__mutmut_13': x_setup_hindex_routes__mutmut_13, 
    'x_setup_hindex_routes__mutmut_14': x_setup_hindex_routes__mutmut_14, 
    'x_setup_hindex_routes__mutmut_15': x_setup_hindex_routes__mutmut_15, 
    'x_setup_hindex_routes__mutmut_16': x_setup_hindex_routes__mutmut_16, 
    'x_setup_hindex_routes__mutmut_17': x_setup_hindex_routes__mutmut_17, 
    'x_setup_hindex_routes__mutmut_18': x_setup_hindex_routes__mutmut_18, 
    'x_setup_hindex_routes__mutmut_19': x_setup_hindex_routes__mutmut_19, 
    'x_setup_hindex_routes__mutmut_20': x_setup_hindex_routes__mutmut_20, 
    'x_setup_hindex_routes__mutmut_21': x_setup_hindex_routes__mutmut_21, 
    'x_setup_hindex_routes__mutmut_22': x_setup_hindex_routes__mutmut_22, 
    'x_setup_hindex_routes__mutmut_23': x_setup_hindex_routes__mutmut_23, 
    'x_setup_hindex_routes__mutmut_24': x_setup_hindex_routes__mutmut_24, 
    'x_setup_hindex_routes__mutmut_25': x_setup_hindex_routes__mutmut_25, 
    'x_setup_hindex_routes__mutmut_26': x_setup_hindex_routes__mutmut_26, 
    'x_setup_hindex_routes__mutmut_27': x_setup_hindex_routes__mutmut_27, 
    'x_setup_hindex_routes__mutmut_28': x_setup_hindex_routes__mutmut_28, 
    'x_setup_hindex_routes__mutmut_29': x_setup_hindex_routes__mutmut_29, 
    'x_setup_hindex_routes__mutmut_30': x_setup_hindex_routes__mutmut_30, 
    'x_setup_hindex_routes__mutmut_31': x_setup_hindex_routes__mutmut_31, 
    'x_setup_hindex_routes__mutmut_32': x_setup_hindex_routes__mutmut_32, 
    'x_setup_hindex_routes__mutmut_33': x_setup_hindex_routes__mutmut_33, 
    'x_setup_hindex_routes__mutmut_34': x_setup_hindex_routes__mutmut_34, 
    'x_setup_hindex_routes__mutmut_35': x_setup_hindex_routes__mutmut_35, 
    'x_setup_hindex_routes__mutmut_36': x_setup_hindex_routes__mutmut_36, 
    'x_setup_hindex_routes__mutmut_37': x_setup_hindex_routes__mutmut_37, 
    'x_setup_hindex_routes__mutmut_38': x_setup_hindex_routes__mutmut_38, 
    'x_setup_hindex_routes__mutmut_39': x_setup_hindex_routes__mutmut_39, 
    'x_setup_hindex_routes__mutmut_40': x_setup_hindex_routes__mutmut_40, 
    'x_setup_hindex_routes__mutmut_41': x_setup_hindex_routes__mutmut_41, 
    'x_setup_hindex_routes__mutmut_42': x_setup_hindex_routes__mutmut_42
}

def setup_hindex_routes(*args, **kwargs):
    result = _mutmut_trampoline(x_setup_hindex_routes__mutmut_orig, x_setup_hindex_routes__mutmut_mutants, *args, **kwargs)
    return result 

setup_hindex_routes.__signature__ = _mutmut_signature(x_setup_hindex_routes__mutmut_orig)
x_setup_hindex_routes__mutmut_orig.__name__ = 'x_setup_hindex_routes'


