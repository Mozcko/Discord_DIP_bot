import discord
from discord.ext import commands
import pytube
from discord import FFmpegPCMAudio

class Music(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.is_playing = False

        # Parametros de FFmpeg
        self.ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("No estas en un canal de voz")
            return

        voice_client = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice_client is None:
            try:
                voice_client = await ctx.author.voice.channel.connect()
            except Exception as e:
                await ctx.send("No pude conectarme al canal de voz")
        else:
            try:
                await voice_client.move_to(ctx.author.voice.channel)
            except Exception as e:
                await ctx.send("No pude moverme al canal de voz")

    @commands.command()
    async def leave(self, ctx):
        voice_client = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice_client.is_connected():
            await voice_client.disconnect()
        else:
            await ctx.send("No estoy conectado a ningun canal de voz")
   
    @commands.command()
    async def play(self, ctx, url):
        if not ctx.message.author.voice:
            await ctx.send("No estas en un canal de voz")
            return

        voice_channel = ctx.message.author.voice.channel
        voice_client = discord.utils.get(self.client.voice_clients, guild=ctx.guild)

        if not voice_client:
            voice_client = await ctx.author.voice.channel.connect()

        try:
            yt = pytube.YouTube(url)
            stream = yt.streams.filter(only_audio=True).first()
            audio_file = stream.download()

            source = FFmpegPCMAudio(audio_file)
            voice_client.play(source)
        except Exception as e:
            await ctx.send("Ocurrió un error al intentar reproducir el audio.")

    @commands.command()
    async def pause(self, ctx):
        voice_client = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice_client.is_playing():
            voice_client.pause()
        else:
            await ctx.send("No estoy reproduciendo nada en este momento")

    @commands.command()
    async def resume(self, ctx):
        voice_client = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice_client.is_paused():
            voice_client.resume()
        else:
            await ctx.send("No estaba en pausa")

    @play.error
    async def play_error(self, ctx, error):
        if isinstance(error, commands.UserInputError):
            await ctx.send("URL o comando invalido")

    @join.error
    async def join_error(self, ctx, error):
        if isinstance(error, commands.UserInputError):
            await ctx.send("Necesitas estar en un canal de voz para usar este comando")

async def setup(client):
    await client.add_cog(Music(client))
