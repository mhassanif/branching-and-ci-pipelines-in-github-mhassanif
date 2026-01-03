from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    unused_var = "This triggers flake8"  # Unused variable
    x=1+2  # Missing spaces
    return "Hello from main page"

@app.route("/about")
def about():
    return render_template("about.html")


