import requests

# endpoint = "https://httpbin.org/status/200/"
endpoint = "http://localhost:8000/api/" #http://127.0.0.1:8000/

get_response = requests.post(endpoint, json={"title": None, "content": "Hello", "price":"abss26"}) #HTTP Request
print(get_response.headers)
print(get_response.text) # print raw text response

# HTTP Request -> Html
# Rest APi HTTP Request -> Json
# JavaScript Object Notation -> Python Dict

print(get_response.json())
# print(get_response.status_code)
