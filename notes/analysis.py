'''Goal:  Learn to rapidly analyze data using list comprehensions

   Syntax:  [<expr> for <var> in <iterable> if <cond>]

'''

from pprint import pprint
import portfolio

port = portfolio.get_portfolio('notes/stocks.txt')
pprint(port)

# Projections of the data (subset of the columns)
print [trade.symbol for trade in port]
print [trade.shares for trade in port]
print [trade.price for trade in port]

print 'Make a list of the unique symbols in the portfolio of trades'
print 'SELECT DISTINCT symbol FROM Port ORDER BY symbol;'
symbols = sorted(set([trade.symbol for trade in port]))
print symbols

print 'How many shares of Cisco do you own?'
print 'SELECT SUM(shares) FROM Port WHERE symbol == "CSCO";'
print sum([trade.shares for trade in port if trade.symbol == 'CSCO'])

print 'How much did you invest in the market?'
print 'SELECT SUM(shares * price) FROM Port;'
print sum([trade.shares * trade.price for trade in port])

