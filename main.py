import urllib.request
import tabula
import json

base_url = "https://content.ftserussell.com/sites/default/files/"
russell_file = "ru3000_membershiplist_20210628.pdf"

print("downloading file")
urllib.request.urlretrieve(base_url + russell_file, russell_file) 

print("extracting table from pdf")
dfs = tabula.read_pdf(russell_file, pages='all')

symbols = set()
for df in dfs:
    results = df.iloc[:, [1, 4]].stack().values.T.tolist()
    symbols.update(results)

print("writing results file russell-3000.json")
with open('russell-3000.json', 'w') as outfile:
    json.dump(sorted(symbols), outfile, indent=2)
