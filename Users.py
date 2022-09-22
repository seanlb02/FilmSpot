# import pickle 
# import gc
# from AppDf import App_dataframe
# import pandas as pandas 


# class User:


#     def __init__(self, username, watchlist):
#         self.username = username
#         self.watchlist = watchlist 


# ## this is the 'recommendations' function that returns a list of 10 films the user might like, this list can then be added to the users 'to-watch-list'.
#     @staticmethod 
#     def recommender():
#         while True:
#             title_search = str(input(f'Enter a movie title and we\'ll recommend some more from our list: ').title())
#             result = App_dataframe.app_df.loc[App_dataframe.app_df['Name'] == (f'{title_search}')]
#             genre1_result = (result["Genre"].to_string(index=False, header=False))
#             genre2_result = (result["Genre 2"].to_string(index=False, header=False))
#             genre2_result = genre2_result.strip()
#             cert_result = (result["Certificate"]).to_string(index=False, header=False)
#             cast_result = (result["Star1"].to_string(index=False, header=False))
#             director_result = (result["Director"].to_string(index=False, header=False))
#             # subsetDataFrame = App_dataframe.app_df.loc[App_dataframe.app_df.isin([genre1_result, genre2_result]).any(axis=1)]
#             subsetDataFrame = App_dataframe.app_df.loc[(App_dataframe.app_df['Genre'] == genre2_result) & (App_dataframe.app_df['Certificate'] == cert_result) | (App_dataframe.app_df['Genre 2'] == genre2_result) & (App_dataframe.app_df['Certificate'] == cert_result)]
#             # subsetDataFrame = App_dataframe.app_df.loc[App_dataframe.app_df['Genre'].isin([genre1_result, genre2_result])]
#             reccomended_list = subsetDataFrame[["Name", "Year", "Director", "Genre", "Genre 2", "Certificate"]].head(10)
          
#             if  title_search in App_dataframe.app_df.values:
#                 print(f'\nResults for {title_search}: \n')
#                 print(reccomended_list)
#                 # user is then prompted to answer whether they want to add these movies to their 'to-watch-list'
#                 while True:
#                     add_query = input(f'\nDo you want to add this list to your to-watch-list? Enter [Yes/No]\n').title()
#                     if add_query == "No":
#                         break
#                     elif add_query == "Yes": 
#                         try:
#                             account_query = input(f'\nDo you have an account? If so enter your [username], If not, enter [no]: ')
#                             verify_name = account_query 
#                             #this loads in the serialised watchlist of the user to the program:
#                             pickle_in = open(verify_name, "rb")
#                             user_list = pickle.load(pickle_in)
#                             # print(user_list.watchlist)
#                             #this appends the 'reccomended' list of films to a user's watchlist
#                             # appended_df = user_list.watchlist.append(reccomended_list, ignore_index=True)
#                             appended_df = pandas.concat([user_list.watchlist,reccomended_list], axis=0)

#                             user_watchlist = Users(verify_name, appended_df)
#                             # this overwrites the user's watchlist stored/serialised in a pickle:
#                             pickle_out = open(verify_name, "wb")
#                             pickle.dump(user_watchlist, pickle_out)
#                             pickle_out.close() 
#                             print('Movies added to your watchlist!')
#                             break
#                         except FileNotFoundError:
#                                 #this will create an account if there is not one saved in the program, or if user enters 'no' to the above input:
#                             Users.create_user()
#                             print('Account created!')
#                             continue
#             if title_search == "Back":
#                 App_dataframe.show_main_menu()
#                 break
#             elif title_search not in App_dataframe.app_df.values:
#                 print('Hmm...Looks like that one is not in our top 1000. Check your spelling and try again')

# # in this instance, the attribute self.watchlist will store a dafaframe the pandas dataframe that is returned in the 'reccomender' function.
    
#     @staticmethod
#     def create_user():           
#         name = input(f'\nHmm, doesn\'t look like you do. Lets make one now... Enter a username to create your account: ')
#         new_user = Users(name, App_dataframe.dummy_entry)
#         pickle_out = open(name, "wb")
#         pickle.dump(new_user, pickle_out)
#         pickle_out.close()
    
#     @staticmethod
#     def save_new_watchlist():           
#         pass

#     @staticmethod
#     def display_watchlist():
#         get_name = input(f'Enter your username to retrieve your watchlist: ')
#         pickle_in = open(get_name, "rb")
#         user_list = pickle.load(pickle_in)
#         print(user_list.watchlist)
#         while True:
#             back_button = input('To return to the main menu just enter [back]').title()
#             if back_button == "Back":
#                 App_dataframe.show_main_menu()
#                 break
            











