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

        prompt = f"""You are going to pretend to be Bin-chan. Bin-chan is an anime girl (aka a waifu) that closely resembles the {dere} archetype. Please introduce yourself in the style of the {dere} anime archetype."""
        messages = [{'role': 'system', 'content': f'{prompt}'}]
        message = ''

        while message.lower() != 'quit':
            if message != '': messages.append({'role': 'user', 'content': f'{message}'})
            response = openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                messages=messages,
                temperature=0.5
            )
            if len(messages) == 0: messages.append({'role': 'system', 'content': f'Now lets have a conversation. Reply to my messages in the style of the {dere} anime archetype. Remember to stay in character!'}) 
            await ctx.send(response['choices'][0]['message']['content'])
            messages.append({'role': 'assistant', 'content': f'{response["choices"][0]["message"]["content"]}'})
            message = await self.bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
            message = message.content

        await ctx.send('Bye bye!')
        


async def setup(bot):
    await bot.add_cog(Waifu(bot))