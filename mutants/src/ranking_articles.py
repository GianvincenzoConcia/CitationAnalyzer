
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


from flask import render_template, request, flash, redirect, url_for

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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




# Cerca una conferenza su DBLP utilizzando Selenium
# Restituisce il contenuto della pagina della conferenza

def x_search_conference__mutmut_orig(conference_title, driver):
    try:
        search_url = f"https://dblp.org/search?q={conference_title}"
        driver.get(search_url)

        try:
            first_result = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'result-list')))
            first_result.click()
        except TimeoutException:
            # If first_result is not present, check for the presence of toc-link
            try:
                driver.find_element(By.CLASS_NAME, 'toc-link')
                return driver.page_source
            except NoSuchElementException:
                flash(f"Conferenza {conference_title} non trovata", "error")
                return None
        return driver.page_source
    except TimeoutException:
        flash(f"Conferenza {conference_title} non trovata", "error")
        return None


# Cerca una conferenza su DBLP utilizzando Selenium
# Restituisce il contenuto della pagina della conferenza

def x_search_conference__mutmut_1(conference_title, driver):
    try:
        search_url = None
        driver.get(search_url)

        try:
            first_result = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'result-list')))
            first_result.click()
        except TimeoutException:
            # If first_result is not present, check for the presence of toc-link
            try:
                driver.find_element(By.CLASS_NAME, 'toc-link')
                return driver.page_source
            except NoSuchElementException:
                flash(f"Conferenza {conference_title} non trovata", "error")
                return None
        return driver.page_source
    except TimeoutException:
        flash(f"Conferenza {conference_title} non trovata", "error")
        return None


# Cerca una conferenza su DBLP utilizzando Selenium
# Restituisce il contenuto della pagina della conferenza

def x_search_conference__mutmut_2(conference_title, driver):
    try:
        search_url = f"https://dblp.org/search?q={conference_title}"
        driver.get(None)

        try:
            first_result = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'result-list')))
            first_result.click()
        except TimeoutException:
            # If first_result is not present, check for the presence of toc-link
            try:
                driver.find_element(By.CLASS_NAME, 'toc-link')
                return driver.page_source
            except NoSuchElementException:
                flash(f"Conferenza {conference_title} non trovata", "error")
                return None
        return driver.page_source
    except TimeoutException:
        flash(f"Conferenza {conference_title} non trovata", "error")
        return None


# Cerca una conferenza su DBLP utilizzando Selenium
# Restituisce il contenuto della pagina della conferenza

def x_search_conference__mutmut_3(conference_title, driver):
    try:
        search_url = f"https://dblp.org/search?q={conference_title}"
        driver.get(search_url)

        try:
            first_result = WebDriverWait(None, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'result-list')))
            first_result.click()
        except TimeoutException:
            # If first_result is not present, check for the presence of toc-link
            try:
                driver.find_element(By.CLASS_NAME, 'toc-link')
                return driver.page_source
            except NoSuchElementException:
                flash(f"Conferenza {conference_title} non trovata", "error")
                return None
        return driver.page_source
    except TimeoutException:
        flash(f"Conferenza {conference_title} non trovata", "error")
        return None


# Cerca una conferenza su DBLP utilizzando Selenium
# Restituisce il contenuto della pagina della conferenza

def x_search_conference__mutmut_4(conference_title, driver):
    try:
        search_url = f"https://dblp.org/search?q={conference_title}"
        driver.get(search_url)

        try:
            first_result = WebDriverWait(driver, 11).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'result-list')))
            first_result.click()
        except TimeoutException:
            # If first_result is not present, check for the presence of toc-link
            try:
                driver.find_element(By.CLASS_NAME, 'toc-link')
                return driver.page_source
            except NoSuchElementException:
                flash(f"Conferenza {conference_title} non trovata", "error")
                return None
        return driver.page_source
    except TimeoutException:
        flash(f"Conferenza {conference_title} non trovata", "error")
        return None


# Cerca una conferenza su DBLP utilizzando Selenium
# Restituisce il contenuto della pagina della conferenza

def x_search_conference__mutmut_5(conference_title, driver):
    try:
        search_url = f"https://dblp.org/search?q={conference_title}"
        driver.get(search_url)

        try:
            first_result = WebDriverWait( 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'result-list')))
            first_result.click()
        except TimeoutException:
            # If first_result is not present, check for the presence of toc-link
            try:
                driver.find_element(By.CLASS_NAME, 'toc-link')
                return driver.page_source
            except NoSuchElementException:
                flash(f"Conferenza {conference_title} non trovata", "error")
                return None
        return driver.page_source
    except TimeoutException:
        flash(f"Conferenza {conference_title} non trovata", "error")
        return None


# Cerca una conferenza su DBLP utilizzando Selenium
# Restituisce il contenuto della pagina della conferenza

def x_search_conference__mutmut_6(conference_title, driver):
    try:
        search_url = f"https://dblp.org/search?q={conference_title}"
        driver.get(search_url)

        try:
            first_result = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'XXresult-listXX')))
            first_result.click()
        except TimeoutException:
            # If first_result is not present, check for the presence of toc-link
            try:
                driver.find_element(By.CLASS_NAME, 'toc-link')
                return driver.page_source
            except NoSuchElementException:
                flash(f"Conferenza {conference_title} non trovata", "error")
                return None
        return driver.page_source
    except TimeoutException:
        flash(f"Conferenza {conference_title} non trovata", "error")
        return None


# Cerca una conferenza su DBLP utilizzando Selenium
# Restituisce il contenuto della pagina della conferenza

def x_search_conference__mutmut_7(conference_title, driver):
    try:
        search_url = f"https://dblp.org/search?q={conference_title}"
        driver.get(search_url)

        try:
            first_result = None
            first_result.click()
        except TimeoutException:
            # If first_result is not present, check for the presence of toc-link
            try:
                driver.find_element(By.CLASS_NAME, 'toc-link')
                return driver.page_source
            except NoSuchElementException:
                flash(f"Conferenza {conference_title} non trovata", "error")
                return None
        return driver.page_source
    except TimeoutException:
        flash(f"Conferenza {conference_title} non trovata", "error")
        return None


# Cerca una conferenza su DBLP utilizzando Selenium
# Restituisce il contenuto della pagina della conferenza

def x_search_conference__mutmut_8(conference_title, driver):
    try:
        search_url = f"https://dblp.org/search?q={conference_title}"
        driver.get(search_url)

        try:
            first_result = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'result-list')))
            first_result.click()
        except TimeoutException:
            # If first_result is not present, check for the presence of toc-link
            try:
                driver.find_element(By.CLASS_NAME, 'XXtoc-linkXX')
                return driver.page_source
            except NoSuchElementException:
                flash(f"Conferenza {conference_title} non trovata", "error")
                return None
        return driver.page_source
    except TimeoutException:
        flash(f"Conferenza {conference_title} non trovata", "error")
        return None


# Cerca una conferenza su DBLP utilizzando Selenium
# Restituisce il contenuto della pagina della conferenza

def x_search_conference__mutmut_9(conference_title, driver):
    try:
        search_url = f"https://dblp.org/search?q={conference_title}"
        driver.get(search_url)

        try:
            first_result = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'result-list')))
            first_result.click()
        except TimeoutException:
            # If first_result is not present, check for the presence of toc-link
            try:
                driver.find_element(By.CLASS_NAME, 'toc-link')
                return driver.page_source
            except NoSuchElementException:
                flash(f"Conferenza {conference_title} non trovata", "XXerrorXX")
                return None
        return driver.page_source
    except TimeoutException:
        flash(f"Conferenza {conference_title} non trovata", "error")
        return None


# Cerca una conferenza su DBLP utilizzando Selenium
# Restituisce il contenuto della pagina della conferenza

def x_search_conference__mutmut_10(conference_title, driver):
    try:
        search_url = f"https://dblp.org/search?q={conference_title}"
        driver.get(search_url)

        try:
            first_result = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'result-list')))
            first_result.click()
        except TimeoutException:
            # If first_result is not present, check for the presence of toc-link
            try:
                driver.find_element(By.CLASS_NAME, 'toc-link')
                return driver.page_source
            except NoSuchElementException:
                flash(f"Conferenza {conference_title} non trovata", "error")
                return None
        return driver.page_source
    except TimeoutException:
        flash(f"Conferenza {conference_title} non trovata", "XXerrorXX")
        return None

x_search_conference__mutmut_mutants = {
'x_search_conference__mutmut_1': x_search_conference__mutmut_1, 
    'x_search_conference__mutmut_2': x_search_conference__mutmut_2, 
    'x_search_conference__mutmut_3': x_search_conference__mutmut_3, 
    'x_search_conference__mutmut_4': x_search_conference__mutmut_4, 
    'x_search_conference__mutmut_5': x_search_conference__mutmut_5, 
    'x_search_conference__mutmut_6': x_search_conference__mutmut_6, 
    'x_search_conference__mutmut_7': x_search_conference__mutmut_7, 
    'x_search_conference__mutmut_8': x_search_conference__mutmut_8, 
    'x_search_conference__mutmut_9': x_search_conference__mutmut_9, 
    'x_search_conference__mutmut_10': x_search_conference__mutmut_10
}

def search_conference(*args, **kwargs):
    result = _mutmut_trampoline(x_search_conference__mutmut_orig, x_search_conference__mutmut_mutants, *args, **kwargs)
    return result 

search_conference.__signature__ = _mutmut_signature(x_search_conference__mutmut_orig)
x_search_conference__mutmut_orig.__name__ = 'x_search_conference'




# Trova l'anno della conferenza
# Restituisce l'elemento dell'anno o None se non trovato
def x_get_year_element__mutmut_orig(soup, conference_year):
    year_element = soup.find('span', {'itemprop': 'datePublished'},
                             string=lambda text: str(conference_year) in text)

    if not year_element:
        flash(f"Anno della conferenza {conference_year} non trovato.", 'error')
        return None

    return year_element


# Trova l'anno della conferenza
# Restituisce l'elemento dell'anno o None se non trovato
def x_get_year_element__mutmut_1(soup, conference_year):
    year_element = soup.find('XXspanXX', {'itemprop': 'datePublished'},
                             string=lambda text: str(conference_year) in text)

    if not year_element:
        flash(f"Anno della conferenza {conference_year} non trovato.", 'error')
        return None

    return year_element


# Trova l'anno della conferenza
# Restituisce l'elemento dell'anno o None se non trovato
def x_get_year_element__mutmut_2(soup, conference_year):
    year_element = soup.find('span', {'XXitempropXX': 'datePublished'},
                             string=lambda text: str(conference_year) in text)

    if not year_element:
        flash(f"Anno della conferenza {conference_year} non trovato.", 'error')
        return None

    return year_element


