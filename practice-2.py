from collections import Counter
import heapq
import requests

base_url = "https://httpbin.org/get"
parameters = {"name":"Ravi"}
response = requests.get(base_url, params=parameters, timeout=10)
print(response.raise_for_status())
print(response.json())
