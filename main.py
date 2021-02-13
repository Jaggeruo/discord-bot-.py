import discord
from discord.ext import commands
import json
from os import listdir

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

for cog_file in listdir("./cogs"):
    if cog_file.endswith(".py"):
        client.load_extension(f"cogs.{cog_file[:-3]}")


def owner_check(user):
    if user == owner:
        return True


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
    if owner_check(ctx.message.author.id):
        await client.close()
    else:
        await ctx.send("You don't own this bot")


@client.command()
async def load(ctx, cogName):
    if owner_check(ctx.message.author.id):
        try:
            client.load_extension(f"cogs.{cogName.lower()}")
        except commands.ExtensionNotFound:
            await ctx.send(f"{cogName} don't exist")
        except commands.ExtensionAlreadyLoaded:
            await ctx.send(f"{cogName} already loaded")
    else:
        await ctx.send("You are not the owner")


@client.command()
async def unload(ctx, cogName):
    if owner_check(ctx.message.author.id):
        try:
            client.unload_extension(f"cogs.{cogName.lower()}")
        except commands.ExtensionNotLoaded:
            await ctx.send(f"{cogName} isn't loaded")
    else:
        await ctx.send("You are not the owner")


@client.command()
async def reload(ctx, cogName):
    if owner_check(ctx.message.author.id):
        try:
            client.reload_extension(f"cogs.{cogName.lower()}")
        except commands.ExtensionNotLoaded:
            await ctx.send(f"{cogName} isn't loaded")
        except commands.ExtensionNotFound:
            await ctx.send(f"{cogName} don't exist loaded")
    else:
        await ctx.send("You are not the owner")


client.run(token)
