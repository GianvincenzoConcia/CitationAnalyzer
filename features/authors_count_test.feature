# Created by Windows at 06/12/2023
Feature: Test della feature authors_count

  Scenario: Data fine precedente a data inizio
    Given l'utente è sulla pagina principale
    When l'utente seleziona l'opzione "Autori più presenti nella conferenza"
    And l'utente inserisce "3D Data Processing Visualization and Transmission" come titolo della conferenza
    And l'utente inserisce "2012" come anno d'inizio
    And l'utente inserisce "2011" come anno di fine
    And l'utente clicca sul pulsante "Cerca"
    Then l'utente visualizza il messaggio di errore

  Scenario: Ricerca e visualizzazione del grafico degli autori più presenti
    Given l'utente è sulla pagina principale
    When l'utente seleziona l'opzione "Autori più presenti nella conferenza"
    And l'utente inserisce "3D Data Processing Visualization and Transmission" come titolo della conferenza
    And l'utente inserisce "2012" come anno d'inizio
    And l'utente inserisce "2012" come anno di fine
    And l'utente clicca sul pulsante "Cerca"
    And l'utente clicca sul menù "Seleziona Grafico"
    Then l'utente visualizza il grafico degli autori

  Scenario: Ricerca e visualizzazione della classifica degli autori più presenti
    Given l'utente è sulla pagina principale
    When l'utente seleziona l'opzione "Autori più presenti nella conferenza"
    And l'utente inserisce "3D Data Processing Visualization and Transmission" come titolo della conferenza
    And l'utente inserisce "2012" come anno d'inizio
    And l'utente inserisce "2012" come anno di fine
    And l'utente clicca sul pulsante "Cerca"
    And l'utente clicca sul menù "Seleziona Classifica"
    Then l'utente visualizza la classifica degli autori