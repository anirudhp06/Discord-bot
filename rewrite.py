import discord
from discord.ext import commands
with open('token.txt','r') as tok:
    TOKEN=tok.readline()
class MyClient(discord.Client):
    async def on_ready(self):
        print('Ready')
    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        if str(message.channel) == "youtube-notif" and message.content.lower() == "done":
            await message.channel.purge(limit=2)
client = MyClient()
client.run(TOKEN)