import csv
wanted = ('Created')

with open('test.csv') as f:
    rdr = csv.DictReader(f)

    result = []
    for row in rdr:
        result.append({k: v for k, v in row.items() if k in wanted})

for r in result:
    print(r['Created'])
