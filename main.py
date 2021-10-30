import discord
from discord.ext import commands
import music
import os

cogs = [music]
client = commands.Bot(command_prefix="!", Intents=discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
