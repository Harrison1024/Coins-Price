# 📈 Crypto Price Tracker con Sheety y Telegram

Este script obtiene el precio actual de **Bitcoin**, **Ethereum** y **Dogecoin** usando la API pública de [CoinGecko](https://www.coingecko.com/), guarda los datos en un **Google Sheet** a través de [Sheety](https://sheety.co/) y envía una notificación automática por **Telegram**.

---

## 🚀 Características

* Consulta en tiempo real el precio en USD de las criptomonedas definidas.
* Guarda fecha, hora, nombre de la moneda y precio en un Google Sheet.
* Envía un mensaje formateado a un chat de Telegram.

---

## 📋 Requisitos

Antes de ejecutar este script, necesitas:

1. **Python 3.8 o superior**
2. Librerías instaladas:

   ```bash
   pip install requests
   ```
3. Una cuenta y proyecto configurado en:

   * **CoinGecko API** (gratuita, no requiere registro)
   * **Sheety API** (para conectar con Google Sheets)
   * **Bot de Telegram** (creado con BotFather)
4. Un archivo `app_config.py` en el mismo directorio con:

   ```python
   SHEETY_TOKEN = "tu_token_de_sheety"
   SHEETY_API = "https://api.sheety.co/tu_id/tu_hoja/precios"
   TELEGRAM_BOT_KEY = "tu_token_de_bot_telegram"
   TELEGRAM_USER = "tu_chat_id"
   ```

---

## ⚙️ Uso

1. Clonar el repositorio:
2. Crear y configurar `app_config.py` con tus claves y tokens.
3. Ejecutar:

   ```bash
   python main.py
   ```
4. Verifica:

   * Que los datos aparezcan en tu **Google Sheet**.
   * Que recibas un mensaje por **Telegram**.

---

## 📌 Ejemplo de Mensaje en Telegram

```
📊 Precios actuales:
BITCOIN → $118,491 USD
ETHEREUM → $4,251.56 USD
DOGECOIN → $0.242372 USD
```

---

## 🔒 Seguridad

* **No publiques** `app_config.py` ni tus claves en repositorios públicos.
* Usa un archivo `.gitignore` para excluirlo:

  ```
  app_config.py
  __pycache__/
  ```

---

## 📜 Licencia

Este proyecto se distribuye bajo la licencia MIT. Eres libre de usarlo y modificarlo, pero sin garantías.

---
