import discord
from discord.ext import commands
import requests
import json
parameters = {"limit":1}
class Dota(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

#komennot joilla kaverit voi tarkastella toistensa edellisen dotapelin voittoa
    @commands.command()
    async def betsVD(self, ctx):
        r = requests.get('https://api.opendota.com/api/players/1807096/wl', params = parameters)
        data = r.json()
        if data['win'] == 1:
            await ctx.send("Ez win")
        else:
            await ctx.send("nope")

    @commands.command()
    async def betsKirillos(self, ctx):
        r = requests.get('https://api.opendota.com/api/players/16562021/wl', params = parameters)
        data = r.json()
        if data['win'] == 1:
            await ctx.send("Ez win")
        else:
            await ctx.send("nope")

    @commands.command()
    async def betsOskari(self, ctx):
        r = requests.get('https://api.opendota.com/api/players/23007265/wl', params = parameters)
        data = r.json()
        if data['win'] == 1:
            await ctx.send("Ez win")
        else:
            await ctx.send("nope")

    @commands.command()
    async def betsOtso(self, ctx):
        r = requests.get('https://api.opendota.com/api/players/45675850/wl', params = parameters)
        data = r.json()
        if data['win'] == 1:
            await ctx.send("Ez win")
        else:
            await ctx.send("nope")

    @commands.command()
    async def betsSara(self, ctx):
        r = requests.get('https://api.opendota.com/api/players/41632943/wl', params = parameters)
        data = r.json()
        if data['win'] == 1:
            await ctx.send("Ez win")
        else:
            await ctx.send("nope")

def setup(bot):
    bot.add_cog(Dota(bot))