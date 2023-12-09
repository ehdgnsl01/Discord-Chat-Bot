import requests
import discord
from discord.ext import commands
import asyncio
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import json
import time
from data import Riot_api_key

class LOL(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='티어')
    async def get_tier(self, ctx, *, summoner_name):
        start = time.time()

        final_name = summoner_name.replace(" ", "+")

        url = f"https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{final_name}"
        res = requests.get(url, headers={"X-Riot-Token": Riot_api_key})

        if res.status_code == 200:
            resobj = json.loads(res.text)
            player_icon = str(resobj["profileIconId"])
            player_id = str(resobj["id"])
            url = f"https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/{player_id}"
            res = requests.get(url, headers={"X-Riot-Token": Riot_api_key})
            rankinfo = json.loads(res.text)

            if len(rankinfo) == 0:
                await ctx.send("소환사의 랭크 정보가 없습니다")
                return

            for i in rankinfo:
                if i["queueType"] == "RANKED_SOLO_5x5":
                    rank = str(i["rank"])
                    tier = str(i["tier"])
                    leaguepoints = str(i["leaguePoints"])
                    wins = str(i["wins"])
                    losses = str(i["losses"])
                    ratio = str(round(int(wins) * 100 / (int(wins) + int(losses)), 1))

                    url = f"https://kr.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{player_id}"
                    res = requests.get(url, headers={"X-Riot-Token": Riot_api_key})
                    player_mastery = json.loads(res.text)

                    for i in player_mastery:
                        most_champion_id = int(i["championId"])
                        most_champion_points = str(i["championPoints"])

                        url = "http://ddragon.leagueoflegends.com/cdn/10.25.1/data/ko_KR/champion.json"
                        res = requests.get(url)
                        champion_name = json.loads(res.text)

                        champion_name_list = champion_name["data"]

                        global most_champion_name
                        for i in champion_name_list:
                            if champion_name["data"][i]["key"] == str(most_champion_id):
                                most_champion_name = champion_name["data"][i]["name"]
                                break

                        embed = discord.Embed(title="", description="", color=0xd5d5d5)
                        embed.set_author(name=f"{final_name}님의 전적 검색", url=f"http://www.op.gg/summoner/userName={final_name}", icon_url=f"http://ddragon.leagueoflegends.com/cdn/10.25.1/img/profileicon/{player_icon}.png")
                        embed.add_field(name=f"{tier} {rank} | {leaguepoints} LP", value=f"{wins}승 {losses}패 | {ratio}%", inline=False)
                        embed.add_field(name="가장 높은 숙련도", value=f"{most_champion_name} {most_champion_points} 점 ", inline=False)
                        embed.set_footer(text='CuriHuS LAB')
                        embed.set_thumbnail(url=f"http://z.fow.kr/img/emblem/{tier.lower()}.png")
                        await ctx.send(embed=embed)
                        break

        else:
            await ctx.send("소환사가 존재하지 않습니다")

def setup(bot):
    bot.add_cog(LOL(bot))
