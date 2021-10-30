import discord
from discord.ext import commands
import music
import os

cogs = [music]
client = commands.Bot(command_prefix="!", Intents=discord.Intents.all())

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("!help "))

for i in range(len(cogs)):
    cogs[i].setup(client)

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
