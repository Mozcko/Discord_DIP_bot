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

# This Python class defines a Discord bot cog for handling chat and image generation using OpenAI's
# ChatGPT and DALL-E models, respectively.
class Chat(commands.Cog):
    def __init__(self, client):
        self.__AI_TOKEN: str = os.getenv("OPENAI_API_KEY")
        self.__AI_ORGANIZATION: str = os.getenv("OPENAI_ORGANIZATION")
        self.client = client

        # se crea un cliente para la conexión con la api de Open AI
        self.__client: OpenAI = OpenAI(
            organization=self.__AI_ORGANIZATION,
            api_key=self.__AI_TOKEN
        )
    
    # commando que  obtiene el mensaje del usuario y lo convierte en el prompt 
    # del modelo de ChatGPT 3.5-turbo mandando como mensaje la respuesta del modelo 
    @commands.command()
    async def ask(self, ctx, *,message) -> None:
        try: 
            # manda el prompt a la api de OpenAI
            output = self.__client.chat.completions.create(model='gpt-3.5-turbo-0125',
                                                        messages=[
                                                            {"role": "user",
                                                            "content":
                                                                message}
                                                        ])
            
            # recupera unicamente el contenido pertinente y reacciona al mensaje del usuario
            await ctx.send(output.choices[0].message.content)
            await ctx.message.add_reaction('🤖')  #agrega un emoji

        # excepciones de la api de Open AI
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

    # commando que  obtiene el mensaje del usuario y lo convierte en el prompt 
    # del modelo de Dall E 2 mandando como mensaje la respuesta del modelo 
    @commands.command()
    async def visualize(self, ctx, *, message) -> None:
        try:
            # manda un mensaje temporal en lo que se recibe la respuesta
            response = await ctx.send("generando imagen")
            # manda el prompt a la api de OpenAI

            output = self.__client.images.generate(
                model="dall-e-2",
                prompt=message,
                size="512x512",
                quality="standard",
                n=1,
            )

            # recupera unicamente el contenido pertinente, modifica el mensaje
            # temporal y reacciona al mensaje del usuario
            await response.edit(content=output.data[0].url, embed=None)
            await ctx.message.add_reaction('🖼')  #agrega un emoji
        
        # excepciones de la api de Open AI
        except APIConnectionError as e: 
            print("Server connection error: {e.__cause__}")
            await ctx.send(f'Hubo un error con la conexión con Dall-E')
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

# función de Setup para la extension de comandos
async def setup(client) -> None:
    await client.add_cog(Chat(client))
