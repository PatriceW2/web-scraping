from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scrape


app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_mission"
mongo = PyMongo(app)

@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)


@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scrape.scrape()
    mars.update({}, mars_data, upsert=True)
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)


