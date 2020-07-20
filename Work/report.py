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
