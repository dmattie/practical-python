# report.py
#
# Exercise 2.4
'''Read the holdings from a portfolio'''


import csv
import fileparse

def read_portfolio(filename):
    return fileparse.parse_csv(filename, select=['name','shares','price'], types=[str,int,float])

def read_prices(filename):

    return dict(fileparse.parse_csv(filename,types=[str,float], has_headers=False))

def make_report(portfolio, prices):

    rows = []
    for stock in portfolio:
        current_price = prices[stock['name']]
        change = current_price - stock['price']
        summary = (stock['name'], stock['shares'], current_price, change)
        rows.append(summary)
    return rows

def portfolio_report(portfoliofile,pricefile):        
    '''
    Make a stock report given portfolio and price data files.
    '''
    # Read data files 
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Create the report data
    report = make_report(portfolio,prices)

    # Print it out
    print_report(report)



def print_report(reportdata):
    '''
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    '''
    headers = ('Name','Shares','Price','Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-'*10 + ' ')*len(headers))
    for row in reportdata:
        print('%10s %10d %10.2f %10.2f' % row)

portfolio_report('Data/portfolio.csv',
                 'Data/prices.csv')