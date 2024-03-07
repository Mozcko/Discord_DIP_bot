import discord
import asyncio
from discord.ext import commands
from ytomp3 import give_link, download_vid, find_music_name, remove_all_files


class Music(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def pause(self, ctx):
        if ctx.voice_client and ctx.voice_client.is_playing():  # if the music is already playing
            ctx.voice_client.pause()  # pausing the music
            await ctx.send("Playback paused.")  # sending confirmation on  channel
        else:
            await ctx.send(
                '[-] An error occured: You have to be in voice channel to use this commmand')  # if you are not in vc

    @commands.command()
    async def resume(self, ctx):
        if ctx.voice_client and ctx.voice_client.is_paused():  # If the music is already paused
            ctx.voice_client.resume()  # resuming the music
            await ctx.send("Playback resumed.")  # sending confirmation on  channel
        else:
            await ctx.send(
                '[-] An error occured: You have to be in voice channel to use this commmand')  # if you are not in vc

    @commands.command()
    async def leave(self, ctx):
        if ctx.voice_client:  # if you are in vc
            await ctx.guild.voice_client.disconnect()  # disconnecting from the vc
            await ctx.send("Lefted the voice channel")  # sending confirmation on channel
            sleep(1)
            remove_all_files(
                "music")  # deleting the all the files in the folder that  we downloaded to not waste space on your pc

        else:
            await ctx.send(
                "[-] An Error occured: You have to be in a voice channel to run this command")  # if you are not in vc

    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice:
            channel = ctx.message.author.voice.channel
            try:
                await channel.connect()  # connecting to channel
            except:
                await ctx.send("[-] An error occured: Couldn't connect to the channel")  # if there is an error

        else:
            await ctx.send(
                "[-] An Error occured: You have to be in a voice channel to run this command")  # if you are not in vc

    @commands.command(name="play")
    async def play(self, ctx, *, title):
        download_vid(title)  # Downloading the mp4 of the desired vid
        voice_channel = ctx.author.voice.channel

        if not ctx.voice_client:  # if you are not in  vc
            voice_channel = await voice_channel.connect()  # connecting to vc

        try:
            async with ctx.typing():
                player = discord.FFmpegPCMAudio(executable="C:\\ffmpeg\\ffmpeg.exe",
                                                # hay que cambiarlo para que funcione en linux
                                                source=f"music/{find_music_name()}")  # executable part is where we downloaded ffmpeg. We are writing our find_mmusic name func because , we want to bot to play our desired song fro the folder
                ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
            await ctx.send(f'Now playing: {find_music_name()}')  # sening confirmmation

            while ctx.voice_client.is_playing():
                await asyncio.sleep(1)
            delete_selected_file(find_music_name())  # deleting the file after it played

        except Exception as e:
            await ctx.send(f'Error: {e}')  # sending error


def setup(client):
    client.add_cog(Music(client))
