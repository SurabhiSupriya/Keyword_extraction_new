import requests

url = "https://unfound-keywords-extraction-v1.p.rapidapi.com/extraction/keywords"

payload = "{\n    \"input_data\": [\n        \"https://en.wikipedia.org/wiki/Donald_Trump\",\n        \"https://en.wikipedia.org/wiki/Hillary_Clinton\"\n    ],\n    \"input_type\": \"url\",\n    \"N\": 10\n}"
headers = {
    'content-type': "application/json",
    'x-rapidapi-key': "70032a0077mshbba96f1eeefb173p173048jsn20c468016c38",
    'x-rapidapi-host': "unfound-keywords-extraction-v1.p.rapidapi.com"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)














