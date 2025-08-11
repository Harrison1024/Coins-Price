import requests
from datetime import datetime
from app_config import *

# Obtener datos de las criptomonedas
COINS = ["bitcoin", "ethereum", "dogecoin"] # Criptomonedas de interes
COINGECKO_API = "https://api.coingecko.com/api/v3/simple/price" # API de CoinGecko

# Headers de autorización para Sheety
headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

# Parametros 
params = {
    "ids": ",".join(COINS), # Convierte el arreglo COINS en "bitcoin,ethereum,dogecoin"
    "vs_currencies": "usd"
    }

response = requests.get(COINGECKO_API, params=params)
response.raise_for_status()
data = response.json()
print(data)
