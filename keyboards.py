from telegram import (
    ReplyKeyboardMarkup, KeyboardButton
)


start_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='☀️Ob-havoni bilish', request_location=True)
        ]
    ],
    resize_keyboard=True
)
