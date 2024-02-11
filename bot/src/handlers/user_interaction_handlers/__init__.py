from aiogram import Router
from aiogram.filters import Command

from .start import start_command


def register_user_interaction_handlers(router: Router) -> None:
    router.message.register(start_command, Command(commands=["start"]))
