import discord
from discord.ext import commands
import music

cogs = [music]
client = commands.Bot(command_prefix="!", Intents=discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)

client.run('OTA0MDQ4Nzk1MTIwMTk3NjYy.YX13DQ.flgx0lbyhRfvGZbHvK1N-k5ftuI')