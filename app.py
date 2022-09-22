from ensurepip import bootstrap
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)

bootstrap = Bootstrap5(app)

@app.get("/")
def index():
    return render_template('index.html.jinja')


@app.errorhandler(404)
def page_not_found(exc):
    return render_template('404.html.jinja'), 404


@app.errorhandler(500)
def internal_server_error(exc):
    return render_template('500.html.jinja'), 500
