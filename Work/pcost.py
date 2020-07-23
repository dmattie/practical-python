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

def main(args):
    if len(args) != 2:
        raise SystemExit('Usage: %s portfoliofile' % args[0])
    filename = args[1]
    print('Total cost:', portfolio_cost(filename))

if __name__ == '__main__':
    import sys
    main(sys.argv)



