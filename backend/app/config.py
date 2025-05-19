from pydantic import BaseSettings

class Settings(BaseSettings):
    BOT_TOKEN: str
    PREFIX: str = "!"
    DATABASE_URL: str = "sqlite:///./test.db"
    DISCORD_CLIENT_ID: str
    DISCORD_CLIENT_SECRET: str

settings = Settings()
