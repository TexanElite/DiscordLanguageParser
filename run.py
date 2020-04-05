import discord
from shamanld import Shaman
from bot_token import *

client = discord.Client()

languages = [
    'actionscript'
    'asp',
    'bash',
    'c',
    'csharp',
    'css',
    'haxe',
    'html',
    'java',
    'js',
    'jsp',
    'objc',
    'perl',
    'php',
    'python',
    'ruby',
    'sql',
    'swift',
    'vbs',
    'xml',
]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('```'):
        newline = message.content.find('\n')
        if newline >= 0 and message.content[3:newline] in languages:
            return
        code = message.content[3:-3]
        res = Shaman.default().detect(code)
        if (len(res) == 0 or res[0][1] < 1):
            return
        language = res[0][0]
        if language == 'c#':
            language = 'csharp'
        if language == 'objective-c':
            language = 'objc'
        if language == 'visualbasic':
            language = 'vbs'
        if language == 'javascript':
            language = 'js'
        await message.channel.send(message.author.name + ' (' + language + '): ```' + language + '\n' + message.content[3:])

client.run(bot_token)
