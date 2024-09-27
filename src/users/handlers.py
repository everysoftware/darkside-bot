from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

import src.users.keyboards as user_kb
from src.users import constants as constants

router = Router()


@router.message(Command("start"))
async def start(msg: Message) -> None:
    await msg.answer(constants.WELCOME_MSG, reply_markup=user_kb.reply_main_kb)


@router.message(Command("author"))
@router.message(F.text == "Автор бота")
async def author(msg: Message) -> None:
    await msg.answer(constants.AUTHOR_MSG)