# Trova l'anno della conferenza
# Restituisce l'elemento dell'anno o None se non trovato
def x_get_year_element__mutmut_3(soup, conference_year):
    year_element = soup.find('span', {'itemprop': 'XXdatePublishedXX'},
                             string=lambda text: str(conference_year) in text)

    if not year_element:
        flash(f"Anno della conferenza {conference_year} non trovato.", 'error')
        return None

    return year_element


# Trova l'anno della conferenza
# Restituisce l'elemento dell'anno o None se non trovato
def x_get_year_element__mutmut_4(soup, conference_year):
    year_element = soup.find('span', {'itemprop': 'datePublished'},
                             string=lambda text: str(None) in text)

    if not year_element:
        flash(f"Anno della conferenza {conference_year} non trovato.", 'error')
        return None

    return year_element


# Trova l'anno della conferenza
# Restituisce l'elemento dell'anno o None se non trovato
def x_get_year_element__mutmut_5(soup, conference_year):
    year_element = soup.find('span', {'itemprop': 'datePublished'},
                             string=lambda text: str(conference_year) not in text)

    if not year_element:
        flash(f"Anno della conferenza {conference_year} non trovato.", 'error')
        return None

    return year_element


# Trova l'anno della conferenza
# Restituisce l'elemento dell'anno o None se non trovato
def x_get_year_element__mutmut_6(soup, conference_year):
    year_element = soup.find('span', {'itemprop': 'datePublished'},
                             string=lambda text: None)

    if not year_element:
        flash(f"Anno della conferenza {conference_year} non trovato.", 'error')
        return None

    return year_element


# Trova l'anno della conferenza
# Restituisce l'elemento dell'anno o None se non trovato
def x_get_year_element__mutmut_7(soup, conference_year):
    year_element = soup.find('span', {'itemprop': 'datePublished'},)

    if not year_element:
        flash(f"Anno della conferenza {conference_year} non trovato.", 'error')
        return None

    return year_element


# Trova l'anno della conferenza
# Restituisce l'elemento dell'anno o None se non trovato
def x_get_year_element__mutmut_8(soup, conference_year):
    year_element = None

    if not year_element:
        flash(f"Anno della conferenza {conference_year} non trovato.", 'error')
        return None

    return year_element


# Trova l'anno della conferenza
# Restituisce l'elemento dell'anno o None se non trovato
def x_get_year_element__mutmut_9(soup, conference_year):
    year_element = soup.find('span', {'itemprop': 'datePublished'},
                             string=lambda text: str(conference_year) in text)

    if  year_element:
        flash(f"Anno della conferenza {conference_year} non trovato.", 'error')
        return None

    return year_element


# Trova l'anno della conferenza
# Restituisce l'elemento dell'anno o None se non trovato
def x_get_year_element__mutmut_10(soup, conference_year):
    year_element = soup.find('span', {'itemprop': 'datePublished'},
                             string=lambda text: str(conference_year) in text)

    if not year_element:
        flash(f"Anno della conferenza {conference_year} non trovato.", 'XXerrorXX')
        return None

    return year_element

x_get_year_element__mutmut_mutants = {
'x_get_year_element__mutmut_1': x_get_year_element__mutmut_1, 
    'x_get_year_element__mutmut_2': x_get_year_element__mutmut_2, 
    'x_get_year_element__mutmut_3': x_get_year_element__mutmut_3, 
    'x_get_year_element__mutmut_4': x_get_year_element__mutmut_4, 
    'x_get_year_element__mutmut_5': x_get_year_element__mutmut_5, 
    'x_get_year_element__mutmut_6': x_get_year_element__mutmut_6, 
    'x_get_year_element__mutmut_7': x_get_year_element__mutmut_7, 
    'x_get_year_element__mutmut_8': x_get_year_element__mutmut_8, 
    'x_get_year_element__mutmut_9': x_get_year_element__mutmut_9, 
    'x_get_year_element__mutmut_10': x_get_year_element__mutmut_10
}

def get_year_element(*args, **kwargs):
    result = _mutmut_trampoline(x_get_year_element__mutmut_orig, x_get_year_element__mutmut_mutants, *args, **kwargs)
    return result 

get_year_element.__signature__ = _mutmut_signature(x_get_year_element__mutmut_orig)
x_get_year_element__mutmut_orig.__name__ = 'x_get_year_element'




# Entra nella pagina contents della conferenza che contiene gli articoli citati
# Restituisce il contenuto della pagina contents
def x_get_contents_link__mutmut_orig(year_element, driver):
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


# Entra nella pagina contents della conferenza che contiene gli articoli citati
# Restituisce il contenuto della pagina contents
def x_get_contents_link__mutmut_1(year_element, driver):
    contents_line = year_element.find_next('XXaXX', {'class': 'toc-link'})
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


# Entra nella pagina contents della conferenza che contiene gli articoli citati
# Restituisce il contenuto della pagina contents
def x_get_contents_link__mutmut_2(year_element, driver):
    contents_line = year_element.find_next('a', {'XXclassXX': 'toc-link'})
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


# Entra nella pagina contents della conferenza che contiene gli articoli citati
# Restituisce il contenuto della pagina contents
def x_get_contents_link__mutmut_3(year_element, driver):
    contents_line = year_element.find_next('a', {'class': 'XXtoc-linkXX'})
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


# Entra nella pagina contents della conferenza che contiene gli articoli citati
# Restituisce il contenuto della pagina contents
def x_get_contents_link__mutmut_4(year_element, driver):
    contents_line = None
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


# Entra nella pagina contents della conferenza che contiene gli articoli citati
# Restituisce il contenuto della pagina contents
def x_get_contents_link__mutmut_5(year_element, driver):
    contents_line = year_element.find_next('a', {'class': 'toc-link'})
    if contents_line:
        try:
            driver.get(contents_line['XXhrefXX'])
            return driver.page_source
        except TimeoutException:
            flash("Timeout durante il caricamento della pagina dei contenuti", 'error')
            return None
    else:
        flash("Nessun articolo trovato", 'error')
        return None


# Entra nella pagina contents della conferenza che contiene gli articoli citati
# Restituisce il contenuto della pagina contents
def x_get_contents_link__mutmut_6(year_element, driver):
    contents_line = year_element.find_next('a', {'class': 'toc-link'})
    if contents_line:
        try:
            driver.get(contents_line[None])
            return driver.page_source
        except TimeoutException:
            flash("Timeout durante il caricamento della pagina dei contenuti", 'error')
            return None
    else:
        flash("Nessun articolo trovato", 'error')
        return None


# Entra nella pagina contents della conferenza che contiene gli articoli citati
# Restituisce il contenuto della pagina contents
def x_get_contents_link__mutmut_7(year_element, driver):
    contents_line = year_element.find_next('a', {'class': 'toc-link'})
    if contents_line:
        try:
            driver.get(contents_line['href'])
            return driver.page_source
        except TimeoutException:
            flash("XXTimeout durante il caricamento della pagina dei contenutiXX", 'error')
            return None
    else:
        flash("Nessun articolo trovato", 'error')
        return None


# Entra nella pagina contents della conferenza che contiene gli articoli citati
# Restituisce il contenuto della pagina contents
def x_get_contents_link__mutmut_8(year_element, driver):
    contents_line = year_element.find_next('a', {'class': 'toc-link'})
    if contents_line:
        try:
            driver.get(contents_line['href'])
            return driver.page_source
        except TimeoutException:
            flash("Timeout durante il caricamento della pagina dei contenuti", 'XXerrorXX')
            return None
    else:
        flash("Nessun articolo trovato", 'error')
        return None


# Entra nella pagina contents della conferenza che contiene gli articoli citati
# Restituisce il contenuto della pagina contents
def x_get_contents_link__mutmut_9(year_element, driver):
    contents_line = year_element.find_next('a', {'class': 'toc-link'})
    if contents_line:
        try:
            driver.get(contents_line['href'])
            return driver.page_source
        except TimeoutException:
            flash("Timeout durante il caricamento della pagina dei contenuti", 'error')
            return None
    else:
        flash("XXNessun articolo trovatoXX", 'error')
        return None


# Entra nella pagina contents della conferenza che contiene gli articoli citati
# Restituisce il contenuto della pagina contents
def x_get_contents_link__mutmut_10(year_element, driver):
    contents_line = year_element.find_next('a', {'class': 'toc-link'})
    if contents_line:
        try:
            driver.get(contents_line['href'])
            return driver.page_source
        except TimeoutException:
            flash("Timeout durante il caricamento della pagina dei contenuti", 'error')
            return None
    else:
        flash("Nessun articolo trovato", 'XXerrorXX')
        return None

x_get_contents_link__mutmut_mutants = {
'x_get_contents_link__mutmut_1': x_get_contents_link__mutmut_1, 
    'x_get_contents_link__mutmut_2': x_get_contents_link__mutmut_2, 
    'x_get_contents_link__mutmut_3': x_get_contents_link__mutmut_3, 
    'x_get_contents_link__mutmut_4': x_get_contents_link__mutmut_4, 
    'x_get_contents_link__mutmut_5': x_get_contents_link__mutmut_5, 
    'x_get_contents_link__mutmut_6': x_get_contents_link__mutmut_6, 
    'x_get_contents_link__mutmut_7': x_get_contents_link__mutmut_7, 
    'x_get_contents_link__mutmut_8': x_get_contents_link__mutmut_8, 
    'x_get_contents_link__mutmut_9': x_get_contents_link__mutmut_9, 
    'x_get_contents_link__mutmut_10': x_get_contents_link__mutmut_10
}

def get_contents_link(*args, **kwargs):
    result = _mutmut_trampoline(x_get_contents_link__mutmut_orig, x_get_contents_link__mutmut_mutants, *args, **kwargs)
    return result 

get_contents_link.__signature__ = _mutmut_signature(x_get_contents_link__mutmut_orig)
x_get_contents_link__mutmut_orig.__name__ = 'x_get_contents_link'




def x_get_block_elements__mutmut_orig(page_source):
    soup = BeautifulSoup(page_source, 'html.parser')
    return soup.find_all("cite", attrs={"class": "data tts-content"})


def x_get_block_elements__mutmut_1(page_source):
    soup = BeautifulSoup(None, 'html.parser')
    return soup.find_all("cite", attrs={"class": "data tts-content"})


def x_get_block_elements__mutmut_2(page_source):
    soup = BeautifulSoup(page_source, 'XXhtml.parserXX')
    return soup.find_all("cite", attrs={"class": "data tts-content"})


def x_get_block_elements__mutmut_3(page_source):
    soup = BeautifulSoup( 'html.parser')
    return soup.find_all("cite", attrs={"class": "data tts-content"})


def x_get_block_elements__mutmut_4(page_source):
    soup = None
    return soup.find_all("cite", attrs={"class": "data tts-content"})


