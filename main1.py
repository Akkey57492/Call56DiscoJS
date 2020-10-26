import discord # Discord.py

from discord.ext import commands # コマンドに必須なコード
from discord.ext import tasks

bot = commands.Bot(command_prefix='>') # コマンドPrefix

@bot.event
async def on_ready(): # Bot起動時の処理
    print('ログインしました') # Bot起動時「ログインしました」を表示
    await bot.change_presence(activity=discord.Game(name=f'[>help]Bot正常稼働中 | サーバー数={len(bot.guilds)}', type=1))  # ステータス表示

@tasks.loop(seconds=1)
async def status():
   await bot.change_presence(activity=discord.Game(name=f'[>help]Bot正常稼働中 | サーバー数={len(bot.guilds)}'))

bot.remove_command('help') # コマンド「help」を削除

@bot.command()
async def help(help): # コマンド「help」を追加
    embed = discord.Embed(title="ヘルプ | Help", description="ヘルプページです\nOP=オペレーター専用\nBeta段階=試験段階(正常動作は保証しない\nDM=ダイレクトメッセージで実行可能)", color=0xff6600)  # 送信する内容
    embed.set_thumbnail(url="https://illust8.com/wp-content/uploads/2018/08/mark_hatena_question_illust_901.png")  # 表示する画像を指定
    embed.add_field(name="コマンド一覧", value="Call56Botで使えるコマンドの一覧です", inline=False)
    embed.add_field(name=">help", value="ヘルプを表示します[DM]", inline=False)
    embed.add_field(name=">mcsvconnect", value="MCサーバーの接続情報を見ることができます[DM]", inline=False)
    embed.add_field(name=">botinvite {Clientid}", value="ボットの招待リンクを生成します[DM]", inline=False)
    embed.add_field(name=">mcbefraudinfo", value="MCPEの不正情報を確認します[DM]", inline=False)
    embed.add_field(name=">mcsvadd {ServerName} {IP} {Port}", value="MCSVの追加リンクを生成します[DM]", inline=False)
    embed.add_field(name=">message {タイトル} {内容}", value="Embedメッセージを生成します[OP]", inline=False)
    embed.add_field(name=">clear", value="チャンネルのメッセージを削除します。[OP]", inline=False)
    embed.add_field(name=">kick @Mention {理由}", value="ユーザーをキックします[OP]", inline=False)
    embed.add_field(name=">ban @Mention {理由}", value="ユーザーをBanします[OP]", inline=False)
    embed.add_field(name=">myinfo", value="自分の情報を確認します", inline=False)
    embed.add_field(name=">mentionuserinfo @Mention", value="メンション先のユーザーの情報を確認します", inline=False)
    embed.add_field(name=">iduserinfo {ClientID}", value="該当するIDのユーザーの情報を確認します[Beta段階]", inline=False)
    embed.add_field(name=">server", value="メッセージを送信したDiscordサーバーの情報を確認します", inline=False)
    embed.add_field(name=">chinfo", value="チャンネルの情報を確認します。", inline=False)
    embed.add_field(name=">role {RoleID}", value="該当するIDのロールの基本的なパーミッションを確認します。[Beta段階]", inline=False)
    embed.add_field(name=">guildeditname {新しい名前} {変更理由}", value="サーバーの名前を変更します。[Beta段階 | OP]", inline=False)
    embed.add_field(name=">ping", value="Ping値を測定します。[Beta段階 | DM]", inline=False)
    embed.add_field(name=">mdm @Mention {送信内容}", value="メンション先のユーザーにダイレクトメッセージを送信します。[OP]", inline=False)
    embed.add_field(name=">report {内容}", value="レポートを行います。[DM]", inline=False)
    await help.send (embed=embed) # 内容を送信

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
async def ban(ban, member: discord.Member, *, reason=None): # コマンド「ban」を追加
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
async def mentionuserinfo(mentionuserinfo, member: discord.Member): # コマンド「mentionuserinfo」を追加
    if member.bot:
        b='Bot'
    else:
        b='User'
    embed=discord.Embed (title=f'基本ID={member}', description=f"ニックネーム={member.nick}\nID={member.id}\nアカウント作成日={member.created_at}\nサーバー参加日={member.joined_at}\nアカウントの種類={b}", color=0xff0000) # 送信する内容
    embed.set_thumbnail(url=f"{member.avatar_url}")
    await mentionuserinfo.send(embed=embed) # 内容を送信

@bot.command()
async def iduserinfo(iduserinfo, id: int): # コマンド「iduserinfo」を追加
    user = await bot.fetch_user(id)
    if user.bot:
        b='Bot'
    else:
        b='User'
    embed = discord.Embed(title=f'基本ID={user}', description=f"アカウント作成日={user.created_at}\nID={user.id}\nBotであるか(True=はい | False=いいえ)={b}", color=0xff0000) # 送信する内容
    embed.set_thumbnail(url=f"{user.avatar_url}")
    await iduserinfo.send(embed=embed) # 内容を送信

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

@bot.command()
async def report(report, *, main):
    dm = await bot.fetch_user(ID)
    embed = discord.Embed(title=f'Report | レポート元={report.author}', description=f'レポート内容={main}')
    await dm.send(embed=embed)
    await report.send('レポートが完了しました。')

bot.run('Token')
