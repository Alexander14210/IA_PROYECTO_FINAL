# bot.py
import os

from discord.ext import commands
import discord
import aiohttp
from dotenv import load_dotenv
from IA_Proyecto_FrasesAnalisis import encontrar_polaridad



load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

#Ejemplo: !emocion "Don't wanna wake up, coz I'm happier here"
@bot.command(name='emocion', help='Ingresa una frase para descubrir la emocion asociada')
async def emocion(ctx, frase: str):
  
  emocionAsociada, frase_esta_en_df = encontrar_polaridad(frase)
  output = 'Pienso que la frase que introduciste presenta un sentimiento ' + emocionAsociada

  if frase_esta_en_df:
    output += '\nEncontre esta frase en el set de datos'



  async with aiohttp.ClientSession() as cs:
      async with cs.get("https://random.dog/woof.json") as r:  
          data = await r.json()
          url = data['url']

          embed = discord.Embed( 
                        title="OUTPUT", 
                        description=output, 
                        colour=discord.Colour.purple() 
                        )

          embed.set_image(url=url)

          await ctx.send(output, embed=embed)




@bot.event
async def on_ready():
    print(f'{bot.user.name} se ha conectado a Discord correctamente!')


bot.run(TOKEN)