def x_get_block_elements__mutmut_5(page_source):
    soup = BeautifulSoup(page_source, 'html.parser')
    return soup.find_all("XXciteXX", attrs={"class": "data tts-content"})


def x_get_block_elements__mutmut_6(page_source):
    soup = BeautifulSoup(page_source, 'html.parser')
    return soup.find_all("cite", attrs={"XXclassXX": "data tts-content"})


def x_get_block_elements__mutmut_7(page_source):
    soup = BeautifulSoup(page_source, 'html.parser')
    return soup.find_all("cite", attrs={"class": "XXdata tts-contentXX"})


def x_get_block_elements__mutmut_8(page_source):
    soup = BeautifulSoup(page_source, 'html.parser')
    return soup.find_all("cite",)

x_get_block_elements__mutmut_mutants = {
'x_get_block_elements__mutmut_1': x_get_block_elements__mutmut_1, 
    'x_get_block_elements__mutmut_2': x_get_block_elements__mutmut_2, 
    'x_get_block_elements__mutmut_3': x_get_block_elements__mutmut_3, 
    'x_get_block_elements__mutmut_4': x_get_block_elements__mutmut_4, 
    'x_get_block_elements__mutmut_5': x_get_block_elements__mutmut_5, 
    'x_get_block_elements__mutmut_6': x_get_block_elements__mutmut_6, 
    'x_get_block_elements__mutmut_7': x_get_block_elements__mutmut_7, 
    'x_get_block_elements__mutmut_8': x_get_block_elements__mutmut_8
}

def get_block_elements(*args, **kwargs):
    result = _mutmut_trampoline(x_get_block_elements__mutmut_orig, x_get_block_elements__mutmut_mutants, *args, **kwargs)
    return result 

get_block_elements.__signature__ = _mutmut_signature(x_get_block_elements__mutmut_orig)
x_get_block_elements__mutmut_orig.__name__ = 'x_get_block_elements'




# Restituisce i dati degli articoli con titolo, autori e numero di citazioni in ordine di numero
def x_get_article_data_list__mutmut_orig(block_elements):
    article_data_list = []

    for i in range(1, len(block_elements)):
        authors = block_elements[i].find_all("span", attrs={"itemprop": "author"})
        author_list = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
        article_title = block_elements[i].find("span", attrs={"class": "title"}).text.strip()
        numero_citazioni = get_citations(article_title)

        article_data_list.append((article_title, author_list, int(numero_citazioni)))

    article_data_list.sort(reverse=True, key=lambda x: x[2])
    return article_data_list


# Restituisce i dati degli articoli con titolo, autori e numero di citazioni in ordine di numero
def x_get_article_data_list__mutmut_1(block_elements):
    article_data_list = None

    for i in range(1, len(block_elements)):
        authors = block_elements[i].find_all("span", attrs={"itemprop": "author"})
        author_list = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
        article_title = block_elements[i].find("span", attrs={"class": "title"}).text.strip()
        numero_citazioni = get_citations(article_title)

        article_data_list.append((article_title, author_list, int(numero_citazioni)))

    article_data_list.sort(reverse=True, key=lambda x: x[2])
    return article_data_list


# Restituisce i dati degli articoli con titolo, autori e numero di citazioni in ordine di numero
def x_get_article_data_list__mutmut_2(block_elements):
    article_data_list = []

    for i in range(2, len(block_elements)):
        authors = block_elements[i].find_all("span", attrs={"itemprop": "author"})
        author_list = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
        article_title = block_elements[i].find("span", attrs={"class": "title"}).text.strip()
        numero_citazioni = get_citations(article_title)

        article_data_list.append((article_title, author_list, int(numero_citazioni)))

    article_data_list.sort(reverse=True, key=lambda x: x[2])
    return article_data_list


# Restituisce i dati degli articoli con titolo, autori e numero di citazioni in ordine di numero
def x_get_article_data_list__mutmut_3(block_elements):
    article_data_list = []

    for i in range(1, len(block_elements)):
        authors = block_elements[None].find_all("span", attrs={"itemprop": "author"})
        author_list = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
        article_title = block_elements[i].find("span", attrs={"class": "title"}).text.strip()
        numero_citazioni = get_citations(article_title)

        article_data_list.append((article_title, author_list, int(numero_citazioni)))

    article_data_list.sort(reverse=True, key=lambda x: x[2])
    return article_data_list


# Restituisce i dati degli articoli con titolo, autori e numero di citazioni in ordine di numero
def x_get_article_data_list__mutmut_4(block_elements):
    article_data_list = []

    for i in range(1, len(block_elements)):
        authors = block_elements[i].find_all("XXspanXX", attrs={"itemprop": "author"})
        author_list = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
        article_title = block_elements[i].find("span", attrs={"class": "title"}).text.strip()
        numero_citazioni = get_citations(article_title)

        article_data_list.append((article_title, author_list, int(numero_citazioni)))

    article_data_list.sort(reverse=True, key=lambda x: x[2])
    return article_data_list


# Restituisce i dati degli articoli con titolo, autori e numero di citazioni in ordine di numero
def x_get_article_data_list__mutmut_5(block_elements):
    article_data_list = []

    for i in range(1, len(block_elements)):
        authors = block_elements[i].find_all("span", attrs={"XXitempropXX": "author"})
        author_list = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
        article_title = block_elements[i].find("span", attrs={"class": "title"}).text.strip()
        numero_citazioni = get_citations(article_title)

        article_data_list.append((article_title, author_list, int(numero_citazioni)))

    article_data_list.sort(reverse=True, key=lambda x: x[2])
    return article_data_list


# Restituisce i dati degli articoli con titolo, autori e numero di citazioni in ordine di numero
def x_get_article_data_list__mutmut_6(block_elements):
    article_data_list = []

    for i in range(1, len(block_elements)):
        authors = block_elements[i].find_all("span", attrs={"itemprop": "XXauthorXX"})
        author_list = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
        article_title = block_elements[i].find("span", attrs={"class": "title"}).text.strip()
        numero_citazioni = get_citations(article_title)

        article_data_list.append((article_title, author_list, int(numero_citazioni)))

    article_data_list.sort(reverse=True, key=lambda x: x[2])
    return article_data_list


# Restituisce i dati degli articoli con titolo, autori e numero di citazioni in ordine di numero
def x_get_article_data_list__mutmut_7(block_elements):
    article_data_list = []

    for i in range(1, len(block_elements)):
        authors = block_elements[i].find_all("span",)
        author_list = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
        article_title = block_elements[i].find("span", attrs={"class": "title"}).text.strip()
        numero_citazioni = get_citations(article_title)

        article_data_list.append((article_title, author_list, int(numero_citazioni)))

    article_data_list.sort(reverse=True, key=lambda x: x[2])
    return article_data_list


# Restituisce i dati degli articoli con titolo, autori e numero di citazioni in ordine di numero
def x_get_article_data_list__mutmut_8(block_elements):
    article_data_list = []

    for i in range(1, len(block_elements)):
        authors = None
        author_list = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
        article_title = block_elements[i].find("span", attrs={"class": "title"}).text.strip()
        numero_citazioni = get_citations(article_title)

        article_data_list.append((article_title, author_list, int(numero_citazioni)))

    article_data_list.sort(reverse=True, key=lambda x: x[2])
    return article_data_list


# Restituisce i dati degli articoli con titolo, autori e numero di citazioni in ordine di numero
def x_get_article_data_list__mutmut_9(block_elements):
    article_data_list = []

    for i in range(1, len(block_elements)):
        authors = block_elements[i].find_all("span", attrs={"itemprop": "author"})
        author_list = [author.find("XXspanXX", attrs={"itemprop": "name"}).text.strip() for author in authors]
        article_title = block_elements[i].find("span", attrs={"class": "title"}).text.strip()
        numero_citazioni = get_citations(article_title)

        article_data_list.append((article_title, author_list, int(numero_citazioni)))

    article_data_list.sort(reverse=True, key=lambda x: x[2])
    return article_data_list


# Restituisce i dati degli articoli con titolo, autori e numero di citazioni in ordine di numero
def x_get_article_data_list__mutmut_10(block_elements):
    article_data_list = []

    for i in range(1, len(block_elements)):
        authors = block_elements[i].find_all("span", attrs={"itemprop": "author"})
        author_list = [author.find("span", attrs={"XXitempropXX": "name"}).text.strip() for author in authors]
        article_title = block_elements[i].find("span", attrs={"class": "title"}).text.strip()
        numero_citazioni = get_citations(article_title)

        article_data_list.append((article_title, author_list, int(numero_citazioni)))

    article_data_list.sort(reverse=True, key=lambda x: x[2])
    return article_data_list


# Restituisce i dati degli articoli con titolo, autori e numero di citazioni in ordine di numero
def x_get_article_data_list__mutmut_11(block_elements):
    article_data_list = []

    for i in range(1, len(block_elements)):
        authors = block_elements[i].find_all("span", attrs={"itemprop": "author"})
        author_list = [author.find("span", attrs={"itemprop": "XXnameXX"}).text.strip() for author in authors]
        article_title = block_elements[i].find("span", attrs={"class": "title"}).text.strip()
        numero_citazioni = get_citations(article_title)

        article_data_list.append((article_title, author_list, int(numero_citazioni)))

    article_data_list.sort(reverse=True, key=lambda x: x[2])
    return article_data_list


# Restituisce i dati degli articoli con titolo, autori e numero di citazioni in ordine di numero
def x_get_article_data_list__mutmut_12(block_elements):
    article_data_list = []

    for i in range(1, len(block_elements)):
        authors = block_elements[i].find_all("span", attrs={"itemprop": "author"})
        author_list = [author.find("span",).text.strip() for author in authors]
        article_title = block_elements[i].find("span", attrs={"class": "title"}).text.strip()
        numero_citazioni = get_citations(article_title)

        article_data_list.append((article_title, author_list, int(numero_citazioni)))

    article_data_list.sort(reverse=True, key=lambda x: x[2])
    return article_data_list


# Restituisce i dati degli articoli con titolo, autori e numero di citazioni in ordine di numero
def x_get_article_data_list__mutmut_13(block_elements):
    article_data_list = []

    for i in range(1, len(block_elements)):
        authors = block_elements[i].find_all("span", attrs={"itemprop": "author"})
        author_list = None
        article_title = block_elements[i].find("span", attrs={"class": "title"}).text.strip()
        numero_citazioni = get_citations(article_title)

        article_data_list.append((article_title, author_list, int(numero_citazioni)))

    article_data_list.sort(reverse=True, key=lambda x: x[2])
    return article_data_list


