import discord # Discord.py
import requests
from discord.ext import commands # コマンドに必須なコード

bot = commands.Bot(command_prefix='>') # コマンドPrefix

@bot.event
async def on_ready(): # Bot起動時の処理
    print('ログインしました') # Bot起動時「ログインしました」を表示
    webhook_url = '起動通知に使用するWebhook' # 起動通知

    main_content = {
        "username": "起動通知の名前",
        "avatar_url": "起動通知に使用するアイコン",
        "content": "起動通知のメッセージ"
    }

    requests.post(webhook_url, main_content) # 起動通知
    await bot.change_presence(activity=discord.Game(name="ゲームステータス", type=1))  # ステータス表示

bot.remove_command('help') # コマンド「help」を削除

@bot.command()
async def help(help): # コマンド「help」を追加
    embed = discord.Embed(title="ヘルプ | Help", description="ヘルプページです", color=0xff6600)  # 送信する内容
    embed.set_thumbnail(url="https://illust8.com/wp-content/uploads/2018/08/mark_hatena_question_illust_901.png")  # 表示する画像を指定
    embed.add_field(name="コマンド一覧", value="Call56Botで使えるコマンドの一覧です", inline=False)
    embed.add_field(name=">help", value="ヘルプを表示します", inline=False)
    embed.add_field(name=">adsense", value="広告閲覧用リンクを表示します", inline=False)
    embed.add_field(name=">mcsvconnect", value="MCサーバーの接続情報を見ることができます", inline=False)
    embed.add_field(name=">botinvite {Clientid}", value="ボットの招待リンクを生成します", inline=False)
    embed.add_field(name=">mcbefraudinfo", value="MCPEの不正情報を確認します", inline=False)
    embed.add_field(name=">mcsvadd {ServerName} {IP} {Port}", value="MCSVの追加リンクを生成します", inline=False)
    embed.add_field(name=">kick @Mention {理由}", value="ユーザーをキックします", inline=False)
    embed.add_field(name=">ban @Mention {理由}", value="ユーザーをBanします", inline=False)
    embed.add_field(name=">myinfo", value="自分の情報を確認します", inline=False)
    embed.add_field(name=">mentionuserinfo @Mention", value="メンション先のユーザーの情報を確認します", inline=False)
    embed.add_field(name=">iduserinfo {ClientID}", value="該当するIDのユーザーの情報を確認します", inline=False)
    embed.add_field(name=">server {ServerID}", value="該当するIDのDiscordサーバーの情報を確認します", inline=False)
    await help.send (embed=embed) # 内容を送信

@bot.command()
async def adsense(adsense): # コマンド「adsense」を追加
    embed = discord.Embed(title="広告表示", description=f"[広告閲覧](https://call56.info/adsense.html)")  # 送信する内容
    embed.add_field(name="広告収益", value="この広告によって収益を得ているわけではありません", inline=False)
    await adsense.send (embed=embed) # 内容を送信

@bot.command()
async def mcsvconnect(mcsvconnect): # コマンド「mcsvconnect」を追加
    embed = discord.Embed(title="MCSV接続情報", description=f"MCサーバーの接続情報を確認できます(アドレス等)", color=0x669933)  # 送信する内容
    embed.add_field(name="Call56NetWorkJava版", value="アドレス=play.call56.net\nポート=25565\nアドレス欄入力=play.call56.net:25565",inline=False)
    embed.add_field(name="Call56NetWorkBedRock版", value="アドレス=ComingSoon...\nポート=ComingSoon...", inline=False)
    await mcsvconnect.send (embed=embed) # 内容を送信

@bot.command()
async def botinvite(botinvite, clientid): # コマンド「botinvite」を追加
    embed = discord.Embed(title=f'以下のリンクへブラウザでアクセスすることでBotを招待できます', description=f"https://discord.com/oauth2/authorize?client_id={clientid}&permissions=8&scope=bot") # 送信する内容
    await botinvite.send (embed=embed) # 内容を送信

