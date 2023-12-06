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


@when('l\'utente inserisce "3D Data Processing Visualization and Transmission" come titolo della conferenza')
def step_when_user_enters_conference_title(context):
    input_conference = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'conference_title'))
    )
    input_conference.send_keys("3D Data Processing Visualization and Transmission")
    time.sleep(2)


@step('l\'utente inserisce "2012" come anno')
def step_when_user_enters_conference_year(context):
    input_conference = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'conference_year'))
    )
    input_conference.send_keys("2012")
    time.sleep(2)


@step('l\'utente clicca sul pulsante "Cerca"')
def step_when_click_search(context):

    button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//input[@type="submit" and @value="Cerca"]'))
    )
    button.click()
    time.sleep(2)

@step('l\'utente clicca sul menù "Seleziona Classifica"')
def step_when_user_select_option(context):
    button = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'selectOption'))
    )
    button.click()
    dropdown = Select(button)

    # Seleziona l'opzione con value="classifica"
    dropdown.select_by_value("classifica")
    time.sleep(2)
#
# @step('l\'utente clicca sull\'opzione "Classifica"')
# def step_when_user_select_classifica(context):
#     button = WebDriverWait(context.driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, '//input[@type="option" and @value="Classifica"]'))
#     )
#     button.click()
#     time.sleep(2)


@then("l'utente visualizza la classifica degli articoli")
def step_then_user_sees_article_ranking(context):
    assert "Risultati" in context.driver.find_element(By.ID, "classifica-container").text

    time.sleep(1)
    context.driver.quit()


