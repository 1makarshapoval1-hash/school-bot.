import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils.executor import start_webhook

BOT_TOKEN = os.getenv("BOT_TOKEN")

WEBHOOK_HOST = os.getenv("WEBHOOK_URL")  # URL Railway
WEBHOOK_PATH = f"/webhook/{BOT_TOKEN}"
WEBHOOK_URL = WEBHOOK_HOST + WEBHOOK_PATH

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=["start"])
async def start(message: Message):
    await message.answer("Привет 👋 Я помогу решить задачу! Пришли фото или текст задания.")

# Обработчик фото
@dp.message_handler(content_types=["photo"])
async def handle_photo(message: types.Message):
    await message.answer("Фото получил 📷. В MVP пока просто сохраняю. В будущем здесь будет решение.")

async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)

async def on_shutdown(dp):
    await bot.delete_webhook()

if __name__ == "__main__":
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host="0.0.0.0",
        port=int(os.getenv("PORT", 5000)),
    )
