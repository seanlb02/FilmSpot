import pickle 
import gc


# Users is a class to store (1) a users account and (2) their dynamic 'watchlist'

class Users:


    def __init__(self, username, watchlist):
        self.username = username
        self.watchlist = watchlist 

# in this instance, the attribute self.watchlist will store a dafaframe the pandas dataframe that is returned in the 'reccomender' function.

def create_user():           
    name = input(f'Enter a username to create or login to your account: ')
    new_user = Users(name, App_dataframe.app_df.head(10))
    pickle_out = open(name, "wb")
    pickle.dump(new_user, pickle_out)
    pickle_out.close()

    @staticmethod
    def display_watchlist():
        get_name = input(f'Enter your username to retrieve your watchlist: ')
        pickle_in = open(get_name, "rb")
        user_list = pickle.load(pickle_in)
        print(user_list.watchlist)


    create_user()
    # display_watchlist()






