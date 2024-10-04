import requests

res = requests.post(
    "http://127.0.0.1:8000/items/",
    json={"name":"Tシャツ","price":2000,"description":"白Tシャツ"},    
)

