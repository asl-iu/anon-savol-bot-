from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging
import os

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler()
async def handle_message(message: types.Message):
    user = message.from_user
    text = f"✉️ *Yangi anonim xabar!*\n\n👤 Ismi: @{user.username or 'No username'}\n🆔 ID: {user.id}\n\n💬 Xabar:\n{message.text}"
    await bot.send_message(ADMIN_ID, text, parse_mode="Markdown")
    await message.answer("✅ Xabaringiz anonim tarzda yuborildi!")

if __name__ == "__main__":
    executor.start_polling(dp)
