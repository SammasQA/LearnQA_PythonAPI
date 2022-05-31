import requests
import time

status = "Job is NOT ready"
result = "Job is ready"
error = "No job linked to this token"
token = "LearnQA"

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")

resp_token = response.json()['token']
resp_time = response.json()['seconds']

print(response.text)

response_with_token = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={
    'token': 'resp_token'})
print(response_with_token.text)

time.sleep(resp_time)

data = {
    'token': resp_token
}

response2 = requests.get(
    "https://playground.learnqa.ru/api/longtime_job",
    params=data
)
if response2.json()['status'] == status:
    print(f"PASSED! Server answer when job is not ready: {response2.json()['status']}")
else:
    print(f"FAILED! Wrong server answer when job is not ready: {response2.json()['status']}")
print(f"Response text: {response2.text}")

print(" ")
time.sleep(resp_time)
response3 = requests.get(
    "https://playground.learnqa.ru/api/longtime_job",
    params=data
)

if response3.json()['status'] == result:
    print(f"PASSED! Correct server answer when job is ready: {response3.json()['status']}. Job time: {resp_time}")
else:
    print(f"FAILED! Wrong server answer: {response3.json()['status']}. Job time: {resp_time}")
print(f"Response text: {response3.text}")

print(" ")

response4 = requests.get(
    "https://playground.learnqa.ru/api/longtime_job",
    params={'token': token}
)

if response4.json()['error'] == error:
    print(f"PASSED! Correct server answer: {response4.json()['error']}")

else:
    print(f"FAILED! Wrong server answer: {response4.json()['error']}")
    print(f"Response text: {response4.text}")