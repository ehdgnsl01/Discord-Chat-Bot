from data import token
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents) #명령어의 시작이 "!"

@client.event
async def on_ready():
    print("=========================")
    print("다음으로 로그인 합니다 : ")
    print(client.user.name)
    print("connection was successful")
    activity = discord.CustomActivity(name='정보의 문단속 중...')
    print("=========================")
    await client.change_presence(status=discord.Status.online, activity=activity)

client.run(token)