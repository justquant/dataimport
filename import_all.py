from pymongo import MongoClient
from tusharelib import TushareLib
import json
import datetime

# Import all data from tushare until today.
# This is used to initialize/re-initialize all the data base tables

# Connect to mongodb
# TODO:
client = MongoClient('localhost', 27017)
db = client['tushare']


# Truncate all table
db.stock_basics.drop()
db.tick_data.drop()
db.history_data.drop()
db.history_data_au.drop()

# instantiate TushareLib
tusharelib = TushareLib()

# STEP1: Get stock_basics.
stock_basics = tusharelib.get_stock_basics()
db.stock_basics.insert(json.loads(stock_basics.to_json(orient='records')))

# STEP2: For each stock in stock_basics, get its history data with autype, 2 years' data per run
currentDate = datetime.datetime.now().date()
stocks = ['600446']
# for code in stock_basics.index[0:1]:
for code in stocks:
    # time_to_market = datetime.strftime(stock_basics.ix[code]['timeToMarket'],'%Y%m%d')
    ordinal = stock_basics.ix[code]['timeToMarket']
    start = datetime.date(year=ordinal // 10000, month=ordinal //100 % 100, day=ordinal % 100)
    while start < currentDate:
        end = start.replace(start.year + 2)
        if currentDate < end:
            end = currentDate
        history_data = tusharelib.get_history_data_au(code, start.strftime('%Y-%m-%d'), end.strftime('%Y-%m-%d'))
        db.history_data.insert(json.loads(history_data.to_json(orient='records')))
        start = end


#STEP3: for each stock, get its history data, without autype



