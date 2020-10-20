import discord # discord.py

client = discord.Client()

@client.event
async def on_message(message):
    if message.author.bot: # メッセージを送信した人がBotであれば無視する
        return
    GLOBAL_CH_NAME = "call-global-chat" # グローバルチャットのチャンネル名

    if message.channel.name == GLOBAL_CH_NAME: # メッセージを転送

        await message.delete() # 元メッセージを削除

        channels = client.get_all_channels()
        global_channels = [ch for ch in channels if ch.name == GLOBAL_CH_NAME]

        embed = discord.Embed(title="call-global-chat", # グローバルチャットのチャンネル名
            description=message.content, color=0x00bfff)

        embed.set_author(name=message.author.display_name, # 投稿場所等の詳細な設定
            icon_url=message.author.avatar_url_as(format="png"))
        embed.set_footer(text=f"{message.guild.name} / {message.channel.name}",
            icon_url=message.guild.icon_url_as(format="png"))

        for channel in global_channels: # メッセージを埋め込み形式で送信
            await channel.send(embed=embed) # 埋め込みメッセージを送信

client.run('BotToken') # BotToken
