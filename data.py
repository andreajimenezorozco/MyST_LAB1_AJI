
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: Lab. 1                                                         -- #
# -- script: main.py : python script with the main functionality                                         -- #
# -- author: Andrea Jiménez IF706970 Github: andreajimenezorozco                                                                       -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository: https://github.com/andreajimenezorozco/Lab-1_MyST_Spring2021                                                                  -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

import pandas as pd
import pandas_datareader.data as web
import os
import glob


# ADJ.CLOSED PRICES YAHOO
def get_closes(tickers, start_date=None, end_date=None, freq=None):
    closes = pd.DataFrame(columns=tickers, index=web.YahooDailyReader(tickers[0], start=start_date, end=end_date
                                                                      , interval=freq).read().index)
    for ticker in tickers:
        df = web.YahooDailyReader(symbols=ticker, start=start_date, end=end_date, interval=freq).read()
        closes[ticker] = df['Adj Close']
    closes.index_name = 'Date'
    closes = closes.sort_index()
    return closes


# READ MULTIPLE CSV FILES
def multiple_csv(path):
    all_files = glob.glob(os.path.join(path, "*.csv"))
    df_from_each_file = (pd.read_csv(f, usecols=[0, 1, 3, 4, 16]) for f in all_files)
    concatenated_df = pd.concat(df_from_each_file, ignore_index=True)
    return concatenated_df
