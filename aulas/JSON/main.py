import requests

API_request = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL")
dict_response = API_request.json()

print(dict_response["USDBRL"]["bid"])