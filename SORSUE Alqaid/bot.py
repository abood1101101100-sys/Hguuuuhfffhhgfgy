import os
import sys
from pyrogram import Client, idle
from pyromod import listen
from casery import caes, casery, group, source, photosource, caserid, ch, bot_token, bot_token2

# تغيير مجلد العمل لمجلد البوت
sys.path.insert(0, os.path.dirname(__file__))
os.chdir(os.path.dirname(os.path.abspath(__file__)))

bot = Client("CAR", api_id=15646135, api_hash="b38142278f5181e0815bf7122478dc31", bot_token=bot_token, plugins=dict(root="CASER"))
lolo = Client("hossam", api_id=15646135, api_hash="b38142278f5181e0815bf7122478dc31", session_string=bot_token2)    

DEVS = caes
DEVSs = []
bot_id = bot.bot_token.split(":")[0]

async def start_zombiebot():
    print("تم تشغيل الصانع بنجاح..💗")
    await bot.start()
    await lolo.start()
    try:
      await bot.send_message(casery, "**تم تشغيل الصانع بنجاح..💗**")
    except:
      pass
    await idle()
