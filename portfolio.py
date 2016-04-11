# portfolio.py

import csv
from collections import defaultdict
import urllib

def get_portfolio(filename):
    ''' read in the CSV file of stock trades
          build a dictionary of lists of tuples of the form
          { symbol : [(shares, purchase px), (shares, purchase px), ...], ... }
          { 'CSCO':  [(150, 19.05), (175, 19.56), ...], ... }
    '''
    portfolio = defaultdict(list)
    with open(filename) as f:
        for symbol, shares, price in csv.reader(f):
            portfolio[symbol].append( (int(shares), float(price)) )
    return portfolio

quote_url_template = 'http://download.finance.yahoo.com/d/quotes.csv?s=%s&f=sl1d1t1c1ohgv&e=.csv'
def get_quote(*symbols):
    url = quote_url_template % ','.join(symbols)
    u = urllib.urlopen(url)
    quotes = {}
    for symbol, price, _, _, _, _, _, _, _ in csv.reader(u):
        try:
            quotes[symbol] = float(price)
        except ValueError:
            pass
    return quotes

if __name__ == '__main__':
    filename = 'notes/stocks.txt'
    portfolio = get_portfolio(filename)
    quotes = get_quote(*portfolio)

    heading_template = '%20s %20s %21s %21s'
    row_template = u'%20s %20s %20s\N{small dollar sign} %20s\N{small dollar sign}'
    header = 'Ticker', 'Shares', 'Market Value', 'Profit'
    print heading_template % header
    print heading_template % tuple(['-' * len(h) for h in header])
    total_mkt_price = 0
    total_profit = 0
    for symbol, trades in portfolio.items():
        total_proceeds = sum([shares*price for shares,price in trades])
        total_shares = [shares for shares,_ in trades]
        
        mkt_price = sum(total_shares) * quotes[symbol]
        profit = mkt_price - total_proceeds
                
        total_mkt_price += mkt_price
        total_profit += profit
        
        print row_template % (symbol, sum(total_shares), mkt_price, profit)

    print row_template % ('total', '', total_mkt_price, total_profit)
n
