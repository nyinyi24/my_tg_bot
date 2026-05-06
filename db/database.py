import aiosqlite
import os

# ဖိုင်လမ်းကြောင်းကို main folder ထဲမှာပဲ ရှိအောင် ထားပါသည်
DB_PATH = 'bot_database.db'

async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                credits INTEGER DEFAULT 5
            )
        ''')
        await db.commit()

async def get_user_credits(user_id):
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute('SELECT credits FROM users WHERE user_id = ?', (user_id,)) as cursor:
            row = await cursor.fetchone()
            if row:
                return row[0]
            else:
                await db.execute('INSERT INTO users (user_id, credits) VALUES (?, ?)', (user_id, 5))
                await db.commit()
                return 5

async def deduct_credit(user_id):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('UPDATE users SET credits = credits - 1 WHERE user_id = ? AND credits > 0', (user_id,))
        await db.commit()