#import discord
#from discord.ext import commands, tasks

import discord
import random
from discord.ext import commands
from discord import embeds
from discord.colour import Color

#noa esquecer que o b é maiusculo bot = commands.Bot("$")
bot = commands.Bot("!")

@bot.event
async def on_ready():
    print (f"o {bot.user} está online")


@bot.command(name ="oi")
async def ola (ctx):
    name = ctx.author.name

    response = "ola, " + name 

    await ctx.send (response)


@bot.command(name ="pv")
async def pv(ctx):

    name = ctx.author.name

    await ctx.author.send("ola, " + name)



@bot.command(name ="game")
async def game(ctx):
    
    number = random.randint(1, 6)

    if number == 1:
        await ctx.send (f"voçê tirou impar. ({number})")

    if number == 2:
        await ctx.send (f"voçê tirou par. ({number})")

    if number == 3:
        await ctx.send (f"voçê tirou impar. ({number})")

    if number == 4:
        await ctx.send (f"voçê tirou par. ({number})")

    if number == 5:
        await ctx.send (f"voçê tirou impar. ({number})")

    if number == 6:
        await ctx.send (f"voçê tirou par. ({number})")


@bot.command(name = "comandos")
async def comandos(ctx):
    embed = discord.Embed(
        title = "Comandos",
        description = "Listagem de Comandos deste servidor",
        color = 0x800080
    )

    embed.set_author(name=bot.user.name, icon_url = bot.user.avatar_url)
    embed.add_field(name="------------------------------------------------------------------------", value="!oi  !pv  !game")

    await ctx.send(embed=embed)





bot.run ("aqui vai o token")