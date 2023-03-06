import datetime
import json
from flask import (
    Flask,
    render_template,
    request
)
from pymongo import MongoClient


def create_app():
    app = Flask(__name__)

    mongodb_cred = json.load(open("../credentials.json"))["MongoDB"]
    client = MongoClient(
        host=f"mongodb+srv://{mongodb_cred['username']}:{mongodb_cred['password']}@cluster0.xu53fou.mongodb.net/")
    app.db = client.Micro
    app.coll = app.db.entries

    @app.route("/",methods=["GET","POST"])
    def home():               
        if request.method == "POST":
            entry_content = request.form.get("content")
            if entry_content:            
                cur_date = datetime.datetime.today()
                app.coll.insert_one({"cur_date":cur_date,
                                    "entry":entry_content})
        return render_template("home.html",entries=list(app.coll.find({})))
    
    return app