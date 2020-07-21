import pandas as pd
# import numpy as np

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

# Reading the data files and concatenate the DFs:
laLiga0910 = pd.read_csv('C:/Users/User/PycharmProjects/DS/Spanish La Liga Dataset/season-0910_csv.csv')
laLiga1011 = pd.read_csv('C:/Users/User/PycharmProjects/DS/Spanish La Liga Dataset/season-1011_csv.csv')
laLiga1112 = pd.read_csv('C:/Users/User/PycharmProjects/DS/Spanish La Liga Dataset/season-1112_csv.csv')
laLiga1213 = pd.read_csv('C:/Users/User/PycharmProjects/DS/Spanish La Liga Dataset/season-1213_csv.csv')
laLiga1314 = pd.read_csv('C:/Users/User/PycharmProjects/DS/Spanish La Liga Dataset/season-1314_csv.csv')
laLiga1415 = pd.read_csv('C:/Users/User/PycharmProjects/DS/Spanish La Liga Dataset/season-1415_csv.csv')
laLiga1516 = pd.read_csv('C:/Users/User/PycharmProjects/DS/Spanish La Liga Dataset/season-1516_csv.csv')
laLiga1617 = pd.read_csv('C:/Users/User/PycharmProjects/DS/Spanish La Liga Dataset/season-1617_csv.csv')
laLiga1718 = pd.read_csv('C:/Users/User/PycharmProjects/DS/Spanish La Liga Dataset/season-1718_csv.csv')
laLiga1819 = pd.read_csv('C:/Users/User/PycharmProjects/DS/Spanish La Liga Dataset/season-1819_csv.csv')
frames = [laLiga0910, laLiga1011, laLiga1112, laLiga1213, laLiga1314, laLiga1415, laLiga1516, laLiga1617, laLiga1718, laLiga1819]
laLiga0919Concatenated = pd.concat(frames)  # Chaining vertically the different DFs.

## Modifying the DF:
# Leave relevant columns:
laLiga0919Filtered = laLiga0919Concatenated[['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR', 'HTHG', 'HTAG', 'HTR']].copy()
# la_liga_0919_df['Year'] = pd.DatetimeIndex(la_liga_0919_df['Date']).year  # year column.
laLiga0919Filtered2 = laLiga0919Filtered[((laLiga0919Filtered.HTR == 'H')
                                          | (laLiga0919Filtered.HTR == 'A'))].copy()  # Filter out games that draw at HT
laLiga0919Filtered2.reset_index(drop=True, inplace=True)
# print(laLiga0919Filtered2.head())
