from fastapi import FastAPI
from .api import router as api_router
from .bot import start_discord_bot
from .scheduler import init_scheduler

app = FastAPI()
app.include_router(api_router, prefix="/api")

@app.on_event("startup")
async def startup_event():
    init_scheduler(app)
    start_discord_bot(app)
