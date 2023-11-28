from flask import Flask, render_template
from waitress import serve

from ranking_articles import setup_classifica_routes

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('interfaccia_web.html', result=None)


if __name__ == '__main__':
    setup_classifica_routes(app)
  #  setup_autori_routes(app)

    serve(app, host="0.0.0.0", port=8080)
