    from fastapi import APIRouter, Depends, HTTPException
    from sqlalchemy.ext.asyncio import AsyncSession
    from ..database import get_db
    from ..models.template import Template
    from ..schemas.template import TemplateCreate, TemplateRead

    router = APIRouter(prefix="/templates", tags=["Templates"])

    @router.post("/", response_model=TemplateRead)
    async def create_template(
        tpl_in: TemplateCreate,
        db: AsyncSession = Depends(get_db)
    ):
        """Создать новый шаблон"""
        tpl = Template(**tpl_in.dict())
        db.add(tpl)
        await db.commit()
        await db.refresh(tpl)
        return tpl

    @router.get("/{tpl_id}", response_model=TemplateRead)
    async def get_template(tpl_id: str, db: AsyncSession = Depends(get_db)):
        """Получить шаблон по ID"""
        tpl = await db.get(Template, tpl_id)
        if not tpl:
            raise HTTPException(status_code=404, detail="Шаблон не найден")
        return tpl
    ```\n- `services/`: business logic — schedule tasks with APScheduler, backup, stats logging.\n- `purple/`: modules using `pygetwindow`, `pywinauto`, `pyautogui`, `pytesseract` to detect and automate Purple NSsoft chat.\n- `telegram/`: wrappers around `aiogram` or `python-telegram-bot`.\n\n**2. Bot (Nextcord)**\n- `bot.py`: loads `cogs`, starts event loop, links with backend scheduler.\n- `cogs/`: include `notifications.py`, `roles.py`, `media_messages.py`, `music.py`, `stats.py`, `multi_server.py`, etc.\n- `scheduler.py`: configures APScheduler Cron/Interval jobs to check and dispatch notifications.\n- `audio/`: integration via `yt-dlp`, `ffmpeg`, `lavalink` or Python wrapper.\n\n**3. Frontend (React + Tailwind)**\n- Use `Vite` for fast dev.\n- `App.jsx`: top-level router, auth guard, theme switcher.\n- `services/auth.js`: handles Discord OAuth2 redirect, token storage.\n- `components/`: Cards, Tables, Forms for CRUD on events, templates, servers.\n- Multi-theme support via CSS variables and Tailwind config.\n\n**4. Environment & Deployment**\n- `.env.example`: `DISCORD_TOKEN`, `DISCORD_CLIENT_ID`, `DISCORD_CLIENT_SECRET`, `DATABASE_URL`, `FRONTEND_URL`, `TELEGRAM_TOKEN`, `OAUTH_CALLBACK` etc.\n- `docker-compose.yml`: optional: PostgreSQL, backend, frontend, bot as separate services.\n\n**Next Steps**\n1. Initialize Git repository and `README.md`.\n2. Create Python virtual environment and install `FastAPI`, `uvicorn`, `SQLAlchemy`, `APScheduler`, `nextcord`, `pywinauto`, `pygetwindow`, `pyautogui`, `pytesseract`, `python-telegram-bot`, etc.\n3. Scaffold React app via `npm create vite@latest frontend --template react`.\n4. Implement OAuth2 flow in `backend/auth.py` and frontend login.\n5. Wire up Discord bot to backend scheduler and database.\n6. Build Purple automation scripts and test on Windows.\n7. Add UI pages for managing notifications, templates, servers.\n8. Test Telegram integration.\n9. Polish documentation and add CI/CD pipelines.\n\n*Feel free to request specific modules or starter code for any piece.*
