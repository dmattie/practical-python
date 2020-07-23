# pcost.py
#
# Exercise 1.27
import sys
import csv
import report

def portfolio_cost(filename):    

    portfolio = report.read_portfolio(filename)
    total_cost= sum([s['shares']*s['price'] for s in portfolio])

    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input('Enter a filename:')


print('Total cost:', portfolio_cost(filename))


