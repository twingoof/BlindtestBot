#!/usr/bin/python3

import discord
from discord.ext import commands

TOKEN = 'NjczODYzODMzODg1OTk5MTI0.XwUJNg.Fnp7LDY2YLKmXgKHoAIpHEUf0k8'
client = commands.Bot(command_prefix='@')

@client.event
async def on_ready():
    print('\x1b[32m------------\n|Bot online|\n------------\x1b[37m')

@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()


client.run(TOKEN)
