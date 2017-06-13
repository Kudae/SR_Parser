import csv
wanted = ('Created', 'Activity Type', 'Assigned To', 'Comment')

with open('test.csv') as f:
    rdr = csv.DictReader(f)

    result = []
    for row in rdr:
        result.append({k: v for k, v in row.items() if k in wanted})

newfile = open("sortedSR.txt", "w+")

for r in result:
    if(r['Assigned To'] == 'SADMIN' and r['Activity Type'] == 'Email - Outbound'):
        pass
    else:
        newfile.write(r['Created'] + '\n')
        newfile.write(r['Activity Type'] + '\n')
        newfile.write(r['Assigned To'] + '\n')
        newfile.write(r['Comment'] + '\n')
        newfile.write('\n')

newfile.close()
