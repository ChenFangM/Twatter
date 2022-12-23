# REST Cafe by coffeebuds 

## Roster  
* Fang Min Chen (PM)
  * Flask: Routing/linkages
  * Incorporating apis for the destress page
  * Building HTML pages
* Abid Talukder
  * Using Bootstrap to build the site
  * Building HTML pages
* Faiza Huda
  * Constructing a to-do list db and incorporating its functionality
* Ziying Jian
  * Constructing a functioning login and registration page
  * Incorporating YouTube embed to create a radio
  
## Description
REST Cafe is a cute and comforting study website with a radio, to-do lists, Pomodoro timers, coffee, Dad jokes, and more (inspired by [Lofi Cafe](https://www.lofi.cafe/)). We intend to have a homepage and destress tab accessible to logged-in users and passerbys; this includes the radio, pomodoro timer, random jokes and cat pictures to make studying less tedious. We will also have a signup and login so that returning users will be able to save their to-do list and modify it as long as they're logged in. Our website incorporates function, focus, and fun (FFF) to make sure you'll bookmark us for the next time you're last-minute studying.

## APIs Used
* [CatAPI](https://github.com/stuy-softdev/notes-and-code/blob/main/api_kb/411_on_CatAPI.md)
* [DadJokes](https://github.com/stuy-softdev/notes-and-code/blob/main/api_kb/411_on_DadJokes.md)
* [Giphy](https://github.com/stuy-softdev/notes-and-code/blob/main/api_kb/411_on_Giphy.md)
* [OpenTriviaDB](https://github.com/stuy-softdev/notes-and-code/blob/main/api_kb/411_on_OpenTriviaDB.md)

## Launch Code
Clone this repo.
``` 
$ git clone https://github.com/ChenFangM/coffeebuds.git
```

Find your way into the repo.
```
$ cd coffeebuds/
```

Install required packages
```
$ pip install -r requirements.txt
```

Find your way into the app directory.
```
$ cd app/
```

Run Flask
```
$ python3 __init__.py  
```

Enjoy REST Cafe via your local host address ``http://127.0.0.1:5000/`` in your browser.
