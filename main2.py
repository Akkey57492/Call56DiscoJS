import discord # discord.py
import json
from discord.ext import commands
import random

token_json_open = open("token.json", "r")
token = json.load(token_json_open)
client = discord.Client()

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == ('>server'):
        embed = discord.Embed(title='サーバー情報', description=f'サーバー名=**{message.guild.name}**\nサーバーID={message.guild.id}\nサーバーレベル={message.guild.premium_tier}\nサーバーブースト数={message.guild.premium_subscription_count}')
        await message.channel.send(embed=embed)

    elif message.content == ('>chinfo'):
        if message.channel.nsfw:
            nw='NSFW'
        else:
            nw='Normal'
        embed = discord.Embed(title='チャンネル情報', description=f'チャンネル名={message.channel.name}\nチャンネルID={message.channel.id}\nチャンネルタイプ={nw}')
        await message.channel.send(embed=embed)

    elif message.content == ('>rn'):
        await message.channel.send(random.randint(1,99999))

client.run(token["token"]) # ボットトークン(BotToken)
