
import asyncio
from datetime import datetime
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ContentType
import logging
import config


bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

async def send_image_to_group():
    group_id = -1002103917974
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
    if current_time in ("2024-03-10 20:20"):
        with open("test.jpg", "rb") as photo:
            await bot.send_photo(chat_id=group_id, photo=photo, caption="sotib olasan karoch")
        logging.info("Rasmlar yuborildi.")

async def scheduled(wait_for):
    while True:
        await asyncio.sleep(wait_for)
        await send_image_to_group()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    loop = asyncio.get_event_loop()
    loop.create_task(scheduled(60))
    loop.run_forever()