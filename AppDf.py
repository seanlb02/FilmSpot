
import pandas as pandas
import numpy as n 
import pickle 




class App_dataframe:
    

    # the primary database class is initialised by making the pandas dataframe an attriubte 
    # this makes the dataframe easily accessbile by sub-classes and methods 

    def __init__(self, app_df):
        self.app_df = app_df

    #here we create the dataframe by (1) reading in a pandas Dataframe (2) cleaning the data (3) setting the key class variable "app_df"

    df = pandas.read_csv('/home/lucian2/Sean_Gyuris_T1_A3/Assets/imdb_top_1000.csv')
    df = df.drop(df.columns[[0, 4, 8, 14, 15]], axis=1)
    df.rename(columns = {'Series_Title':'Name', 'Released_Year':'Year', 'Overview':'Synopsis', 'IMDB_Rating':'IMBD rating'}, inplace = True)
    df[["Genre", "Genre 2", "Genre 3"]] = df["Genre"].str.split(",", expand=True)
    df["Genre 2"] = df["Genre 2"].str.strip()
    titles = df["Name"]
    capitalised_titles = (f'{titles}').title()
    df["Name"] = df["Name"].str.title()
    df.index.name = "Rank"
    df.index += 1
    #This formats the data so it displays fully in the terminal without breaks
    pandas.set_option('display.max_rows', None)
    pandas.set_option('display.width', None)
    pandas.set_option('display.max_colwidth', None)

    #Primary class variable
    app_df = df
    #I use this 'dummy_entry to initialise new accounts - its an [almost] empty dataframe
    dummy_entry = app_df.iloc[[14]]
    dummy_entry = dummy_entry[["Name", "Year", "Director", "Genre", "Genre 2", "Certificate"]]

    """Below is the method for the 'filter/search' functionality

    params/args: null 
    """

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
                    print(f'\n---Results for {year_search}---')
                    print(search_result)
                    break

            while filter_method == "Genre":
                genre_search = (input(f'Enter one or more genres from the following [Action, Drama, Comedy, Adventure, Animation, Biography, Horror, Fantasy, History]: ').title())
                result = App_dataframe.app_df[App_dataframe.app_df.isin([f'{genre_search}']).any(axis=1)]
                search_result = result[["Name", "Year", "IMBD rating", "Director"]]
                if genre_search == "Back":
                    break
                elif genre_search not in App_dataframe.app_df.values:
                    print('Oops...Looks like what you have entered is invalid')
                else:
                    print(f'\n---Results for {genre_search}--- \n')
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
                    print(f'\n---Results for {cast_search}--- \n')
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
        print("\n-------------------Welcome to the main menu--------------------\n\n\n 1.    Search the FilmSpot database       2.     Your favourites \n\n 3.    Your Recommendations               4.     FilmSpot Trivia!\n\n\n")
       
        while True:
            menu_selection = str(input(f'Select where you would like to go[Enter 1,2,3 or 4]: ').title())
            if menu_selection == "1":
                App_dataframe.filter_function()
                break
            elif menu_selection == "2":
                User.display_watchlist()
                break
            elif menu_selection == "3":
                User.recommender()
                break
            elif menu_selection == "4":
                App_dataframe.trivia()
                break
            elif menu_selection == "Back":
                print('Sad to see you go! So long!')
                break
            else:
                print('Invalid input, try again')
                continue


    @staticmethod
    def trivia ():
        print('\n-------------------------\n Welcome to Filmspot Trivia!!!.\n----------------------------\n Test your movie knowledge and find a great flick in the process!\n ')
        score = 0
        play_round = 0
        while True:
            start = str(input("Enter [start] to begin!: ").title())
            if start != "Start":
                continue
            while start == "Start":
                play_round +=1
                print(f"----------------------------------\n\n Round: {play_round}. Can you name this movie?\n")
                random_movie = (App_dataframe.app_df.sample(1))
                random_bio = (random_movie["Synopsis"].to_string(index=False, header=False))
                random_name = (random_movie["Name"].to_string(index=False, header=False))
                random_year = (random_movie["Year"].to_string(index=False, header=False))
                random_director = (random_movie["Director"].to_string(index=False, header=False))
                print(random_bio)
                
                while True:
                    answer1 = input("\nWhats the title of this movie? [need a hint? enter [hint]: ").title()
                    if (answer1) == ((f'{random_name}').title()):
                        score += 5
                        print("\n----------------------------------\n\nThats Right!!!")
                        print(f"Your score is now: {score}\n")
                        break
                    elif answer1 == "Hint":
                        print(f'\nHint: it was directed by {random_director} in {random_year}')
                        continue
                    else  :
                        print(f'{answer1}? C\'mon I thought you knew this!')
                        while True:
                            try_again = input("Sorry, wrong answer!  Enter [yes] to start again. Enter [back] if you have had enough: ").title()
                            if try_again == "Back":
                                App_dataframe.show_main_menu()
                                return
                            if try_again == "Yes":
                                play_round = 0
                                score = 0
                                break
                        break
                
                
            break
        
