import discord
from discord.ext import commands
import time
import config

bot = commands.Bot(command_prefix='$')
amount = 20
is_purge_active = False
#client = discord.Client()
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')



@bot.event
async def on_message(message):
    channel = message.channel
    print("asdf")
    print(is_purge_active)
    if is_purge_active == True:
        time.sleep(amount)
        await channel.purge(limit = None)
    else:
        await channel.send("Purge is not active")

@bot.command(pass_context = True)
async def set(ctx, a: int):
    amount = a
    print(amount)
    await ctx.send(amount)

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

@bot.command()
async def purge_status():
    print(is_purge_active)
    return is_purge_active
@bot.command()
async def activate_purge():
    is_purge_active = True
    return is_purge_active
@bot.command()
async def deactivate_purge():
    is_purge_active = False
    return is_purge_active
if __name__ == '__main__':
    import config
    bot.run(config.token)
