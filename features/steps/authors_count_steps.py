import time
from selenium.webdriver.support import expected_conditions as EC

from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

use_step_matcher("re")


@when('l\'utente seleziona l\'opzione "Autori più presenti nella conferenza"')
def step_when_user_selects_authors(context):

    button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Autori più presenti nella conferenza']"))
    )
    button.click()

    time.sleep(2)


@step('l\'utente inserisce "2012" come anno d\'inizio')
def step_when_user_inserts_start_year(context):
    input_conference = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'start_year'))
    )
    input_conference.send_keys("2012")
    time.sleep(2)


@step('l\'utente inserisce "2012" come anno di fine')
def step_when_user_inserts_end_year(context):
    input_conference = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'end_year'))
    )
    input_conference.send_keys("2012")
    time.sleep(2)


@then("l'utente visualizza la classifica degli autori")
def step_when_user_sees_authors_count(context):
    assert "Autori" in context.driver.find_element(By.ID, "classifica-container").text

    time.sleep(1)
    context.driver.quit()


@then("l'utente visualizza il grafico degli autori")
def step_when_user_sees_authors_chart(context):
    time.sleep(1)
    grafico_container = context.driver.find_element(By.ID, "grafico-container")

    assert grafico_container.is_displayed(), "Il grafico non è visibile"