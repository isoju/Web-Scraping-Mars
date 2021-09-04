#listing dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of our Flask app.
app = Flask(__name__)

# Create connection variable
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


mongo.db.mars_dict.drop()
# Pass connection to the pymongo instance.


@app.route("/")
def index():
    mars_dict = mongo.db.mars_dict.find_one()
    return render_template("index.html", mars = mars_dict)

@app.route("/scrape")
def scrape():
    mars_data = scrape_mars.scrape()
    mongo.db.mars_dict.update({}, mars_data, upsert = True)
    return redirect("/", code= 302)

if __name__ == "__main__":
    app.run(debug=True)
