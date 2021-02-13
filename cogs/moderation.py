import discord
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("test1")


def setup(client):
    client.add_cog(Moderation(client))
    print("Moderation cog loaded")
