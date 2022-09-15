
import numpy as n
import pandas as pandas

# this will set up out database but (1) cleaning original data and (2) setting up a pandas Dataframe

df = pandas.read_csv('/home/lucian2/data for terminal app/imdb_top_1000.csv')
df = df.drop(df.columns[[0, 3, 4, 8, 14, 15]], axis=1)
df.rename(columns = {'Series_Title':'Name', 'Released_Year':'Year', 'Overview':'Synopsis', 'IMDB_Rating':'IMBD rating'}, inplace = True)
df[["Genre", "Genre 2", "Genre 3"]] = df["Genre"].str.split(",", expand=True)
df.index.name = "Rank"
df.index += 1


app_df = df

print(app_df.head(10))