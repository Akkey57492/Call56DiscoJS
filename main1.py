import discord # Discord.py
import json
import time

status = input("ステータス表示を指定(1: Online | 2: FakeOffline): ")
if status == "1":
    s = discord.Status.online
elif status == "2":
    s = discord.Status.invisible
else:
    print("1か2で指定してください。")
    time.sleep(10)
    exit()

from discord.ext import commands # コマンドに必須なコード

bot = commands.Bot(command_prefix='>') # コマンドPrefix

token_json_open = open("token.json", "r")
token = json.load(token_json_open)

@bot.event
async def on_ready(): # Bot起動時の処理
    print('ログインしました') # Bot起動時「ログインしました」を表示
    Activity = discord.Game(name='>help', type=1)
    await bot.change_presence(activity=Activity, status=s)  # ステータス表示

bot.remove_command('help') # コマンド「help」を削除

@bot.command()
async def help(help, page): # コマンド「help」を追加
    if page == ('1'):
        help1 = discord.Embed(title="ヘルプ | Help | 1", description="ヘルプページです\nOP=オペレーター専用\nBeta段階=試験段階(正常動作は保証しない)\nDM=ダイレクトメッセージで実行可能",color=0xff6600)  # 送信する内容
        help1.set_thumbnail(url="https://illust8.com/wp-content/uploads/2018/08/mark_hatena_question_illust_901.png")  # 表示する画像を指定
        help1.add_field(name="コマンド一覧", value="Call56Botで使えるコマンドの一覧です", inline=False)
        help1.add_field(name=">help {ページ(1-4)}", value="ヘルプを表示します[DM]", inline=False)
        help1.add_field(name=">mcsvconnect", value="MCサーバーの接続情報を見ることができます[DM]", inline=False)
        help1.add_field(name=">botinvite {Clientid}", value="ボットの招待リンクを生成します[DM]", inline=False)
        help1.add_field(name=">mcbefraudinfo", value="MCPEの不正情報を確認します[DM]", inline=False)
        await help.send(embed=help1)
    if page == ('2'):
        help2 = discord.Embed(title="ヘルプ | Help | 2", description="ヘルプページです\nOP=オペレーター専用\nBeta段階=試験段階(正常動作は保証しない)\nDM=ダイレクトメッセージで実行可能",color=0xff6600)  # 送信する内容
        help2.add_field(name=">mcsvadd {ServerName} {IP} {Port}", value="MCSVの追加リンクを生成します[DM]", inline=False)
        help2.add_field(name=">message {タイトル} {内容}", value="Embedメッセージを生成します[OP]", inline=False)
        help2.add_field(name=">clear", value="チャンネルのメッセージを削除します。[OP]", inline=False)
        help2.add_field(name=">kick @Mention {理由}", value="ユーザーをキックします[OP]", inline=False)
        help2.add_field(name=">ban @Mention {理由}", value="ユーザーをBanします[OP]", inline=False)
        help2.add_field(name=">myinfo", value="自分の情報を確認します", inline=False)
        await help.send(embed=help2)
    if page == ('3'):
        help3 = discord.Embed(title="ヘルプ | Help | 3",description="ヘルプページです\nOP=オペレーター専用\nBeta段階=試験段階(正常動作は保証しない)\nDM=ダイレクトメッセージで実行可能",color=0xff6600)  # 送信する内容
        help3.add_field(name=">mui @Mention", value="メンション先のユーザーの情報を確認します", inline=False)
        help3.add_field(name=">iui {ClientID}", value="該当するIDのユーザーの情報を確認します[Beta段階]", inline=False)
        help3.add_field(name=">server", value="メッセージを送信したDiscordサーバーの情報を確認します", inline=False)
        help3.add_field(name=">chinfo", value="チャンネルの情報を確認します。", inline=False)
        help3.add_field(name=">role {RoleID}", value="該当するIDのロールの基本的なパーミッションを確認します。[Beta段階]", inline=False)
        help3.add_field(name=">guildeditname {新しい名前} {変更理由}", value="サーバーの名前を変更します。[Beta段階 | OP]", inline=False)
        await help.send(embed=help3)
    if page == ('4'):
        help4 = discord.Embed(title="ヘルプ | Help | 4", description="ヘルプページです\nOP=オペレーター専用\nBeta段階=試験段階(正常動作は保証しない)\nDM=ダイレクトメッセージで実行可能",color=0xff6600)  # 送信する内容
        help4.add_field(name=">ping", value="Ping値を測定します。[DM]", inline=False)
        help4.add_field(name=">mdm @Mention {送信内容}", value="メンション先のユーザーにダイレクトメッセージを送信します。[OP]", inline=False)
        help4.add_field(name=">report {内容}", value="レポートを行います。[DM]", inline=False)
        await help.send (embed=help4) # 内容を送信

