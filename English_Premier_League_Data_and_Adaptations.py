import sqlite3
import pandas as pd
import warnings  # current version of seaborn generates a bunch of warnings that we'll ignore

warnings.filterwarnings("ignore")

# notes on files: http://www.football-data.co.uk/notes.txt:
# Div = League Division
# Date = Match Date (dd/mm/yy)
# Time = Time of match kick off
# HomeTeam = Home Team
# AwayTeam = Away Team
# FTHG and HG = Full Time Home Team Goals
# FTAG and AG = Full Time Away Team Goals
# FTR and Res = Full Time Result (H=Home Win, D=Draw, A=Away Win)
# HTHG = Half Time Home Team Goals
# HTAG = Half Time Away Team Goals
# HTR = Half Time Result (H=Home Win, D=Draw, A=Away Win)
#
# Match Statistics (where available)
# Attendance = Crowd Attendance
# Referee = Match Referee
# HS = Home Team Shots
# AS = Away Team Shots
# HST = Home Team Shots on Target
# AST = Away Team Shots on Target
# HHW = Home Team Hit Woodwork
# AHW = Away Team Hit Woodwork
# HC = Home Team Corners
# AC = Away Team Corners
# HF = Home Team Fouls Committed
# AF = Away Team Fouls Committed
# HFKC = Home Team Free Kicks Conceded
# AFKC = Away Team Free Kicks Conceded
# HO = Home Team Offsides
# AO = Away Team Offsides
# HY = Home Team Yellow Cards
# AY = Away Team Yellow Cards
# HR = Home Team Red Cards
# AR = Away Team Red Cards
# HBP = Home Team Bookings Points (10 = yellow, 25 = red)
# ABP = Away Team Bookings Points (10 = yellow, 25 = red)

# Master df extracted
con = sqlite3.connect("C:/Users/User/PycharmProjects/"
                      "DS/English Premier League Dataset/SQLite data/EPL_Seasons_1993-2017_RAW_Table.sqlite")
# con2 = sqlite3.connect("C:/Users/User/PycharmProjects/"
#                        "DS/English Premier League Dataset/SQLite data/EPL_Seasons_1993-2017_RAW_Tables.sqlite") # Useless
dfRawTable = pd.read_sql_query("SELECT * FROM EPL", con)
# dfRawTables = pd.read_sql_query("SELECT * FROM EPL1993", con2) # (Useless)
# print(dfRawTable.head())
# print(dfRawTable.columns)

## Modifying the DF:
# Leave relevant columns:
premierLeague9518Filtered = dfRawTable[924:][['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR', 'HTHG', 'HTAG', 'HTR']].copy()
# la_liga_0919_df['Year'] = pd.DatetimeIndex(la_liga_0919_df['Date']).year  # year column.
# Filter out games that draw at HT:
premierLeague9518Filtered2 = premierLeague9518Filtered[((premierLeague9518Filtered.HTR == 'H') |
                                                        (premierLeague9518Filtered.HTR == 'A'))].copy()
premierLeague9518Filtered2.reset_index(drop=True, inplace=True)
# print(premierLeague9518Filtered2.head())
