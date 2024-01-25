import json
import csv

def csv_to_json(filename):
    data = {}
    with open(filename, 'r') as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            format = row['format']
            data[format] = row
    print(data)
        

csv_to_json("nft-naming-csv.csv")