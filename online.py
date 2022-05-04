import discord
import os
from discord.ext import commands
import datetime, time
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())
import datetime, time
pickup=["shut up or else i'll shut u up with my lips","Will you be my valentine?🥺","So lone that u tagged me? Lets go on date!","I ought to complain to Spotify for you not being named this week’s hottest single.",
        "I never believed in love at first sight, but that was before I saw you.","You’re like a fine wine. The more of you I drink in, the better I feel.","Do you have a map? I just got lost in your eyes."]
import random
import os
from sys import exit
book={'ping':'pong','pong':'ping','andrew':'andrew senpai'}
act=os.path.isfile('rest.txt')
def restart():
        import sys
        print("argv was",sys.argv)
        print("sys.executable was", sys.executable)
        print("restart is reqested hence restarting")
        os.execv(sys.executable, ['python'] + sys.argv)
class MyClient(discord.Client):
    async def on_ready(self):
        #print('Logged on as', self.user)
        print('Logged in successfully!!! Changing presence')
        activity=discord.Activity(type=discord.ActivityType.watching, name="beauty of being subtle")
        await self.change_presence(status=discord.Status.idle, activity=activity)
        print('Presence Changed!')
        if act:
            with open('rest.txt','r') as f:
                id=int(f.readline())
            os.remove('rest.txt')
            channel = client.get_channel(id)
            await channel.send('-----------------')
            await channel.send('Restarted the bot')
            await channel.send('-----------------')
        global startTime
        startTime = time.time()
        print('Ready to take input')
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
        if message.content.lower() == 'restart':
            await message.channel.send('Restarting the bot and will respond once restarted successfully')
            with open('rest.txt','w') as f:
                f.write('{}'.format(message.channel.id))
            restart()
        if message.content.lower()=='shutdown':
            await message.channel.send('Shutting down bot :wave:')
            exit(0)
            exit(0)
        if message.content.lower()=='uptime':
            uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
            await message.channel.send(uptime)
        if message.content.lower()=='latency':
            before = time.monotonic()
            await message.channel.send("Pong!")
            ping = (time.monotonic() - before) * 1000
            await message.channel.edit(content=f"Pong!  `{int(ping)}ms`")
            print(f'Ping! {int(ping)}ms')
client = MyClient()
client.run(os.getenv('TOKEN'))