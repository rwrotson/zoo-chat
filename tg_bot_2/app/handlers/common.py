from aiogram import types, Dispatcher


async def default_message(message: types.Message):
    await message.answer('FUCK YOU')


def register_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(default_message)
