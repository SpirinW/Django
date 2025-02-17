import telebot
import requests
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("token")
api_key = os.getenv("api_key")  # ключ от API валют

bot = telebot.TeleBot(token)

def convert_currency(from_currency, to_currency, amount):
    url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}&access_key={api_key}"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200 or not data.get("success"):
        return "Ошибка при получении данных о курсе валют."

    if "info" not in data or "quote" not in data["info"]:
        return "Ошибка ответа от API."

    rate = data["info"]["quote"]
    result = round(amount * rate, 2)

    return f"Курс: {rate}\nРезультат: {result} {to_currency}"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я помогу тебе конвертировать валюты. Напиши команду в формате:\n\n<from_currency> <to_currency> <amount>\nПример: USD EUR 100")

@bot.message_handler(func=lambda message: True)
def handle_conversion(message):
    try:
        parts = message.text.split()
        if len(parts) != 3:
            bot.reply_to(message, "Неверный формат. Напишите в формате: <from_currency> <to_currency> <amount>\nПример: USD EUR 100")
            return

        from_currency = parts[0].upper()
        to_currency = parts[1].upper()
        amount = float(parts[2])

        result = convert_currency(from_currency, to_currency, amount)
        bot.reply_to(message, result)

    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка: {e}")

bot.polling()