@bot.command()
async def botinvite(botinvite, clientid): # コマンド「botinvite」を追加
    embed = discord.Embed(title=f'以下のリンクへブラウザでアクセスすることでBotを招待できます', description=f"https://discord.com/oauth2/authorize?client_id={clientid}&permissions=8&scope=bot") # 送信する内容
    await botinvite.send (embed=embed) # 内容を送信

@bot.command()
async def mcjefraudinfo(mcbefraudinfo):
    embed = discord.Embed(title="MCJE不正情報", description=f"MinecraftJavaEditionの不正の情報です。", color=0x800000) # 送信する内容
    embed.add_field(name="Wurst", value="Javaでは定番のクライアントで高性能かつアップデートが早いクライアントです。")
    embed.add_field(name="Sigma", value="PVP向けのクライアントです。")
    embed.add_field(name="Sigma5", value="Sigmaの後継でClickGUIが追加されたりAntiCheatByPass機能が追加されたりしました。\n現在は開発が停止しておりもう間もなく提供も停止するようです。\n(ByPassは回避等と言う意味があり、ByPassは有料でした。)")
    embed.add_field(name="Aristois", value="少し有名なクライアントでWurstよりも有能なくらいすごいクライアントです。")
    embed.add_field(name="Impact", value="Impactは2b2tで使える1.12のクライアントです。")
    await mcjefraudinfo.send(embed=embed)

@bot.command()
async def mcsvadd(mcsvadd, svname, svip, svport): # コマンド「mcsvadd」を追加
    embed = discord.Embed(title=f'以下のリンクへブラウザでアクセスすることでサーバーが追加されます', description=f"minecraft://?addExternalServer={svname}|{svip}:{svport}") # 送信する内容
    await mcsvadd.send (embed=embed) # 内容を送信

@bot.command()
async def message(message, title, *, text): # コマンド「message」を追加
    if message.author.guild_permissions.administrator:
        embed = discord.Embed(title=f'{title}', description=f"{text}")  # 送信する内容
        await message.channel.send(embed=embed)  # 内容を送信
    else:
        embed = discord.Embed(title='権限無し', description='管理者権限がないため埋め込みメッセージの送信を実行することができません。')
        await message.channel.send(embed=embed)

@bot.command()
async def clear(clear):
    if clear.author.guild_permissions.administrator: # パーミッションレベルを指定
        await clear.channel.purge() # チャンネルのメッセージをすべて取得して削除
        embed = discord.Embed(title='完了', description='メッセージをすべて削除しました。')
    else:
        embed = discord.Embed(title='権限無し', description='管理者権限がないためメッセージの完全削除を実行することができません。')
        await clear.channel.send(embed=embed)

