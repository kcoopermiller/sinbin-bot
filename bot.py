from discord.ext import commands
import os
from dotenv import load_dotenv
import discord
import asyncio

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='.', help_command=None, intents=discord.Intents.all())

async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await load_extensions()
        await bot.start(TOKEN)
        
asyncio.run(main())