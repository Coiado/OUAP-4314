import csv
from pymongo import MongoClient

client = MongoClient()
db = client.primer
coll = coll = db['kickstarter']
reader = csv.reader(open('ks-projects-201801-sample.csv', 'r'))
d = {}
for row in reader:
   print(row[0])