import requests
import discord
import asyncio
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import json
import time
from data import token, api_key
    

async def on_message(message):

    if message.content.startswith('!티어'):

        start = time.time()
    

        Name = message.content[4:len(message.content)]
        Final_Name = Name.replace(" ","+")


        URL = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+Final_Name #0.8초 소요
        res = requests.get(URL, headers={"X-Riot-Token": api_key})
        print(res.text)


        if res.status_code == 200:
            #코드가 200일때
            resobj = json.loads(res.text)
            URL = "https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/"+resobj["id"]+"?"+api_key
            player_icon = str(resobj["profileIconId"])
            player_id = str(resobj["id"])

            URL = "https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/"+resobj["id"]+"?"+api_key
            res = requests.get(URL, headers={"X-Riot-Token": api_key})
            rankinfo = json.loads(res.text) #list class


            if len(rankinfo) == 0:
                await message.channel.send("소환사의 랭크 정보가 없습니다")
            print(time.time()-start)


            for i in rankinfo:
                if i["queueType"] == "RANKED_SOLO_5x5":
                    rank = str(i["rank"])
                    tier = str(i["tier"])
                    leaguepoints = str(i["leaguePoints"])
                    wins = str(i["wins"])
                    losses = str(i["losses"])
                    ratio = str(round(int(wins)*100/(int(wins)+int(losses)), 1))

                    print(rank)
                    print(tier)

                    URL = "https://kr.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/"+player_id
                    res = requests.get(URL, headers={"X-Riot-Token": api_key})
                    player_mastery = json.loads(res.text) # player mastery : list class

                    print(time.time()-start)

                    for i in player_mastery: # i : dictionary class
                        most_champion_id = int(i["championId"])
                        most_champion_points = str(i["championPoints"])

                        URL = "http://ddragon.leagueoflegends.com/cdn/13.20.1/data/ko_KR/champion.json"
                        res = requests.get(URL)
                        print(time.time()-start)
                        champion_name = json.loads(res.text)
                        #print(champion_name)

                        champion_name_list = champion_name["data"] #champion_name : dictionary class / list : dict class
                        print(type(champion_name_list))

                        global most_champion_name
                        for i in champion_name_list: #key 값은 str class
                            if(champion_name["data"][i]["key"]) == str(most_champion_id):
                                most_champion_name = champion_name["data"][i]["name"]
                                break

                        print(most_champion_name)
                        print(most_champion_points)
                        print(time.time()-start)
                        
                    
                        embed = discord.Embed(title="", description="", color=0xd5d5d5)
                        embed.set_author(name=Final_Name  +"님의 전적 검색", url="http://www.op.gg/summoner/userName="+Final_Name, icon_url="http://ddragon.leagueoflegends.com/cdn/13.20.1/img/profileicon/"+player_icon+".png")
                        # cdn/버전/img : 버전을 최신화 시켜주어야 업데이트된 아이콘 사용 가능
                        embed.add_field(name=tier+" "+rank+" | "+leaguepoints+" LP", value=wins+"승"+" "+losses +"패"+" | "+ratio+"%", inline=False)
                        embed.add_field(name="가장 높은 숙련도",value= most_champion_name +" "+ most_champion_points +" 점 ", inline= False)
                        embed.set_footer(text='CuriHuS LAB')
                        embed.set_thumbnail(url="http://z.fow.kr/img/emblem/"+tier.lower()+".png")
                        await message.channel.send(embed=embed)
                        break
                    


        else:
            await message.channel.send("소환사가 존재하지 않습니다")
