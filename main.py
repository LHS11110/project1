import discord
from discord.ext import commands
import music

cogs = [music]
client = commands.Bot(command_prefix="!", Intents=discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)

client.run('봇 토큰')
