
import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import config
from handlers import start, order
from database import init_db

init_db()

async def main() -> None:
    logging.basicConfig(level=logging.INFO)

    if not config.BOT_TOKEN:
        raise ValueError("BOT_TOKEN not found in environment variables")

    bot = Bot(token=config.BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(order.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())