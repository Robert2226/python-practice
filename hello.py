print("Hello, Data Center")
import requests
response = requests.get("https://api.github.com")
print("Status Code:", response.status_code)
print("Content.")
print(response.text[:500])