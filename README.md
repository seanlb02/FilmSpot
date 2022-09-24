## FilmSpot: A python terminal app

FilmSpot is a program where users can search and find films listed on IMBDs 'top 1000 movies of all time' list. Users can create a profile, search the database, retrieve film reccommendations based on their favourites then add them to their own 'watchlist'. An additional feature is FilmSpot Trivia, a component of the app where any user can test their Hollywood knowledge and discover great films in the process.

### Dependancies 

Filmspot requires Python3, pip, as well as the following dependancies in order to run via your terminal: <em>Pandas, Numpy</em>:

```
$ pip install pandas
$ pip install numpy
```

## How to download and run

Open your terminal and execute the following.

1. Download Zip:

```
$ curl -LJO https://github.com/seanlb02/FilmSpot/archive/refs/heads/main.zip 
```
2. Extract the zip to a directory of your choosing...

3. <em>Enter</em> the 'FilmSpot-main' directory:

```
$ cd {directory zip was extracted}
$ cd FilmSpot-main
```

4. Launch program with:
```
$ python3 main.py
```

## Instructions 

At start-up the main menu is launched. Choose between options 1-4 to navigate the app. Entering 'back' will terminate the program. 

** Remember, to return to the main menu, simply keep entering 'back' **

![](/Assets/MainMenu.png)

### Option 1. Database Search

Entering 1. will take you to the database search. Once here, you will have the choice of searching the database by movie Title, Year, Cast member or Director. 

    Enter [Name] or [Year] or [Cast] or [Director]

*Don't worry, our inputs aren't case-sensitive

Once a search method is chosen, you may then type who/what/when you're interested in and have a peruse through the database. 

All results (if there are any) will be displayed for you instantly. 

### Option 2. My Watchlist 

Entering 2. on the main menu will open your watchlist. 

FilmSpot allows users to create an account and store movies to their 'watchlist'. Movies can only be stored from FilmSpots recommended list. Don't worry, our selections are great, and remember our goal is to get you watching the top 1000 movies before you die. So lets get cracking.

If you have an account, enter your user name and your watchlist will appear on the screen. 

To create an account, have a go at the reccomendations menu option - Option 3.

### Option 3. Reccomendations 

Selecting 3. on the main menu will take you to our movie reccomendation function. 

All you need to do is enter the title of a movie you are fond of. Then Filmspot will return a list of 10 movies that we think you might like. Not all movies will be similar to the one you selected, our intent is to broaden your horizons, right after you point us in the right direction of course. 

Once you have returned a list of movies, you are given the option to add them to your watchlist. Enter 'yes' here to add and authenticate by entering your account username. 

If you do not yet have an account, don't stress. You will be prompted to enter a username which will set you up. After entering a name and saving your first reccomended list to your watchlist, you will be set up in our system.

Go 'back' to the main menu and have another go at looking at your watchlist ('Option 2.
')

### Option 4. FilmSpot Trivia

Film spot trivia is a simple hollywood knowledge-tester. Users who are game are provided with a short film bio per round, and are tasked with guessing the film's title.

Don't stress if you cant get it straight away, just enter 'hint' and we will give you a hand. 

Earn 5 points per correct answer and discover some gems in the process. 

** As always, to return to the main menu, just enter 'back' until you get there **

## Quick termination

To terminate the program instantly, simply enter ctrl+'c'. 

Enjoy!

## Unit Testing

Three tests were designed and run on the main menu, search, and trivia functions. These files are included in the program directory downloaded as zip. Because all functions and methods were packeaged in infinite loops, tests were designed to run through a single iteration using multiple inputs. 