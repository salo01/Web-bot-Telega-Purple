from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from fastapi import FastAPI

def init_scheduler(app: FastAPI):
    scheduler = AsyncIOScheduler()
    scheduler.add_job(lambda: print("Heartbeat"), CronTrigger(minute='*/10'))
    scheduler.start()
