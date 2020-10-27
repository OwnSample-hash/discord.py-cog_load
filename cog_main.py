import discord
from discord.ext import commands
from discord.ext.commands import Bot

from test import Test
from fun import Fun

bot = commands.Bot(command_prefix=".")

@bot.event
async def on_ready():
    print("Logged in")

cogs = ["Test", "Fun"] # Ide kerüljenek a class nevek
def add_cogs():
    for cog in cogs:
        eval(f"bot.add_cog({cog}(bot))")

add_cogs()
bot.run("")
