import requests

methods_list = [{"method":"GET"}, {"method":"POST"}, {"method":"PUT"}, {"method":"DELETE"}]

for param in methods_list:
        result = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=param)
        print(f"method GET with parameter params={param} has following result {result} with status code {result.status_code}")
        result = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", data=param)
        print(f"method GET with parameter data={param} has following result {result} with status code {result.status_code}")
        result = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=param)
        print(f"method POST with parameter data={param} has following result {result} with status code {result.status_code}")
        result = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", params=param)
        print(f"method POST with parameter params ={param} has following result {result} with status code {result.status_code}")
        result = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=param)
        print(f"method PUT with parameter data={param} has following result {result} with status code {result.status_code}")
        result = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", params=param)
        print(f"method PUT with parameter params ={param} has following result {result} with status code {result.status_code}")
        result = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=param)
        print(f"method DELETE with parameter data={param} has following result {result} with status code {result.status_code}")
        result = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", params=param)
        print(f"method DELETE with parameter params ={param} has following result {result} with status code {result.status_code}")



