import csv
wanted = ('Created', 'Activity Type', 'Assigned To', 'Comment')

with open('test.csv') as f:
    rdr = csv.DictReader(f)

    result = []
    for row in rdr:
        result.append({k: v for k, v in row.items() if k in wanted})

		
for r in result:
	if(r['Assigned To'] == 'SADMIN' and r['Activity Type'] == 'Email - Outbound'):
		pass
	else:
		print(r['Created'])
		print(r['Activity Type'])
		print(r['Assigned To'])
		print(r['Comment'])
		print('')