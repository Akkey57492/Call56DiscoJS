import discord # discord.py

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

    elif message.content == ('@everyone'):
        embed = discord.Embed(title='警告', description=f'{message.author.mention} everyonの使い過ぎにはご注意ください。')
        await message.channel.send(embed=embed)

    elif message.content == ('@here'):
        embed = discord.Embed(title=f'警告', description=f'{message.author.mention} hereの使い過ぎにはご注意ください。')
        await message.channel.send(embed=embed)

client.run('Token') # ボットトークン(BotToken
