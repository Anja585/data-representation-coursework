import json
from urllib import response
import requests

url = 'https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIM07/JSON-stat/2.0/en'
response = requests.get(url)
data = response.json()

with open('cso.json', 'w') as f:
    json.dump(data, f)