# Restituisce i dati degli articoli con titolo, autori e numero di citazioni in ordine di numero
def x_get_article_data_list__mutmut_14(block_elements):
    article_data_list = []

    for i in range(1, len(block_elements)):
        authors = block_elements[i].find_all("span", attrs={"itemprop": "author"})
        author_list = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
        article_title = block_elements[None].find("span", attrs={"class": "title"}).text.strip()
        numero_citazioni = get_citations(article_title)

        article_data_list.append((article_title, author_list, int(numero_citazioni)))

    article_data_list.sort(reverse=True, key=lambda x: x[2])
    return article_data_list


# Restituisce i dati degli articoli con titolo, autori e numero di citazioni in ordine di numero
def x_get_article_data_list__mutmut_15(block_elements):
    article_data_list = []

    for i in range(1, len(block_elements)):
        authors = block_elements[i].find_all("span", attrs={"itemprop": "author"})
        author_list = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
        article_title = block_elements[i].find("XXspanXX", attrs={"class": "title"}).text.strip()
        numero_citazioni = get_citations(article_title)

        article_data_list.append((article_title, author_list, int(numero_citazioni)))

    article_data_list.sort(reverse=True, key=lambda x: x[2])
    return article_data_list


# Restituisce i dati degli articoli con titolo, autori e numero di citazioni in ordine di numero
def x_get_article_data_list__mutmut_16(block_elements):
    article_data_list = []

    for i in range(1, len(block_elements)):
        authors = block_elements[i].find_all("span", attrs={"itemprop": "author"})
        author_list = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
        article_title = block_elements[i].find("span", attrs={"XXclassXX": "title"}).text.strip()
        numero_citazioni = get_citations(article_title)

        article_data_list.append((article_title, author_list, int(numero_citazioni)))

    article_data_list.sort(reverse=True, key=lambda x: x[2])
    return article_data_list


# Restituisce i dati degli articoli con titolo, autori e numero di citazioni in ordine di numero
def x_get_article_data_list__mutmut_17(block_elements):
    article_data_list = []

    for i in range(1, len(block_elements)):
        authors = block_elements[i].find_all("span", attrs={"itemprop": "author"})
        author_list = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
        article_title = block_elements[i].find("span", attrs={"class": "XXtitleXX"}).text.strip()
        numero_citazioni = get_citations(article_title)

        article_data_list.append((article_title, author_list, int(numero_citazioni)))

    article_data_list.sort(reverse=True, key=lambda x: x[2])
    return article_data_list


# Restituisce i dati degli articoli con titolo, autori e numero di citazioni in ordine di numero
def x_get_article_data_list__mutmut_18(block_elements):
    article_data_list = []

    for i in range(1, len(block_elements)):
        authors = block_elements[i].find_all("span", attrs={"itemprop": "author"})
        author_list = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
        article_title = block_elements[i].find("span",).text.strip()
        numero_citazioni = get_citations(article_title)

        article_data_list.append((article_title, author_list, int(numero_citazioni)))

    article_data_list.sort(reverse=True, key=lambda x: x[2])
    return article_data_list


# Restituisce i dati degli articoli con titolo, autori e numero di citazioni in ordine di numero
def x_get_article_data_list__mutmut_19(block_elements):
    article_data_list = []

    for i in range(1, len(block_elements)):
        authors = block_elements[i].find_all("span", attrs={"itemprop": "author"})
        author_list = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
        article_title = None
        numero_citazioni = get_citations(article_title)

        article_data_list.append((article_title, author_list, int(numero_citazioni)))

    article_data_list.sort(reverse=True, key=lambda x: x[2])
    return article_data_list


# Restituisce i dati degli articoli con titolo, autori e numero di citazioni in ordine di numero
def x_get_article_data_list__mutmut_20(block_elements):
    article_data_list = []

    for i in range(1, len(block_elements)):
        authors = block_elements[i].find_all("span", attrs={"itemprop": "author"})
        author_list = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
        article_title = block_elements[i].find("span", attrs={"class": "title"}).text.strip()
        numero_citazioni = get_citations(None)

        article_data_list.append((article_title, author_list, int(numero_citazioni)))

    article_data_list.sort(reverse=True, key=lambda x: x[2])
    return article_data_list


# Restituisce i dati degli articoli con titolo, autori e numero di citazioni in ordine di numero
def x_get_article_data_list__mutmut_21(block_elements):
    article_data_list = []

    for i in range(1, len(block_elements)):
        authors = block_elements[i].find_all("span", attrs={"itemprop": "author"})
        author_list = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
        article_title = block_elements[i].find("span", attrs={"class": "title"}).text.strip()
        numero_citazioni = None

        article_data_list.append((article_title, author_list, int(numero_citazioni)))

    article_data_list.sort(reverse=True, key=lambda x: x[2])
    return article_data_list


# Restituisce i dati degli articoli con titolo, autori e numero di citazioni in ordine di numero
def x_get_article_data_list__mutmut_22(block_elements):
    article_data_list = []

    for i in range(1, len(block_elements)):
        authors = block_elements[i].find_all("span", attrs={"itemprop": "author"})
        author_list = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
        article_title = block_elements[i].find("span", attrs={"class": "title"}).text.strip()
        numero_citazioni = get_citations(article_title)

        article_data_list.append((article_title, author_list, int(None)))

    article_data_list.sort(reverse=True, key=lambda x: x[2])
    return article_data_list


# Restituisce i dati degli articoli con titolo, autori e numero di citazioni in ordine di numero
def x_get_article_data_list__mutmut_23(block_elements):
    article_data_list = []

    for i in range(1, len(block_elements)):
        authors = block_elements[i].find_all("span", attrs={"itemprop": "author"})
        author_list = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
        article_title = block_elements[i].find("span", attrs={"class": "title"}).text.strip()
        numero_citazioni = get_citations(article_title)

        article_data_list.append((article_title, author_list, int(numero_citazioni)))

    article_data_list.sort(reverse=False, key=lambda x: x[2])
    return article_data_list


# Restituisce i dati degli articoli con titolo, autori e numero di citazioni in ordine di numero
def x_get_article_data_list__mutmut_24(block_elements):
    article_data_list = []

    for i in range(1, len(block_elements)):
        authors = block_elements[i].find_all("span", attrs={"itemprop": "author"})
        author_list = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
        article_title = block_elements[i].find("span", attrs={"class": "title"}).text.strip()
        numero_citazioni = get_citations(article_title)

        article_data_list.append((article_title, author_list, int(numero_citazioni)))

    article_data_list.sort(reverse=True, key=lambda x: x[3])
    return article_data_list


# Restituisce i dati degli articoli con titolo, autori e numero di citazioni in ordine di numero
def x_get_article_data_list__mutmut_25(block_elements):
    article_data_list = []

    for i in range(1, len(block_elements)):
        authors = block_elements[i].find_all("span", attrs={"itemprop": "author"})
        author_list = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
        article_title = block_elements[i].find("span", attrs={"class": "title"}).text.strip()
        numero_citazioni = get_citations(article_title)

        article_data_list.append((article_title, author_list, int(numero_citazioni)))

    article_data_list.sort(reverse=True, key=lambda x: x[None])
    return article_data_list


# Restituisce i dati degli articoli con titolo, autori e numero di citazioni in ordine di numero
def x_get_article_data_list__mutmut_26(block_elements):
    article_data_list = []

    for i in range(1, len(block_elements)):
        authors = block_elements[i].find_all("span", attrs={"itemprop": "author"})
        author_list = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
        article_title = block_elements[i].find("span", attrs={"class": "title"}).text.strip()
        numero_citazioni = get_citations(article_title)

        article_data_list.append((article_title, author_list, int(numero_citazioni)))

    article_data_list.sort(reverse=True, key=lambda x: None)
    return article_data_list


# Restituisce i dati degli articoli con titolo, autori e numero di citazioni in ordine di numero
def x_get_article_data_list__mutmut_27(block_elements):
    article_data_list = []

    for i in range(1, len(block_elements)):
        authors = block_elements[i].find_all("span", attrs={"itemprop": "author"})
        author_list = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
        article_title = block_elements[i].find("span", attrs={"class": "title"}).text.strip()
        numero_citazioni = get_citations(article_title)

        article_data_list.append((article_title, author_list, int(numero_citazioni)))

    article_data_list.sort( key=lambda x: x[2])
    return article_data_list


# Restituisce i dati degli articoli con titolo, autori e numero di citazioni in ordine di numero
def x_get_article_data_list__mutmut_28(block_elements):
    article_data_list = []

    for i in range(1, len(block_elements)):
        authors = block_elements[i].find_all("span", attrs={"itemprop": "author"})
        author_list = [author.find("span", attrs={"itemprop": "name"}).text.strip() for author in authors]
        article_title = block_elements[i].find("span", attrs={"class": "title"}).text.strip()
        numero_citazioni = get_citations(article_title)

        article_data_list.append((article_title, author_list, int(numero_citazioni)))

    article_data_list.sort(reverse=True,)
    return article_data_list

x_get_article_data_list__mutmut_mutants = {
'x_get_article_data_list__mutmut_1': x_get_article_data_list__mutmut_1, 
    'x_get_article_data_list__mutmut_2': x_get_article_data_list__mutmut_2, 
    'x_get_article_data_list__mutmut_3': x_get_article_data_list__mutmut_3, 
    'x_get_article_data_list__mutmut_4': x_get_article_data_list__mutmut_4, 
    'x_get_article_data_list__mutmut_5': x_get_article_data_list__mutmut_5, 
    'x_get_article_data_list__mutmut_6': x_get_article_data_list__mutmut_6, 
    'x_get_article_data_list__mutmut_7': x_get_article_data_list__mutmut_7, 
    'x_get_article_data_list__mutmut_8': x_get_article_data_list__mutmut_8, 
    'x_get_article_data_list__mutmut_9': x_get_article_data_list__mutmut_9, 
    'x_get_article_data_list__mutmut_10': x_get_article_data_list__mutmut_10, 
    'x_get_article_data_list__mutmut_11': x_get_article_data_list__mutmut_11, 
    'x_get_article_data_list__mutmut_12': x_get_article_data_list__mutmut_12, 
    'x_get_article_data_list__mutmut_13': x_get_article_data_list__mutmut_13, 
    'x_get_article_data_list__mutmut_14': x_get_article_data_list__mutmut_14, 
    'x_get_article_data_list__mutmut_15': x_get_article_data_list__mutmut_15, 
    'x_get_article_data_list__mutmut_16': x_get_article_data_list__mutmut_16, 
    'x_get_article_data_list__mutmut_17': x_get_article_data_list__mutmut_17, 
    'x_get_article_data_list__mutmut_18': x_get_article_data_list__mutmut_18, 
    'x_get_article_data_list__mutmut_19': x_get_article_data_list__mutmut_19, 
    'x_get_article_data_list__mutmut_20': x_get_article_data_list__mutmut_20, 
    'x_get_article_data_list__mutmut_21': x_get_article_data_list__mutmut_21, 
    'x_get_article_data_list__mutmut_22': x_get_article_data_list__mutmut_22, 
    'x_get_article_data_list__mutmut_23': x_get_article_data_list__mutmut_23, 
    'x_get_article_data_list__mutmut_24': x_get_article_data_list__mutmut_24, 
    'x_get_article_data_list__mutmut_25': x_get_article_data_list__mutmut_25, 
    'x_get_article_data_list__mutmut_26': x_get_article_data_list__mutmut_26, 
    'x_get_article_data_list__mutmut_27': x_get_article_data_list__mutmut_27, 
    'x_get_article_data_list__mutmut_28': x_get_article_data_list__mutmut_28
}

