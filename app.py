from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo


app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_mission"
mongo = PyMongo(app)

@app.route("/")
    def index():
         listings = mongo.db.listings.find_one()
        return render_template("index.html", listings=listings)
