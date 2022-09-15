from database import app_df
import pandas as pandas
import numpy as n 



#welcome message when app opens:
print('Welcome to FilmSpot: home to the top 1000 movies')

print('*** Always remember, to go back, just enter: back ****')
# filter_method = str(input(f"Select how you want to filter our database [Name, Year, Genre, Cast, Director]: ").title())


class App_dataframe:


    def __init__(self, app_df):
        self.app_df = app_df


    #this is the method for the filter functionality
    @staticmethod
    def filter_function():


        while True:
            filter_method = str(input(f"Select how you want to filter our database [Name, Year, Genre, Cast, Director]: ").title())
            while filter_method == "Name":
                title_search = str(input(f'Enter your movie title: ').title())
                result = app_df.loc[app_df['Name'] == (f'{title_search}')]
                if title_search == "Back":
                    break
                elif title_search not in app_df.values:
                    print('Hmm...Looks like that one is not in our top 1000. Check your spelling and try again')
                else:
                    print(f'Yep! its in there: ')
                    print(result)
                    break

            while filter_method == "Year":
                year_search = str(input(f'Enter a year: ').title())
                result = app_df.loc[app_df['Year'] == (f'{year_search}')]
                if year_search == "Back":
                    break
                elif year_search not in app_df.values:
                    print("Invalid input, give it another go")
                else:
                    print(f'---Results for {year_search}---')
                    print(result)
                    break

            while filter_method == "Genre":
                genre_search = (input(f'Enter one or more genres from the following [Action, Drama, Comedy, Adventure, Animation, Biography, Horror, Fantasy, History]: ').title())
                result = app_df[app_df.isin([f'{genre_search}']).any(axis=1)]
                if genre_search == "Back":
                    break
                elif genre_search not in app_df.values:
                    print('Oops...Looks like what you have entered is invalid')
                else:
                    print(f'---Results for {genre_search}--- ')
                    print(result)
                    break

            while filter_method == "Cast":
                cast_search = (input(f'Enter the name of an actor or actress: ').title())
                result = app_df[app_df.isin([f'{cast_search}']).any(axis=1)]
                if cast_search == "Back":
                    break
                elif cast_search not in app_df.values:
                    print(f"Hmm... either {cast_search} isnt in our 1000, or you made them up...")
                else:
                    print(f'---Results for {cast_search}--- ')
                    print(result)
                    break

            while filter_method == "Director":
                director_search = str(input(f'Enter the full name of a director: ').title())
                result = app_df.loc[app_df['Director'] == (f'{director_search}')]
                if director_search == "Back":
                    break
                elif director_search not in app_df.values:
                    print(f"Hmm... either {director_search} isnt in our 1000, you misspelt, or you made them up...")
                else: 
                    print(f'---Results for {director_search}--- ')
                    print(result)
                    break

            if filter_method == "Back":
                break
            else:
                print('Want to give it another go?')

App_dataframe.filter_function()

print("Welcome back to the main menu")

