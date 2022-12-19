from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
from flask import session, redirect, url_for
import requests, json
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
trivToken = "YOURTOKENHERE"
cheats.setup()

username = "hello"
password = "bye"

@app.route("/",methods=['GET', 'POST']) # At the root, we just return the homepage
def index():
    print("hello")
    global backgrounds

    # GIPHY API KEY
    with open('keys/key_giphy.txt', 'r') as f:
        key = f.read()

    gif_info = requests.get(f"https://api.giphy.com/v1/gifs/search?api_key={key}&q=lofi&limit=25&offset=0&rating=g&lang=en")
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

@app.route("/destress")
def destress():
    return render_template("destress.html")

@app.route("/catpics")
def catpics():
    cat_info = requests.get(f"https://api.thecatapi.com/v1/images/search")
    cat_info = json.loads(cat_info.text)
    return render_template("catpics.html", caturl = cat_info[0]['url'])

@app.route("/dadjokes")
def dadjokes():
    with open('keys/key_dadjokes.txt', 'r+') as f:
        key = f.read()

    joke_info = requests.get(f"https://dad-jokes.p.rapidapi.com/random/joke?rapidapi-key={key}")
    joke_info = json.loads(joke_info.text)
    return render_template("dadjokes.html", jokeSetup=joke_info["body"][0]["setup"], punchline=joke_info["body"][0]["punchline"])

@app.route("/trivia")
def trivia():
    global trivToken
    category = 0
    triv_info = requests.get(f"https://opentdb.com/api.php?amount=1&token={trivToken}&category={category}&type=multiple")
    triv_info = json.loads(triv_info.text)
    if (triv_info["response_code"] != 0):
        trivToken = json.loads((requests.get("https://opentdb.com/api_token.php?command=request")).text)["token"] 
        return trivia()
    else:
        return render_template("trivia.html", question=triv_info["results"][0]["question"])

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
