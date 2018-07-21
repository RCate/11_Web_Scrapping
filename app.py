from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import Scraping_Mars

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/Mars_DB"
mongo = PyMongo(app)


@app.route("/")
def index():
    Mars = mongo.db.Mars_info.find_one()
    return render_template("index.html", Mars=Mars)


@app.route("/scrape")
def scrape():
    print("Starting scrape...")
    news = Scraping_Mars.scrape_News()
    # image = Scraping_Mars.scrape_image()
    weather = Scraping_Mars.scrape_weather()
    table_info = Scraping_Mars.scrape_table_info()

    mars_data = {
        "News_Title": news["News_title"],
        "News_Announcement": news["News_paragraphs"],
        # "Mars_Current_Image": image["featured_image_url"],
        "Mars_Current_Weather": weather["mars_weather"],
        "Mars_General_Information": table_info["Table"]
        
    }
    print(mars_data)
 
    mongo.db.Mars_info.insert_one(mars_data)  
   
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
