import requests
import pprint


'''
r = requests.get("https://fr.openfoodfacts.org/additives&json=1")
'''

payload = {"search_terms": "Lindt, "json": 1}
r = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?search_terms=Lindt&json=1")

print(r)

'''

data = r.json()

c = data['tags']


for i in c:
    print(i['name'])

'''