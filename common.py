import discord
from discord.ext import commands, tasks

class Common(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    #Olemattomasta commandista huomautus
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send('Command not found')
      
    #Rivien tyhjennyskomento, toimii vain jos käyttäjällä on oikeus poistaa muiden kommentteja
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount : int):
        await ctx.channel.purge(limit=amount)

   
    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Specify message clear amount')

def setup(bot):
    bot.add_cog(Common(bot))