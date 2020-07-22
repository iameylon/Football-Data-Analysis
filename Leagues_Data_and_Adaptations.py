import pandas as pd
import sqlite3

from pandas import to_numeric

### Function Helpers:
def df_creator(path, file):
    file = pd.read_csv(path + file)
    return file


la_liga_path = "C:/Users/User/PycharmProjects/Football-Data-Analysis/Spanish La Liga Dataset/"
files_list = ['season-0910_csv.csv',
              'season-1011_csv.csv',
              'season-1112_csv.csv',
              'season-1213_csv.csv',
              'season-1314_csv.csv',
              'season-1415_csv.csv',
              'season-1516_csv.csv',
              'season-1617_csv.csv',
              'season-1718_csv.csv',
              'season-1819_csv.csv']
laLiga0919Concatenated = pd.concat([df_creator(la_liga_path, file) for file in files_list])


## Modifying the DF:
# Leave relevant columns:
laLiga0919Filtered = laLiga0919Concatenated[['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR', 'HTHG', 'HTAG', 'HTR']].copy()
# la_liga_0919_df['Year'] = pd.DatetimeIndex(la_liga_0919_df['Date']).year  # year column.

# Filter out games that draw at HT:
laLiga0919Filtered2 = laLiga0919Filtered[((laLiga0919Filtered.HTR == 'H')
                                          | (laLiga0919Filtered.HTR == 'A'))].copy()  # Filter out games that draw at HT
laLiga0919Filtered2.reset_index(drop=True, inplace=True)
# print(laLiga0919Filtered2.head(50))


# Filter out games that draw at HT and leader leads by exactly 1:
laLiga0919Filtered3 = laLiga0919Filtered[((laLiga0919Filtered.HTR == 'H') | (laLiga0919Filtered.HTR == 'A'))].copy()
                                                                                                        # Filter out games that draw at HT
laLiga0919Filtered3 = laLiga0919Filtered3[abs(to_numeric(laLiga0919Filtered3.HTHG) - to_numeric(laLiga0919Filtered3.HTAG))
                                              == 1].copy()  # Leader leads by exactly 1
laLiga0919Filtered3.reset_index(drop=True, inplace=True)
# print(laLiga0919Filtered3.head(50))

# Filter out games that draw at HT and leader leads by more than 1:
laLiga0919Filtered4 = laLiga0919Filtered[((laLiga0919Filtered.HTR == 'H') | (laLiga0919Filtered.HTR == 'A'))].copy()
                                                                                                        # Filter out games that draw at HT
laLiga0919Filtered4 = laLiga0919Filtered4[abs(to_numeric(laLiga0919Filtered4.HTHG) - to_numeric(laLiga0919Filtered4.HTAG))
                                              > 1].copy()  # Leader leads by exactly 1
laLiga0919Filtered4.reset_index(drop=True, inplace=True)
# print(laLiga0919Filtered4.head(50))




### Master Premier League df extracted:
con = sqlite3.connect("C:/Users/User/PycharmProjects/"
                      "DS/English Premier League Dataset/SQLite data/EPL_Seasons_1993-2017_RAW_Table.sqlite")
dfRawTable = pd.read_sql_query("SELECT * FROM EPL", con)

## Modifying the DF:
# Leave relevant columns:
premierLeague9518Filtered = dfRawTable[924:][['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR', 'HTHG', 'HTAG', 'HTR']].copy()
# premierLeague9518Filtered['Year'] = pd.DatetimeIndex(la_liga_0919_df['Date']).year  # year column.

# Filter out games that draw at HT:
premierLeague9518Filtered2 = premierLeague9518Filtered[((premierLeague9518Filtered.HTR == 'H') |
                                                        (premierLeague9518Filtered.HTR == 'A'))].copy()  # Filter out games that draw at HT
premierLeague9518Filtered2.reset_index(drop=True, inplace=True)
# print(premierLeague9518Filtered2.head(50))

# Filter out games that draw at HT and leader leads by exactly 1:
premierLeague9518Filtered3 = premierLeague9518Filtered[((premierLeague9518Filtered.HTR == 'H') |
                                                        (premierLeague9518Filtered.HTR == 'A'))].copy()  # Filter out games that draw at HT
premierLeague9518Filtered3 = premierLeague9518Filtered3[abs(to_numeric(premierLeague9518Filtered3.HTHG) -
                                                            to_numeric(premierLeague9518Filtered3.HTAG))
                                                            == 1].copy()  # Leader leads by exactly 1
premierLeague9518Filtered3.reset_index(drop=True, inplace=True)
# print(premierLeague9518Filtered3.head(50))


# Filter out games that draw at HT and leader leads by more than 1:
premierLeague9518Filtered4 = premierLeague9518Filtered[((premierLeague9518Filtered.HTR == 'H') |
                                                        (premierLeague9518Filtered.HTR == 'A'))].copy()  # Filter out games that draw at HT
premierLeague9518Filtered4 = premierLeague9518Filtered4[abs(to_numeric(premierLeague9518Filtered4.HTHG) -
                                                            to_numeric(premierLeague9518Filtered4.HTAG))
                                                            > 1].copy()  # Leader leads by exactly 1
premierLeague9518Filtered4.reset_index(drop=True, inplace=True)
# print(premierLeague9518Filtered4.head(50))
