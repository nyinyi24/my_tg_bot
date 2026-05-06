from aiogram import Dispatcher, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from db.database import get_user_credits, deduct_credit
from ai.gemini_handler import generate_content
from keyboards.keyboards import get_main_menu, get_tone_menu

# Admin User ID
ADMIN_USER_ID = 7656340616

class BotStates(StatesGroup):
    waiting_for_topic = State()
    waiting_for_tone = State()

async def cmd_start(message: types.Message, state: FSMContext):
    await state.clear()
    user_name = message.from_user.full_name
    welcome_text = (
        f"မင်္ဂလာပါ {user_name}! 🙏\n\n"
        "ကျွန်တော်ကတော့ Advanced Contentwriter Bot ဖြစ်ပါတယ်။\n"
        "သင့်အတွက် Facebook Post၊ Telegram Ad နဲ့ Video Script တွေကို မြန်မာလို အကောင်းဆုံး ရေးသားပေးနိုင်ပါတယ်။"
    )
    await message.answer(welcome_text, reply_markup=get_main_menu())

# Help Command အတွက် Function
async def cmd_help(message: types.Message):
    help_text = (
        "📖 **Bot အသုံးပြုနည်း လမ်းညွှန်**\n\n"
        "၁။ `/start` ကိုနှိပ်ပြီး မိမိရေးသားချင်သော Content အမျိုးအစားကို ရွေးချယ်ပါ။\n"
        "၂။ AI ကို ရေးသားစေလိုသော အကြောင်းအရာ (Topic) ကို ပေးပို့ပါ။\n"
        "၃။ စာသား၏ အမူအရာ (Tone) ကို ရွေးချယ်ပေးပါ။\n"
        "၄။ ခဏစောင့်ဆိုင်းပြီးနောက် AI မှ ရေးသားပေးသော စာသားကို ရရှိပါမည်။\n\n"
        "💡 **သိကောင်းစရာများ**\n"
        "• Script တစ်ခါထုတ်လျှင် Credit (၁) ခု ကုန်ဆုံးပါမည်။\n"
        "• အခမဲ့ Credit ကုန်ဆုံးပါက Admin ထံတွင် ထပ်မံဝယ်ယူနိုင်ပါသည်။\n\n"
        "🆘 အကူအညီလိုအပ်ပါက - @independence_N"
    )
    await message.answer(help_text)

async def check_credits_callback(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    credits = await get_user_credits(user_id)
    if user_id == ADMIN_USER_ID:
        await callback_query.message.answer("💰 Admin: Unlimited Credits")
    else:
        await callback_query.message.answer(f"💰 သင့်ရဲ့ လက်ကျန် Credit: {credits} ခု")
    await callback_query.answer()

async def select_type_callback(callback_query: types.CallbackQuery, state: FSMContext):
    content_type = callback_query.data.split("_")[1]
    await state.update_data(content_type=content_type)
    user_id = callback_query.from_user.id
    credits = await get_user_credits(user_id)
    
    if user_id != ADMIN_USER_ID and credits <= 0:
        await callback_query.message.answer("⚠️ Credit မလုံလောက်တော့ပါ။ Admin @independence_N ကို ဆက်သွယ်ပါ။")
        return await callback_query.answer()

    await callback_query.message.answer("ဘယ်အကြောင်းအရာအတွက် ရေးပေးရမလဲ? (ဥပမာ - ကော်ဖီဆိုင် ကြော်ငြာ)")
    await state.set_state(BotStates.waiting_for_topic)
    await callback_query.answer()

async def process_topic(message: types.Message, state: FSMContext):
    await state.update_data(topic=message.text)
    await message.answer("ဘယ်လိုပုံစံ (Tone) နဲ့ ရေးပေးရမလဲ ရွေးချယ်ပေးပါ။", reply_markup=get_tone_menu())
    await state.set_state(BotStates.waiting_for_tone)

async def process_tone_callback(callback_query: types.CallbackQuery, state: FSMContext):
    tone = callback_query.data.split("_")[1]
    user_data = await state.get_data()
    topic, content_type = user_data.get('topic'), user_data.get('content_type')
    user_id = callback_query.from_user.id
    
    processing_msg = await callback_query.message.answer("⏳ AI က စာသားများကို ရေးသားနေပါတယ်။ ခဏစောင့်ပေးပါ...")
    
    try:
        generated_text = await generate_content(topic, content_type, tone)
        if user_id == ADMIN_USER_ID:
            new_credits = "Unlimited (Admin)"
        else:
            await deduct_credit(user_id)
            new_credits = f"{await get_user_credits(user_id)} ခု"
        
        response_text = (
            f"✨ **သင့်အတွက် ရေးသားပေးထားသော စာသား:**\n\n{generated_text}\n\n"
            f"💰 လက်ကျန် Credit: {new_credits}\n"
            f"━━━━━━━━━━━━━━━\n"
            f"🆘 အကူအညီလိုအပ်ပါက သို့မဟုတ် Credit ဝယ်ယူရန် - @independence_N"
        )
        await callback_query.message.answer(response_text)
        await processing_msg.delete()
    except Exception as e:
        await callback_query.message.answer(f"❌ Error: {str(e)}")
    
    await state.clear()
    await callback_query.answer()

def register_handlers(dp: Dispatcher):
    dp.message.register(cmd_start, Command("start"))
    dp.message.register(cmd_help, Command("help")) # Help Command အသစ်
    dp.callback_query.register(check_credits_callback, F.data == "check_credits")
    dp.callback_query.register(select_type_callback, F.data.startswith("type_"))
    dp.message.register(process_topic, BotStates.waiting_for_topic)
    dp.callback_query.register(process_tone_callback, F.data.startswith("tone_"), BotStates.waiting_for_tone)