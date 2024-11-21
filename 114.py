import requests #Helps me find webpages on the net (http request

response = requests.get("https://en.wikipedia.org/")
if response.status_code == 200:
    print("Wikipedia page found")

