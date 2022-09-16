from sklearn.decomposition import PCA
import pandas as pandas
import numpy as n 






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
    titles = df["Name"]
    capitalised_titles = (f'{titles}').title()
    df["Name"] = df["Name"].str.title()
    df.index.name = "Rank"
    df.index += 1

    pandas.set_option('display.max_rows', None)
    pandas.set_option('display.width', None)
    # pandas.set_option('display.max_colwidth', -1)

## Set the class variable ##
    app_df = df

    #this is the method for the 'filter/search' functionality
    @staticmethod
    def filter_function():
        print(f"\n Welcome to FilmSpot\'s top 1000 movies database!")
        while True:
            
            filter_method = str(input(f"\nSelect how you want to filter our database [Name, Year, Genre, Cast, Director]: ").title())
            while filter_method == "Name":
                title_search = str(input(f'Enter your movie title: ').title())
                result = App_dataframe.app_df.loc[App_dataframe.app_df['Name'] == (f'{title_search}')]
                search_result = result[["Name", "Year", "Genre", "IMBD rating", "Director"]]
                if  title_search in App_dataframe.app_df.values:
                    print(f'\nYep! its in there: \n')
                    print(search_result)
                    break
                if title_search == "Back":
                    break
                elif title_search not in App_dataframe.app_df.values:
                    print('Hmm...Looks like that one is not in our top 1000. Check your spelling and try again')
                              
            while filter_method == "Year":
                year_search = str(input(f'Enter a year: ').title())
                result = App_dataframe.app_df.loc[App_dataframe.app_df['Year'] == (f'{year_search}')]
                search_result = result[["Name", "Year", "Genre", "IMBD rating", "Director"]]
                if year_search == "Back":
                    break
                elif year_search not in App_dataframe.app_df.values:
                    print("Invalid input, give it another go")
                else:
                    print(f'---Results for {year_search}---')
                    print(search_result)
                    break

            while filter_method == "Genre":
                genre_search = (input(f'Enter one or more genres from the following [Action, Drama, Comedy, Adventure, Animation, Biography, Horror, Fantasy, History]: ').title())
                result = App_dataframe.app_df[App_dataframe.app_df.isin([f'{genre_search}']).any(axis=1)]
                search_result = result[["Name", "Year", "Genre", "IMBD rating", "Director"]]
                if genre_search == "Back":
                    break
                elif genre_search not in App_dataframe.app_df.values:
                    print('Oops...Looks like what you have entered is invalid')
                else:
                    print(f'---Results for {genre_search}--- ')
                    print(search_result)
                    break

            while filter_method == "Cast":
                cast_search = (input(f'Enter the name of an actor or actress: ').title())
                result = App_dataframe.app_df[App_dataframe.app_df.isin([f'{cast_search}']).any(axis=1)]
                search_result = result[["Name", "Year", "Genre", "IMBD rating", "Director"]]
                if cast_search == "Back":
                    break
                elif cast_search not in App_dataframe.app_df.values:
                    print(f"Hmm... either {cast_search} isnt in our 1000, or you made them up...")
                else:
                    print(f'---Results for {cast_search}--- ')
                    print(search_result)
                    break

            while filter_method == "Director":
                director_search = str(input(f'Enter the full name of a director: ').title())
                result = App_dataframe.app_df.loc[App_dataframe.app_df['Director'] == (f'{director_search}')]
                search_result = result[["Name", "Year", "Genre", "IMBD rating", "Director"]]
                if director_search == "Back":
                    break
                elif director_search not in App_dataframe.app_df.values:
                    print(f"Hmm... either {director_search} isnt in our 1000, you misspelt, or you made them up...")
                else: 
                    print(f'---Results for {director_search}--- ')
                    print(search_result)
                    break

            if filter_method == "Back":
                App_dataframe.show_main_menu()
                break
            else:
                print('\n\nWant to give it another go? Remember, you can enter [back] to return to the main menu')

# this is the main menu - a static fuction, called when the program opens and then when the user enters 'back' enough times while the program is running

    @staticmethod
    def show_main_menu():
        print("\n-------------------Welcome to the main menu--------------------\n\n\n 1.    Search the FilmSpot database       2.     Your to-watch-list \n\n 3.    Your Recommendations               4.     FilmSpot Trivia!\n\n\n")
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
        score = 0
        play_round = 0
        while True:
            start = input("Enter [start] to begin!: ")
            while start != "start":
                break
            while start == "start":
                play_round +=1
                print(f"----------------------------------\n\n Round: {play_round}. Can you name this movie?\n")
                random_movie = (App_dataframe.app_df.sample(1))
                random_bio = (random_movie["Synopsis"].to_string(index=False, header=False))
                random_name = (random_movie["Name"].to_string(index=False, header=False))
                random_year = (random_movie["Year"].to_string(index=False, header=False))
                random_director = (random_movie["Director"].to_string(index=False, header=False))
                print(random_bio)
                print((random_name).title())
                print(random_year)
                while True:
                    answer1 = input("\nWhats the title of this movie? [need a hint? enter [hint]: ").title()
                    if (answer1) == ((f'{random_name}').title()):
                        score += 5
                        print("\n----------------------------------\n\nThats Right!!!")
                        print(f"Your score is now: {score}\n")
                        break
                    if answer1 == "Hint":
                        print(f'\nHint: it was directed by {random_director} in {random_year}')
                        continue
                    else:
                        print(f'{answer1}? C\'mon I thought you knew this!')
                        while True:
                            try_again = input("Sorry, wrong answer!  Enter [yes] to start again. Enter [back] if you have had enough: ").title()
                            if try_again == "Back":
                                App_dataframe.show_main_menu()
                                break
                            if try_again == "Yes":
                                play_round = 0
                                score = 0
                                break
                        break
                break
            break
                    
        
## this trivia loop is a bit verbose because dealing with booleans with Pandas Dfs is a challenege. Extra step was done to turn Df values to dtring variables so booleans can be run
## Traditional trivia games make you start again for a wrong answer, since many of these movies are obscure/old I figued i'd make the game more educational by letting the user continue even if wrong

###### Start Program (everything above this can probably go into its own module)#####
#welcome message when app opens:
print('Welcome to FilmSpot: home to the top 1000 movies\n -----------------------------------------------------')

print('*** Always remember, to go back, just enter: back ****\n')
# filter_method = str(input(f"Select how you want to filter our database [Name, Year, Genre, Cast, Director]: ").title())


      
# this triggers the main menu
App_dataframe.show_main_menu()





