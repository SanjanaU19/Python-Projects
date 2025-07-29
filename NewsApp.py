import requests

query  =input("What type of News are you inteseted in today?")
api = "2dfd745f9ccc4b009ac4c4b4cd285687"

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-06-29&sortBy=publishedAt&apiKey={api}"

print(url)

r = requests.get(url)

data  = r.json()
articles = data["articles"]

for index,article in enumerate(articles):
    print(index + 1 , article["title"],article["url"])
    print("\n*****************************\n")
    

   