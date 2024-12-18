from flask import Flask, render_template
from waitress import serve

from src.authors_count import setup_authcount_routes
from src.conf_hindex import setup_hindex_routes
from src.ranking_articles import setup_classifica_routes

app = Flask(__name__, template_folder='templates')
app.secret_key = 'il tuo segreto'

@app.route('/')
def index():
    return render_template('interfaccia_web.html', result=None)


if __name__ == '__main__':
    setup_classifica_routes(app)
    setup_hindex_routes(app)
    setup_authcount_routes(app)

    serve(app, host="0.0.0.0", port=8080)
