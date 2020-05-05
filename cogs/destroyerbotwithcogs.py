import discord
from discord.ext import commands
import time

class Example(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.is_purge_active = 0
        self.amount = 600

    @commands.Cog.listener()
    async def on_ready(self):
        print("bot is online")

    @commands.Cog.listener()
    async def on_message(self,message):
        channel = message.channel
        if self.is_purge_active == 1:
            print("Purge Is Active")
            time.sleep(self.amount)
            await channel.purge(limit = None)
        elif self.is_purge_active == 0:
            print("Purge Is Not Active")

    @commands.command()
    async def status(self, ctx):
        print(self.is_purge_active)
        await ctx.send("Purge Is Set To: {}")
        await ctx.send(self.is_purge_active)

    @commands.command()
    async def activate_purge(self, ctx, a: int):
        print(self.is_purge_active)
        self.is_purge_active = a

    @commands.command()
    async def set(self, ctx, amount: int):
        print(amount)
        self.amount = amount
        await ctx.send("Purge Time Is Set To:")
        await ctx.send(self.amount)

def setup(client):
    client.add_cog(Example(client))
