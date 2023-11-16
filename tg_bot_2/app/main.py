from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TELEGRAM_TOKEN
from handlers import admin, bestiary, common, tech


async def on_startup(_):
    pass


bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

admin.register_handlers(dp)
tech.register_handlers(dp)
bestiary.register_handlers(dp)
common.register_handlers(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
