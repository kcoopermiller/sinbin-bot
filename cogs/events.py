import discord
from discord.ext import commands
from discord.utils import get



class Events(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=".help"))


async def setup(bot):
    await bot.add_cog(Events(bot))
