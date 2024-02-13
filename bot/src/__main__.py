import asyncio
import logging
import os
from typing import NoReturn

from aiogram import Bot, Dispatcher, types
from dotenv import find_dotenv, load_dotenv

from handlers import (register_conversion_handlers,
                      register_user_interaction_handlers)
from utils import bot_commands as bot_cmd


async def main() -> NoReturn:
    logging.basicConfig(level=logging.INFO)

    load_dotenv(find_dotenv())

    dp = Dispatcher()
    bot = Bot(token=os.getenv("TELEGRAM_TOKEN"))

    await register_commands(bot=bot, bot_commands=bot_cmd)
    await register_handlers(dp=dp)
    await start_bot(dp=dp, bot=bot)


async def start_bot(dp: Dispatcher, bot: Bot) -> NoReturn:
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    except Exception as e:
        logging.info(f"Error starting bot: {e}")


async def register_handlers(dp: Dispatcher) -> None:
    handlers = [
        register_user_interaction_handlers,
        register_conversion_handlers,
    ]

    for handler in handlers:
        handler(dp)


async def register_commands(bot: Bot, bot_commands: list) -> None:
    commands = []
    for cmd in bot_commands:
        commands.append(types.BotCommand(command=cmd[0], description=cmd[1]))

    await bot.set_my_commands(commands=commands)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        logging.exception(f"Error starting bot: {e}")