@bot.command()
async def mcbefraudinfo(mcbefraudinfo): # コマンド「mcbefraudinfo」を追加
    embed = discord.Embed(title="MCPE不正情報", description=f"MinecraftBedRockEditionの不正の情報です。", color=0x800000) # 送信する内容
    embed.set_thumbnail(url="https://avatars3.githubusercontent.com/u/50295306?s=200&v=4")  # 表示する画像を指定
    embed.add_field(name="Flare", value="1.14.30と1.14.60用の不正クライアントです。\n現在はすでに開発が終了していますがHorionの次に優秀なクライアントでした。",inline=False)
    embed.add_field(name="Horion", value="1.16.40にも対応していて今もなお更新が続いている非常に優秀なクライアントです。\nアップデートは遅いですが機能もたくさんあります。",inline=False)
    embed.add_field(name="Chron",value="1.16.1には対応していますが1.16.20以降のバージョンには対応していないクライアントです。\n開発者の知識不足で参加者と協力して1.16.20のPachを開発しています。",inline=False)
    embed.add_field(name="Atom", value="Flareの後続で製作所も同一人物です。\n1.16.20で開発が終了していて不安定なクライアントです。", inline=False)
    embed.add_field(name="Nitro",value="とにかく早さを求めたクライアント。\n歩く速度、攻撃速度、ジャンプ後の着地速度等何もかもが早くなります。\nお手軽なクライアントでアップデートも非常に速いです。\n1.16.40にも対応しています。",inline=False)
    embed.add_field(name="Cipher",value="CipherはAtomをJavaに移植した物で制作者は違います。\nクライアントは安定していてUIに対応しています。\n現在有料か無料かの議論が行われています。",inline=False)
    embed.add_field(name="Otco", value="とある事情により開発が停止されているクライアントです。\n1.16.1に対応しています。", inline=False)
    embed.add_field(name="Hydrogen",value="こちらもAtomの後続で制作者はAtom開発者と同じであります。\nクライアントは安定しておりAtomとは違う姿で進化して返ってくる可能性があります。\n現在ランチャーはすでに完成しておりあとは不正ファイルの制作が完成するのを待つのみです。",inline=False)
    await mcbefraudinfo.send (embed=embed) # 内容を送信

@bot.command()
async def mcsvadd(mcsvadd, svname, svip, svport): # コマンド「mcsvadd」を追加
    embed = discord.Embed(title=f'以下のリンクへブラウザでアクセスすることでサーバーが追加されます', description=f"minecraft://?addExternalServer={svname}|{svip}:{svport}") # 送信する内容
    await mcsvadd.send (embed=embed) # 内容を送信

@bot.command()
@commands.has_permissions (administrator=True) # パーミッションレベルを指定
async def message(message, title, *, text): # コマンド「message」を追加
    embed = discord.Embed(title=f'{title}', description=f"{text}") # 送信する内容
    await message.send (embed=embed) # 内容を送信

@bot.command()
async def clear(message):
    if message.author.guild_permissions.administrator: # パーミッションレベルを指定
        await message.channel.purge() # チャンネルのメッセージをすべて取得して削除
        await message.channel.send("メッセージをすべて削除しました") # 削除後のメッセージ
    else:
        await message.channel.send("メッセージをすべて削除する権限がありません") # 権限がない時のメッセージ

@bot.command()
@commands.has_permissions (administrator=True) # パーミッションレベルを指定
async def kick(kick, member: discord.Member, *, reason=None): # コマンド「kick」を追加
    await member.kick (reason=reason) # メンバーのキックを実行
    embed = discord.Embed (title=f'Kickを実行したユーザー={kick.author}', description=f"Kickされたユーザー={member.mention}", color=0xff0000) # 送信する内容
    embed.add_field (name=f"{member.id}", value=f"{kick.author.created_at}", inline=False)
    await kick.send (embed=embed) # 内容を送信

@bot.command()
@commands.has_permissions (administrator=True) # パーミッションレベルを指定
async def ban(ban, member: discord.Member, *, reason=None): # コマンド「ban」を追加
    await member.ban(reason=reason) # メンバーのBanを実行
    embed=discord.Embed (title=f'Banを実行したユーザー={ban.author}', description=f"Banされたユーザー={member.mention}", color=0xff0000) # 送信する内容
    embed.add_field (name=f"{member.id}", value=f"{ban.author.created_at}", inline=False)
    await ban.send (embed=embed) # 内容を送信

@bot.command()
@commands.has_permissions (administrator=True) # パーミッションレベルを指定
async def editgame(editgame, game): # コマンド「editgame」を追加
    await bot.change_presence(activity=discord.Game(name=(game), type=1))  # ステータス表示

@bot.command()
async def myinfo(myinfo): # コマンド「myinfo」を追加
    embed=discord.Embed (title=f'基本ID={myinfo.author}', description=f"ID={myinfo.author.id}\nBotであるか(True=はい | False=いいえ)={myinfo.author.bot}", color=0xff0000) # 送信する内容
    await myinfo.send(embed=embed) # 内容を送信

@bot.command()
async def mentionuserinfo(mentionuserinfo, member: discord.Member): # コマンド「mentionuserinfo」を追加
    embed=discord.Embed (title=f'基本ID={member}', description=f"ニックネーム={member.nick}\nID={member.id}\nアカウント作成日={member.created_at}\nBotであるか(True=はい | False=いいえ)={member.bot}", color=0xff0000) # 送信する内容
    await mentionuserinfo.send(embed=embed) # 内容を送信

@bot.command()
async def iduserinfo(iduserinfo, id: int): # コマンド「iduserinfo」を追加
    user = await bot.fetch_user(id)
    embed = discord.Embed(title=f'基本ID={user}', description=f"表示名={user.display_name}\nID={user.id}\nBotであるか(True=はい | False=いいえ)={user.bot}", color=0xff0000) # 送信する内容
    await iduserinfo.send(embed=embed) # 内容を送信

bot.run('BotToken') # ボットトークン
