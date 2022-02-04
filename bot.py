import discord
from discord.ext import commands
from discord_slash import SlashCommand
from vars import *
from confidential import *
import db.dbfunc as dbfunc

intents = discord.Intents.default()
intents.presences = True
client = commands.Bot("~", intents=intents)
slash = SlashCommand(client, sync_commands=True, override_type=True)

@client.event
async def on_ready():
    print("Spoticord is online")

@slash.slash(name='dummmy', guild_ids=GUILD_IDS)
async def dummmy(ctx):
    dbfunc.get_user_ids()
    await ctx.send("Dummmy thick ;)")




client.run(RUN_ID)