import requests

#conoHa用
BASE_URL = "http://160.251.236.70:8000/"

#ローカル用
#BASE_URL = "http://127.0.0.1:8000"

res = requests.get(
    f"{BASE_URL}",
    headers={"Authorization":"Bearer A1B2C3D4"},
)

print(res.status_code)
print(res.text)
print(res.headers)
