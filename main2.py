import discord # discord.py

client = discord.Client()

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    if message.content == ('>server'):
        await message.channel.send(f'サーバー名=**{message.guild.name}**\nサーバーID={message.guild.id}\nサーバーレベル={message.guild.premium_tier}\nサーバーブースト数={message.guild.premium_subscription_count}')

    elif message.content == ('>chinfo'):
        await message.channel.send(f'チャンネル名={message.channel.name}\nチャンネルID={message.channel.id}\nNSFW(False=通常,True=NSFW)={message.channel.nsfw}')

    elif message.content == ('@everyone'):
        embed = discord.Embed(title='警告', description=f'{message.author.mention} everyonの使い過ぎにはご注意ください。')
        await message.channel.send(embed=embed)

    elif message.content == ('@here'):
        embed = discord.Embed(title=f'警告', description=f'{message.author.mention} hereの使い過ぎにはご注意ください。')
        await message.channel.send(embed=embed)

    elif message.content == ('>glchadd'):
        guild = client.get_guild(message.guild.id)
        glchadd = await guild.create_text_channel("call-global-chat")
        await glchadd.send("グローバルチャット用チャンネルの作成が完了しました!")

    elif message.content == ('おやすみ'):
        await message.channel.send('おやすみなさい...')

    elif message.content == ('おはよう'):
        await message.channel.send('おはようございます!')

    elif message.content == ('うんこ'):
        await message.channel.send('精神年齢小学生以下かよwww(せいしんねんれいしょうがくせいいかかよわらわらわら)')

    elif message.content == ('雑魚'):
        await message.channel.send('そんな煽りしかできないのかなぁー?www')

    elif message.content == ('everyoneしていい?'):
        await message.channel.send('注意して使ってね!')

client.run('BotToken') # ボットトークン(BotToken)
