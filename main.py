import pandas as pandas
import numpy as n 
import pickle 
from AppDf import *


if __name__ == '__main__':
    #welcome message when app opens:
    try:
        print('\n\nWelcome to FilmSpot: home to the top 1000 movies ever made!\n ---------------------------------------------------------------------------------------------')

        print('\n*** Always remember, to go back, just enter: back ****\n')



        # this triggers the main menu upon start up
        App_dataframe.show_main_menu()
    except (KeyboardInterrupt):
        print("\n\nSad to see you go. Until next time!")


