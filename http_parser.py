from bs4 import BeautifulSoup

# https://stackoverflow.com/questions/11790535/extracting-data-from-html-table

html = """
<table class="details" border="0" cellpadding="5" cellspacing="2" width="95%">
    <tr valign="top">
      <th>Created</th>
      <th>Activity Type</th>
      <th>Audience</th>
      <th>Description</th>
      <th>Start Date</th>
      <th>Comment</th>
   </tr>
   <tr valign="top" class="Failure">
     <td>103</td>
     <td>24</td>
     <td>76.70%</td>
     <td>71 ms</td>
     <td>0 ms</td>
     <td>829 ms</td>
  </tr>
</table>"""



soup = BeautifulSoup(html)
table = soup.find("table", attrs={"class":"details"})

# The first tr contains the field names.
headings = [th.get_text() for th in table.find("tr").find_all("th")]

datasets = []
for row in table.find_all("tr")[1:]:
    dataset = zip(headings, (td.get_text() for td in row.find_all("td")))
    datasets.append(dataset)

print (list(datasets[0]))
