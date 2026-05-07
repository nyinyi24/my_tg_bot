import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

SYSTEM_INSTRUCTION = (
    "မင်းက မြန်မာဘာသာစကား ကျွမ်းကျင်တဲ့ Social Media Marketing Expert တစ်ယောက်ဖြစ်တယ်။ "
    "စာသားတွေကို ဆွဲဆောင်မှုရှိအောင်၊ Emoji လေးတွေပါအောင်၊ Hook, Body နဲ့ Call to Action (CTA) ပါဝင်အောင် ရေးပေးပါ။ "
    "မြန်မာလိုပဲ ပြန်ဖြေပေးပါ။"
)

async def generate_content(prompt_text, content_type, tone):
    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash-lite", 
        system_instruction=SYSTEM_INSTRUCTION
    )
    
    full_prompt = f"Content Type: {content_type}\nTone: {tone}\nTopic: {prompt_text}\n\nအထက်ပါ အကြောင်းအရာအတွက် ဆွဲဆောင်မှုရှိသော စာသားကို ရေးပေးပါ။"
    
    response = model.generate_content(full_prompt)
    return response.text