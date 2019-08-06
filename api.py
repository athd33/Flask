import requests
import pprint

r = requests.get("https://fr.openfoodfacts.org/categories&json=1")

data = r.json()

c = data['tags']


for i in c:
    print(i['name'])