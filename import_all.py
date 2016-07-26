from pymongo import MongoClient
import datalib
import json
import datetime

# Import all data from tushare until today.
# This is used to initialize/re-initialize all the data base tables

# Connect to mongodb
client = MongoClient('localhost', 27017)
db = client['tushare']


# Truncate all table
db.stock_basics.drop()
db.history_data.drop()


# STEP1: Get all stock_basics.
stock_basics = datalib.get_stock_basics()
db.stock_basics.insert(json.loads(stock_basics.to_json(orient='records')))

# STEP2: For each stock in stock_basics, get its history data with autype, 2 years' data per run
current_date = datetime.datetime.now().date()
curr_year = current_date.year
curr_quarter = (current_date.month - 1) // 3 + 1
stocks = ['600446']
# for code in stock_basics.index[0:1]:
for code in stocks:
    ordinal = stock_basics.ix[code]['timeToMarket']
    year = ordinal // 10000

    #start = datetime.date(year=ordinal // 10000, month=ordinal //100 % 100, day=ordinal % 100)
    while year <= curr_year:
        for quarter in range(1, 5):
            if year == curr_year and quarter > curr_quarter:
                break
            history_data = datalib.get_h_data_sina(code, year, quarter)
            if len(history_data) > 0:
                db.history_data.insert(history_data)

        year += 1



#STEP3: for each stock, get its history data, without autype



