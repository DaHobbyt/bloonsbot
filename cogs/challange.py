import discord
from discord.ext import commands
import aiohttp
import json

class Challenge(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="challenge", description="Get challenge data")
    async def challenge(self, ctx, challenge_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://data.ninjakiwi.com/btd6/challenges/challenge/{challenge_id}") as response:
                data = await response.json()
                if not data or not data.get("body"):
                    await ctx.respond("Error: No data available")
                    return
                embed = discord.Embed(title="Challenge Data", description="Here is the challenge data:", color=0x00ff00)
                embed.add_field(name="Name", value=data["body"]["name"], inline=False)
                embed.add_field(name="Description", value=data["body"]["description"], inline=False)
                embed.add_field(name="Image", value=data["body"]["image"], inline=False)
                embed.add_field(name="Difficulty", value=data["body"]["difficulty"], inline=False)
                embed.add_field(name="Rewards", value=data["body"]["rewards"], inline=False)
                embed.set_footer(text="Made with <3 by DaHobby")
                await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Challenge(bot))