import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.all()  # permite todos los intents
intents.members = True
help_command = commands.DefaultHelpCommand(no_category="Miscelánea")  # se crea un comando de ayuda
client = commands.Bot(command_prefix=os.getenv("PREFIX"), help_command=help_command, intents=intents)
client.remove_command("help")  # se remueve el comando por defecto (se hará uno mas adelante)
emojis = None


@client.event
async def on_ready():
    try:  # Comprueba si se puede conectar al bot
        print(f'Login successful, Logged in as {client.user}')

        # carga el resto de comandos
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                await client.load_extension(f"cogs.{filename[:-3]}")
    except Exception as e:
        print(f"[!] Couldn't connect, an Error occurred {e}")


# carga los emojis personalizados del server
@client.command()
async def setup(ctx):
    global emojis
    if not emojis:
        emojis = {e.name: str(e) for e in ctx.bot.emojis}
    await ctx.send("Setup completo")
    await ctx.message.add_reaction('👍')


if __name__ == '__main__':
    client.run(os.getenv("TOKEN"))
