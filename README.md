# Citation Analyzer

## Introduzione
Il Citation Analyzer è uno strumento progettato per l'analisi delle citazioni in ambito accademico. Questo README fornisce una guida completa alla progettazione, implementazione e utilizzo del tool.

## Funzionalità Principali

### 1. Classifica degli Articoli
Il Citation Analyzer permette di classificare gli articoli di una conferenza in base al numero di citazioni ricevute. Questa funzionalità è cruciale per identificare e valorizzare i contributi più influenti.

### 2. Classifica delle Conferenze
Il tool offre la possibilità di classificare più conferenze in base all'h-index della conferenza. Questa metrica fornisce una panoramica della rilevanza e dell'impatto complessivo di una conferenza nel panorama accademico.

### 3. Classifica degli Autori Frequenti
Il Citation Analyzer facilita la classificazione degli autori più frequenti in diverse edizioni di una conferenza. Questo è particolarmente utile per individuare le personalità di spicco e le tendenze di ricerca all'interno di un determinato campo.

## Tecnologie Utilizzate

Il Citation Analyzer è stato implementato utilizzando il linguaggio di programmazione Python, avvalendosi delle librerie Selenium e Beautiful Soup per l'estrazione e l'analisi dei dati dalle pagine web.

### 1. Python
Il linguaggio di programmazione principale utilizzato per lo sviluppo del tool. La scelta di Python è motivata dalla sua flessibilità, facilità di apprendimento e dalla vasta comunità di supporto.

### 2. Selenium
Selenium è stato impiegato per l'automazione del browser, consentendo al Citation Analyzer di navigare in modo dinamico attraverso le pagine web delle conferenze e raccogliere dati in modo efficiente.

### 3. Beautiful Soup
Beautiful Soup è stato utilizzato per l'estrazione dei dati HTML restituiti dalle pagine web, semplificando il processo di analisi e manipolazione dei dati.

### Testing

Il testing del Citation Analyzer è stato effettuato utilizzando il modulo unittest di Python per i test di unità e Cucumber per i test di accettazione. Ciò garantisce che il tool sia affidabile, robusto e in grado di gestire una varietà di scenari.

## Istruzioni per l'Installazione

Per installare il Citation Analyzer e avviare l'analisi delle citazioni, seguire questi passaggi:

1. Clonare il repository:

    ```bash
    git clone https://github.com/GianvincenzoConcia/CitationAnalyzer.git
    ```

2. Spostarsi nella directory del tool:

    ```bash
    cd CitationAnalyzer
    ```

3. Installare le dipendenze:

    ```bash
    pip install -r requirements.txt
    ```

3. Dopo aver installato le librerie necessarie, eseguire il tool:

    ```bash
    python app.py
    ```

4. Per aprire la web app, clicca sul link: http://127.0.0.1:8080/