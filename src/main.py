import os
from discord.ext import commands
from dotenv import load_dotenv
import discord

load_dotenv()


bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True,  # Commands aren't case-sensitive
    intents=discord.Intents.all()
)

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
client = discord.Client(intents=intents)



bot.author_id = 7300  # Change to your discord id!!!

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx):
    await ctx.send('pong')




@bot.command()
async def count(ctx):
    online = []
    offline = []
    dnd = []
    idle = []

    for member in ctx.guild.members:
        if member.raw_status == 'online':
            online.append(member.name)
        elif member.raw_status == 'dnd':
            dnd.append(member.name)
        elif member.raw_status  == 'idle':
            idle.append(member.name)
        else:
            offline.append(member.name)
    await ctx.send(f'{len(online)} Online member(s): {online}')
    #

    await ctx.send(f'{len(dnd)} Do not disturb member(s): {dnd}')


    await ctx.send(f'{len(idle)} Absent member(s): {idle}')


    await ctx.send(f'{len(offline)} Offline member(s): {offline}')


if __name__ == '__main__':
    bot.run(TOKEN)  # Starts the bot