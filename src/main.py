import os
from discord.ext import commands
from discord import Role, Permissions, colour, guild, permissions, Colour, Member
from discord.ext.commands.errors import BadInviteArgument
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

@bot.command()
async def name(ctx):
    name = ctx.author.display_name
    await ctx.send(name)



@bot.command()
async def admin(ctx, member: Member):
    guild = ctx.guild
    roles = guild.roles

    check_member = 0
    for user in guild.members:
        if user.display_name == member.display_name:
            check_member = 1
            break
    if check_member:
        ctx.sed(f"User nickname {member.display_name} doesn't exist :(")
        return

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
            


if __name__ == '__main__':

    bot.run(TOKEN)  # Starts the bot