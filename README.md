# Documentation - Terminal assignment 

## App Overview 

FilmSpot is a program where users can search and find films listed on IMBDs top 1000 movies of all time database. Users can create a profile, add movies from the database to their own 'my favourites' folder then retrieve film reccommendations based on these favourites. An additional feature is FilmSpot Trivia, a component of the app where users can test their Hollywood knowledge and discover great films in the process.

Work was completed within a Kanban agile framework via Trello. 


## App Features
---

### 1. User accounts & sessions 

Users have the option to search the (IMBD) FilmSpot database and play trivia without creating or signing into their account. However, to utilise the 'my favourites' and 'my recommended' funcitons, they will be asked to enter their full name with will log them in, or create a new user. 

### 2. Database Search

Users can search the database by entering '1' on the main menu. 

![](/Assets/MainMenu.png)

Users then are prompted to filter their search by chosing to search by movie Title, Year, Cast or Director.

### 3. My Reccomendations 

This is a simple function that returns a list of 10 movies 

<em>Limitations </em>

Clarification should be made regarding the sophistocation of the reccommended list returned. Due to the low quality of data in the IMBD dataset used in this terminal app, I was unable to build a proper reccomendations algorithem, I also did not have time to try to enhance the results by performing a Multiple Factor Analysis or PCA that would have helped significantly. In turn, the 'reccomended' list is considered more a list not of 'similar' movies to the on the user inputs, but a list of movies they might enjoy (being the same rating and similar genres). Either way I felt the tool was usefull to the average user. 

### 3. My to-watch-list

Users can sign in/create an account which allows them to store the list they are recomended in the 'my reccomendations' section (menu item 4.). Users are prompted whether they wish to 'add' (append) the recommendations list onto their 'to-watch-list. 
