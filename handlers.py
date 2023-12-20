from telegram.ext import CallbackContext
from telegram import Update
from keyboards import start_keyboard
from settings import API_KEY
import requests

def start(update: Update, context: CallbackContext):
    user = update.effective_user
    bot = context.bot
    bot.send_message(user.id, 'Asslomu alaykum.', reply_markup=start_keyboard)

def send_location(update: Update, context: CallbackContext):
    user = update.effective_user
    bot = context.bot
    lat = update.message.location.latitude
    lon = update.message.location.longitude
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"
    response = requests.get(url).json()

    weather = f"""
☀️weather-{response['weather'][0]['main']},
🌡temp-{response["main"]['temp']-273.15}
"""

    bot.sendMessage(user.id,weather , reply_markup=start_keyboard)
    



