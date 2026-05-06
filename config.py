import os
from dotenv import load_dotenv

# .env file ကို လှမ်းဖတ်သည်
# အရင်က: load_dotenv()
# အခုလို ပြင်ပါ:
load_dotenv(override=True)

# Token ကို ဆွဲထုတ်သည်
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# စစ်ဆေးရန် (Terminal မှာ ပေါ်လာပါလိမ့်မည်)
if not TELEGRAM_BOT_TOKEN:
    print("❌ Error: Telegram Bot Token မတွေ့ပါ။ .env file ကို စစ်ဆေးပါ။")