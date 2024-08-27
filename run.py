import asyncio
import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from app.handlers import router_handlers

load_dotenv()


async def main():
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()
    dp.include_router(router_handlers)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        print('БОТ ЗАПУЩЕН')
        asyncio.run(main())

    except KeyboardInterrupt:
        print('БОТ ВЫКЛЮЧЕН')
