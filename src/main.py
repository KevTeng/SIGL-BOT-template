import os

from discord import Permissions
from discord.ext import commands
from dotenv import load_dotenv
import discord
from discord.utils import get

load_dotenv()

bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True,  # Commands aren't case-sensitive
    intents=discord.Intents.all()
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

@bot.command()
async def name(ctx):
    name = ctx.author.display_name
    await ctx.send(name)




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

@bot.command()
async def mute(ctx, member: discord.Member):
    guild = ctx.guild

    # if not get(ctx.guild.roles, name="Ghost"):
    role = await guild.create_role(name="Ghost", permissions=Permissions(send_messages=False))
    await member.add_roles(role)
    await ctx.send(f'{member} +  is muted. good night :)')






@bot.command()
async def admin(ctx, member: discord.Member):
    guild = ctx.guild
    roles = guild.roles

    check_role = 0
    for role in roles:
        if role.name == "Admin":
            admin_role = role
            check_role = 1
            break
    if not check_role:
        admin_role = await guild.create_role(name="Admin", permissions=Permissions(manage_channels=True, ban_members=True, kick_members=True))

    for role_member in member.roles:
        if role_member.name == admin_role.name:
            await ctx.send(f"User {member} already has the role Admin")
            return

    await member.add_roles(admin_role)
    await ctx.send(f"User {member} is now an admin ! Gz")
            
@bot.command()
async def ban(ctx, member: discord.Member):
    await member.ban()
    await ctx.send(f"{member.display_name} has been banned :o")

if __name__ == '__main__':

    bot.run(TOKEN)  # Starts the bot