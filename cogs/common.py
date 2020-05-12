import discord
from discord.ext import commands, tasks

class Common(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #Rivien tyhjennyskomento, toimii vain jos käyttäjällä on oikeus poistaa muiden kommentteja
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount : int):
        await ctx.channel.purge(limit=amount)


def setup(bot):
    bot.add_cog(Common(bot))