import discord
from discord.ext import commands
import json

with open("data.json", "r") as data_file:
    data = json.load(data_file)
    prefix = data["prefix"]
    token = data["token"]
    owner = data["owner"]


client = commands.Bot(
    command_prefix=prefix,
    status="online",
    activity=discord.Game(name="h.help"),
    case_insensitive=False,
    self_bot=False,
    help_command=None,
)


@client.event
async def on_ready():
    print("Bot is ready!")


@client.command()
async def ping(ctx):
    # * Shows bot ping
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")


@client.command(aliases=["close", "quit"])
async def logout(ctx):
    # * End bot connection (only by owner specified in data.json file)
    if ctx.message.author.id == owner:
        await client.close()
    else:
        await ctx.send("You don't own this bot")


client.run(token)
