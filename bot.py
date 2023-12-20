from settings import TOKEN
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from handlers import (
    start,
    send_location
)


def main():
    # create updater obj.
    updater = Updater(TOKEN)
    
    # create dispatcher obj.
    dispatcher = updater.dispatcher
    
    # add command handlers
    dispatcher.add_handler(
        handler=CommandHandler(
            command=['start', 'boshlash'], 
            callback=start
        )
    )
    dispatcher.add_handler(
        handler=MessageHandler(
            filters=Filters.location,
            callback=send_location
        )
    )
    updater.start_polling()
    updater.idle()

main()