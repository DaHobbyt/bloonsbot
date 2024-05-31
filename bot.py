import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="/", intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

bot.load_extension("cogs.race")
bot.load_extension("cogs.boss")
bot.load_extension("cogs.viewrace")
bot.load_extension("cogs.challange")
bot.load_extension("cogs.ct")
bot.load_extension("cogs.ctId")
bot.load_extension("cogs.leaderboard")

bot.run("")