def get_article_data_list(*args, **kwargs):
    result = _mutmut_trampoline(x_get_article_data_list__mutmut_orig, x_get_article_data_list__mutmut_mutants, *args, **kwargs)
    return result 

get_article_data_list.__signature__ = _mutmut_signature(x_get_article_data_list__mutmut_orig)
x_get_article_data_list__mutmut_orig.__name__ = 'x_get_article_data_list'




# Ottiene il numero di citazioni da Scopus per un determinato titolo dell'articolo.
def x_get_citations__mutmut_orig(article_title):
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


# Ottiene il numero di citazioni da Scopus per un determinato titolo dell'articolo.
def x_get_citations__mutmut_1(article_title):
    try:
        # Esegui una ricerca su Scopus utilizzando la chiave API
        url = None
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


# Ottiene il numero di citazioni da Scopus per un determinato titolo dell'articolo.
def x_get_citations__mutmut_2(article_title):
    try:
        # Esegui una ricerca su Scopus utilizzando la chiave API
        url = f'https://api.elsevier.com/content/search/scopus?query=TITLE("{article_title}")&apiKey={SCOPUS_API_KEY}'
        response = requests.get(None)
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


# Ottiene il numero di citazioni da Scopus per un determinato titolo dell'articolo.
def x_get_citations__mutmut_3(article_title):
    try:
        # Esegui una ricerca su Scopus utilizzando la chiave API
        url = f'https://api.elsevier.com/content/search/scopus?query=TITLE("{article_title}")&apiKey={SCOPUS_API_KEY}'
        response = None
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


# Ottiene il numero di citazioni da Scopus per un determinato titolo dell'articolo.
def x_get_citations__mutmut_4(article_title):
    try:
        # Esegui una ricerca su Scopus utilizzando la chiave API
        url = f'https://api.elsevier.com/content/search/scopus?query=TITLE("{article_title}")&apiKey={SCOPUS_API_KEY}'
        response = requests.get(url)
        data = None

        # Estrai il numero di citazioni dall'output della ricerca
        if 'search-results' in data and 'entry' in data['search-results']:
            entry = data['search-results']['entry'][0]
            if 'citedby-count' in entry:
                return entry['citedby-count']
        return 0
    except Exception as e:
        print(f"Errore nel recuperare citazioni per '{article_title}' da Scopus: {str(e)}")
        return 0


# Ottiene il numero di citazioni da Scopus per un determinato titolo dell'articolo.
def x_get_citations__mutmut_5(article_title):
    try:
        # Esegui una ricerca su Scopus utilizzando la chiave API
        url = f'https://api.elsevier.com/content/search/scopus?query=TITLE("{article_title}")&apiKey={SCOPUS_API_KEY}'
        response = requests.get(url)
        data = response.json()

        # Estrai il numero di citazioni dall'output della ricerca
        if 'XXsearch-resultsXX' in data and 'entry' in data['search-results']:
            entry = data['search-results']['entry'][0]
            if 'citedby-count' in entry:
                return entry['citedby-count']
        return 0
    except Exception as e:
        print(f"Errore nel recuperare citazioni per '{article_title}' da Scopus: {str(e)}")
        return 0


# Ottiene il numero di citazioni da Scopus per un determinato titolo dell'articolo.
def x_get_citations__mutmut_6(article_title):
    try:
        # Esegui una ricerca su Scopus utilizzando la chiave API
        url = f'https://api.elsevier.com/content/search/scopus?query=TITLE("{article_title}")&apiKey={SCOPUS_API_KEY}'
        response = requests.get(url)
        data = response.json()

        # Estrai il numero di citazioni dall'output della ricerca
        if 'search-results' not in data and 'entry' in data['search-results']:
            entry = data['search-results']['entry'][0]
            if 'citedby-count' in entry:
                return entry['citedby-count']
        return 0
    except Exception as e:
        print(f"Errore nel recuperare citazioni per '{article_title}' da Scopus: {str(e)}")
        return 0


# Ottiene il numero di citazioni da Scopus per un determinato titolo dell'articolo.
def x_get_citations__mutmut_7(article_title):
    try:
        # Esegui una ricerca su Scopus utilizzando la chiave API
        url = f'https://api.elsevier.com/content/search/scopus?query=TITLE("{article_title}")&apiKey={SCOPUS_API_KEY}'
        response = requests.get(url)
        data = response.json()

        # Estrai il numero di citazioni dall'output della ricerca
        if 'search-results' in data and 'XXentryXX' in data['search-results']:
            entry = data['search-results']['entry'][0]
            if 'citedby-count' in entry:
                return entry['citedby-count']
        return 0
    except Exception as e:
        print(f"Errore nel recuperare citazioni per '{article_title}' da Scopus: {str(e)}")
        return 0


# Ottiene il numero di citazioni da Scopus per un determinato titolo dell'articolo.
def x_get_citations__mutmut_8(article_title):
    try:
        # Esegui una ricerca su Scopus utilizzando la chiave API
        url = f'https://api.elsevier.com/content/search/scopus?query=TITLE("{article_title}")&apiKey={SCOPUS_API_KEY}'
        response = requests.get(url)
        data = response.json()

        # Estrai il numero di citazioni dall'output della ricerca
        if 'search-results' in data and 'entry' not in data['search-results']:
            entry = data['search-results']['entry'][0]
            if 'citedby-count' in entry:
                return entry['citedby-count']
        return 0
    except Exception as e:
        print(f"Errore nel recuperare citazioni per '{article_title}' da Scopus: {str(e)}")
        return 0


# Ottiene il numero di citazioni da Scopus per un determinato titolo dell'articolo.
def x_get_citations__mutmut_9(article_title):
    try:
        # Esegui una ricerca su Scopus utilizzando la chiave API
        url = f'https://api.elsevier.com/content/search/scopus?query=TITLE("{article_title}")&apiKey={SCOPUS_API_KEY}'
        response = requests.get(url)
        data = response.json()

        # Estrai il numero di citazioni dall'output della ricerca
        if 'search-results' in data and 'entry' in data['XXsearch-resultsXX']:
            entry = data['search-results']['entry'][0]
            if 'citedby-count' in entry:
                return entry['citedby-count']
        return 0
    except Exception as e:
        print(f"Errore nel recuperare citazioni per '{article_title}' da Scopus: {str(e)}")
        return 0


# Ottiene il numero di citazioni da Scopus per un determinato titolo dell'articolo.
def x_get_citations__mutmut_10(article_title):
    try:
        # Esegui una ricerca su Scopus utilizzando la chiave API
        url = f'https://api.elsevier.com/content/search/scopus?query=TITLE("{article_title}")&apiKey={SCOPUS_API_KEY}'
        response = requests.get(url)
        data = response.json()

        # Estrai il numero di citazioni dall'output della ricerca
        if 'search-results' in data and 'entry' in data[None]:
            entry = data['search-results']['entry'][0]
            if 'citedby-count' in entry:
                return entry['citedby-count']
        return 0
    except Exception as e:
        print(f"Errore nel recuperare citazioni per '{article_title}' da Scopus: {str(e)}")
        return 0


# Ottiene il numero di citazioni da Scopus per un determinato titolo dell'articolo.
def x_get_citations__mutmut_11(article_title):
    try:
        # Esegui una ricerca su Scopus utilizzando la chiave API
        url = f'https://api.elsevier.com/content/search/scopus?query=TITLE("{article_title}")&apiKey={SCOPUS_API_KEY}'
        response = requests.get(url)
        data = response.json()

        # Estrai il numero di citazioni dall'output della ricerca
        if 'search-results' in data or 'entry' in data['search-results']:
            entry = data['search-results']['entry'][0]
            if 'citedby-count' in entry:
                return entry['citedby-count']
        return 0
    except Exception as e:
        print(f"Errore nel recuperare citazioni per '{article_title}' da Scopus: {str(e)}")
        return 0


# Ottiene il numero di citazioni da Scopus per un determinato titolo dell'articolo.
def x_get_citations__mutmut_12(article_title):
    try:
        # Esegui una ricerca su Scopus utilizzando la chiave API
        url = f'https://api.elsevier.com/content/search/scopus?query=TITLE("{article_title}")&apiKey={SCOPUS_API_KEY}'
        response = requests.get(url)
        data = response.json()

        # Estrai il numero di citazioni dall'output della ricerca
        if 'search-results' in data and 'entry' in data['search-results']:
            entry = data['XXsearch-resultsXX']['entry'][0]
            if 'citedby-count' in entry:
                return entry['citedby-count']
        return 0
    except Exception as e:
        print(f"Errore nel recuperare citazioni per '{article_title}' da Scopus: {str(e)}")
        return 0


# Ottiene il numero di citazioni da Scopus per un determinato titolo dell'articolo.
def x_get_citations__mutmut_13(article_title):
    try:
        # Esegui una ricerca su Scopus utilizzando la chiave API
        url = f'https://api.elsevier.com/content/search/scopus?query=TITLE("{article_title}")&apiKey={SCOPUS_API_KEY}'
        response = requests.get(url)
        data = response.json()

        # Estrai il numero di citazioni dall'output della ricerca
        if 'search-results' in data and 'entry' in data['search-results']:
            entry = data[None]['entry'][0]
            if 'citedby-count' in entry:
                return entry['citedby-count']
        return 0
    except Exception as e:
        print(f"Errore nel recuperare citazioni per '{article_title}' da Scopus: {str(e)}")
        return 0


# Ottiene il numero di citazioni da Scopus per un determinato titolo dell'articolo.
def x_get_citations__mutmut_14(article_title):
    try:
        # Esegui una ricerca su Scopus utilizzando la chiave API
        url = f'https://api.elsevier.com/content/search/scopus?query=TITLE("{article_title}")&apiKey={SCOPUS_API_KEY}'
        response = requests.get(url)
        data = response.json()

        # Estrai il numero di citazioni dall'output della ricerca
        if 'search-results' in data and 'entry' in data['search-results']:
            entry = data['search-results']['XXentryXX'][0]
            if 'citedby-count' in entry:
                return entry['citedby-count']
        return 0
    except Exception as e:
        print(f"Errore nel recuperare citazioni per '{article_title}' da Scopus: {str(e)}")
        return 0


