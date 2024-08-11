import discord
from discord.ext import commands
import aiohttp
from datetime import datetime
from util.error import error_embed

class CT(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name="ct",
        description="Get CT data"
    )
    async def ct(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://data.ninjakiwi.com/btd6/ct") as response:
                data = await response.json()

        if not data:
            return await ctx.respond(embed=error_embed("No data available.."))
        
        embeds = []
        for i, event in enumerate(data["body"], start=1):
            start_datetime = datetime.fromtimestamp(event['start'] / 1000)
            end_datetime = datetime.fromtimestamp(event['end'] / 1000)
            if len(embeds) == 25:
                embeds.append(discord.Embed(title="CT Data (continued)", description="", color=0x00ff00))
            if not embeds:
                embed = discord.Embed(title="CT Data", description="Here is the CT data:", color=0x00ff00)
            else:
                embed = embeds[-1]
            embed.add_field(name=f"Event {i} ID", value=event['id'], inline=False)
            embed.add_field(name="Start", value=start_datetime.strftime("%Y-%m-%d %H:%M:%S"), inline=False)
            embed.add_field(name="End", value=end_datetime.strftime("%Y-%m-%d %H:%M:%S"), inline=False)
            embed.add_field(name="Player", value=event['totalScores_player'], inline=False)
            embed.add_field(name="Team", value=event['totalScores_team'], inline=False)
            embed.add_field(name="Tiles", value=event['tiles'], inline=False)
            embed.add_field(name="Player LB", value=event['leaderboard_player'], inline=False)
            embed.add_field(name="Team LB", value=event['leaderboard_team'], inline=False)
            embed.set_footer(text="Made with <3 by DaHobby")
            if not embeds:
                await ctx.respond(embed=embed)
                embeds.append(embed)

        if embeds:
            await ctx.respond(embed=embeds[-1])

def setup(bot):
    bot.add_cog(CT(bot))