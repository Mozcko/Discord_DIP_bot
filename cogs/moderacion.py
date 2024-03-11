import discord
import asyncio
from discord.ext import commands


# se puede utilizar asyncio y time para efectuar los comandos de forma temporal
# en lugar de hacerlo de forma permanente 


class Mod(commands.Cog):

    def __init__(self, client):
        self.client = client

    # comando para dar ban a personas
    @commands.command()
    @commands.has_permissions(ban_members=True)  # comprueba los permisos del usuario
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} fue banneado")
        await ctx.message.add_reaction('🤡')  # agrega un emoji

    # comando para kickear personas
    @commands.command()
    @commands.has_permissions(kick_members=True)  # comprueba los permisos del usuario
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} fue kickeado")
        await ctx.message.add_reaction('🤡')  # agrega un emoji

    # comando para des bannear personas
    @commands.command()
    @commands.has_permissions(ban_members=True)  # comprueba los permisos del usuario
    async def unban(self, ctx, *, member: discord.Member):
        # obtiene la lists de los usuarios banneados
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")
        found: bool = False

        # busca si el usuario esta en la lista de los usuarios banneados
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                found = True
                await ctx.guild.unban(user)  # quita el ban
                await ctx.send(f"{member} fue des banneado")
                await ctx.message.add_reaction('🤡')  # agrega un emoji

        # si no encuentra al usuario se notifica
        if not found:
            await ctx.send(f"{member} No fue encontrado")
            await ctx.message.add_reaction('🤡')  # agrega un emoji

    # borra mensajes por defecto 30
    @commands.command()
    @commands.has_permissions(manage_messages=True)  # comprueba los permisos del usuario
    async def clear(self, ctx, amount=30):
        await ctx.channel.purge(limit=amount)
        await ctx.send(f"{amount} mensajes eliminados")
        print(f"{amount} cleared")

    #  mutea a una persona (le agrega un rol que le impide mandar mensajes)
    @commands.command()
    @commands.has_permissions(manage_messages=True)  # comprueba los permisos del usuario
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member: discord.Member):
        # obtiene el rol que mutea a la persona
        muted_role = ctx.guild.get_role()  # hace falta el ID del rol

        # agrega el rol
        await member.add_roles(muted_role)
        await ctx.send(f"{member.mention} fue muteado")
        await ctx.message.add_reaction('🤡')  # agrega un emoji

    # des mutea a una persona (le quita el rol de muteado)
    @commands.command()
    @commands.has_permissions(manage_messages=True)  # comprueba los permisos del usuario
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, member: discord.Member):
        # obtiene el rol que mutea a la persona
        muted_role = ctx.guild.get_role()  # hace falta el ID del rol

        # remueve el rol
        await member.remove_roles(muted_role)
        await ctx.send(f"{member.mention} fue des muteado")
        await ctx.message.add_reaction('🤡')  # agrega un emoji


# función de Setup para la extension de comandos
async def setup(client):
    await client.add_cog(Mod(client))
