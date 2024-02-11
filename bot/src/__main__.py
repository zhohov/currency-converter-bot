import os
import logging
import asyncio
from typing import NoReturn
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv, find_dotenv


async def main() -> NoReturn:
    logging.basicConfig(level=logging.INFO)

    load_dotenv(find_dotenv())

    dp = Dispatcher()
    bot = Bot(token=os.getenv('TELEGRAM_TOKEN'))

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())

    except Exception as e:
        logging.info(msg='Long polling error')
