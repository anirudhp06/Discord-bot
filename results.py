import discord
import requests
import os
import datetime
from dotenv import find_dotenv,load_dotenv
from discord.ext import commands, tasks
load_dotenv(find_dotenv())
from bs4 import BeautifulSoup as bs
bot = commands.Bot(command_prefix = "!")
class GetStat:
    code=0
    def getStat(self):
        return self.code
    def setStat(self,code):
        self.code=code

st=GetStat()
@bot.event
async def on_ready():
    print("Bot Now Online!")
    activity=discord.Activity(type=discord.ActivityType.watching, name="results 😈")
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    #await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="beauty of being subtle"))
    print('Presence Changed to "results 😈"!')
    checkResult.start()
@tasks.loop(seconds=5)
async def checkResult():
        x = datetime.datetime.now()
        res=requests.get("https://cetonline.karnataka.gov.in/kea/Pgcet22",verify=False)
        soup=bs(res.text,features="html.parser")
        doc=soup.find(id="ContentPlaceHolder1_req_accordion")
        if(len(doc)>20):
            code=1
            print("Result is out")
            discord_channel_id=965606396567634010
            discord_channel=bot.get_channel(discord_channel_id)
            msg="<@&951907130955432058> Results are out go check here {}. Please check it out.".format("https://cetonline.karnataka.gov.in/kea/Pgcet22")
            await discord_channel.send(msg)
        else:
            code=0
            print(x.strftime("%I:%M:%S %p"), end=" ")
            print("Waiting for update from https://cetonline.karnataka.gov.in/kea/Pgcet22")
@bot.command()
async def status(ctx):
    if(st.getStat()==0):
        await ctx.send("Results are not out")
    print("!status command called")
bot.run(os.getenv("TOKEN"))