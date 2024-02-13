import logging

from aiogram import types
from aiogram.filters import CommandObject

from dto.convert_currency import ConvertInfo
from services.currency_api import get_convert_currency


async def convert_command(
    message: types.Message, command: CommandObject
) -> types.Message:

    try:
        args = command.args.split()

        convert = ConvertInfo(
            currency_from=args[1].lower(),
            currency_to=args[3].lower(),
            amount=int(args[0]),
        )

        try:
            convert_result = get_convert_currency(convert)
            return await message.answer(
                text=f"{int(convert_result)}{convert.currency_to.upper()}"
            )
        except Exception as e:
            logging.info(f"Exception {e}")
            return await message.answer(
                text="Произошла ошибка, попробуйте конвертировать заново"
            )

    except Exception as e:
        logging.info(f"Exception {e}")
