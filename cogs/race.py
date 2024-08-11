import discord
from discord.ext import commands
import aiohttp

class Race(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name="race",
        description="Get race data"
    )
    async def race(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://data.ninjakiwi.com/btd6/races") as response:
                data = await response.json()
                if not data or not data.get("body"):
                    await ctx.respond("Error: No data available")
                    return
                embed = discord.Embed(title="Race Data", description="Here is some funny data!", color=0x00ff00)
                for race in data["body"]:
                    start_time = f"<t:{race['start'] // 1000}:F>"
                    end_time = f"<t:{race['end'] // 1000}:F>"
                    embed.add_field(name=race["name"], value=f"**Start Time:** {start_time}\n**End Time:** {end_time}\n**Total Scores:** {race['totalScores']}", inline=False)
                    embed.set_footer(text="Made with <3 by DaHobby")
                await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Race(bot))