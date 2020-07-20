# report.py
#
# Exercise 2.4
'''Read the holdings from a portfolio'''


import csv

def read_portfolio(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding={}

            holding['name']=row[0]
            holding['shares']=int(row[1])
            holding['price']=float(row[2])
            #holding = [row[0],int(row[1]),float(row[2])]
            portfolio.append(holding)
    return portfolio
def read_prices(filename):

    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass

    return prices

def make_report(portfolio, prices):

    rows = []
    for stock in portfolio:
        current_price = prices[stock['name']]
        change = current_price - stock['price']
        summary = (stock['name'], stock['shares'], current_price, change)
        rows.append(summary)
    return rows

portfolio = read_portfolio('Data/portfolio.csv')
prices    = read_prices('Data/prices.csv')

total_cost = 0.0
for s in portfolio:
    total_cost += s['shares']*s['price']

total_value = 0.0
for s in portfolio:
    total_value += s['shares']*prices[s['name']]

print('Total cost', total_cost)
print('Current value', total_value)
print('Gain', total_value - total_cost)

report = make_report(portfolio, prices)
for r in report:
        print('%10s %10d %10.2f %10.2f' % r)