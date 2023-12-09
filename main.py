import discord
from discord.ext import commands
import os
from data import token, APPLICATION_ID, Riot_api_key, Open_api_key, bot_activity, bot_status, GITHUB




 
intents = discord.Intents.default()
intents.messages = True
 
bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("!"),
    intents=intents,
)

cogs_path = 'Cogs'
abs_cogs_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), cogs_path)

for ext in os.listdir(abs_cogs_path):
    if ext.endswith(".py"):
        bot.load_extension(f"Cogs.{ext.split('.')[0]}")

@bot.event
async def on_ready():
    print("=========================")
    print("다음으로 로그인 합니다 : ")
    print(bot.user.name)
    print("connection was successful")
    print("=========================")
    await bot.change_presence(status=bot_status, activity=bot_activity)

@bot.command()  # 봇 명령어
async def hello(ctx):  # !hello라고 사용자가 입력하면
    await ctx.send("Hello world")  # 봇이 Hello world!라고 대답함


bot.run(token)