import requests
url = "http://localhost:1800/messages"

data = {
    "content": "hello fams, i am koloman",
    "sender": "koloman"
}
response = requests.post(url,json=data)
# print(response.json())
getresponse = requests.get(url)
# datum = getresponse.text()
print(getresponse.text)
