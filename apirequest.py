import requests

reqUrl = "http://127.0.0.1:8000/items"

headersList = {
 "Accept": "*/*",
 "User-Agent": "Thunder Client (https://www.thunderclient.com)" 
}

payload = ""

response = requests.request("GET", reqUrl, data=payload,  headers=headersList)

# Get the response and put into a list
responseList = response.json()

# From reponseList, get the first item and print it
# print(responseList[0])

# From reponseList, form first item get the name and print it
ID = responseList[0]["ID"]
name = responseList[0]["Name"]
price = responseList[0]["Price"]

print("ID ->", ID)
print("Name ->", name)
print("Price -> ", str(price))