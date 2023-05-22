import requests

url = "https://dark-sky.p.rapidapi.com/+37.774929,-122.419418"

querystring = {"lang":"en","units":"auto"}

headers = {
	"X-RapidAPI-Key": "3fc228024fmsh1cf13948472401ep1b25f3jsn88aa0d6e5e7d",
	"X-RapidAPI-Host": "dark-sky.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())