import time

from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

use_step_matcher("re")


@when('l\'utente seleziona l\'opzione "Conferenze classificate per h-index"')
def step_when_user_selects_hindex(context):

    button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Conferenze classificate per h-index']"))
    )
    button.click()

    time.sleep(2)


@step('l\'utente clicca sul pulsante "Aggiungi conferenza"')
def step_when_user_adds_conference(context):
    button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Aggiungi conferenza')]"))
    )

    button.click()
    time.sleep(2)


@step('l\'utente inserisce "International Conference on Automated Software Engineering" come titolo della seconda conferenza')
def step_when_user_inserts_conference(context):
    input_conference = WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located((By.NAME, 'conference_list'))
    )
    input_conference[1].send_keys("International Conference on Automated Software Engineering")
    time.sleep(2)


@then("l'utente visualizza la classifica della conferenza per h-index")
def step_when_user_sees_hindex_ranking(context):
    assert "Conferenze" in context.driver.find_element(By.ID, "classifica-container").text

    time.sleep(1)
    context.driver.quit()


@step('l\'utente inserisce "3D Data Processing Visualization and Transmission" come titolo della prima conferenza')
def step_when_user_inserts_first_conference(context):
    input_conference = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'conference_list'))
    )
    input_conference.send_keys("3D Data Processing Visualization and Transmission")
    time.sleep(2)