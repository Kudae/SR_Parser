import csv
from collections import defaultdict
columns = defaultdict(list)

with open('test.csv', 'rU') as f:
    reader = csv.DictReader(f)
    for row in reader:
        for (k, v) in row.items():
            columns[k].append(v)

for i in xrange(len(columns['Created'])):
    print(columns['Created'][i])