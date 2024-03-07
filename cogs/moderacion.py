import discord
import asyncio
from discord.ext import commands


class Mod(commands.Cog):

    def __init__(self, client):
        self.client = client

    # comando para banear personas
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(member.mention + "fue banneado")
        await ctx.message.add_reaction('')  # agrega un emogi

    # comando para kickear personas
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(member.mention + "fue kickeado")
        await ctx.message.add_reaction('')  # agrega un emogi

    # comando para desbanear personas
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member: discord.Member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"{member} fue desbanneado")
                await ctx.message.add_reaction('')  # agrega un emogi

    #  mutea a una persona (le agrega un rol que le impide mandar mensajes)
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, member: discord.Member):
        muted_role = ctx.guild.get_role()  # hace falta el ID del rol
        await member.add_roles(muted_role)
        await ctx.send(member.mention + "fue muteado")
        await ctx.message.add_reaction('')  # agrega un emogi

    # desmutea a una persona (le quita el rol de muteado)
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def unmute(self, ctx, member: discord.Member):
        muted_role = ctx.guild.get_role()  # hace falta el ID del rol
        await member.remove_roles(muted_role)
        await ctx.send(member.mention + "fue desmuteado")
        await ctx.message.add_reaction('')  # agrega un emogi

    # borra mensajes por defecto 30
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=30):
        await ctx.channel.purge(limit=amount)
        await ctx.send(f"{amount} mensajes eliminados")
        print(f"{amount} cleared")


# carga la extencion al cliente principal
def setup(client):
    client.add_cog(Mod(client))
