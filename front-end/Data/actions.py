from amadeus import Client, ResponseError
from urllib import request

amadeus = Client(
        client_id='biFnzZXehvqrcMlATt3bhwwY0kBYkzEP',
        client_secret='xtalsAwFeaeUqfZM'
    )
def getFlights(originPlace, destinationPlace, deptTime, adultNum):
    try:
        response = amadeus.shopping.flight_offers_search.get(
            originLocationCode=originPlace,
            destinationLocationCode=destinationPlace,
            departureDate=deptTime,
            adults=adultNum)
        print(response.data)
    except ResponseError as error:
        print(error)

getFlights("MAA", "BLR", '2022-10-20', 1)
import requests
# Change this to be your API key.
# MY_API_KEY="YYEBMP4NFQ4BEAGNQYAAYNKMC37B"

# url = "https://beta3.api.climatiq.io/travel/flights"

# activity_id = "flight-domestic"
# # You must always specify your AUTH token in the "Authorization" header like this.
# authorization_headers = {"Authorization": f"Bearer: {MY_API_KEY}"}

# query_params = {
#         "legs": [
#             {
#                 "from": "MAA",
#                 "to": "BOM",
#                 "passengers": 1,
#                 "class": "first"
#             }
#         ]
#     }

# # This performs the request and returns the result as JSON
# response = requests.post(url, json=query_params, headers=authorization_headers).json()

# # And here you can do whatever you want with the results
# print(response)

# import requests

# url = "https://partner-test.api.chooose.today/v1/footprint/flights/distance?km=4000&travelClass=economy&roundtrip=true&passengers=2&flights=1"

# payload={}
# headers = {}

# response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)


    
