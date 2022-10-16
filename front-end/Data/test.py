import requests

url = "https://login.microsoftonline.com/04300fc2-8f04-4555-9a5d-c6fac7f23d0c/oauth2/token"

payload='grant_type=client_credentials&client_id=%5BClient%20ID%5D&client_secret=%5BClient%20secret%5D&resource=https%3A%2F%2Fpartner-test.api.chooose.today'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)