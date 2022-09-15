from sklearn.decomposition import PCA
import pandas as pandas
import numpy as n 

# setting up the primary moveis database with Pandas #


# df = pandas.read_csv('/home/lucian2/data for terminal app/imdb_top_1000.csv')
# df = df.drop(df.columns[[0, 3, 4, 8, 14, 15]], axis=1)
# df.rename(columns = {'Series_Title':'Name', 'Released_Year':'Year', 'Overview':'Synopsis', 'IMDB_Rating':'IMBD rating'}, inplace = True)
# df[["Genre", "Genre 2", "Genre 3"]] = df["Genre"].str.split(",", expand=True)
# df.index.name = "Rank"
# df.index += 1


# app_df = df

# the primary movies data base is stored in a class called App_dataframe


class App_dataframe:
    

    # the primary database class is initialised by making the pandas dataframe an attriubte 
    # this makes the dataframe easily accessbile by sub-classes and methods 

    def __init__(self, app_df):
        self.app_df = app_df

    #here we create the dataframe by (1) setting up a pandas Dataframe (2) cleaning the data (3) setting the key class variable "app_df"


    df = pandas.read_csv('/home/lucian2/data for terminal app/imdb_top_1000.csv')
    df = df.drop(df.columns[[0, 3, 4, 8, 14, 15]], axis=1)
    df.rename(columns = {'Series_Title':'Name', 'Released_Year':'Year', 'Overview':'Synopsis', 'IMDB_Rating':'IMBD rating'}, inplace = True)
    df[["Genre", "Genre 2", "Genre 3"]] = df["Genre"].str.split(",", expand=True)
    df.index.name = "Rank"
    df.index += 1

## Set the class variable ##
    app_df = df

    #this is the method for the 'filter/search' functionality
    @staticmethod
    def filter_function():

        while True:
            filter_method = str(input(f"Select how you want to filter our database [Name, Year, Genre, Cast, Director]: ").title())
            while filter_method == "Name":
                title_search = str(input(f'Enter your movie title: ').title())
                result = App_dataframe.app_df.loc[App_dataframe.app_df['Name'] == (f'{title_search}')]
                if title_search == "Back":
                    break
                elif title_search not in App_dataframe.app_df.values:
                    print('Hmm...Looks like that one is not in our top 1000. Check your spelling and try again')
                else:
                    print(f'Yep! its in there: ')
                    print(result)
                    break

            while filter_method == "Year":
                year_search = str(input(f'Enter a year: ').title())
                result = App_dataframe.app_df.loc[App_dataframe.app_df['Year'] == (f'{year_search}')]
                if year_search == "Back":
                    break
                elif year_search not in App_dataframe.app_df.values:
                    print("Invalid input, give it another go")
                else:
                    print(f'---Results for {year_search}---')
                    print(result)
                    break

            while filter_method == "Genre":
                genre_search = (input(f'Enter one or more genres from the following [Action, Drama, Comedy, Adventure, Animation, Biography, Horror, Fantasy, History]: ').title())
                result = App_dataframe.app_df[App_dataframe.app_df.isin([f'{genre_search}']).any(axis=1)]
                if genre_search == "Back":
                    break
                elif genre_search not in App_dataframe.app_df.values:
                    print('Oops...Looks like what you have entered is invalid')
                else:
                    print(f'---Results for {genre_search}--- ')
                    print(result)
                    break

            while filter_method == "Cast":
                cast_search = (input(f'Enter the name of an actor or actress: ').title())
                result = App_dataframe.app_df[App_dataframe.app_df.isin([f'{cast_search}']).any(axis=1)]
                if cast_search == "Back":
                    break
                elif cast_search not in App_dataframe.app_df.values:
                    print(f"Hmm... either {cast_search} isnt in our 1000, or you made them up...")
                else:
                    print(f'---Results for {cast_search}--- ')
                    print(result)
                    break

            while filter_method == "Director":
                director_search = str(input(f'Enter the full name of a director: ').title())
                result = App_dataframe.app_df.loc[App_dataframe.app_df['Director'] == (f'{director_search}')]
                if director_search == "Back":
                    break
                elif director_search not in App_dataframe.app_df.values:
                    print(f"Hmm... either {director_search} isnt in our 1000, you misspelt, or you made them up...")
                else: 
                    print(f'---Results for {director_search}--- ')
                    print(result)
                    break

            if filter_method == "Back":
                App_dataframe.show_main_menu()
                break
            else:
                print('\n\nWant to give it another go? Remember, you can enter [back] to return to the main menu')

# this is the main menu - a static fuction, called when the program opens and then when the user enters 'back' enough times while the program is running

    @staticmethod
    def show_main_menu():
        print("-------------------Welcome to the main menu--------------------\n\n\n 1.    Search the FilmSpot database       2.     Your to-watch-list \n\n 3.    Your Recommendations               4.     FilmSpot Trivia!\n\n\n")
        menu_selection = str(input(f'Select where you would like to go[Enter 1,2,3 or 4]: ').title())
        while True:
            if menu_selection == "1":
                App_dataframe.filter_function()
                break
            elif menu_selection == "2":
                print('hi')
                break
            elif menu_selection == "3":
                App_dataframe.pca()
                break
            elif menu_selection == "4":
                App_dataframe.trivia()
                break
            elif menu_selection == "Back":
                print('Sad to see you go! So long!')
                break
            else:
                print('Invalid input, try again')
                break


## this is the 'recommendations' function built on a PCA analysis condcuted by feeding input data from the app_df into a scikit-learn package framework...

    @staticmethod 
    def pca ():
        print('\n-------------------------\n Welcome to the Reccomendations page.\n----------------------------\n Tell us some of your favourite movies and we will give some tips on you might like to watch next!\n ')
        user_favs_list = str(input(f'Enter 10 of your favourite movies from Filmspots top 1000 (if you need to have a look them again, enter [search]): ').title())
        if user_favs_list == "Search":
            App_dataframe.filter_function()


    @staticmethod
    def trivia ():
        print('\n-------------------------\n Welcome to Filmspot Trivia!!!.\n----------------------------\n Test your movie knowledge and find a great flick in the process!\n ')
        start = input("Enter [start] to begin!: ")
        score = 0

        while start == "start":
            print("Can you name this movie?")
            random = (App_dataframe.app_df.sample(1))
            print(random["Synopsis"].to_string())
            answer1 = input("Whats the title of this movie? [need a hint? enter [hint]:").title()
            if answer1 == random["Name"]:
                score += 1
                print("Thats Right!!!")
                print(f"Your score is now: {score}")
            elif answer1 == "Hint":
                print(random["Year"].to_string())
            else:
                print("Sorry, wrong answer. Lets start again shall we...")
                break
        



###### Start Program (everything above this can probably go into its own module)#####
#welcome message when app opens:
print('Welcome to FilmSpot: home to the top 1000 movies\n -----------------------------------------------------')

print('*** Always remember, to go back, just enter: back ****\n')
# filter_method = str(input(f"Select how you want to filter our database [Name, Year, Genre, Cast, Director]: ").title())


      
# this triggers the main menu
App_dataframe.show_main_menu()





