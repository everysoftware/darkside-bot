import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher

from src.config import Config
from src.services.sql import Database

db = Database('products.db')
dp = Dispatcher()
bot = Bot(Config.token, parse_mode='HTML')


async def main() -> None:
    from handlers import dp
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    # Включаем логирование.
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    # Запускаем поток.
    asyncio.run(main())
