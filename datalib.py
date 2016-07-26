from io import StringIO
from lxml import html
from urllib.request import urlopen, Request
import tushare as ts


#从新浪获取后复权数据
def get_h_data_sina(stock_code,year,quarter):
    result = []
    url = "http://vip.stock.finance.sina.com.cn/corp/go.php/vMS_FuQuanMarketHistory/stockid/%s.phtml?year=%d&jidu=%d"%(stock_code, year, quarter)
    request = Request(url)
    text = urlopen(request, timeout=10).read()
    text = text.decode('GBK')
    page = html.parse(StringIO(text))
    table = page.xpath('//*[@id=\"FundHoldSharesTable\"]/tr')

    for tr in table[1:]:
        data = dict()
        data['date'] = tr[0].text_content().strip()
        data['open'] = tr[1].text_content().strip()
        data['high'] = tr[2].text_content().strip()
        data['close']= tr[3].text_content().strip()
        data['low'] = tr[4].text_content().strip()
        data['volume'] = tr[5].text_content().strip()
        data['amount'] = tr[6].text_content().strip()
        data['factor'] = tr[7].text_content().strip()
        result.append(data)

    return result

# get basic info from tushare
def get_stock_basics():
    df = ts.get_stock_basics()
    df['code'] = df.index
    return df[['code', 'name', 'industry', 'area', 'timeToMarket']]
