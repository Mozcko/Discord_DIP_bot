import discord
import os

from openai import APIConnectionError
from openai import RateLimitError
from openai import APIStatusError
from openai import BadRequestError
from openai import OpenAI
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

class Chat(commands.Cog):
    def __init__(self, client):
        self.__AI_TOKEN = os.getenv("OPENAI_API_KEY")
        self.__AI_ORGANIZATION = os.getenv("OPENAI_ORGANIZATION")
        self.client = client

        self.__client = OpenAI(
            organization=self.__AI_ORGANIZATION,
            api_key=self.__AI_TOKEN
        )
        
    @commands.command()
    async def ask(self, ctx, *,message):
        try: 
            output = self.__client.chat.completions.create(model='gpt-3.5-turbo-0125',
                                                        messages=[
                                                            {"role": "user",
                                                            "content":
                                                                message}
                                                        ])

            await ctx.send(output.choices[0].message.content)
            await ctx.message.add_reaction('🤖')  #agrega un emoji

        except APIConnectionError as e: 
            print("Server connection error: {e.__cause__}")
            await ctx.send(f'Hubo un error con la conexión con Chat GPT')
        except RateLimitError as e:
            print(f"OpenAI RATE LIMIT error {e.status_code}: (e.response)")
            await ctx.send(f'Se acabaron los fondos XD')
        except APIStatusError as e:
            print(f"OpenAI STATUS error {e.status_code}: (e.response)")
            await ctx.send(f'El estatus de ChatGPT no es optimo')
        except BadRequestError as e:
            print(f"OpenAI BAD REQUEST error {e.status_code}: (e.response)")
            await ctx.send(f'Hubo un error inesperado')
        except Exception as e:
            print(f'Exception raised {e} cause: {e.__cause__}')

    @commands.command()
    async def visualize(self, ctx, *, message):
        try:
            response = await ctx.send("generando imagen")
            output = self.__client.images.generate(
                model="dall-e-2",
                prompt=message,
                size="512x512",
                quality="standard",
                n=1,
            )
            await response.edit(content=output.data[0].url, embed=None)
            await ctx.message.add_reaction('🖼')  #agrega un emoji
        
        except APIConnectionError as e: 
            print("Server connection error: {e.__cause__}")
            await ctx.send(f'Hubo un error con la conexión con Chat GPT')
        except RateLimitError as e:
            print(f"OpenAI RATE LIMIT error {e.status_code}: {e.response}")
            await ctx.send(f'Se acabaron los fondos XD')
        except APIStatusError as e:
            print(f"OpenAI STATUS error {e.status_code}: {e.response}")
            await ctx.send(f'El estatus de Dall-E no es optimo')
        except BadRequestError as e:
            print(f"OpenAI BAD REQUEST error {e.status_code}: (e.response)")
            await ctx.send(f'Hubo un error inesperado')
        except Exception as e:
            print(f'Exception raised {e} cause: {e.__cause__}')

async def setup(client):
    await client.add_cog(Chat(client))
