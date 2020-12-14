import requests

response = requests.post("https://wrapapi.com/use/sadcatofficial/123/ekatalog2/2.1.0", json={
  "search": "iphone 12",
  "wrapAPIKey": "v9vkQf9EQRGVYDjf3i8ppizdggbFgFOI"
})
print (response.json())
