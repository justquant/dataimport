import algorithm
import pandas as pd
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['tushare']

data = db.history_data.find()

df = pd.DataFrame(list(data))

prices = df['close'].values

print(prices[-1])

print(algorithm.sma(prices,5)[-1])
