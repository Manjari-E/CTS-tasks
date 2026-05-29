import requests

try:
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")

    if response.status_code == 200:
        data = response.json()
        print("Name:", data["name"])
        print("Email:", data["email"])
    else:
        print("Data not found")

except requests.exceptions.RequestException:
    print("Network Error")