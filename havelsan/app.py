import requests

response = requests.get("https://animechan.vercel.app/api/quotes/anime?title=naruto")
print(response.json())