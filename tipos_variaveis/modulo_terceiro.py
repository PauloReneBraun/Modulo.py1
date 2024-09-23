# pip3 install request==2.31.0

print("\nExemplo de importação de um módulo de terceiros:")
import requests

url = "https://www.google.com"
response = requests.get(url)  
print(response.status_code)