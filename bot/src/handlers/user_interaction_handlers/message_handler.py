from aiogram import types

from services.message_service import handle_message_service


async def handle_message(message: types.Message) -> types.Message:
    text = message.text.lower()
    answer = handle_message_service(text=text)
    print(text)
    return await message.answer(text=answer)
