#ALONE CODER
from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.API_ID = int(getenv("API_ID", "17596251"))
        self.API_HASH = getenv("API_HASH", "e58343b4c0193e293e391daf97603fcd")

        self.BOT_TOKEN = getenv("BOT_TOKEN", "Apna Bot Token")
        self.MONGO_URL = getenv("MONGO_URL", "Apna Mongo Db Dalo")

        self.LOGGER_ID = int(getenv("LOGGER_ID", "Apna Log Group Id Dalo"))
        self.OWNER_ID = int(getenv("OWNER_ID", "Owner I'd dalo"))
        
        self.SESSION1 = getenv("SESSION", "Apna String Dalo")
        self.SESSION2 = getenv("SESSION2", None)
        self.SESSION3 = getenv("SESSION3", None)

        self.SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/shona_bots")
        self.SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/shona_support")

        self.AUTO_END: bool = getenv("AUTO_END", False)
        self.AUTO_LEAVE: bool = getenv("AUTO_LEAVE", False)
        self.VIDEO_PLAY: bool = getenv("VIDEO_PLAY", True)

        self.QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", "200"))
        self.DURATION_LIMIT = int(getenv("DURATION_LIMIT", "5400"))
        self.PLAYLIST_LIMIT = int(getenv("PLAYLIST_LIMIT", "200"))
        self.COOKIES_URL = [
            url for url in getenv("COOKIES_URL", "").split(" ")
            if url and "batbin.me" in url
        ]
        self.DEFAULT_THUMB = getenv("DEFAULT_THUMB", "https://silabotov.ru/img/5846a037-85b8-455c-9dbe-3d6f9bd3508c.jpg")
        self.PING_IMG = getenv("PING_IMG", "https://silabotov.ru/img/5846a037-85b8-455c-9dbe-3d6f9bd3508c.jpg")
        self.START_IMG = getenv("START_IMG", "https://silabotov.ru/img/5846a037-85b8-455c-9dbe-3d6f9bd3508c.jpg")

    def check(self):
        missing = [
            var
            for var in ["API_ID", "API_HASH", "BOT_TOKEN", "MONGO_URL", "LOGGER_ID", "OWNER_ID", "SESSION1"]
            if not getattr(self, var)
        ]
        if missing:
            raise SystemExit(f"Missing required environment variables: {', '.join(missing)}")
