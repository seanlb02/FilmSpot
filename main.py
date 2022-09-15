from database import app_df
import pandas as pandas
import numpy as n 



#welcome message when app opens:
print('Welcome to FilmSpot: home to the top 1000 movies')



class App_dataframe:


    def __init__(self, app_df):
        self.app_df = app_df


    #this is the method for the filter functionality
    @staticmethod
    def filter_function(filter_method):


        # try:
        if filter_method == "Name":
            title_search = str(input(f'Enter your movie title: ').title())
            result = app_df.loc[app_df['Name'] == (f'{title_search}')]
            print(f'Yep! its in there: ')
            print(result)
        elif filter_method == "Year":
            year_search = str(input(f'Enter a year: '))
            result = app_df.loc[app_df['Year'] == (f'{year_search}')]
            print(f'---Results for {year_search}---')
            print(result)
        elif filter_method == "Genre":
            genre_search = (input(f'Enter one or more genres from the following [Action, Drama, Comedy, Adventure, Animation, Biography, Horror, Fantasy, History]: ').title())
            # result = app_df.loc[app_df['Genre'] == (f'{genre_search}'.capitalize())]
            result = app_df[app_df.isin([f'{genre_search}']).any(axis=1)]
            if app_df.empty == False:
                print(f'Results for {genre_search}: ')
                print(result)
            else:
                
        elif filter_method == "Cast":
            cast_search = (input(f'Enter the name of an actor/acress: ').title())
            result = app_df[app_df.isin([f'{cast_search}']).any(axis=1)]
            print(f'Results for {cast_search}: ')
            print(result)
        if filter_method == "Director":
                director_search = str(input(f'Enter the full name of a director: ').title())
                result = app_df.loc[app_df['Director'] == (f'{director_search}')]
                print(f'Results for {director_search}: ')
                print(result)
            # if director_search not in app_df.values:
        if app_df.empty == True:
            print(f"Can't find that one, lets try again")
            input((f'Enter the full name of a director: ').title())

        # except [TypeError, IndexError]:
        #     return "Invalid input"

filter_method = str(input(f"Select how you want to filter our database [Name, Year, Genre, Cast, Director]: ").title())

# App_dataframe.filter_function(filter_method)

