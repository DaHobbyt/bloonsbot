import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.command_prefix = "!"

        for filename in os.listdir("cogs"):
            if filename.endswith(".py"):
                self.load_extension(f"cogs.{filename[:-3]}")

    async def on_ready(self):
        print(f"Logged in as {self.user.name}")

    def run(self):
        super().run(os.getenv("TOKEN"))
        

bot = commands.Bot(intents=discord.Intents.default())
bot.run()