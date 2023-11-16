from aiogram import types, Dispatcher


async def help(message: types.Message):
    await message.answer('FUCK YOU')


def register_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(help)
