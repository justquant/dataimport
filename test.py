import algorithm
import pandas as pd
from pymongo import MongoClient
import pymongo

client = MongoClient('localhost', 27017)
db = client['tushare']

data = db.history_data.find({'code':'600446'}).sort([("date", pymongo.ASCENDING)])

df = pd.DataFrame(list(data))

prices = df['close'].values

print(prices[-1])

sma5 = algorithm.sma(prices,5)
sma5.reverse()
print(sma5)

diff, dea, cd = algorithm.macd(prices)
diff.reverse()
print(diff)

