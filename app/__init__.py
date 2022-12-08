from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
from flask import session
import requests
import sqlite3
import os
import datetime
import random

app = Flask(__name__)
app.secret_key = os.urandom(16)
backgrounds = []

@app.route("/",methods=['GET', 'POST']) # At the root, we just return the homepage
def index():
    global backgrounds
    
    gif_info = requests.get("https://api.giphy.com/v1/gifs/search?api_key=1Ko27SdmSbweUZpNNz6FljJfxQdAoV9X&q=lofi&limit=25&offset=0&rating=g&lang=en")
    gif_info = gif_info.json()
    
    for i in gif_info["data"]:
        print(i["images"]["original"]["mp4"])
        backgrounds.append(i["images"]["original"]["url"][:-5])
        
    
    return render_template("index.html", gif=random.choice(backgrounds), audio="../static/assets/Field-of-Fireflies.mp3")
    

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()