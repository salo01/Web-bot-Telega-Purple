from pydantic import BaseSettings, Field, AnyUrl

class Settings(BaseSettings):
    # Project
    PROJECT_NAME: str = "Multifunction Discord Bot"
    VERSION: str = "0.1.0"

    # Server
    HOST: str = Field("0.0.0.0", env="HOST")
    PORT: int = Field(8000, env="PORT")

    # Database
    DATABASE_URL: AnyUrl = Field(..., env="DATABASE_URL")  # e.g. sqlite+aiosqlite:///./db.sqlite3

    # Discord OAuth2
    DISCORD_CLIENT_ID: str = Field(..., env="DISCORD_CLIENT_ID")
    DISCORD_CLIENT_SECRET: str = Field(..., env="DISCORD_CLIENT_SECRET")
    OAUTH_CALLBACK_URL: AnyUrl = Field(..., env="OAUTH_CALLBACK_URL")
    DISCORD_BOT_TOKEN: str = Field(..., env="DISCORD_BOT_TOKEN")

    # Telegram
    TELEGRAM_TOKEN: str = Field("", env="TELEGRAM_TOKEN")

    # Scheduler
    SCHEDULER_INTERVAL_MINUTES: int = Field(10, env="SCHEDULER_INTERVAL_MINUTES")

    # OAuth cookie
    SECRET_KEY: str = Field(..., env="SECRET_KEY")
    ALGORITHM: str = Field("HS256", env="ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(60 * 24, env="ACCESS_TOKEN_EXPIRE_MINUTES")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
```\n- `database.py`: SQLAlchemy async engine, session and Base model.
```python
