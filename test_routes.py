import requests


res = requests.post('http://127.0.0.1:5000/roll', headers={"content-type": "application/json"}, json={
    "previous": 6,
    "prediction": "higher"
})

print(res)
print(res.json())
