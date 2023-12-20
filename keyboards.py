from telegram import (
    ReplyKeyboardMarkup, KeyboardButton
)


start_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Ob-havoni', request_location=True)
        ]
    ],
    resize_keyboard=True
)
