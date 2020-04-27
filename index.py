import json
import csv
import pandas as pd

data = [json.loads(line) for line in open('covid1.json', 'r', encoding = 'utf8')]
print(len(data))
with open('covid.csv', mode='w', encoding = 'utf8') as csv_file:
    fieldnames = ['title', 'url', 'text']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(100):
        writer.writerow({'title': data[i]['title'], 'url': data[i]['url'], 'text': data[i]['text']})

data = pd.read_csv('covid.csv')
data = data.dropna()
print(data['MESSAGE'])

