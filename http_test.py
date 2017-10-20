from bs4 import BeautifulSoup as bs

import sys

# htmlfile = sys.argv[1]
htmlfile = open("output.HTML",'r', encoding="utf-8")

# htmlfile = open(htmlfile,'r', encoding="utf-8")

bs_html = bs(htmlfile, 'lxml')

table = bs_html.find('table')

headings = []
for th in table.find('tr').find_all('th'):
    headings.append(th.get_text())

datasets = []
for row in table.find_all("tr")[1:]:
    for td in row.find_all("td"):
        for br in td.find_all("br"):
            br.replace_with("\n")
    dataset = zip(headings, (td.get_text() for td in row.find_all("td")))
    datasets.append(dataset)

dict_data = []

for row in datasets:
    row = list(row)
    dict_data.append(dict(row))

wanted = ['Activity Type', 'Description', 'Created', 'Comment']

for row in dict_data:
    for key in row:
        if key in wanted:
            print('{} == {}'.format(key, row[key]))
    print('-    -    ' * 5)
