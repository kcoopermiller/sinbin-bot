from discord.ext import commands
from dotenv import load_dotenv
import os
import openai

class Waifu(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def chat(self, ctx, flag=None, *, args=None):

        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")

        if flag == '-d': prompt = f"""You are going to pretend to be Bin-chan. Bin-chan is an anime girl (aka a waifu) that closely resembles the {args} archetype. Please introduce yourself in the style of the {args} anime archetype."""
        if flag == '-c': prompt = f"""You are going to pretend to be an anime girl version of {args}. If {args} is already an anime character then just act similarly to how they do. If they are not an anime charcter, then add some traits that you'd find in an anime girl to your impersonation of {args} (your goal is to be a waifu version of {args}). Now, please introduce yourself."""
        else: 
            await ctx.send('Please specify a flag\n.chat -d [dere]\n.chat -c [character]')
            return

        messages = [{'role': 'system', 'content': f'{prompt}'}]
        message = ''

        while message.lower() != 'quit':
            if message != '': messages.append({'role': 'user', 'content': f'{message}'})
            response = openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                messages=messages,
                temperature=0.5
            )
            if len(messages) == 0: 
                if flag == '-d': messages.append({'role': 'system', 'content': f'Now lets have a conversation. Reply to my messages in the style of the {args} anime archetype. Remember to stay in character!'}) 
                if flag == '-c': messages.append({'role': 'system', 'content': f'Now lets have a conversation. Reply to my messages in the style of {args}. Remember to stay in character!'})
            await ctx.send(response['choices'][0]['message']['content'])
            messages.append({'role': 'assistant', 'content': f'{response["choices"][0]["message"]["content"]}'})
            message = await self.bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
            message = message.content

        await ctx.send('Bye bye!')
        


async def setup(bot):
    await bot.add_cog(Waifu(bot))