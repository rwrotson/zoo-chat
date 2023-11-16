import logging
from telegram.ext.updater import Updater

from bot.handlers import register_handlers
from bot.


logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    register_handlers(updater)
    updater.start_polling()


if __name__=='__main__':
    main()

