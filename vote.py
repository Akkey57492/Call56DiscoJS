import discord
from discord.ext import tasks

client = discord.Client()

channel_sent = None
@tasks.loop(hours=24)
async def vote24h():
    embed = discord.Embed(title="投票", description=f"monocraftで\nCall56NetWorkJava版\nに投票しませんか?\n投票し続けると「投票ガチ勢」になれます。")
    embed.add_field(name="投票を行う",value="[投票](https://monocraft.net/servers/PB5nBWoSHtg3dNkQmuFp)")
    await channel_sent.send(embed=embed)
@client.event
async def on_ready():
    global channel_sent
    channel_sent = client.get_channel(ID)
    vote24h.start()

client.run("BotToken")
