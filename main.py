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

# Solicitud a la API de criptomonedas
response_coins = requests.get(url=COINGECKO_API, params=params)
response_coins.raise_for_status()
data = response_coins.json()

# Subida de datos al Excel
# Determinacion de la fecha y hora de los datos
fecha = datetime.now().strftime("%Y-%m-%d")
hora = datetime.now().strftime("%H:%M:%S")

# Crear el JSON de los datos para el sheets
for coin in COINS:
    json_coin = {
        "precios": {
            "fecha" : fecha,
            "hora" : hora,
            "moneda" : coin.upper(),
            "precioUsd" : data[coin]["usd"]
        }
    }
    # Hacer el envio de datos a la hoja de google sheets
    response_sheety = requests.post(url= SHEETY_API, json= json_coin, headers= headers)
    response_sheety.raise_for_status()

# Envio de datos por Telegram
# Creacion de mensaje
mensaje = "📊 Precios actuales:\n"
for coin in COINS:
    mensaje += f"{coin.upper()} → ${data[coin]['usd']} USD\n"

# Envio del mensaje por Telegram
TELEGRAM_API = f"https://api.telegram.org/bot{TELEGRAM_BOT_KEY}/sendMessage"
requests.post(url= TELEGRAM_API, data={'chat_id': TELEGRAM_USER, 'text': mensaje})
