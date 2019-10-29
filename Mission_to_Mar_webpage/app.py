# Import libraries
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


# Create instance of Flask app
app = Flask(__name__)


# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)
    

# Create route to query Mongo and pass the mars data into the HTML template to display.
@app.route("/")
def index():

    mars_web = mongo.db.mars.find_one()
    print(mars_web)
    return render_template("index.html", mars_web=mars_web)



# Create route that renders mission to mars template
@app.route("/scrape")
def scrapper():
    mars_web = mongo.db.mars
    mars_data = scrape_mars.scrape()
    mars_web.update({}, mars_data, upsert=True)
    return redirect("/", code=302)




if __name__ == "__main__":
    app.run(debug=True)