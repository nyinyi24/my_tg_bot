import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from config import TELEGRAM_BOT_TOKEN
from handlers.bot_handlers import register_handlers
from db.database import init_db

async def set_main_menu(bot: Bot):
    # ဘယ်ဘက်အောက်ခြေက Menu Button အတွက် commands များ
    main_menu_commands = [
        BotCommand(command="/start", description="Bot ကိုပြန်စတင်ရန်"),
        BotCommand(command="/help", description="အကူအညီရယူရန်"),
    ]
    await bot.set_my_commands(main_menu_commands)

async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    dp = Dispatcher()

    await init_db()
    register_handlers(dp)
    
    # Menu Button သတ်မှတ်ခြင်း
    await set_main_menu(bot)

    print("Bot is running...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())