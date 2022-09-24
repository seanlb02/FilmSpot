# Documentation - Terminal assignment 

## Repo: https://github.com/seanlb02/terminal_app
### Video Walkthrough: https://vimeo.com/753217247

## App Overview 

FilmSpot is a program where users can search and find films listed on IMBDs 'top 1000 movies of all time' database. Users can create a profile, search the database add movies from the database to their own 'watchlist' then retrieve film reccommendations based on these favourites. An additional feature is FilmSpot Trivia, a component of the app where any user can test their Hollywood knowledge and discover great films in the process.

Work was completed within a Kanban agile framework using Trello to track progress.

Code styling followed the PEP8 Python style guide (PEP8, 2001).

### Recognition 

The app utilises IMBD's official top 1000 movies data via a dataset compiled by Omar Hany licenced via the IMBD authors and accessed via Kaggle.

## App Features
---

### 1. User accounts

Users have the option to search the (IMBD) FilmSpot database, play trivia and get reccomendations without creating or signing into their account. However, to utilise the 'watchlist' funciton, they will be asked to either login or create an account. User names and their 'watchlist' are stored as instances of a class called <em>Users</em>. This instance is create with a static method within the class and is permanently stored as a serialized instance via python pickle.

### 2. Database Search

Users can search the database by entering '1' on the main menu. 

![](/Assets/MainMenu.png)

Users then are prompted to filter their search by chosing to search by movie Title, Year, Cast or Director. After choosing a filter method, users can enter a search keyword and the system returns a search result. 

### 3. Reccomendation 

This is a simple function that returns a list of 10 movies that the user might like. It works by asking the user to enter a film, and the system renders movies that match (1) the input film's classification and (2) either the primary or secondary genre.

<em>Limitations </em>

Clarification should be made regarding the sophistocation of the reccomendation "algorithm". Due to the low quality of data in the IMBD dataset used in this terminal app, I was unable to build a proper reccomendations algorithm, I also did not have time to try to enhance the results by performing a Multiple Factor Analysis or PCA that would have helped significantly. In turn, the 'reccomended' list is considered more a list NOT of 'similar' movies to the on the user inputs, but a list of movies they might enjoy (being the same rating and similar genres). Either way I felt the tool would be usefull to the average user.

### 3. User Watchlist

Once a user has used the recommendation function, they can chose to add the returned list of movies to their movie watchlist, which is stored/pickled on their account.

The process:

    (1) Recommended movie list (10) is returned 
    (2) User is asked to enter a username, 
                if an account exists in their folder:
                the program unpickles their instance
                watchlist, appends the reccommended 
                movie list to the preexisting 
                watchlist dataframe and then saves it 
                by pickling and overwriting the users 
                instance. 
                if no account is stored in the file: 
                the user enters a username to create 
                an account and a new instance is
                generated + pickled in the folder,
                ready to be appended with a 
                reccomended movies list. 

## Development Implelentation Plan 
---

Trello Kanban project tracking was implemented to guide the following task checklists in the development of each app component:


![](/Assets/trelloSS1.png)

### Database cleaning, formatting and storage as a class 

1. Write command within primary database Class that loads in the data stored on csv within program folder.
2. Data needs to be cleaned: remove unecessary columns, convert values to title-case string
3. format pandas so that when printed, dataframes and values are displayed in their entirety

### Search/filter function 

1. Initialise staticmethod within primary dataframe class
2. build an input function that accepts any value yet converts to a title-cased string.
3. write initialiser prompt that asks user how they wish to search the database: title, cast member, year, director
4. make if/else block within an infinite while loop that returns a dataframe with rows that match the users input
5. Ensure errors are caught either with else or Try blocks - write an error handler to ensure also that while loop is not broken 
6. ensure user can return to the main menu and end while loop with an input 'back


### Trivia function

1. Create static mthod within primary database class that is accessible in the main menu function
2. Allow user to decide when to start by inputting 'start. Start will initate an infinite while loop that terminates when/if user enters 'back' to main menu
3. Once started, write loop that fetches a RANDOM row from the database and prints ONLY the value string from the 'synopsis' column. User is then prompted to guess the movie title with another input
4. build a hint option that returns the movie's year and director if the user asks for it
5. Add a counter component to the loop that tracks what number question is being asked and also what the user score is. These counts are reset if there is a wrong answer inputted and the game ends. 


### Reccomender/account creation function

1. Write a function that takes a users input: a movie title, and returns (prints) the top 10 results of the returned dataframe that shares the same Genre 1, Genre 2 and Classification as the users inputted movie title
2. prompt the user to chose whether they want to add the list to their 'watchlist'. User is asked to enter a username, if a name exists in the folder as a picked instance, this will add the recommended list to their 'watchlist'. 
3. if username does not exist, user is asked if they want to make an account. Entering any user name will make and pickle a new instance of User class - the attributes being the username and an empty dataframe
4. Like all component functions, users must be able to be able to enter 'back' to break out of the function loop.

### Display user watchlist function 

1. Option 2 on the main menu will trigger the watchlist function/component. 
2. the function must be an infinite while loop where users can input a username, if the username exists in pickled format, it will be unpacked and  the 'watchlist' instance attribute/varibale will be printed.
3. loop can be broken by pressing back (breaks loop and returns to main menu via calling the main menu function) 


### main menu function

1. Main menu component is a simple function containing a primary while loop that starts with an input which asks users to enter a number between 1 and 4. Each number corresponds with a menu item/option. 
2. Continuing the loop and error handling with a try block if user inputs any value 
3. build conditonal: if user input is 'back' the program terminates with a goodbye message printed. 

---

### References

van Rossum, G., Warsaw, B., Coghlan, N. 2001. Python Enhancements Proposal 8 - Style guide for Python code. https://peps.python.org/pep-0008/. Accessed 21/9/22. 

Hany, O. 2020. IMDB top 1000 movies dataset. https://www.kaggle.com/datasets/omarhanyy/imdb-top-1000. Accessed 10/9/22