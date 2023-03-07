import discord
from discord.ext import commands


class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title='**Available Commands:**', description='.chat -d [dere]\n .chat -c [character]\n.quit to end chat', color=0x36393f)
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Help(bot))
