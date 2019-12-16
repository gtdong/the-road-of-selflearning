import requests

res = requests.get('http://127.0.0.1:8000/api/',headers={'key':'03e3867f416efb5bd6e8036b3dcea49f|1571819775.407893'})
print(res.text)