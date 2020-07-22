import sqlite3
import pandas as pd
import warnings  # current version of seaborn generates a bunch of warnings that we'll ignore
import numpy as np
import matplotlib.pyplot as plt
from pandas import RangeIndex

warnings.filterwarnings("ignore")
# sns.set(style="white", color_codes=True)

# Master df extracted
con = sqlite3.connect('C:/Users/user/PycharmProjects/DS/database.sqlite')
# df_countries = pd.read_sql_query("SELECT * FROM Country", con)
df_leagues = pd.read_sql_query("SELECT * FROM League", con)
df_matches = pd.read_sql_query("SELECT * FROM Match", con)
# df_players = pd.read_sql_query("SELECT * FROM Player", con)
# df_players_attributes = pd.read_sql_query("SELECT * FROM Player_Attributes", con)
df_teams = pd.read_sql_query("SELECT * FROM Team", con)
# df_teams_attributes = pd.read_sql_query("SELECT * FROM Team_Attributes", con)

# Spanish La Liga:
# Spanish La Liga teams:
df_teams_copy = df_teams.copy()
df_teams_La_Liga = df_teams_copy[251:284]
df_teams_La_Liga = df_teams_La_Liga.drop(columns=['id', 'team_fifa_api_id'])
df_teams_La_Liga.rename(columns={'team_long_name': 'team_name'}, inplace=True)
df_teams_La_Liga['original_index'] = range(251, 284) # original indexes
df_teams_La_Liga['indexes'] = list(range(1, 34)) # indexes from 1 to 33
df_teams_La_Liga = df_teams_La_Liga.set_index(['indexes']) # indexes from 1 to 33
# print(df_teams_La_Liga)

# Spanish La Liga Matches:
df_matches_copy = df_matches.copy()
df_matches_La_Liga = df_matches_copy[21517:24557]
print(df_matches_La_Liga)
for col in df_matches_copy.columns.tolist():
    print(col)
# print(df_leagues)
# print(df_matches[df_matches['home_team_api_id'] == 10267].index.values)

# print(df_leagues.head(10))
# print(df_matches.head())