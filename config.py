from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("APP_ID", "9661697")
APP_HASH = os.environ.get("APP_HASH", "4ae76784fdfecd5df142004955bb8393")
SESSION = os.environ.get("SESSION")
SaiKo = TelegramClient(StringSession(SESSION), APP_ID, APP_HASH)
SaiKo.start()
