# Created by gianvincenzoconcia at 06/12/23
Feature: Test della feature ranking_articles

  Scenario: Ricerca e visualizzazione della classifica
  Given l'utente è sulla pagina principale
    When l'utente seleziona l'opzione "Classifica articoli più citati"
    And l'utente inserisce "3D Data Processing Visualization and Transmission" come titolo della conferenza
  And l'utente inserisce "2012" come anno
  And l'utente clicca sul pulsante "Cerca"
    And l'utente clicca sul menù "Seleziona Classifica"
  Then l'utente visualizza la classifica degli articoli

