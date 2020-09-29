import discord # discord.py

client = discord.Client()

ID_CHANNEL_README = ChannelID # チャンネルID
ID_ROLE_WELCOME = RoleID # ロールID

@client.event
async def on_raw_reaction_add(payload):
    channel = client.get_channel(payload.channel_id)

    if channel.id != ID_CHANNEL_README:
        return
    guild = client.get_guild(payload.guild_id)

    member = guild.get_member(payload.user_id)

    role = guild.get_role(ID_ROLE_WELCOME)

    await member.add_roles(role)

client.run('BotToken') # ボットトークン(BotToken)
