# bot.py

import os
from re import I

from discord.ext import commands
import discord
import aiohttp
import urllib
from dotenv import load_dotenv
import random
from IA_Proyecto_FrasesAnalisis import encontrar_polaridad



load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
IMGUR_ID = os.getenv('IMGUR_CLIENT_ID')

bot = commands.Bot(command_prefix='!')


headers = {
  "accept": "application/json",
  'Authorization': "Client-ID " + IMGUR_ID
  }

#Ejemplo: !emocion "Don't wanna wake up, coz I'm happier here"
@bot.command(name='emocion', help='Ingresa una frase para descubrir la emocion asociada')
async def emocion(ctx, frase: str):
  
  resultado = encontrar_polaridad(frase)
  title = 'Pienso que la frase que introduciste presenta un sentimiento ' + resultado['sentimiento']

  color = 0 

  
  if resultado['serie'] == 'tlor':
    output = '¡Hey! Mira que coincidencia, ¡está frase es de El Señor de los Anillos! \nLa dijo ' + resultado['nombre']
    personaje_a_buscar = resultado['nombre']
    saga_a_buscar = 'The Lord of The Rings'
    color = 0xa84300 #Naranja

  elif resultado['serie'] == 'hp':
    output = '¡Hey! Mira que coincidencia, ¡está frase es de Harry Potter! \nLa dijo ' + resultado['nombre']
    personaje_a_buscar = resultado['nombre']
    saga_a_buscar = 'Harry Potter'
    color = 0x71368a #Purpura

  else:
    if resultado['sentimiento'] == 'positivo 😄':
      output = "¡Me gustó esa frase! \nEspero que tengas un buen día."
      personaje_a_buscar = 'dog'
      saga_a_buscar = 'happy'
      color = 0xf1c40f #Dorado

    elif resultado['sentimiento'] == 'negativo 😕':
      output = "Espero que tú estado de ánimo pueda mejorar, ¡Vendrán días mejores!"
      personaje_a_buscar = 'cat'
      saga_a_buscar = 'neutral'
      color = 0x3498db #Azul
    elif resultado['sentimiento'] == 'neutral 😐':
      output = "No todos los días tienen que ser una aventura, a veces, hay felicidad en la cotidianidad"
      personaje_a_buscar = 'happy cat'
      saga_a_buscar = 'happy'
      color = 0x95a5a6 # Gris

  input_url = f"https://api.imgur.com/3/gallery/search/top/all/?q_all={personaje_a_buscar}&q_any={saga_a_buscar}&q_type=jpg"

 
  async with aiohttp.ClientSession() as cs:
      async with cs.request("GET", input_url, headers=headers) as r:  
          data = await r.json()
          list_data = data['data']
          image_url = list_data[0]['images'][0]['link']

          
          embed = discord.Embed(title=title, description=output, colour=color)
                        
          embed.set_image(url=image_url)

          await ctx.send(embed=embed)
          


@bot.event
async def on_ready():
    print(f'{bot.user.name} se ha conectado a Discord correctamente!')


bot.run(TOKEN)