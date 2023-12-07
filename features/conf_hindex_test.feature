# Created by Windows at 06/12/2023
Feature: Test della feature conf_hindex
  # Enter feature description here

  Scenario: Visualizzazione della classifica degli h-index di una conferenza
    Given l'utente è sulla pagina principale
    When l'utente seleziona l'opzione "Conferenze classificate per h-index"
    And l'utente inserisce "2012" come anno d'inizio
    And l'utente inserisce "2012" come anno di fine
    And l'utente inserisce "3D Data Processing Visualization and Transmission" come titolo della conferenza
    And l'utente clicca sul pulsante "Cerca"
    And l'utente clicca sul menù "Seleziona Classifica"
    Then l'utente visualizza la classifica della conferenza per h-index
