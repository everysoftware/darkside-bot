import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from src.config import conf
from src.payments.handlers import router as payment_router
from src.users.handlers import router as user_router

routers = [user_router, payment_router]
dp = Dispatcher()
dp.include_routers(*routers)
bot = Bot(conf.bot_token, default=DefaultBotProperties(parse_mode="HTML"))

if __name__ == "__main__":
    # Включаем логирование.
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    # Запускаем поток.
    try:
        asyncio.run(dp.start_polling(bot))
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot stopped")
