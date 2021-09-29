import os
from discord.ext import commands

import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True  # Commands aren't case-sensitive
)

TOKEN = os.getenv('DISCORD_TOKEN')




bot.author_id = 7300  # Change to your discord id!!!

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx):
    await ctx.send('pong')


if __name__ == '__main__':

    bot.run(TOKEN)  # Starts the bot