# Ottiene il numero di citazioni da Scopus per un determinato titolo dell'articolo.
def x_get_citations__mutmut_15(article_title):
    try:
        # Esegui una ricerca su Scopus utilizzando la chiave API
        url = f'https://api.elsevier.com/content/search/scopus?query=TITLE("{article_title}")&apiKey={SCOPUS_API_KEY}'
        response = requests.get(url)
        data = response.json()

        # Estrai il numero di citazioni dall'output della ricerca
        if 'search-results' in data and 'entry' in data['search-results']:
            entry = data['search-results'][None][0]
            if 'citedby-count' in entry:
                return entry['citedby-count']
        return 0
    except Exception as e:
        print(f"Errore nel recuperare citazioni per '{article_title}' da Scopus: {str(e)}")
        return 0


# Ottiene il numero di citazioni da Scopus per un determinato titolo dell'articolo.
def x_get_citations__mutmut_16(article_title):
    try:
        # Esegui una ricerca su Scopus utilizzando la chiave API
        url = f'https://api.elsevier.com/content/search/scopus?query=TITLE("{article_title}")&apiKey={SCOPUS_API_KEY}'
        response = requests.get(url)
        data = response.json()

        # Estrai il numero di citazioni dall'output della ricerca
        if 'search-results' in data and 'entry' in data['search-results']:
            entry = data['search-results']['entry'][1]
            if 'citedby-count' in entry:
                return entry['citedby-count']
        return 0
    except Exception as e:
        print(f"Errore nel recuperare citazioni per '{article_title}' da Scopus: {str(e)}")
        return 0


# Ottiene il numero di citazioni da Scopus per un determinato titolo dell'articolo.
def x_get_citations__mutmut_17(article_title):
    try:
        # Esegui una ricerca su Scopus utilizzando la chiave API
        url = f'https://api.elsevier.com/content/search/scopus?query=TITLE("{article_title}")&apiKey={SCOPUS_API_KEY}'
        response = requests.get(url)
        data = response.json()

        # Estrai il numero di citazioni dall'output della ricerca
        if 'search-results' in data and 'entry' in data['search-results']:
            entry = data['search-results']['entry'][None]
            if 'citedby-count' in entry:
                return entry['citedby-count']
        return 0
    except Exception as e:
        print(f"Errore nel recuperare citazioni per '{article_title}' da Scopus: {str(e)}")
        return 0


# Ottiene il numero di citazioni da Scopus per un determinato titolo dell'articolo.
def x_get_citations__mutmut_18(article_title):
    try:
        # Esegui una ricerca su Scopus utilizzando la chiave API
        url = f'https://api.elsevier.com/content/search/scopus?query=TITLE("{article_title}")&apiKey={SCOPUS_API_KEY}'
        response = requests.get(url)
        data = response.json()

        # Estrai il numero di citazioni dall'output della ricerca
        if 'search-results' in data and 'entry' in data['search-results']:
            entry = None
            if 'citedby-count' in entry:
                return entry['citedby-count']
        return 0
    except Exception as e:
        print(f"Errore nel recuperare citazioni per '{article_title}' da Scopus: {str(e)}")
        return 0


# Ottiene il numero di citazioni da Scopus per un determinato titolo dell'articolo.
def x_get_citations__mutmut_19(article_title):
    try:
        # Esegui una ricerca su Scopus utilizzando la chiave API
        url = f'https://api.elsevier.com/content/search/scopus?query=TITLE("{article_title}")&apiKey={SCOPUS_API_KEY}'
        response = requests.get(url)
        data = response.json()

        # Estrai il numero di citazioni dall'output della ricerca
        if 'search-results' in data and 'entry' in data['search-results']:
            entry = data['search-results']['entry'][0]
            if 'XXcitedby-countXX' in entry:
                return entry['citedby-count']
        return 0
    except Exception as e:
        print(f"Errore nel recuperare citazioni per '{article_title}' da Scopus: {str(e)}")
        return 0


# Ottiene il numero di citazioni da Scopus per un determinato titolo dell'articolo.
def x_get_citations__mutmut_20(article_title):
    try:
        # Esegui una ricerca su Scopus utilizzando la chiave API
        url = f'https://api.elsevier.com/content/search/scopus?query=TITLE("{article_title}")&apiKey={SCOPUS_API_KEY}'
        response = requests.get(url)
        data = response.json()

        # Estrai il numero di citazioni dall'output della ricerca
        if 'search-results' in data and 'entry' in data['search-results']:
            entry = data['search-results']['entry'][0]
            if 'citedby-count' not in entry:
                return entry['citedby-count']
        return 0
    except Exception as e:
        print(f"Errore nel recuperare citazioni per '{article_title}' da Scopus: {str(e)}")
        return 0


# Ottiene il numero di citazioni da Scopus per un determinato titolo dell'articolo.
def x_get_citations__mutmut_21(article_title):
    try:
        # Esegui una ricerca su Scopus utilizzando la chiave API
        url = f'https://api.elsevier.com/content/search/scopus?query=TITLE("{article_title}")&apiKey={SCOPUS_API_KEY}'
        response = requests.get(url)
        data = response.json()

        # Estrai il numero di citazioni dall'output della ricerca
        if 'search-results' in data and 'entry' in data['search-results']:
            entry = data['search-results']['entry'][0]
            if 'citedby-count' in entry:
                return entry['XXcitedby-countXX']
        return 0
    except Exception as e:
        print(f"Errore nel recuperare citazioni per '{article_title}' da Scopus: {str(e)}")
        return 0


# Ottiene il numero di citazioni da Scopus per un determinato titolo dell'articolo.
def x_get_citations__mutmut_22(article_title):
    try:
        # Esegui una ricerca su Scopus utilizzando la chiave API
        url = f'https://api.elsevier.com/content/search/scopus?query=TITLE("{article_title}")&apiKey={SCOPUS_API_KEY}'
        response = requests.get(url)
        data = response.json()

        # Estrai il numero di citazioni dall'output della ricerca
        if 'search-results' in data and 'entry' in data['search-results']:
            entry = data['search-results']['entry'][0]
            if 'citedby-count' in entry:
                return entry[None]
        return 0
    except Exception as e:
        print(f"Errore nel recuperare citazioni per '{article_title}' da Scopus: {str(e)}")
        return 0


# Ottiene il numero di citazioni da Scopus per un determinato titolo dell'articolo.
def x_get_citations__mutmut_23(article_title):
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
        return 1
    except Exception as e:
        print(f"Errore nel recuperare citazioni per '{article_title}' da Scopus: {str(e)}")
        return 0


# Ottiene il numero di citazioni da Scopus per un determinato titolo dell'articolo.
def x_get_citations__mutmut_24(article_title):
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
        print(f"Errore nel recuperare citazioni per '{article_title}' da Scopus: {str(None)}")
        return 0


# Ottiene il numero di citazioni da Scopus per un determinato titolo dell'articolo.
def x_get_citations__mutmut_25(article_title):
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
        return 1

x_get_citations__mutmut_mutants = {
'x_get_citations__mutmut_1': x_get_citations__mutmut_1, 
    'x_get_citations__mutmut_2': x_get_citations__mutmut_2, 
    'x_get_citations__mutmut_3': x_get_citations__mutmut_3, 
    'x_get_citations__mutmut_4': x_get_citations__mutmut_4, 
    'x_get_citations__mutmut_5': x_get_citations__mutmut_5, 
    'x_get_citations__mutmut_6': x_get_citations__mutmut_6, 
    'x_get_citations__mutmut_7': x_get_citations__mutmut_7, 
    'x_get_citations__mutmut_8': x_get_citations__mutmut_8, 
    'x_get_citations__mutmut_9': x_get_citations__mutmut_9, 
    'x_get_citations__mutmut_10': x_get_citations__mutmut_10, 
    'x_get_citations__mutmut_11': x_get_citations__mutmut_11, 
    'x_get_citations__mutmut_12': x_get_citations__mutmut_12, 
    'x_get_citations__mutmut_13': x_get_citations__mutmut_13, 
    'x_get_citations__mutmut_14': x_get_citations__mutmut_14, 
    'x_get_citations__mutmut_15': x_get_citations__mutmut_15, 
    'x_get_citations__mutmut_16': x_get_citations__mutmut_16, 
    'x_get_citations__mutmut_17': x_get_citations__mutmut_17, 
    'x_get_citations__mutmut_18': x_get_citations__mutmut_18, 
    'x_get_citations__mutmut_19': x_get_citations__mutmut_19, 
    'x_get_citations__mutmut_20': x_get_citations__mutmut_20, 
    'x_get_citations__mutmut_21': x_get_citations__mutmut_21, 
    'x_get_citations__mutmut_22': x_get_citations__mutmut_22, 
    'x_get_citations__mutmut_23': x_get_citations__mutmut_23, 
    'x_get_citations__mutmut_24': x_get_citations__mutmut_24, 
    'x_get_citations__mutmut_25': x_get_citations__mutmut_25
}

def get_citations(*args, **kwargs):
    result = _mutmut_trampoline(x_get_citations__mutmut_orig, x_get_citations__mutmut_mutants, *args, **kwargs)
    return result 

get_citations.__signature__ = _mutmut_signature(x_get_citations__mutmut_orig)
x_get_citations__mutmut_orig.__name__ = 'x_get_citations'




