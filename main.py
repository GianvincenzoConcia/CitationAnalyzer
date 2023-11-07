from flask import Flask, render_template, request
import requests

app = Flask(__name__)


# La funzione ricerca la conferenza su DBLP
def cerca_conferenza(conference_query):
    pass


# Pagina iniziale con il form di ricerca per la conferenza specifica
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        conference_query = request.form['conference_query']
        results = cerca_conferenza(conference_query)
        if results:
            return render_template('results.html', results=results)
        else:
            return "Errore nella ricerca della conferenza."
    return render_template('interfaccia_web.html')


if __name__ == '__main__':
    app.run(debug=True)
