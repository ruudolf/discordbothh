import discord
from discord.ext import commands

#Botin komentojen prefixin määritys
bot = commands.Bot(command_prefix = '-')

@bot.event
async def on_ready():
        print('Bot ready')

@bot.event
async def on_member_join(member):
    print(f'{member} has joined the server.')

@bot.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

@bot.command
async def clear(ctx, amount=3):
    await ctx.channel.purge(limit=amount)


bot.run('')