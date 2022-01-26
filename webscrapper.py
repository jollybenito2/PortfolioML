## Recolectar Datos Reales
import os
import pandas_datareader as pdr
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import date, datetime, timedelta
import investpy


#Var1=pd.read_csv('Name_Stocks.csv', dtype = str)
stocks2=['AAPL', 'BAC', 'AMZN', 'T', 'GOOG', 'MO', 'DAL',
        'AA', 'AXP', 'DD', 'BABA', 'ABT', 'UA', 'AMAT','AMGN',
            'AAL','AIG','ALL','ADBE','GOOGL', 'ACN','ABBV','MT',
            'LLY','APA','ADP','AKAM','NLY','ATVI',
            'ADSK','ADM','GPS','WBA','ARNA','LUV','ACAD','PANW',
            'AEP','ALXN','AVGO','EA','DB','PBR','RIOT','GE',
            'AEM','APD','AMBA','NVS','GSAT','ANF',
            'UBS','SAVE','F','AMX','ERC',
            'AOS','AAP','AES','AFL','A','APD','ALK','ALB','ARE',
             'LNT','GOOG','AMT','AWK','AMP','ABC',
             'AME','APH','ADI','ANSS','ANTM','APTV','AJG','SPGI',
             'AZO','AVB','AVY','BKR','BLL','BAC','BK','BAX',
             'BDX','BBY','BLK','BA','BWA','CPB' ]


for ticker in stocks2:
    df = investpy.get_stock_historical_data(ticker, country='united states',
                                  from_date='01/01/2018', to_date='31/12/2021')
    df.to_csv('HetPortV3/Stocks/{}.csv'.format(ticker.rstrip("\n")))










import bs4 as bs
import datetime as dt
import os
import pandas_datareader as pdr
import pickle
import requests
import yfinance as yf
from pathlib import Path
import pandas as pd

output_dir = Path('C:/Users/benit/Downloads/stock_dfs_2020')
os.chdir(r'C:/Users/benit/Downloads')


def get_data_from_yahoo(reload_sp500=False):
    tickers = stocks2

    start = dt.datetime(2020, 1, 1)
    end = dt.datetime(2020, 12, 31)
    for ticker in tickers:
        # just in case your connection breaks, we'd like to save our progress!
        if not os.path.exists('stock_dfs_2020/{}.csv'.format(ticker.rstrip("\n"))):
            #df = pdr.DataReader(ticker.rstrip("\n"), start, 
            #           end, data_source='yahoo')['Adj Close']
            df = yf.download(ticker.rstrip("\n"), start, end, "1m")      
            df.reset_index(inplace=True)
            df.set_index("Date", inplace=True)
            
            output_file = '/{}.csv'.format(ticker.rstrip("\n"))
            output_dir.mkdir(parents=True, exist_ok=True)
            df.to_csv(output_dir / output_file)  # can join path elements with / operator
            # df = df.drop("Symbol", axis=1)
            df.to_csv('stock_dfs_2020/{}.csv'.format(ticker.rstrip("\n")))
        else:
            print('Already have {}'.format(ticker.rstrip("\n")))

get_data_from_yahoo()