@bot.command()
async def kick(kick, member: discord.Member, *, reason=None): # コマンド「kick」を追加
    if kick.author.guild_permissions.administrator:
        await member.kick(reason=reason)  # メンバーのキックを実行
        embed = discord.Embed(title=f'Kickを実行したユーザー={kick.author}', description=f"Kickされたユーザー={member.mention}",color=0xff0000)  # 送信する内容
        embed.add_field(name=f"{member.id}", value=f"{kick.author.created_at}", inline=False)
        await kick.channel.send(embed=embed)  # 内容を送信
    else:
        embed = discord.Embed(title='権限無し', description='管理者権限がないためKickを実行することができません。')
        await kick.channel.send(embed=embed)

@bot.command()
async def ban(ban, member: discord.Member, *, reason="Ban時に理由が記入されませんでした。"): # コマンド「ban」を追加
    if ban.author.guild_permissions.administrator:
        await member.ban(reason=reason)  # メンバーのBanを実行
        embed = discord.Embed(title=f'Banを実行したユーザー={ban.author}', description=f"Banされたユーザー={member.mention}",color=0xff0000)  # 送信する内容
        embed.add_field(name=f"{member.id}", value=f"{ban.author.created_at}", inline=False)
        await ban.send(embed=embed)  # 内容を送信
    else:
        embed = discord.Embed(title='権限無し', description='管理者権限がないためBanを実行することができません。')
        await ban.channel.send(embed=embed)

@bot.command()
async def editgame(editgame, game): # コマンド「editgame」を追加
    if editgame.author.guild_permissions.administrator:
        await editgame.change_presence(activity=discord.Game(name=(game), type=1))  # ステータス表示
    else:
        embed = discord.Embed(title='権限無し', description='管理者権限がないためステータスを変更することができません。')
        await editgame.channel.send(embed=embed)

@bot.command()
async def myinfo(myinfo): # コマンド「myinfo」を追加
    if myinfo.author.bot:
        b='Bot'
    else:
        b='User'
    embed=discord.Embed (title=f'基本ID={myinfo.author}', description=f"ID={myinfo.author.id}\nアカウント作成日={myinfo.author.created_at}\nサーバー参加日={myinfo.author.joined_at}\nアカウントタイプ={b}", color=0xff0000) # 送信する内容
    embed.set_thumbnail(url=f"{myinfo.author.avatar_url}")
    await myinfo.send(embed=embed) # 内容を送信

@bot.command()
async def mui(mui, member: discord.Member): # コマンド「mentionuserinfo」を追加
    if member.bot:
        b='Bot'
    else:
        b='User'
    embed=discord.Embed (title=f'基本ID={member}', description=f"ニックネーム={member.nick}\nID={member.id}\nアカウント作成日={member.created_at}\nサーバー参加日={member.joined_at}\nアカウントの種類={b}", color=0xff0000) # 送信する内容
    embed.set_thumbnail(url=f"{member.avatar_url}")
    await mui.send(embed=embed) # 内容を送信

@bot.command()
async def iui(iui, id: int): # コマンド「iduserinfo」を追加
    user = await bot.fetch_user(id)
    if user.bot:
        b='Bot'
    else:
        b='User'
    embed = discord.Embed(title=f'基本ID={user}', description=f"アカウント作成日={user.created_at}\nID={user.id}\nBotであるか(True=はい | False=いいえ)={b}", color=0xff0000) # 送信する内容
    embed.set_thumbnail(url=f"{user.avatar_url}")
    await iui.send(embed=embed) # 内容を送信

