# Documentation - Terminal assignment 

## Repo: https://github.com/seanlb02/terminal_app

## App Overview 

FilmSpot is a program where users can search and find films listed on IMBDs 'top 1000 movies of all time' database. Users can create a profile, search the database add movies from the database to their own 'watchlist' then retrieve film reccommendations based on these favourites. An additional feature is FilmSpot Trivia, a component of the app where any user can test their Hollywood knowledge and discover great films in the process.

Work was completed within a Kanban agile framework using Trello to track progress.

Code styling followed the PEP8 Python style guide (PEP8, 2001).


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

### Database cleaning, formatting and storage as a class 

sdfwe

![](/Assets/trelloSS1.png)


---

### References

van Rossum, G., Warsaw, B., Coghlan, N. 2001. Python Enhancements Proposal 8 - Style guide for Python code. https://peps.python.org/pep-0008/. Accessed 21/9/22. 