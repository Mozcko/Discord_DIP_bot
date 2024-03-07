import discord
import asyncio
from random import randint
from discord.ext import commands
from constants import rules, comms


class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client

    # muestra el conjunto de reglas del servidor
    @commands.command()
    async def reglas(self, ctx):
        message = await ctx.send("writing rules...")
        color = randint(0, 0xFFFFFF)
        pEmbed = discord.Embed(title="Rules", color=color)
        for i in rules:
            pEmbed.add_field(name=i, value=rules[i], inline=False)
        pEmbed.add_field(
            value=" recuerda que si tienes alguna duda o necesitas ayuda puedes preguntar a cualquiera con el rol de scouter",
            inline=True)

        await message.edit(content=None, embed=pEmbed)
        await ctx.message.add_reaction('')  # agrega un emogi

    # comando de ayuda personalizado
    @commands.command()
    async def help(self, ctx):
        message = await ctx.send("escribiendo el comando de ayuda")
        color = randint(0, 0xFFFFFF)
        embed = discord.Embed(title="Help", color=color)
        for i in comms:
            embed.add_field(name=i, value=comms[i], inline=True)

        await message.edit(content=None, embed=embed)
        await ctx.message.add_reaction('')  # agrega un emogi

    # envia un link de invitacion que no expira
    @commands.command()
    async def invite(self, ctx):
        await ctx.send("usa este enlace para invitar a otros")
        await ctx.send("")  # falta agregar el link
        await ctx.message.add_reaction('')  # agrega un emogi

    # buzon de quejas (no sirve)
    @commands.command()
    async def sugerencias(self, ctx):
        embeed = discord.Embed(
            title="si tienes alguna sugerencia, usa este link para mandarla",
            description="",  # falta el link
            color=randint(0, 0xFFFFFF), )
        await ctx.send(embed=embeed)


def setup(client):
    client.add_cog(Misc(client))
