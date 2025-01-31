# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "17995671"))
API_HASH = getenv("API_HASH", "37adac03f1c113a3126b1f9eea32aff4")
BOT_TOKEN = getenv("BOT_TOKEN", "7225784537:AAGExU7BN3nlNYe2BUVM7S08XRO_IpZiR-c")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7320838935").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://moviee3shub:OPQwRulV6Y8IUTB0@cluster0.zm9ak.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")LOG_GROUP = getenv("LOG_GROUP", "https://t.me/+NY4qkOlNZS1lMzQ9")
LOG_GROUP = getenv("LOG_GROUP", "https://t.me/+_pdU8rH7ojA0ODdl")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002288683572"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "")
AD_API = getenv("AD_API", "")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", None)
