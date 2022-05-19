import requests


response = requests.get("https://playground.learnqa.ru/api/hello", timeout=(2, 5))
print(response.text)