def x_setup_classifica_routes__mutmut_orig(app):
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
                                return render_template('classifica.html', result=article_titles,
                                                       conference_title=conference_title, conference_year=conference_year)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_1(app):
    @app.route('XX/search_classificaXX', methods=['GET'])
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
                                return render_template('classifica.html', result=article_titles,
                                                       conference_title=conference_title, conference_year=conference_year)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_2(app):
    @app.route('/search_classifica', methods=['XXGETXX'])
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
                                return render_template('classifica.html', result=article_titles,
                                                       conference_title=conference_title, conference_year=conference_year)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_3(app):
    @app.route('/search_classifica',)
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
                                return render_template('classifica.html', result=article_titles,
                                                       conference_title=conference_title, conference_year=conference_year)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_4(app):

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
                                return render_template('classifica.html', result=article_titles,
                                                       conference_title=conference_title, conference_year=conference_year)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_5(app):
    @app.route('/search_classifica', methods=['GET'])
    def show_classifica():
        return render_template('XXclassifica.htmlXX', result=None)

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
                                return render_template('classifica.html', result=article_titles,
                                                       conference_title=conference_title, conference_year=conference_year)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_6(app):
    @app.route('/search_classifica', methods=['GET'])
    def show_classifica():
        return render_template('classifica.html',)

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
                                return render_template('classifica.html', result=article_titles,
                                                       conference_title=conference_title, conference_year=conference_year)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_7(app):
    @app.route('/search_classifica', methods=['GET'])
    def show_classifica():
        return render_template('classifica.html', result=None)

    @app.route('XX/classificaXX', methods=['POST'])
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
                                return render_template('classifica.html', result=article_titles,
                                                       conference_title=conference_title, conference_year=conference_year)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_8(app):
    @app.route('/search_classifica', methods=['GET'])
    def show_classifica():
        return render_template('classifica.html', result=None)

    @app.route('/classifica', methods=['XXPOSTXX'])
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
                                return render_template('classifica.html', result=article_titles,
                                                       conference_title=conference_title, conference_year=conference_year)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_9(app):
    @app.route('/search_classifica', methods=['GET'])
    def show_classifica():
        return render_template('classifica.html', result=None)

    @app.route('/classifica',)
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
                                return render_template('classifica.html', result=article_titles,
                                                       conference_title=conference_title, conference_year=conference_year)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_10(app):
    @app.route('/search_classifica', methods=['GET'])
    def show_classifica():
        return render_template('classifica.html', result=None)

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
                                return render_template('classifica.html', result=article_titles,
                                                       conference_title=conference_title, conference_year=conference_year)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_11(app):
    @app.route('/search_classifica', methods=['GET'])
    def show_classifica():
        return render_template('classifica.html', result=None)

    @app.route('/classifica', methods=['POST'])
    def handle_classifica():
        conference_title = request.form.get('XXconference_titleXX')
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
                                return render_template('classifica.html', result=article_titles,
                                                       conference_title=conference_title, conference_year=conference_year)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_12(app):
    @app.route('/search_classifica', methods=['GET'])
    def show_classifica():
        return render_template('classifica.html', result=None)

    @app.route('/classifica', methods=['POST'])
    def handle_classifica():
        conference_title = None
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
                                return render_template('classifica.html', result=article_titles,
                                                       conference_title=conference_title, conference_year=conference_year)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_13(app):
    @app.route('/search_classifica', methods=['GET'])
    def show_classifica():
        return render_template('classifica.html', result=None)

    @app.route('/classifica', methods=['POST'])
    def handle_classifica():
        conference_title = request.form.get('conference_title')
        conference_year = request.form.get('XXconference_yearXX')

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
                                return render_template('classifica.html', result=article_titles,
                                                       conference_title=conference_title, conference_year=conference_year)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_14(app):
    @app.route('/search_classifica', methods=['GET'])
    def show_classifica():
        return render_template('classifica.html', result=None)

    @app.route('/classifica', methods=['POST'])
    def handle_classifica():
        conference_title = request.form.get('conference_title')
        conference_year = None

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
                                return render_template('classifica.html', result=article_titles,
                                                       conference_title=conference_title, conference_year=conference_year)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_15(app):
    @app.route('/search_classifica', methods=['GET'])
    def show_classifica():
        return render_template('classifica.html', result=None)

    @app.route('/classifica', methods=['POST'])
    def handle_classifica():
        conference_title = request.form.get('conference_title')
        conference_year = request.form.get('conference_year')

        if conference_title or conference_year:
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
                                return render_template('classifica.html', result=article_titles,
                                                       conference_title=conference_title, conference_year=conference_year)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_16(app):
    @app.route('/search_classifica', methods=['GET'])
    def show_classifica():
        return render_template('classifica.html', result=None)

    @app.route('/classifica', methods=['POST'])
    def handle_classifica():
        conference_title = request.form.get('conference_title')
        conference_year = request.form.get('conference_year')

        if conference_title and conference_year:
            driver = None

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
                                return render_template('classifica.html', result=article_titles,
                                                       conference_title=conference_title, conference_year=conference_year)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_17(app):
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
                page_source = search_conference(None, driver)

                if page_source is not None:
                    soup = BeautifulSoup(page_source, 'html.parser')
                    year_element = get_year_element(soup, conference_year)

                    if year_element is not None:
                        contents_page_source = get_contents_link(year_element, driver)

                        if contents_page_source is not None:
                            block_elements = get_block_elements(contents_page_source)
                            article_titles = get_article_data_list(block_elements)

                            if article_titles is not None:
                                return render_template('classifica.html', result=article_titles,
                                                       conference_title=conference_title, conference_year=conference_year)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_18(app):
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
                page_source = search_conference(conference_title, None)

                if page_source is not None:
                    soup = BeautifulSoup(page_source, 'html.parser')
                    year_element = get_year_element(soup, conference_year)

                    if year_element is not None:
                        contents_page_source = get_contents_link(year_element, driver)

                        if contents_page_source is not None:
                            block_elements = get_block_elements(contents_page_source)
                            article_titles = get_article_data_list(block_elements)

                            if article_titles is not None:
                                return render_template('classifica.html', result=article_titles,
                                                       conference_title=conference_title, conference_year=conference_year)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_19(app):
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
                page_source = search_conference( driver)

                if page_source is not None:
                    soup = BeautifulSoup(page_source, 'html.parser')
                    year_element = get_year_element(soup, conference_year)

                    if year_element is not None:
                        contents_page_source = get_contents_link(year_element, driver)

                        if contents_page_source is not None:
                            block_elements = get_block_elements(contents_page_source)
                            article_titles = get_article_data_list(block_elements)

                            if article_titles is not None:
                                return render_template('classifica.html', result=article_titles,
                                                       conference_title=conference_title, conference_year=conference_year)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_20(app):
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
                page_source = search_conference(conference_title,)

                if page_source is not None:
                    soup = BeautifulSoup(page_source, 'html.parser')
                    year_element = get_year_element(soup, conference_year)

                    if year_element is not None:
                        contents_page_source = get_contents_link(year_element, driver)

                        if contents_page_source is not None:
                            block_elements = get_block_elements(contents_page_source)
                            article_titles = get_article_data_list(block_elements)

                            if article_titles is not None:
                                return render_template('classifica.html', result=article_titles,
                                                       conference_title=conference_title, conference_year=conference_year)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_21(app):
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
                page_source = None

                if page_source is not None:
                    soup = BeautifulSoup(page_source, 'html.parser')
                    year_element = get_year_element(soup, conference_year)

                    if year_element is not None:
                        contents_page_source = get_contents_link(year_element, driver)

                        if contents_page_source is not None:
                            block_elements = get_block_elements(contents_page_source)
                            article_titles = get_article_data_list(block_elements)

                            if article_titles is not None:
                                return render_template('classifica.html', result=article_titles,
                                                       conference_title=conference_title, conference_year=conference_year)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_22(app):
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

                if page_source is  None:
                    soup = BeautifulSoup(page_source, 'html.parser')
                    year_element = get_year_element(soup, conference_year)

                    if year_element is not None:
                        contents_page_source = get_contents_link(year_element, driver)

                        if contents_page_source is not None:
                            block_elements = get_block_elements(contents_page_source)
                            article_titles = get_article_data_list(block_elements)

                            if article_titles is not None:
                                return render_template('classifica.html', result=article_titles,
                                                       conference_title=conference_title, conference_year=conference_year)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_23(app):
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
                    soup = BeautifulSoup(None, 'html.parser')
                    year_element = get_year_element(soup, conference_year)

                    if year_element is not None:
                        contents_page_source = get_contents_link(year_element, driver)

                        if contents_page_source is not None:
                            block_elements = get_block_elements(contents_page_source)
                            article_titles = get_article_data_list(block_elements)

                            if article_titles is not None:
                                return render_template('classifica.html', result=article_titles,
                                                       conference_title=conference_title, conference_year=conference_year)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_24(app):
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
                    soup = BeautifulSoup(page_source, 'XXhtml.parserXX')
                    year_element = get_year_element(soup, conference_year)

                    if year_element is not None:
                        contents_page_source = get_contents_link(year_element, driver)

                        if contents_page_source is not None:
                            block_elements = get_block_elements(contents_page_source)
                            article_titles = get_article_data_list(block_elements)

                            if article_titles is not None:
                                return render_template('classifica.html', result=article_titles,
                                                       conference_title=conference_title, conference_year=conference_year)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_25(app):
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
                    soup = BeautifulSoup( 'html.parser')
                    year_element = get_year_element(soup, conference_year)

                    if year_element is not None:
                        contents_page_source = get_contents_link(year_element, driver)

                        if contents_page_source is not None:
                            block_elements = get_block_elements(contents_page_source)
                            article_titles = get_article_data_list(block_elements)

                            if article_titles is not None:
                                return render_template('classifica.html', result=article_titles,
                                                       conference_title=conference_title, conference_year=conference_year)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_26(app):
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
                    soup = None
                    year_element = get_year_element(soup, conference_year)

                    if year_element is not None:
                        contents_page_source = get_contents_link(year_element, driver)

                        if contents_page_source is not None:
                            block_elements = get_block_elements(contents_page_source)
                            article_titles = get_article_data_list(block_elements)

                            if article_titles is not None:
                                return render_template('classifica.html', result=article_titles,
                                                       conference_title=conference_title, conference_year=conference_year)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_27(app):
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
                    year_element = get_year_element(None, conference_year)

                    if year_element is not None:
                        contents_page_source = get_contents_link(year_element, driver)

                        if contents_page_source is not None:
                            block_elements = get_block_elements(contents_page_source)
                            article_titles = get_article_data_list(block_elements)

                            if article_titles is not None:
                                return render_template('classifica.html', result=article_titles,
                                                       conference_title=conference_title, conference_year=conference_year)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_28(app):
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
                    year_element = get_year_element(soup, None)

                    if year_element is not None:
                        contents_page_source = get_contents_link(year_element, driver)

                        if contents_page_source is not None:
                            block_elements = get_block_elements(contents_page_source)
                            article_titles = get_article_data_list(block_elements)

                            if article_titles is not None:
                                return render_template('classifica.html', result=article_titles,
                                                       conference_title=conference_title, conference_year=conference_year)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_29(app):
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
                    year_element = get_year_element( conference_year)

                    if year_element is not None:
                        contents_page_source = get_contents_link(year_element, driver)

                        if contents_page_source is not None:
                            block_elements = get_block_elements(contents_page_source)
                            article_titles = get_article_data_list(block_elements)

                            if article_titles is not None:
                                return render_template('classifica.html', result=article_titles,
                                                       conference_title=conference_title, conference_year=conference_year)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_30(app):
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
                    year_element = get_year_element(soup,)

                    if year_element is not None:
                        contents_page_source = get_contents_link(year_element, driver)

                        if contents_page_source is not None:
                            block_elements = get_block_elements(contents_page_source)
                            article_titles = get_article_data_list(block_elements)

                            if article_titles is not None:
                                return render_template('classifica.html', result=article_titles,
                                                       conference_title=conference_title, conference_year=conference_year)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_31(app):
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
                    year_element = None

                    if year_element is not None:
                        contents_page_source = get_contents_link(year_element, driver)

                        if contents_page_source is not None:
                            block_elements = get_block_elements(contents_page_source)
                            article_titles = get_article_data_list(block_elements)

                            if article_titles is not None:
                                return render_template('classifica.html', result=article_titles,
                                                       conference_title=conference_title, conference_year=conference_year)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_32(app):
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

                    if year_element is  None:
                        contents_page_source = get_contents_link(year_element, driver)

                        if contents_page_source is not None:
                            block_elements = get_block_elements(contents_page_source)
                            article_titles = get_article_data_list(block_elements)

                            if article_titles is not None:
                                return render_template('classifica.html', result=article_titles,
                                                       conference_title=conference_title, conference_year=conference_year)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_33(app):
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
                        contents_page_source = get_contents_link(None, driver)

                        if contents_page_source is not None:
                            block_elements = get_block_elements(contents_page_source)
                            article_titles = get_article_data_list(block_elements)

                            if article_titles is not None:
                                return render_template('classifica.html', result=article_titles,
                                                       conference_title=conference_title, conference_year=conference_year)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_34(app):
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
                        contents_page_source = get_contents_link(year_element, None)

                        if contents_page_source is not None:
                            block_elements = get_block_elements(contents_page_source)
                            article_titles = get_article_data_list(block_elements)

                            if article_titles is not None:
                                return render_template('classifica.html', result=article_titles,
                                                       conference_title=conference_title, conference_year=conference_year)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_35(app):
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
                        contents_page_source = get_contents_link( driver)

                        if contents_page_source is not None:
                            block_elements = get_block_elements(contents_page_source)
                            article_titles = get_article_data_list(block_elements)

                            if article_titles is not None:
                                return render_template('classifica.html', result=article_titles,
                                                       conference_title=conference_title, conference_year=conference_year)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_36(app):
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
                        contents_page_source = get_contents_link(year_element,)

                        if contents_page_source is not None:
                            block_elements = get_block_elements(contents_page_source)
                            article_titles = get_article_data_list(block_elements)

                            if article_titles is not None:
                                return render_template('classifica.html', result=article_titles,
                                                       conference_title=conference_title, conference_year=conference_year)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_37(app):
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
                        contents_page_source = None

                        if contents_page_source is not None:
                            block_elements = get_block_elements(contents_page_source)
                            article_titles = get_article_data_list(block_elements)

                            if article_titles is not None:
                                return render_template('classifica.html', result=article_titles,
                                                       conference_title=conference_title, conference_year=conference_year)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_38(app):
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

                        if contents_page_source is  None:
                            block_elements = get_block_elements(contents_page_source)
                            article_titles = get_article_data_list(block_elements)

                            if article_titles is not None:
                                return render_template('classifica.html', result=article_titles,
                                                       conference_title=conference_title, conference_year=conference_year)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_39(app):
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
                            block_elements = get_block_elements(None)
                            article_titles = get_article_data_list(block_elements)

                            if article_titles is not None:
                                return render_template('classifica.html', result=article_titles,
                                                       conference_title=conference_title, conference_year=conference_year)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_40(app):
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
                            block_elements = None
                            article_titles = get_article_data_list(block_elements)

                            if article_titles is not None:
                                return render_template('classifica.html', result=article_titles,
                                                       conference_title=conference_title, conference_year=conference_year)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_41(app):
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
                            article_titles = get_article_data_list(None)

                            if article_titles is not None:
                                return render_template('classifica.html', result=article_titles,
                                                       conference_title=conference_title, conference_year=conference_year)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_42(app):
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
                            article_titles = None

                            if article_titles is not None:
                                return render_template('classifica.html', result=article_titles,
                                                       conference_title=conference_title, conference_year=conference_year)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_43(app):
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

                            if article_titles is  None:
                                return render_template('classifica.html', result=article_titles,
                                                       conference_title=conference_title, conference_year=conference_year)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_44(app):
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
                                return render_template('XXclassifica.htmlXX', result=article_titles,
                                                       conference_title=conference_title, conference_year=conference_year)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_45(app):
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
                                return render_template('classifica.html', result=None,
                                                       conference_title=conference_title, conference_year=conference_year)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_46(app):
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
                                return render_template('classifica.html', result=article_titles,
                                                       conference_title=None, conference_year=conference_year)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_47(app):
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
                                return render_template('classifica.html', result=article_titles,
                                                       conference_title=conference_title, conference_year=None)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_48(app):
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
                                return render_template('classifica.html',
                                                       conference_title=conference_title, conference_year=conference_year)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_49(app):
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
                                return render_template('classifica.html', result=article_titles, conference_year=conference_year)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_50(app):
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
                                return render_template('classifica.html', result=article_titles,
                                                       conference_title=conference_title,)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('show_classifica'))


