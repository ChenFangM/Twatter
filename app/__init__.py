from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
from flask import session, redirect, url_for
import requests
import sqlite3
import os
import datetime
import random

app = Flask(__name__)
app.secret_key = os.urandom(16)
backgrounds = []

username = "hello"
password = "bye"

@app.route("/",methods=['GET', 'POST']) # At the root, we just return the homepage
def index():
    global backgrounds
    gif_info = requests.get("https://api.giphy.com/v1/gifs/search?api_key=1Ko27SdmSbweUZpNNz6FljJfxQdAoV9X&q=lofi&limit=25&offset=0&rating=g&lang=en")
    gif_info = gif_info.json()
    for i in gif_info["data"]:
        backgrounds.append(i["images"]["original"]["mp4"])

    if 'username' in session:
        return render_template("index.html", gif=random.choice(backgrounds))
    return render_template("login.html") # add vars 


app.route("/login", methods = ['GET','POST'])
def login():

    # GET request: display the form
    if request.method == "GET":
        return render_template("login.html")

    usr = request.form['username']
    psw = request.form['password']

    if username == usr and password == psw:
        return redirect("index")

    # The Log-In Worked!
    # if User.authenticate_user(usr, psw):
    #     session["username"] = usr
    #     session["user_id"] = User.get_ID(usr)
    #     return render_template('index.html', username = usr, currUsrSess = currentUser(session["user_id"]))

    return render_template('login.html', result = "username or password is incorrect")


#create a new account:
@app.route("/signup", methods = ['GET', 'POST'])
def register():
    if "username" in session:
        return redirect(url_for('index'))

    # GET request: display the form
    if request.method == "GET":
        return render_template("signup.html")

    # POST request: handle the form response and redirect
    username = request.form['username']
    password = request.form['password']
    
    # User.new_user(username, password)

    return redirect(url_for('login'))


# Session clearing/Logout
# Honestly this is for me so I know that the guest page works
@app.route("/log-out", methods = ['GET', 'POST'])
def logout():
    if 'username' in session:
        session.pop('username', None)
        return redirect(url_for('index'))
    return "error.html"



if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()