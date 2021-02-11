import discord
from discord.ext import commands
import json

with open("data.json", "r") as data_file:
    data = json.load(data_file)
    prefix = data["prefix"]
    token = data["token"]


client = commands.Bot(
    command_prefix=prefix, status="online", activity=discord.Game(name="test")
)


@client.event
async def on_ready():
    print("Bot is ready!")


# * ping command - shows bot ping
@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")


client.run(token)
