import discord
from discord.ext import commands
import aiohttp
from discord import option

from util.error import error_embed

class Leaderboard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name="leaderboard",
        description="Get the leaderboard data for a BTD6 challenge"
    )
    @option(
        name="ctid",
        description="The ID of the challenge",
        required=True,
        type=int
    )
    @option(
        name="type",
        description="The type of leaderboard to get (player or team)",
        required=True,
        choices=["player", "team"]
    )
    async def leaderboard(self, ctx, ctid: int, type: str):
        if type not in ["player", "team"]:
            return await ctx.respond(embed=error_embed("Invalid type. Must be 'player' or 'team'."))
        
        url = f"https://data.ninjakiwi.com/btd6/ct/{ctid}/leaderboard/{type}"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()

        if not data or not data.get("body"):
            return await ctx.respond(embed=error_embed("No data available for the ID you entered.."))
        embed = discord.Embed(title=f"{type.capitalize()} Leaderboard Data", description=f"Here is the {type} leaderboard data:", color=0x00ff00)
        for entry in data["body"]:
            if type == "player":
                embed.add_field(name=entry["name"], value=f"**Rank:** {entry['rank']}\n**Score:** {entry['score']}", inline=False)
            elif type == "team":
                embed.add_field(name=entry["name"], value=f"**Rank:** {entry['rank']}\n**Score:** {entry['score']}\n**Members:** {', '.join(entry['members'])}", inline=False)
        embed.set_footer(text="Made with <3 by DaHobby")
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Leaderboard(bot))