@bot.command()
async def role(role, id: discord.Role):
    if id.permissions.administrator:
        svad=':white_check_mark:'
    else:
        svad=':negative_squared_cross_mark:'
    if id.permissions.view_audit_log:
        audit=':white_check_mark:'
    else:
        audit=':negative_squared_cross_mark:'
    if id.permissions.view_guild_insights:
        svins=':white_check_mark:'
    else:
        svins=':negative_squared_cross_mark:'
    if id.permissions.manage_guild:
        svedit=':white_check_mark:'
    else:
        svedit=':negative_squared_cross_mark:'
    if id.permissions.manage_roles:
        sveditrole=':white_check_mark:'
    else:
        sveditrole=':negative_squared_cross_mark:'
    if id.permissions.manage_channels:
        sveditch=':white_check_mark:'
    else:
        sveditch=':negative_squared_cross_mark:'
    if id.permissions.kick_members:
        svuserkick=':white_check_mark:'
    else:
        svuserkick=':negative_squared_cross_mark:'
    if id.permissions.ban_members:
        svuserban=':white_check_mark:'
    else:
        svuserban=':negative_squared_cross_mark:'
    if id.permissions.create_instant_invite:
        svinvite=':white_check_mark:'
    else:
        svinvite=':negative_squared_cross_mark:'
    if id.permissions.change_nickname:
        svcgnick=':white_check_mark:'
    else:
        svcgnick=':negative_squared_cross_mark:'
    if id.permissions.manage_nicknames:
        sveditnick=':white_check_mark:'
    else:
        sveditnick=':negative_squared_cross_mark:'
    if id.permissions.manage_emojis:
        sveditemo=':white_check_mark:'
    else:
        sveditemo=':negative_squared_cross_mark:'
    if id.permissions.manage_webhooks:
        svedithook=':white_check_mark:'
    else:
        svedithook=':negative_squared_cross_mark:'
    if id.permissions.view_channel:
        chvi=':white_check_mark:'
    else:
        chvi=':negative_squared_cross_mark:'
    embed = discord.Embed(title=f'ロール名={id.name}',description=f'ロールID={id.id}\nロール作成日={id.created_at}\nロールの色(16進数カラーコード)={id.color}\n権限コード={id.permissions.value}',color=0x008000)
    embed.add_field(name='基本的な権限',value=f'管理者権限={svad}\n\n監視ログの表示={audit}\n\nサーバーインサイトの表示={svins}\n\nサーバー管理={svedit}\n\nロール管理={sveditrole}\n\nチャンネルの管理={sveditch}\n\nメンバーのKick={svuserkick}\n\nメンバーのBan={svuserban}\n\nインスタント招待の作成={svinvite}\n\nニックネームの変更={svcgnick}\n\nニックネームの管理={sveditnick}\n\n絵文字の管理={sveditemo}\n\nWebHook管理={svedithook}\n\nチャンネルを表示={chvi}', inline=False)
    await role.send(embed=embed)

@bot.command()
async def creator(creator):
    embed = discord.Embed(title='制作者 | 協力', description='制作者=Call56\n協力=名無し | キノコ | [一部のインターネット記事](https://www.bing.com/search?q=discord.py+API%E3%83%AA%E3%83%95%E3%82%A1%E3%83%AC%E3%83%B3%E3%82%B9&cvid=ee44343131a346208a04f3f35ca98587&pglt=515&FORM=ANNTA1&PC=U531)')
    await creator.send(embed=embed)

@bot.command()
async def guildeditname(guildeditname, name, reason):
    if guildeditname.author.guild_permissions.administrator:
        guild = bot.get_guild(guildeditname.guild.id)
        await guild.edit(name=f'{name}', reason=f'{reason}')
        embed = discord.Embed(title='実行', description=f'名前の変更を実行しました。\n変更後の名前={name}\n理由={reason}\n実行者={guildeditname.author}')
        await guildeditname.send(embed=embed)
    else:
        embed = discord.Embed(title='権限無し', description='管理者権限がないためサーバーの名前の変更を実行することができません')
        await guildeditname.send(embed=embed)

@bot.command()
async def mdm(mdm, member: discord.Member, message):
    if mdm.author.guild_permissions.administrator:
        await mdm.send('ダイレクトメッセージ送信中')
        await member.send(message)
        await mdm.send('ダイレクトメッセージを送信しました')
    else:
        embed = discord.Embed(title='権限無し', description='権限がないためDM送信を行うことができません。')
        await mdm.send(embed=embed)

bot.run(token["token"])
