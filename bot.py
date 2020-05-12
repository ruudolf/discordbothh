import discord
import os
from discord.ext import commands, tasks


#Botin komentojen prefixin määritys
bot = commands.Bot(command_prefix = '-')

@bot.event
async def on_ready():
        print('Bot ready')

#Cogien load komennot 
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')

@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    
#helpotusta cogien kutsumiseen
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run('')