from fastapi import APIRouter, Depends, Request, HTTPException
from fastapi.responses import RedirectResponse
from jose import JWTError, jwt
from urllib.parse import urlencode
from .config import settings
from .database import get_db
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

discord_oauth_url = "https://discord.com/api/oauth2/authorize"

def create_discord_oauth_redirect():
    params = {
        "client_id": settings.DISCORD_CLIENT_ID,
        "redirect_uri": settings.OAUTH_CALLBACK_URL,
        "response_type": "code",
        "scope": "identify guilds",
    }
    return f"{discord_oauth_url}?{urlencode(params)}"

@router.get("/login")
async def login():
    return RedirectResponse(create_discord_oauth_redirect())

@router.get("/callback")
async def callback(code: str, request: Request, db: AsyncSession = Depends(get_db)):
    # Exchange code for access token
    # TODO: implement HTTP request to Discord token endpoint
    # TODO: fetch user info, store in DB, create JWT cookie
    # For now, redirect to frontend
    return RedirectResponse(url=settings.FRONTEND_URL)
```\n- `models/`: SQLAlchemy модели.
  - `models/user.py`:
    ```python
