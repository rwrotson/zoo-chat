from telegram.ext.commandhandler import CommandHandler
from telegram.ext.updater import Updater

from bot.routes import start, help, password, send_credentials


def register_handlers(updater: Updater):
    start_handler = CommandHandler('start', start)
    updater.dispatcher.add_handler(start_handler)

    password_handler = CommandHandler('password', password)
    updater.dispatcher.add_handler(password_handler)

    send_hander = CommandHandler('send_credentials', send_credentials)
    updater.dispatcher.add_handler(send_hander)

    help_handler = CommandHandler('help', help)
    updater.dispatcher.add_handler(help_handler)
