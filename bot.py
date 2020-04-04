#!/usr/bin/python3

import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
client = discord.Client()

@client.event
async def on_ready():
    global game_chan
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(f'{client.user} has connected to Discord on {guild.name} (id: {guild.id}) !')
    game_chan = discord.utils.get(client.get_all_channels(), name='bot')
    print(f'Ready to write in channel: {game_chan.name} (id: {game_chan.id})')
    await game_chan.send('Hello !')


@client.event
async def on_message(message):
        global game_chan
        if message.author == client.user:
            return
        elif message.channel != game_chan:
            return
        if message.content == '!.!':
            await game_chan.send('bot')


@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

client.run(TOKEN)
