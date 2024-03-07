import discord
import os
from openai import OpenAI
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

class Chat(commands.Cog):
    def __init__(self, client):
        self.__AI_TOKEN = os.getenv("OPENAI_API_KEY")
        self.__AI_ORGANIZATION = os.getenv("OPENAI_ORGANIZATION")
        self.client = client

        self.chat = OpenAI(
            api_key=self.__AI_TOKEN,
            organization=self.__AI_ORGANIZATION
        )

    @commands.command()
    async def gpt(self, ctx, *,message):
        output = self.client.chat.completions.create(model='gpt-3.5-turbo',
                                                     messages=[
                                                         {"role": "user",
                                                          "content":
                                                              message}
                                                     ])

        await ctx.send(output.choices[0].message.content)
        await ctx.message.add_reaction('')  #agrega un emoji

def setup(client):
    client.add_cog(Chat(client))