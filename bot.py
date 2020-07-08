#!/usr/bin/python3

import discord
from config import *
from discord.ext import commands

TOKEN = bot_token
client = commands.Bot(command_prefix='@')

@client.event
async def on_ready():
    print('\x1b[32m------------\n|Bot online|\n------------\x1b[37m')

@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()


client.run(TOKEN)