def x_setup_classifica_routes__mutmut_51(app):
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
                                return render_template('classifica.html', result=article_titles,
                                                       conference_title=conference_title, conference_year=conference_year)
            finally:
                driver.quit()
        # Se qualcosa va storto o i dati del form sono mancanti, reindirizza alla pagina principale
        return redirect(url_for('XXshow_classificaXX'))

x_setup_classifica_routes__mutmut_mutants = {
'x_setup_classifica_routes__mutmut_1': x_setup_classifica_routes__mutmut_1, 
    'x_setup_classifica_routes__mutmut_2': x_setup_classifica_routes__mutmut_2, 
    'x_setup_classifica_routes__mutmut_3': x_setup_classifica_routes__mutmut_3, 
    'x_setup_classifica_routes__mutmut_4': x_setup_classifica_routes__mutmut_4, 
    'x_setup_classifica_routes__mutmut_5': x_setup_classifica_routes__mutmut_5, 
    'x_setup_classifica_routes__mutmut_6': x_setup_classifica_routes__mutmut_6, 
    'x_setup_classifica_routes__mutmut_7': x_setup_classifica_routes__mutmut_7, 
    'x_setup_classifica_routes__mutmut_8': x_setup_classifica_routes__mutmut_8, 
    'x_setup_classifica_routes__mutmut_9': x_setup_classifica_routes__mutmut_9, 
    'x_setup_classifica_routes__mutmut_10': x_setup_classifica_routes__mutmut_10, 
    'x_setup_classifica_routes__mutmut_11': x_setup_classifica_routes__mutmut_11, 
    'x_setup_classifica_routes__mutmut_12': x_setup_classifica_routes__mutmut_12, 
    'x_setup_classifica_routes__mutmut_13': x_setup_classifica_routes__mutmut_13, 
    'x_setup_classifica_routes__mutmut_14': x_setup_classifica_routes__mutmut_14, 
    'x_setup_classifica_routes__mutmut_15': x_setup_classifica_routes__mutmut_15, 
    'x_setup_classifica_routes__mutmut_16': x_setup_classifica_routes__mutmut_16, 
    'x_setup_classifica_routes__mutmut_17': x_setup_classifica_routes__mutmut_17, 
    'x_setup_classifica_routes__mutmut_18': x_setup_classifica_routes__mutmut_18, 
    'x_setup_classifica_routes__mutmut_19': x_setup_classifica_routes__mutmut_19, 
    'x_setup_classifica_routes__mutmut_20': x_setup_classifica_routes__mutmut_20, 
    'x_setup_classifica_routes__mutmut_21': x_setup_classifica_routes__mutmut_21, 
    'x_setup_classifica_routes__mutmut_22': x_setup_classifica_routes__mutmut_22, 
    'x_setup_classifica_routes__mutmut_23': x_setup_classifica_routes__mutmut_23, 
    'x_setup_classifica_routes__mutmut_24': x_setup_classifica_routes__mutmut_24, 
    'x_setup_classifica_routes__mutmut_25': x_setup_classifica_routes__mutmut_25, 
    'x_setup_classifica_routes__mutmut_26': x_setup_classifica_routes__mutmut_26, 
    'x_setup_classifica_routes__mutmut_27': x_setup_classifica_routes__mutmut_27, 
    'x_setup_classifica_routes__mutmut_28': x_setup_classifica_routes__mutmut_28, 
    'x_setup_classifica_routes__mutmut_29': x_setup_classifica_routes__mutmut_29, 
    'x_setup_classifica_routes__mutmut_30': x_setup_classifica_routes__mutmut_30, 
    'x_setup_classifica_routes__mutmut_31': x_setup_classifica_routes__mutmut_31, 
    'x_setup_classifica_routes__mutmut_32': x_setup_classifica_routes__mutmut_32, 
    'x_setup_classifica_routes__mutmut_33': x_setup_classifica_routes__mutmut_33, 
    'x_setup_classifica_routes__mutmut_34': x_setup_classifica_routes__mutmut_34, 
    'x_setup_classifica_routes__mutmut_35': x_setup_classifica_routes__mutmut_35, 
    'x_setup_classifica_routes__mutmut_36': x_setup_classifica_routes__mutmut_36, 
    'x_setup_classifica_routes__mutmut_37': x_setup_classifica_routes__mutmut_37, 
    'x_setup_classifica_routes__mutmut_38': x_setup_classifica_routes__mutmut_38, 
    'x_setup_classifica_routes__mutmut_39': x_setup_classifica_routes__mutmut_39, 
    'x_setup_classifica_routes__mutmut_40': x_setup_classifica_routes__mutmut_40, 
    'x_setup_classifica_routes__mutmut_41': x_setup_classifica_routes__mutmut_41, 
    'x_setup_classifica_routes__mutmut_42': x_setup_classifica_routes__mutmut_42, 
    'x_setup_classifica_routes__mutmut_43': x_setup_classifica_routes__mutmut_43, 
    'x_setup_classifica_routes__mutmut_44': x_setup_classifica_routes__mutmut_44, 
    'x_setup_classifica_routes__mutmut_45': x_setup_classifica_routes__mutmut_45, 
    'x_setup_classifica_routes__mutmut_46': x_setup_classifica_routes__mutmut_46, 
    'x_setup_classifica_routes__mutmut_47': x_setup_classifica_routes__mutmut_47, 
    'x_setup_classifica_routes__mutmut_48': x_setup_classifica_routes__mutmut_48, 
    'x_setup_classifica_routes__mutmut_49': x_setup_classifica_routes__mutmut_49, 
    'x_setup_classifica_routes__mutmut_50': x_setup_classifica_routes__mutmut_50, 
    'x_setup_classifica_routes__mutmut_51': x_setup_classifica_routes__mutmut_51
}

def setup_classifica_routes(*args, **kwargs):
    result = _mutmut_trampoline(x_setup_classifica_routes__mutmut_orig, x_setup_classifica_routes__mutmut_mutants, *args, **kwargs)
    return result 

setup_classifica_routes.__signature__ = _mutmut_signature(x_setup_classifica_routes__mutmut_orig)
x_setup_classifica_routes__mutmut_orig.__name__ = 'x_setup_classifica_routes'


