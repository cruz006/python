import requests

url = "https://api.coincap.io/v2/assets/"

headers={
   "X-RapidAPI-Key": "3fc228024fmsh1cf13948472401ep1b25f3jsn88aa0d6e5e7d",
	"X-RapidAPI-Host": "bit5.p.rapidapi.com"
 }

response = requests.get(url, headers=headers)
print(response.json())