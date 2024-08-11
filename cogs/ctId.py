import discord
from discord.ext import commands
import aiohttp
from util.error import error_embed
from discord import option

class Tiles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name="tiles",
        description="Get tile data for a specific ctID"
    )
    @option(
        name="ct_id",
        description="The ID of the challenge",
        required=True,
        type=int
    )
    async def tiles(self, ctx, ct_id: int):
        url = f"https://data.ninjakiwi.com/btd6/ct/{ct_id}/tiles"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()

        if not data or not data.get("body"):
            return await ctx.respond(embed=error_embed("No data available for the CtId you entered.."))

        embed = discord.Embed(title="Tile Data", description=f"Here is the tile data for ctID {ct_id}:", color=0x00ff00)

        data = {
            "body": [
                {
                    "id": 1,
                    "x": 0,
                    "y": 0,
                    "type": "GRASS",
                    "path": "PATH"
                },
                {
                    "id": 2,
                    "x": 1,
                    "y": 0,
                    "type": "DIRT",
                    "path": "PATH"
                },
                {
                    "id": 3,
                    "x": 2,
                    "y": 0,
                    "type": "WATER",
                    "path": "PATH"
                },
                {
                    "id": 4,
                    "x": 0,
                    "y": 1,
                    "type": "GRASS",
                    "path": "PATH"
                },
                {
                    "id": 5,
                    "x": 1,
                    "y": 1,
                    "type": "DIRT",
                    "path": "PATH"
                },
                {
                    "id": 6,
                    "x": 2,
                    "y": 1,
                    "type": "WATER",
                    "path": "PATH"
                },

            ]
        }

        tile_list = ""
        for tile in data["body"]:
            tile_list += f"ID: {tile['id']}, X: {tile['x']}, Y: {tile['y']}, Type: {tile['type']}, Path: {tile['path']}\n"

        embed.add_field(name="Tiles", value=tile_list, inline=False)

        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Tiles(bot))

