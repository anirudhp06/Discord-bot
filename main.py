import discord
from discord.ext import commands
import datetime, time
pickup=["shut up or else i'll shut u up with my lips","Will you be my valentine?🥺","So lone that u tagged me? Lets go on date!","I ought to complain to Spotify for you not being named this week’s hottest single.",
        "I never believed in love at first sight, but that was before I saw you.","You’re like a fine wine. The more of you I drink in, the better I feel.","Do you have a map? I just got lost in your eyes."]
import random
import os
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())
book={'ping':'pong','pong':'ping','andrew':'andrew senpai'}
with open('token.txt','r') as tok:
    TOKEN=tok.readline()
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in successfully!!! Changing presence')
        activity=discord.Activity(type=discord.ActivityType.watching, name="art of being subtle")
        await self.change_presence(status=discord.Status.idle, activity=activity)
        print('Presence Changed!')
        global startTime
        startTime = time.time()
    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        if message.content.lower() in book:
            await message.channel.send(book[message.content.lower()])
            print('{0.author},said: {0.content}'.format(message))
        if client.user.mentioned_in(message):
            num=random.randint(0, len(pickup)-1)
            await message.channel.send(pickup[num])
        if str(message.channel) == "youtube-notif" and message.content.lower() == "done":
            await message.channel.purge(limit=2)
        if message.content.lower()=='uptime':
            uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
            await message.channel.send(uptime)
        if message.content.lower()=='latency':
            before = time.monotonic()
            await message.channel.send("Pinging servers...")
            ping = (time.monotonic() - before) * 1000
            await message.channel.send(content=f"Pong!:`{int(ping)}ms`")
            print(f'Ping {int(ping)}ms')
client = MyClient()
client.run(os.getenv('TOKEN'))