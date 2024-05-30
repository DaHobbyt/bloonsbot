import discord
from discord.ext import commands
import aiohttp
import json

class ViewRace(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="viewrace", description="Get race metadata")
    async def race_metadata(self, ctx, race_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://data.ninjakiwi.com/btd6/races/{race_id}/metadata") as response:
                data = await response.json()
                if not data or not data.get("body"):
                    await ctx.respond("No valid race id")
                    return
                embed = discord.Embed(title="Race Metadata", description="Here is the race metadata:", color=0x00ff00)
                embed.add_field(name="Name", value=data["body"]["name"], inline=False)
                embed.add_field(name="Description", value=data["body"]["description"], inline=False)
                embed.add_field(name="Track", value=data["body"]["track"], inline=False)
                embed.add_field(name="Mode", value=data["body"]["mode"], inline=False)
                embed.add_field(name="Difficulty", value=data["body"]["difficulty"], inline=False)
                embed.set_footer(text="Made with <3 by DaHobby")
                await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(ViewRace(bot))