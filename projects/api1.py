import requests

url = "https://openai80.p.rapidapi.com/images/generations"

payload = {
	"prompt": "A cute baby sea otter",
	"n": 2,
	"size": "1024x1024"
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "3fc228024fmsh1cf13948472401ep1b25f3jsn88aa0d6e5e7d",
	"X-RapidAPI-Host": "openai80.p.rapidapi.com", 
     "access-control-allow-credentials": "true",
  "access-control-allow-origin": "*",
  "content-length": "25",
  "content-type": "application/json",
  "date": "Fri, 19 May 2023 20:54:27 GMT",
  "server": "RapidAPI-1.2.8",
  "x-amz-apigw-id": "FMBAjGU0IAMFxUQ=",
  "x-amzn-requestid": "bae23ad8-13f6-4439-8c3f-b82af1a43cf1",
  "x-amzn-trace-id": "Root=1-6467e202-6f2671376c8e8c4d56373c40;Sampled=0;lineage=43307380:0",
  "x-rapidapi-region": "AWS - us-west-2",
  "x-rapidapi-version": "1.2.8",
  "x-ratelimit-tokens-limit": "50000",
  "x-ratelimit-tokens-remaining": "2936",
  "x-ratelimit-tokens-reset": "2361073"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())