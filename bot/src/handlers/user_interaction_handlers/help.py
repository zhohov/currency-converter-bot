from aiogram import types


async def help_command(message: types.Message) -> types.Message:
    return await message.answer(
        text="/start запускает бота и приветствует пользователя.\n\n"
        "/help показывает доступные команды бота и предоставляет инструкции по их использованию.\n\n"
        "/convert позволяет конвертировать заданную сумму из одной валюты в другую. "
        "Формат команды: /convert <сумма> <исходная валюта> to <целевая валюта>. Например, "
        "чтобы сконвертировать 100 долларов США в евро, отправьте сообщение в формате: /convert 100 USD to EUR."
    )
