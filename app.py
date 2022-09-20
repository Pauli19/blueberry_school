from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")
def index():
    return render_template('index.html.jinja')


@app.errorhandler(404)
def page_not_found(exc):
	return render_template('404.html.jinja'), 400
