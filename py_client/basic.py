import requests

# endpoint  = "https://httpbin.org/status/500/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.post(endpoint,params={"abc":123},json={"title":"Hello"})
print(get_response.json())
# print(get_response.text)
# print(get_response.status_code)
