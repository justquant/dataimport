import datetime
import tushare as ts


class TushareLib:
    def __init__(self):
        pass

    def get_stock_basics(self):
        stock_basics = ts.get_stock_basics()
        return stock_basics

    def get_tick_data(self, code, date, retry_count=3, pause=0):
        tick_data = ts.get_tick_data(code=code, date=date, retry_count=retry_count, pause=pause)
        return tick_data

    def get_history_data_au(self, code, start=None, end = None, autype = 'qfq', index=False, retry_count=3, pause=0):
        now = datetime.datetime.now()
        year = now.year
        month = now.month
        day = now.day

        if start is None:
            start = "%d-%d-%d" % (year, month, day)

        if end is None:
            end = "%d-%d-%d" % (year + 1, month, day)

        hist_data = ts.get_h_data(code, start, end, autype, index, retry_count, pause)
        return hist_data

    def get_history_data(self, code, start, end, ktype='D', retry_count=3, pause=0):
        return ts.get_hist_data(code, start, end, ktype, retry_count, pause)

    def get_today_all(self):
        return ts.get_today_all()

    def get_realtime_quotes(self, symbols):
        return ts.get_realtime_quotes(symbols=symbols)

    def get_today_ticks(self, code, retry_count=3,pause=0):
        return ts.get_today_ticks(code=code, retry_count=retry_count, pause=pause)

    def get_dadan(self, code, date='2016-07-12', vol=400, retry_count=3,pause=0):
        return ts.get_sina_dd(code=code, date=date,vol=vol,retry_count=retry_count, pause=pause)

    




