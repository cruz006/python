import requests

url = "https://openai80.p.rapidapi.com/images/generations"

payload = {
	"prompt": input("Please enter a prompt: \n"),
	"n": 2,
	"size": "1024x1024"
}

headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "3fc228024fmsh1cf13948472401ep1b25f3jsn88aa0d6e5e7d",
	"X-RapidAPI-Host": "openai80.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
