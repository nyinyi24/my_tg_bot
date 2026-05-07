# Advanced Telegram AI Contentywriter Bot

ဒီ Bot ဟာ Google Gemini AI ကို အသုံးပြုပြီး Social Media Post Script တွေနဲ့ Channel ကြော်ငြာစာသားတွေကို ရေးသားပေးနိုင်တဲ့ Telegram Bot တစ်ခု ဖြစ်ပါတယ်။ aiogram framework (version 2.x) ကို အသုံးပြုထားပြီး SQLite database နဲ့ Credit စနစ်ကို ထိန်းချုပ်ထားပါတယ်။

## Features

*   **Social Media Content Generation**: Facebook Post, Telegram Ad, TikTok/Reels Script များကို ရေးသားနိုင်ခြင်း။
*   **Tone Selection**: Professional, Friendly, Funny စသည့် Tone များကို ရွေးချယ်နိုင်ခြင်း။
*   **Credit System**: User အသစ်တိုင်းအတွက် အခမဲ့ Credit ၅ ခု ပေးအပ်ပြီး၊ Script တစ်ခါထုတ်တိုင်း Credit ၁ ခု နှုတ်ယူခြင်း။ Credit ကုန်ဆုံးပါက အသိပေးခြင်း။
*   **Myanmar Language Support**: မြန်မာဘာသာစကားဖြင့် အပြန်အလှန်ပြောဆိုနိုင်ခြင်းနှင့် စာသားများ ထုတ်လုပ်ပေးခြင်း။
*   **Prompt Engineering**: Gemini AI အတွက် Social Media Marketing Expert အဖြစ် မြန်မာလို ဆွဲဆောင်မှုရှိသော စာသားများ ထုတ်လုပ်ရန် System Instruction ထည့်သွင်းထားခြင်း။

## Tech Stack

*   **Framework**: `aiogram` (version 2.x)
*   **AI**: `google-generativeai` library (Model: `gemini-1.5-flash`)
*   **Database**: `SQLite` (`aiosqlite`)
*   **Environment Variables**: `python-dotenv`

## Project Structure

```
telegram_ai_copywriter_bot/
├── ai/
│   └── gemini_handler.py         # Gemini AI နှင့် ချိတ်ဆက်ပြီး စာသားထုတ်လုပ်ခြင်း
├── db/
│   └── database.py               # SQLite database နှင့် User Credit စနစ် ထိန်းချုပ်ခြင်း
├── handlers/
│   └── bot_handlers.py           # Telegram Bot Commands နှင့် Callback Query များကို စီမံခန့်ခွဲခြင်း
├── keyboards/
│   └── keyboards.py              # Inline Keyboard Button များ ဖန်တီးခြင်း
├── config.py                     # Environment variables များကို load လုပ်ခြင်း
├── main.py                       # Bot ရဲ့ main entry point
└── .env                          # API Keys များကို သိမ်းဆည်းရန် (ဥပမာ: TELEGRAM_BOT_TOKEN, GEMINI_API_KEY)
└── README.md                     # Project ရှင်းလင်းချက်
```

## Setup and Installation

1.  **Clone the repository (or create the files manually):**

    ```bash
    git clone <repository_url>
    cd telegram_ai_copywriter_bot
    ```

2.  **Create a virtual environment and activate it:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install aiogram==2.x google-generativeai aiosqlite python-dotenv
    ```
    (aiogram version 2.x ကို သုံးရန် သေချာပါစေ။)

4.  **Configure Environment Variables:**

    `.env` ဖိုင်ကို ဖွင့်ပြီး သင့်ရဲ့ Telegram Bot Token နဲ့ Gemini API Key များကို ထည့်သွင်းပါ။

    ```dotenv
    TELEGRAM_BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
    GEMINI_API_KEY=YOUR_GEMINI_API_KEY
    ```

    *   **Telegram Bot Token**: BotFather မှ ရယူပါ။
    *   **Gemini API Key**: Google AI Studio မှ ရယူပါ။

5.  **Run the Bot:**

    ```bash
    python main.py
    ```

## Usage

Bot ကို စတင်ပြီးနောက် `/start` command ကို ပို့လိုက်ပါ။ ထို့နောက် Main Menu မှ လိုအပ်သော လုပ်ဆောင်ချက်များကို ရွေးချယ်ပြီး အသုံးပြုနိုင်ပါသည်။

*   **Facebook Post 📝**: Facebook အတွက် Post ရေးသားရန်။
*   **Telegram Ad 📢**: Telegram Channel ကြော်ငြာ ရေးသားရန်။
*   **TikTok/Reels Script 🎬**: TikTok/Reels အတွက် Script ရေးသားရန်။
*   **Check Credits 💰**: လက်ကျန် Credit များကို စစ်ဆေးရန်။

## Contact

မေးမြန်းစရာများ သို့မဟုတ် အကြံပြုချက်များရှိပါက [သင့်အီးမေးလ် သို့မဟုတ် Telegram Username] သို့ ဆက်သွယ်နိုင်ပါသည်။
