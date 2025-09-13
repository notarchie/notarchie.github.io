import csv
import json

with open('data.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)

with open('data.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(rows, jsonfile, indent=2)