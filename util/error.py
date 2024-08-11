import discord

def error_embed(description):
    embed = discord.Embed(description=description, color=discord.Color.red(), title="An error occurred")
    embed.set_footer(text="Made with <3 by DaHobby")
    return embed
