from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/fancy")
def hello_world_fancy():
    return """
        <html>
        <body>
        <h1>Greeting</h1>
        <body>
        </html>
        """