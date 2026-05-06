from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_main_menu():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="Facebook Post 📝", callback_data="type_facebook"))
    builder.row(InlineKeyboardButton(text="Telegram Ad 📢", callback_data="type_telegram"))
    builder.row(InlineKeyboardButton(text="TikTok/Reels Script 🎬", callback_data="type_tiktok"))
    builder.row(InlineKeyboardButton(text="Check Credits 💰", callback_data="check_credits"))
    return builder.as_markup()

def get_tone_menu():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="Professional (လုပ်ငန်းသုံး)", callback_data="tone_professional"))
    builder.row(InlineKeyboardButton(text="Friendly (ရင်းနှီးသော)", callback_data="tone_friendly"))
    builder.row(InlineKeyboardButton(text="Funny (ဟာသနှောသော)", callback_data="tone_funny"))
    return builder.as_markup()