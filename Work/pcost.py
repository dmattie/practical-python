# pcost.py
#
# Exercise 1.27
import sys
import csv

def portfolio_cost(filename):    

    total_cost = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                nshares = int(row[1])
                price = float(row[2])
                total_cost += nshares * price
            # This catches errors in int() and float() conversions above
            except ValueError:
                print('Bad row:', row)

    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input('Enter a filename:')


print('Total cost:', portfolio_cost(filename))


