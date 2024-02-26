import os
import logging
import asyncio
import urllib.request
import discord
from discord.ext import slash
from discord import Intents
import json
import random


intents = discord.Intents.default()
intents.typing = False
intents.presences = False

delete_time = 10
guildsList = [703086612757872710, 601058505063006208]

client = slash.SlashBot(
    # Pass help_command=None if the bot only uses slash commands
    command_prefix='/', description='', help_command=None,
    intents=intents,
    debug_guild=int(os.environ.get('DISCORD_DEBUG_GUILD', 0)) or None,
    resolve_not_fetch=False, fetch_if_not_get=True
)
#------------------------------------------------
#範例 hello world!
@client.slash_cmd()
async def hello(ctx: slash.Context):
    """Hello World!"""
    await ctx.respond('Hello World!', ephemeral=True)

#================================================
# 1. 更換twitter網址
url_opt = slash.Option( # 選項設定
    type=3, # string
    description="input a X url.",   # 說明
    required=True   # 這個欄位是否必填
    )

spo_opt = slash.Option(
    type=5, # bool
    description="設定為暴雷, 預設False",
    choices=["False", "True"],
    required=False
)

@client.slash_cmd() # global slash command
async def x轉網址(ctx: slash.Context, url: url_opt, spoiler: spo_opt=False):
    """Change X url""" # 指令的說明
    # 取出twitter並替換為vxtwitter後回傳
    temp = url.split("twitter.com")
    message = temp[0] + "vxtwitter.com" + temp[1]
    print(type(spoiler))
    if(spoiler):
        message = "||" + message + " ||"
    await ctx.respond(message)

#------------------------------------------------
# 2. 插香卡片隨機上香
@client.slash_cmd() # global slash command
async def 上香(ctx: slash.Context):
    """用香來測試運氣"""
    await ctx.respond(randomRipGif(), ephemeral=False)
#------------------------------------------------
#詢問bot可不可以吃宵夜
@client.slash_cmd() # global slash command
async def 宵夜(ctx: slash.Context):
    """我可以吃宵ㄇ"""
    if(random.randint(0, 1)):
        s = "吃! JUST DO EAT!"
    else:
        s = "不可以吃宵, U CAN'T."
    await ctx.respond(s, ephemeral=False)
#------------------------------------------------
@client.slash_cmd() # global slash command
async def 屁眼(ctx: slash.Context):
    """哈哈屁眼"""
    if(random.randint(0, 1)):
        s = "屁眼派對"
    else:
        s = "哈哈"
    await ctx.respond(s, ephemeral=False)

#------------------------------------------------
@client.slash_cmd() # global slash command
async def star_burst_stream(ctx: slash.Context):
    """哎額"""
    if(random.randint(0, 1)):
        s = "幫我撐十秒!"
    else:
        s = "你好臭喔"
    await ctx.respond(s, ephemeral=False)

#------------------------------------------------
#抽卡
@client.slash_cmd() # global slash command
async def 抽(ctx:slash.Context):
    """抽卡(SSR=:flag_fi:, SR=:flag_au:)"""
    n=random.uniform(0.0, 100.0)
    i=10
    s=""
    SSR=":flag_fi: "
    SR=":flag_au: "
    R=":flag_cn: "
    while(i > 0):
        n=random.uniform(0.0, 100.0)
        if(n >= 94.0):
            s += SSR
        elif(n >= 85.5):
            s += SR
        else:
            s += R
        i = i - 1
    await ctx.respond(s)
#------------------------------------------------

# #取得minecraft伺服器狀態，可自行加入參數來選擇要查看的IP
address_opt = slash.Option( # 選項設定
    type=3, # string
    description="input a minecraft server IP.",   # 說明
    required=False  # 這個欄位是否必填
)

@client.slash_cmd() # global slash command
async def get_minecraft_status(ctx: slash.Context, address: address_opt=""):
    """get minecraft is online or offline"""
    myServerIP="readseed2014.aternos.me"
    if(address != ""):  #如果有輸入東西，則檢查輸入的位置
        address = myServerIP
        print("address is empty.")
    url = "https://api.mcsrvstat.us/3/" + address

    #取得該server的狀態
    response = urllib.request.urlopen(url)
    serverInfo = json.loads(response.read())
    #print (serverInfo)
    if(serverInfo["online"]):
        print(url + " server is online.")
        playersArray=""
        if(serverInfo["players"]["online"] != 0):
            for index, data in enumerate(serverInfo["players"]["list"]):#{
                if(index == 0):
                    playersArray = data
                else:
                    playersArray += ", " + data
            #}
        # await ctx.respond("This " + serverInfo["version"] + " server is online\!\nOnline player:" + str(serverInfo["players"]["online"]) + "/" + str(serverInfo["players"]["max"]) + ".\nPlayers name: " + playersArray + ".")
        await ctx.respond("This server is online.")
    else:
        await ctx.respond("sorry this server is offline.")

# # use from https://api.mcsrvstat.us/
#================================================
# # show extension logs
logger = logging.getLogger('discord.ext.slash')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())
logger.handlers[0].setFormatter(logging.Formatter(
    '{levelname}\t{name}\t{asctime} {message}', style='{'))
#================================================

#functions

def getName(author):
    name = author.name
    if (author.nick != None):
        name = author.nick
    return name

def randomRipGif(): #上香的隨機抽選
    explosion_RIP="https://media.discordapp.net/attachments/796003875546595329/998901003640373328/eLvdC.gif"
    shark_RIP="https://media.discordapp.net/attachments/660162478440972288/834758134190833674/812615193572933642.gif"
    gura_RIP="https://media.discordapp.net/attachments/612627522806480917/798168690357043210/ezgif-7-d9a58ef46664.gif"
    shark_BigRIP="https://media.discordapp.net/attachments/619557226327310336/739676138430922832/image0.gif"
    fast_RIP="https://cdn.discordapp.com/attachments/796003875546595329/1151799689499389952/fca60b50b1eb6ac4692ee2352e3551b9.png"

    randomNum = random.randint(1, 100)
    print("cmdRIP:", randomNum)
    if randomNum == 1:
        return explosion_RIP
    elif randomNum == 2:
        return fast_RIP
    else:
        randomNum = random.randint(0, 2)
        if randomNum == 0:
            return shark_RIP
        elif randomNum == 1:
            return gura_RIP
        else:
            return shark_BigRIP

#================================================

#open file and run bot
with open('url.json', 'r', encoding = 'utf8') as jfile:
    data = json.load(jfile)
jfile.close()

# with open('botToken.json', 'r', encoding = 'utf8') as jfile:
#     botTokenJson = json.load(jfile)
# jfile.close()

#token = botTokenJson['DISCORD_TOKEN']
# token = botTokenJson['DISCORD_TOKEN_Slash']
try:
    # client.run(token)
    client.run(os.getenv('TOKEN'))
finally:
    print('Goodbye.')
