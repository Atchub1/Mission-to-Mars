# import libraries
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


# create instance of Flask app
app = Flask(__name__)

# # Create connection variable
# conn = 'mongodb://localhost:27017'

# # Pass connection to the pymongo instance.
# client = pymongo.MongoClient(conn)


# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)
    


# create route to query Mongo and pass the mars data into the HTML template to display.
@app.route("/")

def index():

    mars_web = mongo.db.mars.find_one()
    print(mars_web)
    return render_template("index.html", mars_web=mars_web)



# create route that renders mission to mars template
@app.route("/scrape")
def scrapper():
    mars_web = mongo.db.mars
    mars_data = scrape_mars.scrape()
    mars_web.update({}, mars_data, upsert=True)
    return redirect("/", code=302)


#         render_template("scrape_mars.py")

#     # Connect to/create the mars database
#     db = mongo.mars_db

#     # Drop the collection, if available, to remove duplicates
#     db.mars.drop()

#     # create the collection and insert the scrap results as one document
#     db.mars.insert_one(
#         mars_web_dict
#         )





if __name__ == "__main__":
    app.run(debug=True)