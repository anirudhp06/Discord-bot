import discord
import requests
import os
from dotenv import find_dotenv,load_dotenv
from discord.ext import commands, tasks
load_dotenv(find_dotenv())
bot = commands.Bot(command_prefix = "!")
links='https://result.jabincollege.com/'
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
    activity=discord.Activity(type=discord.ActivityType.watching, name="Watching results 😈")
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    #await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="beauty of being subtle"))
    print('Presence Changed!')
    checkResult.start()
@tasks.loop(seconds=300)
async def checkResult():
    try:
        html=requests.get(links)
        print(html.status_code)
    except:
        print("Secure connection cannot be established")
        html=requests.get("http://result.jabincollege.com/")
    if(html.status_code==200):
        print("Jabin college code:{}\nWebsite:{}".format(html.status_code,links))
        discord_channel_id=965606396567634010
        discord_channel=bot.get_channel(discord_channel_id)
        msg="<@&951907130955432058> Results are out go check here {}. Please check it out.".format(links)
        await discord_channel.send(msg)
        print("Calling status object and setting status")
        st.setStat(html.status_code)
        print("Status object set")
    else:
        print("Website not up yet")
        print("Calling status object and setting status")
        st.setStat(html.status_code)
        print("Status object set")
@bot.command()
async def status(ctx):
    await ctx.send("Current status code for {} is {}".format(links,st.getStat()))
    print("!status command called")
bot.run(os.getenv("TOKEN"))