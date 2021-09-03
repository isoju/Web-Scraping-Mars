#listing dependencies
from flask import Flask, render_template, redirect
import pymongo

# Create an instance of our Flask app.
app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

db = client.mars_db

@app.route("/")
def index():
    mars_dict = db.mars_dict.find_one()
    return render_template("index.html", mars = mars_dict)

@app.route("/scrape")
def scrape():

    mars_dict = db.mars_dict
    mars_data = scrape_mars.scrape()
    mars_dict.update({}, mars_data, upsert = True)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
