import openai
import os
from dotenv import load_dotenv

load_dotenv()

# Agent Router ရဲ့ Configuration
client = openai.OpenAI(
    base_url="https://agentrouter.org/v1", 
    api_key=os.getenv("GEMINI_API_KEY") 
)

# ဒီမှာ argument (၃) ခု ဖြစ်အောင် history ကိုပါ ထည့်ပေးလိုက်ပါပြီ
async def generate_content(prompt, tone, history=None):
    try:
        response = client.chat.completions.create(
            model="deepseek-v3", 
            messages=[
                {"role": "system", "content": f"မင်္ဂလာပါ။ သင်သည် ကျွမ်းကျင်သော Content Writer တစ်ဦးဖြစ်သည်။ စာသားများကို {tone} tone ဖြင့် ရေးသားပေးပါ။"},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error: {e}")
        return "ခေတ္တစောင့်ဆိုင်းပေးပါ။ AI နှင့် ချိတ်ဆက်ရာတွင် အခက်အခဲရှိနေပါသည်။"