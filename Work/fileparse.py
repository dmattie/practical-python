# fileparse.py
import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):

    if select and not has_headers:
        raise RuntimeError('select requires column headers')

    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        headers = next(rows) if has_headers else []
        
        if select:
            indices = [ headers.index(colname) for colname in select ]
            headers = select

        records = []
        for rowno, row in enumerate(rows, 1):
            if not row:     
                continue

            
            if select:
                row = [ row[index] for index in indices]

           
            if types:               
                    row = [func(val) for func, val in zip(types, row)]
               
            # Make a dictionary or a tuple
            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)

        return records
