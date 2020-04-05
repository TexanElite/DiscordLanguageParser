import discord
from shamanld import Shaman
from bot_token import *

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('```'):
        code = message.content[3:-3]
        language = Shaman.default().detect(code)[0][0]
        await message.channel.send(message.author.name + ' (' + language + '): ```' + language + '\n' + message.content[3:])

client.run(bot_token)
