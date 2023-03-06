#%%
import datetime
import json
from flask import (
    Flask,
    render_template,
    request
)
from pymongo import MongoClient

app = Flask(__name__)
#%%
mongodb_cred = json.load(open("../credentials.json"))["MongoDB"]

#%%
client = MongoClient(
    host=f"mongodb+srv://{mongodb_cred['username']}:{mongodb_cred['password']}@cluster0.xu53fou.mongodb.net/")

app.db = client.Micro




# entries = []

@app.route("/",methods=["GET","POST"])
def home():
    # print([e for e in app.db.entries.find({})])
    entries_coll = app.db.entries
    
    if request.method == "POST":
        entry_content = request.form.get("content")
        if entry_content:            
            cur_date = datetime.datetime.today()
            # iso_format = cur_date.strftime("%Y-%m-%d")
            # month_format = cur_date.strftime("%b %d")
            # entries.append((entry_content,iso_format,month_format))
            entries_coll.insert_one({"cur_date":cur_date,
                                   "entry":entry_content})
    return render_template("home.html",entries=list(entries_coll.find({})))
