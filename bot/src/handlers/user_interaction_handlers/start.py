from aiogram import types


async def start_command(message: types.Message) -> types.Message:
    return await message.answer(
        text=f"Привет, {message.chat.username}! Я бот конвертер валют."
        "Я могу помочь тебе конвертировать валюты и предоставить актуальные курсы обмена."
        "Просто отправь мне сообщение с командой /help, чтобы узнать, "
        "как со мной взаимодействовать. Начнем!"
    )
