import discord # discord.py

client = discord.Client()

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    if message.content == ">server":
        await message.channel.send(f'サーバー名=**{message.guild.name}**\nサーバーID={message.guild.id}\nサーバーレベル={message.guild.premium_tier}\nサーバーブースト数={message.guild.premium_subscription_count}')

@client.event
async def on_message(message):
    if message.content == ('>chinfo'):
        await message.channel.send(f'チャンネル名={message.channel.name}\nチャンネルID={message.channel.id}\nNSFW(False=通常,True=NSFW)={message.channel.nsfw}')

@client.event
async def on_message(message):
    if message.content == ('@everyone'):
        embed = discord.Embed(title='警告', description=f'{message.author.mention} everyonの使い過ぎにはご注意ください。')
        await message.channel.send(embed=embed)

    elif message.content == ('@here'):
        embed = discord.Embed(title=f'警告', description=f'{message.author.mention} hereの使い過ぎにはご注意ください。')
        await message.channel.send(embed=embed)

client.run('BotToken') # ボットトークン(BotToken)
