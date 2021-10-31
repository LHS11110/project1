import discord, datetime, pytz, chromedriver_autoinstaller, bs4, youtube_dl
from discord import client, FFmpegPCMAudio
from discord.ext import commands
from discord.ext.commands.core import command
from selenium import webdriver
from youtube_dl import YoutubeDL
import re
p = re.compile('^(https?://)[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+/[a-zA-Z0-9-_/.?=]*')

class music(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.channel_id = None

    @commands.command()
    async def 도움말(slef, ctx):
        embed = discord.Embed(title="내스 Bot", description="심심해서 만든 봇",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x9d00e9)

        embed.add_field(name="!help", value="명령어 목록과 봇에 대한 설명을 보여줍니다.", inline=False)
        embed.add_field(name="!hello", value="예의바른 봇임을 증명하는 명령어입니다.", inline=False)
        embed.add_field(name="!ms", value="해당 채널을 음악채널로 지정합니다.", inline=True)
        embed.add_field(name="음악 재생", value="지정된 채널에 유튜브 URL을 입력하면 해당 음악을 재생합니다.", inline=True)

        embed.set_footer(text="Bot Made by. LHS #5801", icon_url="https://cdn.discordapp.com/attachments/850253300557021194/903859655657287750/578c56178e478ad3fddd55b99b40729d.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/850253300557021194/903858600324243476/images00XQNGBX.jpg")
        await ctx.send (embed=embed)

    @commands.command()
    async def ms(slef, ctx):
        slef.channel_id = ctx.channel.id

    @commands.command()
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def play(self, ctx, url):
        if ctx.author.voice is None:
            await ctx.send("음성 채널에 입장해주세요!")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)
        if p.match(url) != None:
            FFMPEG_OPTIONS = {'before_options' : '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options' : '-vn'}
            YDL_OPTIONS = {'format':'bestaudio'}
            vc = ctx.voice_client
            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(url, download=False)
                URL = info['formats'][0]['url']
                source = await discord.FFmpegOpusAudio.from_probe(URL, **FFMPEG_OPTIONS)
                vc.play(source)
        else:
            FFMPEG_OPTIONS = {'before_options' : '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options' : '-vn'}
            YDL_OPTIONS = {'format':'bestaudio'}
            vc = ctx.voice_client
            chromedriver_autoinstaller.install()
            driver = webdriver.Chrome()
            driver.get("https://www.youtube.com/results?search_query=+"+str(url)+"+lyrics")
            source = driver.page_source
            bs = bs4.BeautifulSoup(source, 'lxml')
            entire = bs.find_all('a', {'id': 'video-title'})
            entireNum = entire[0]
            entireText = entireNum.text.strip()
            musicurl = entireNum.get('href')
            url = 'https://www.youtube.com'+musicurl 
            with YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(url, download=False)
                URL = info['formats'][0]['url']
                source = await discord.FFmpegOpusAudio.from_probe(URL, **FFMPEG_OPTIONS)
                vc.play(source)
            await ctx.send(embed = discord.Embed(title= "노래 재생", description = "현재 " + entireText + "을(를) 재생하고 있습니다.", color = 0x00ff00))

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
