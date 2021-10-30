import discord
from discord.ext import commands
from discord.ext.commands.core import command
from discord.player import FFmpegAudio, FFmpegPCMAudio
import youtube_dl

class music(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("음성 채널에 입장해주세요!")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

    @commands.command()
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def play(self, ctx, url):
        FFMPEG_OPTIONS = {'before_options' : '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options' : '-vn'}
        YDL_OPTIONS = {'format':'bestaudio'}
        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            URL = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(URL, **FFMPEG_OPTIONS)
            vc.play(source)

    @commands.command()
    async def pause(self, ctx):
        await ctx.voice_client.pause() 
        await ctx.send("일시중단")

    @commands.command()
    async def resume(self, ctx):
        await ctx.voice_client.resume() 
        await ctx.send("재생")

def setup(client):
    client.add_cog(music(client))