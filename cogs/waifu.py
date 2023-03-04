from discord.ext import commands
from dotenv import load_dotenv
import os
import openai

class Waifu(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def chat(self, ctx, dere):

        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")

        prompt = f"""You are Bin-chan, a living uwu {dere} anime girl (aka a waifu). Please introduce yourself once and then wait for my response. After I respond, reply in the style of the {dere} anime archetype."""
        messages = [{'role': 'system', 'content': f'{prompt}'}]
        message = None

        while message != 'quit':
            if message: messages.append({'role': 'user', 'content': f'{message}'})
            response = openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                messages=messages,
                temperature=0.5
            )
            await ctx.send(response['choices'][0]['message']['content'])
            message = await self.bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
            message = message.content

        await ctx.send('bye bye!')
        


async def setup(bot):
    await bot.add_cog(Waifu(bot))