__all__ = ["register_conversion_handlers"]

from aiogram import Router
from aiogram.filters import Command

from .currency_conversion import convert_command


def register_conversion_handlers(router: Router) -> None:
    router.message.register(convert_command, Command(commands=["convert"]))
