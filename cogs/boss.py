import discord
from discord.ext import commands
import aiohttp
import json

class Boss(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="boss", description="Get boss data")
    async def boss(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://data.ninjakiwi.com/btd6/bosses") as response:
                data = await response.json()
                if not data or not data.get("body"):
                    await ctx.respond("Error: No data available")
                    return
                embed = discord.Embed(title="Boss Data", description="Here is the boss data:", color=0x00ff00)
                for boss in data["body"]:
                    start_time = f"<t:{boss['start'] // 1000}:F>"
                    end_time = f"<t:{boss['end'] // 1000}:F>"
                    embed.add_field(name=boss["name"], value=f"**Start Time:** {start_time}\n**End Time:** {end_time}\n**Total Scores Standard:** {boss['totalScores_standard']}\n**Total Scores Elite:** {boss['totalScores_elite']}", inline=False)
                    embed.set_footer(text="Made with <3 by DaHobby")
                await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Boss(bot))