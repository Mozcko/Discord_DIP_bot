import discord
import asyncio
from random import randint
from discord.ext import commands
from discord import Embed
from constants import rules, comms, exp_comms


class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client

    # # muestra el conjunto de reglas del servidor
    # @commands.command()
    # async def reglas(self, ctx):
    #     # crea un mensaje temporal en lo que se recibe respuesta
    #     message = await ctx.send("writing rules...")

    #     color = randint(0, 0xFFFFFF)

    #     # crea un embed vacío
    #     embed = discord.Embed(title="Rules", color=color)

    #     # itera dentro de las reglas del servidor y las agrega al embed
    #     for i in rules:
    #         embed.add_field(name=i, value=rules[i], inline=True)
    #     embed.add_field(
    #         name="",
    #         value=" Recuerda que si tienes dudas puedes contactar con un Admin",
    #         inline=True)

    #     # modifica el mensaje temporal y envía la modificación 
    #     await message.edit(content=None, embed=embed)
    #     await ctx.message.add_reaction('📜')  # agrega un emoji


    # comando de ayuda personalizado
    @commands.command()
    async def help(self, ctx, command=None) -> None:
        color: int = randint(0, 0xFFFFFF)
        
        # revisa si se pidió información sobre un comando especifico
        if command is not None:

            # revisa que se tenga registro del comando
            if command not in exp_comms:
                await ctx.send("Comando no encontrado")
                return
            
            # encuentra el comando dentro de exp_comms
            comando = exp_comms[command]

            # crea un Embed vacío
            embed = Embed(title=f"Explicación del comando {command}", color=color)

            # apartado de permisos
            if comando["permission"] is not None:
                embed.add_field(name="Permisos para usarlo", value=comando["permission"], inline=False)

            # apartado de descripción
            if comando["description"] is not None:
                embed.add_field(name="Descripción del comando", value=comando["description"], inline=False)

            # apartado de uso
            if comando["usage"] is not None:
                embed.add_field(name="Ejemplo de Uso", value=comando["usage"], inline=False)

            # apartado de Special
            if comando["Special"] is not None:
                embed.add_field(name="Casos especiales", value=comando["Special"], inline=False)

            await ctx.send(embed=embed)
            await ctx.message.add_reaction('👍')  # agrega un emoji
            return

        # crea un mensaje temporal en lo que se recibe respuesta
        message = await ctx.send("escribiendo el comando de ayuda")

        # crea un Embed vacío
        embed = Embed(title="Commandos utilizables", color=color)

        # itera dentro de os comandos del servidor y los agrega al embed
        for i in comms:
            embed.add_field(name=i, value=comms[i], inline=False)

        # modifica el mensaje temporal y envía la modificación 
        await message.edit(content=None, embed=embed)
        await ctx.message.add_reaction('👍')  # agrega un emoji

    # crea y envía un link de invitación temporal para el servidor
    @commands.command()
    async def invite(self, ctx) -> None:
        # crea el link de invitación temporal
        link: str = await ctx.channel.create_invite(max_age = 300)

        # crea el mensaje con el link de invitación temporal
        content = f"usa este enlace para invitar a otros {link}"

        await ctx.send(content)
        await ctx.message.add_reaction('🔗')  # agrega un emoji

    # envía un embed con un link a un google forms para buzón de quejas
    @commands.command()
    async def sugerencias(self, ctx) -> None:
        color: int = randint(0, 0xFFFFFF)
        link: str = ""  # falta el link
        embed = Embed(
            title="si tienes alguna sugerencia, usa este link para mandarla",
            description=link,
            color = color)
        await ctx.send(embed=embed)

# función de Setup para la extension de comandos
async def setup(client) -> None:
    await client.add_cog(Misc(client))
