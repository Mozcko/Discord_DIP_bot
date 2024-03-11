import discord
import asyncio
from random import randint
from discord.ext import commands
from constants import rules, comms


class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client

    # # muestra el conjunto de reglas del servidor
    # @commands.command()
    # async def reglas(self, ctx):
    #     message = await ctx.send("writing rules...")
    #     color = randint(0, 0xFFFFFF)
    #     embed = discord.Embed(title="Rules", color=color)
    #     for i in rules:
    #         embed.add_field(name=i, value=rules[i], inline=False)
    #     embed.add_field(
    #         name="",
    #         value=" Recuerda que si tienes dudas puedes contactar con un Admin",
    #         inline=True)

    #     await message.edit(content=None, embed=embed)
    #     await ctx.message.add_reaction('📜')  # agrega un emogi

    # comando de ayuda personalizado
    @commands.command()
    async def help(self, ctx) -> None:
        message = await ctx.send("escribiendo el comando de ayuda")
        color: int = randint(0, 0xFFFFFF)
        embed = discord.Embed(title="Commandos utilizables", color=color)
        for i in comms:
            embed.add_field(name=i, value=comms[i], inline=True)

        await message.edit(content=None, embed=embed)
        await ctx.message.add_reaction('👍')  # agrega un emogi

    # envia un link de invitacion que no expira
    @commands.command()
    async def invite(self, ctx) -> None:
        await ctx.send("usa este enlace para invitar a otros")
        await ctx.send("")  # falta agregar el link
        await ctx.message.add_reaction('')  # agrega un emogi

    # buzon de quejas (no sirve)
    @commands.command()
    async def sugerencias(self, ctx) -> None:
        color: int = randint(0, 0xFFFFFF)
        link: str = ""  # falta el link
        embeed = discord.Embed(
            title="si tienes alguna sugerencia, usa este link para mandarla",
            description=link,
            color = color)
        await ctx.send(embed=embeed)


async def setup(client) -> None:
    await client.add_cog(Misc(client))
