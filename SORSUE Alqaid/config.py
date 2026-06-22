import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()

# ====== إعدادات البوت ======
BOT_TOKEN = getenv("BOT_TOKEN", "")
SESSION_STRING = getenv("SESSION_STRING", "")

# ====== إعدادات المطور ======
admins = getenv("ADMINS", "div_victor").split()
dev = getenv("DEV", "div_victor")
dev_id = int(getenv("DEV_ID", "6906453300"))

# ====== قناة وجروب السورس ======
source = getenv("SOURCE", "https://t.me/CORANBM")
ch = getenv("CH", "CORANBM")
group = getenv("GROUP", "https://t.me/YA_HYA3")
photosource = getenv("PHOTO_SOURCE", "https://t.me/mkptkm/14")

# ====== إعدادات الاشتراك الإجباري ======
user = getenv("FORCE_SUB", "")
helper = getenv("HELPER", "")

# ====== إعدادات المكالمات ======
call = getenv("CALL_GROUP", "")
appp = getenv("APP", "")

# ====== اللوغر ======
logger = getenv("LOGGER", "")
logger_mode = getenv("LOGGER_MODE", "false").lower() == "true"

# ====== اسم البوت ======
botname = getenv("BOT_NAME", "SORSUE")
