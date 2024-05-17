# Imports
from flask import Flask, render_template, url_for

# Custom Imports
import routes

# App
app = Flask(__name__)

# Routes
app.add_url_rule("/", view_func = routes.homepage)

# Error Handling
@app.errorhandler(404)
def e404(e):
	return render_template("404.html")

# Run
if __name__ == "__main__":
	app.run(debug = True, host = "0.0.0.0")