import discord
from discord.ext import commands

#Botin komentojen prefixin määritys
bot = commands.Bot(command_prefix = '-')

@bot.event
async def on_ready():
        print('Bot ready')

bot.run('')