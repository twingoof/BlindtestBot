#!/usr/bin/python3

import discord
import time

# import youtube_dl #TODO: Remove if unused
from config import *
from discord.ext import commands


TOKEN = bot_token
client = commands.Bot(command_prefix='>')


async def debug(channel: discord.channel.TextChannel, message):
    await channel.send(message)


@client.event
async def on_ready():
    print('\x1b[32m        ------------\n        |Bot online|\n        ------------\x1b[37m')


@client.command(pass_context=True)
async def rick(ctx):
    voip_channel = ctx.message.author.voice.channel
    vc = await voip_channel.connect()
    vc.play(discord.FFmpegPCMAudio(source='rickroll.mp3'), after=lambda e: print('\x1b[35m------- Rickroll done -------\x1b[37m'))
    time.sleep(30)
    await vc.disconnect()


@client.command(pass_context=True)
async def hello(ctx):
    text_channel = ctx.message.channel
    await text_channel.send('Hello')


client.run(TOKEN)