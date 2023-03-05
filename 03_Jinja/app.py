from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def jinja():
    return render_template("jinja_intro.html",
                           name="Lakshman",
                           template="Jinja")
    
@app.route("/expressions/")
def render_expression():
    kwargs = dict(color="brown",
                  animal_one="fox",
                  animal_two="dog",
                  orange_amount=10,
                  apple_amount=20,
                  donate_amount=15,
                  first_name="Captain",
                  last_name="Marvel")
    return render_template("expression.html",**kwargs)