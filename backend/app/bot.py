import discord
from discord.ext import commands, tasks
from .config import settings

bot = commands.Bot(command_prefix=settings.PREFIX, intents=discord.Intents.all())

def start_discord_bot(app):
    @bot.event
    async def on_ready():
        print(f"Bot connected as {bot.user}")
        announce_task.start()

    @tasks.loop(minutes=10)
    async def announce_task():
        print("Running scheduled announcements")

    app.loop.create_task(bot.start(settings.BOT_TOKEN))
