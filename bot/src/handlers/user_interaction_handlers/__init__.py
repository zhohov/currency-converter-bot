from aiogram import F, Router
from aiogram.filters import Command

from .help import help_command
from .message_handler import handle_message
from .start import start_command


def register_user_interaction_handlers(router: Router) -> None:
    router.message.register(start_command, Command(commands=["start"]))
    router.message.register(help_command, Command(commands=["help"]))
    router.message.register(handle_message, F.text)
