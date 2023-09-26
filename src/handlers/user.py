from aiogram.types import Message
from aiogram.filters import Command
from aiogram import F

from src.app import dp
import src.keyboards.user as user_kb
from src.messages.user import MESSAGES


@dp.message(Command('start'))
async def start(msg: Message) -> None:
    await msg.answer(MESSAGES.get('welcome'),
                     reply_markup=user_kb.main)


@dp.message(Command('author'))
@dp.message(F.text == 'Автор бота')
async def author(msg: Message) -> None:
    await msg.answer(MESSAGES.get('author'))
