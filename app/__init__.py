from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
from flask import session, redirect, url_for
import requests
import sqlite3
import os
import datetime
import random

import cheats
from user import User
from current import currentUser

app = Flask(__name__)
app.secret_key = os.urandom(16)
backgrounds = []
cheats.setup()

username = "hello"
password = "bye"

@app.route("/",methods=['GET', 'POST']) # At the root, we just return the homepage
def index():
    print("hello")
    global backgrounds
    gif_info = requests.get("https://api.giphy.com/v1/gifs/search?api_key=1Ko27SdmSbweUZpNNz6FljJfxQdAoV9X&q=lofi&limit=25&offset=0&rating=g&lang=en")
    gif_info = gif_info.json()

    #print(gif_info["data"])
    for i in gif_info["data"]:
        try:
            #print(i["images"]["hd"]["mp4"])
            backgrounds.append(i["images"]["original"]["url"][:-5])
            #print(i["images"]["hd"])
        except:
            None
        #backgrounds.append(i["images"]["original"]["url"])
    # if 'username' in session:
    #     return render_template("index.html", gif=random.choice(backgrounds), audio="../static/assets/Field-of-Fireflies.mp3", islogged=True)
    return render_template("index.html", gif=random.choice(backgrounds), audio="../static/assets/Field-of-Fireflies.mp3")


@app.route("/loginRdrct")
def profileOrLogin():
    if 'username' in session:
        return redirect("/profile")
    return redirect("/login")


#create a new account:
@app.route("/signup", methods = ['GET', 'POST'])    # HARD CODED LOGIN INFORMATION
def register():
    # GET request: display the form
    if request.method == "GET":
        return render_template("signup.html")

    # POST request: handle the form response and redirect
    username = request.form['username']
    password = request.form['password']

    User.new_user(username, password)
    return redirect(url_for('login'))


@app.route("/login", methods = ['GET','POST'])
def login():
    if "username" in session:
        return redirect(url_for('index'))

    # GET request: display the form
    if request.method == "GET":
        return render_template('login.html')

    usr = request.form['username']
    psw = request.form['password']

    # The Log-In Worked!
    if User.authenticate_user(usr, psw):
        session["username"] = usr
        session["user_id"] = User.get_ID(usr)
        # return render_template('index.html', username = usr, currUsrSess = currentUser(session["user_id"]))
        return redirect(url_for('index'))

    return render_template('login.html', result = "username or password is incorrect")


# Session clearing/Logout
@app.route("/logout", methods = ['GET', 'POST'])
def logout():
    if 'username' in session:
        session.pop('username', None)
        return redirect(url_for('index'))
    return "error.html"


@app.route("/profile")
def profile():
    return render_template("profile.html")


if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
