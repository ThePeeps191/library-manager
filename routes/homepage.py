from flask import render_template, url_for

def homepage():
	return render_template("index.html")