import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


use_step_matcher("re")


@given("l\'utente è sulla pagina principale")
def step_given_user_on_homepage(context):
    context.driver = webdriver.Chrome()
    context.driver.get('http://127.0.0.1:8080/')
    time.sleep(2)


@when('l\'utente seleziona l\'opzione "Classifica articoli più citati"')
def step_when_select_classifica(context):

    button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Classifica articoli più citati']"))
    )
    button.click()

    time.sleep(2)


@when('l\'utente inserisce "(.*)" come titolo della conferenza')
def step_when_user_enters_conference_title(context, conference_name):
    input_conference = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'conference_title'))
    )
    input_conference.send_keys(conference_name)
    time.sleep(2)


@step('l\'utente inserisce "(\\d{4})" come anno')
def step_when_user_enters_conference_year(context, year):
    input_conference = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'conference_year'))
    )
    input_conference.send_keys(year)
    time.sleep(2)


@step('l\'utente clicca sul pulsante "Cerca"')
def step_when_click_search(context):

    button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//input[@type="submit" and @value="Cerca"]'))
    )
    button.click()
    time.sleep(2)

@step('l\'utente clicca sul menù "Seleziona Classifica"')
def step_when_user_select_ranking(context):
    button = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'selectOption'))
    )
    button.click()
    dropdown = Select(button)

    # Seleziona l'opzione con value="classifica"
    dropdown.select_by_value("classifica")
    time.sleep(2)


@then("l'utente visualizza la classifica degli articoli")
def step_then_user_sees_article_ranking(context):
    assert "Risultati" in context.driver.find_element(By.ID, "classifica-container").text

    time.sleep(1)
    context.driver.quit()


@step('l\'utente clicca sul menù "Seleziona Grafico"')
def step_when_user_select_chart(context):
    button = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'selectOption'))
    )
    button.click()
    dropdown = Select(button)

    # Seleziona l'opzione con value="grafico"
    dropdown.select_by_value("grafico")
    time.sleep(2)

    @then("l'utente visualizza il grafico")
    def step_then_user_sees_chart(context):
        # Assicurati di attendere che la pagina si carichi completamente
        time.sleep(3)

        # Ottieni l'elemento con id "grafico-container"
        grafico_container = context.driver.find_element(By.ID, "grafico-container")

        # Verifica che l'elemento sia visibile
        assert grafico_container.is_displayed(), "Il grafico non è visibile"


@step('l\'utente inserisce "Conferenza non esistente" come titolo della conferenza')
def step_when_user_search_conference_not_real(context):
    input_conference = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'conference_title'))
    )
    input_conference.send_keys("Conferenza non esistente")
    time.sleep(2)


@then("l'utente visualizza il messaggio di errore")
def step_then_user_sees_error_message(context):
    # Assicurati di attendere che la pagina si carichi completamente
    time.sleep(3)

    error_message_container = context.driver.find_element(By.XPATH, "//div[@style='text-align: center; color: red;']")

    # Verifica che l'elemento sia visibile
    assert error_message_container.is_displayed(), "Il messaggio di errore non è visibile"


@step('l\'utente inserisce "100" come anno')
def step_impl(context):
    input_conference = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'conference_year'))
    )
    input_conference.send_keys("100")
    time.sleep(2)