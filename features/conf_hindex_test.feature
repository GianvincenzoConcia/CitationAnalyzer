# Created by Windows at 06/12/2023
Feature: Test della feature conf_hindex

    Scenario: Conferenza non trovata
    Given l'utente è sulla pagina principale
    When l'utente seleziona l'opzione "Conferenze classificate per h-index"
    And l'utente inserisce "2012" come anno d'inizio
    And l'utente inserisce "2012" come anno di fine
    And l'utente inserisce "3D Data Processing Visualization and Transmission" come titolo della "1"a conferenza
    And l'utente inserisce "International Conference on Automated Software Engineering" come titolo della "2"a conferenza
    And l'utente clicca sul pulsante "Aggiungi conferenza"
    And l'utente inserisce "Conferenza non esistente" come titolo della "3"a conferenza
    And l'utente clicca sul pulsante "Cerca"
    Then l'utente visualizza il messaggio di errore

    Scenario: Visualizzazione della classifica degli h-index di più tre conferenze
    Given l'utente è sulla pagina principale
    When l'utente seleziona l'opzione "Conferenze classificate per h-index"
    And l'utente inserisce "2012" come anno d'inizio
    And l'utente inserisce "2012" come anno di fine
    And l'utente inserisce "3D Data Processing Visualization and Transmission" come titolo della "1"a conferenza
    And l'utente inserisce "International Conference on Automated Software Engineering" come titolo della "2"a conferenza
    And l'utente clicca sul pulsante "Aggiungi conferenza"
    And l'utente inserisce "Software Engineering" come titolo della "3"a conferenza
    And l'utente clicca sul pulsante "Cerca"
    And l'utente clicca sul menù "Seleziona Classifica"
    Then l'utente visualizza la classifica della conferenza per h-index

  Scenario: Visualizzazione della classifica degli h-index di due conferenza
    Given l'utente è sulla pagina principale
    When l'utente seleziona l'opzione "Conferenze classificate per h-index"
    And l'utente inserisce "2012" come anno d'inizio
    And l'utente inserisce "2012" come anno di fine
    And l'utente inserisce "3D Data Processing Visualization and Transmission" come titolo della "1"a conferenza
    And l'utente inserisce "International Conference on Automated Software Engineering" come titolo della "2"a conferenza
    And l'utente clicca sul pulsante "Cerca"
    And l'utente clicca sul menù "Seleziona Classifica"
    Then l'utente visualizza la classifica della conferenza per h-index
