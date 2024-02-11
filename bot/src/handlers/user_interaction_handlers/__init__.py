from aiogram import Router
from aiogram.filters import Command

from .help import help_command
from .start import start_command


def register_user_interaction_handlers(router: Router) -> None:
    router.message.register(start_command, Command(commands=["start"]))
    router.message.register(help_command, Command(commands=["help"]))