class User:


    def __init__(self, username, watchlist):
        self.username = username
        self.watchlist = watchlist 


    ## this is the 'recommendations' function that returns a list of 10 films the user might like, this list can then be added to the users 'to-watch-list'.
    @staticmethod 
    def recommender():
        while True:
            title_search = str(input(f'Enter a movie title and we\'ll recommend some more from our list: ').title())
            result = App_dataframe.app_df.loc[App_dataframe.app_df['Name'] == (f'{title_search}')]
            genre1_result = (result["Genre"].to_string(index=False, header=False))
            genre2_result = (result["Genre 2"].to_string(index=False, header=False))
            genre2_result = genre2_result.strip()
            cert_result = (result["Certificate"]).to_string(index=False, header=False)
            cast_result = (result["Star1"].to_string(index=False, header=False))
            director_result = (result["Director"].to_string(index=False, header=False))
            subsetDataFrame = App_dataframe.app_df.loc[(App_dataframe.app_df['Genre'] == genre2_result) & (App_dataframe.app_df['Certificate'] == cert_result) | (App_dataframe.app_df['Genre 2'] == genre2_result) & (App_dataframe.app_df['Certificate'] == cert_result)]
            reccomended_list = subsetDataFrame[["Name", "Year", "Director", "Genre", "Genre 2", "Certificate"]].head(10)
          
            if  title_search in App_dataframe.app_df.values:
                print(f'\nResults for {title_search}: \n')
                print(reccomended_list)
                # user is then prompted to answer whether they want to add these movies to their 'to-watch-list'
                while True:
                    add_query = input(f'\nDo you want to add this list to your to-watch-list? Enter [Yes/No]\n').title()
                    if add_query == "No":
                        break
                    elif add_query == "Yes": 
                        try:
                            account_query = input(f'\nDo you have an account? If so enter your [username], If not, enter [no]: ')
                            verify_name = account_query 
                            #this loads in the serialised watchlist of the user to the program:
                            pickle_in = open(verify_name, "rb")
                            user_list = pickle.load(pickle_in)
                            # print(user_list.watchlist)
                            #this appends the 'reccomended' list of films to a user's watchlist
                            # appended_df = user_list.watchlist.append(reccomended_list, ignore_index=True)
                            appended_df = pandas.concat([user_list.watchlist,reccomended_list], axis=0)

                            user_watchlist = User(verify_name, appended_df)
                            # this overwrites the user's watchlist stored/serialised in a pickle:
                            pickle_out = open(verify_name, "wb")
                            pickle.dump(user_watchlist, pickle_out)
                            pickle_out.close() 
                            print('Movies added to your watchlist!')
                            break
                        except FileNotFoundError:
                                #this will create an account if there is not one saved in the program, or if user enters 'no' to the above input:
                            User.create_user()
                            print('Account created!')
                            continue
            if title_search == "Back":
                App_dataframe.show_main_menu()
                break
            elif title_search not in App_dataframe.app_df.values:
                print('Hmm...Looks like that one is not in our top 1000. Check your spelling and try again')

    # in this instance, the attribute self.watchlist will store a dafaframe the pandas dataframe that is returned in the 'reccomender' function.
    @staticmethod
    def create_user():           
        name = input(f'\nHmm, doesn\'t look like you do. Lets make one now... Enter a username to create your account: ')
        new_user = User(name, App_dataframe.dummy_entry)
        pickle_out = open(name, "wb")
        pickle.dump(new_user, pickle_out)
        pickle_out.close()
    
    @staticmethod
    def save_new_watchlist():           
        pass

    @staticmethod
    def display_watchlist():
        while True:
            try:
                get_name = input(f'Enter your username to retrieve your watchlist: ')
                pickle_in = open(get_name, "rb")
                user_list = pickle.load(pickle_in)
                print(user_list.watchlist)
                while True:
                    back_button = input('To return to the main menu just enter [back]').title()
                    if back_button == "Back":
                        App_dataframe.show_main_menu()
                        return
            except (FileNotFoundError, TypeError):
                tryagain = input("User does not exist. Enter [try again], or [back] to return to the main menu:  ").title()
                if tryagain == "Back":
                    App_dataframe.show_main_menu()
                    return