from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def jinja():
    return render_template("jinja_intro.html",
                           name="Lakshman",
                           template="Jinja")