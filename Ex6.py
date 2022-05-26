import requests



resp = requests.post('https://playground.learnqa.ru/api/long_redirect', allow_redirects=True)
res1 = resp.history[0]
res2 = resp
print(res1.url)
print(res2.url)

resp.history
for r in resp.history:
    print(r.status_code, r.url)


