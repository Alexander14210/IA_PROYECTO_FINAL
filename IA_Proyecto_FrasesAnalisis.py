# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 22:40:16 2022

@author: Karl Grey, Luis Tapia, Alejandro Santamaría, Leonardo Castillo
"""

import pandas as pd
from textblob import TextBlob



def encontrar_polaridad(frase_inicial: str):
    df_tlor = pd.read_csv('script.csv')
    #df_hp = pd.read_csv('Dialogue.csv')
    
    frase = TextBlob(frase_inicial)

    frase_esta_en_df = (df_tlor['dialog'] == frase_inicial).any()
    sentimiento = ''

    if (df_tlor['dialog'] == frase_inicial).any():
        frase_esta_en_df = True

    if frase.polarity >= -1.00 and frase.polarity <= -0.01:
        sentimiento = 'negativo'
        print("La frase ingresada presenta un sentimiento negativo")

    elif frase.polarity >= 0.00 and frase.polarity <= 0.99:
        sentimiento = 'neutral'
        print("La frase ingresada presenta un sentimiento neutral")

    elif frase.polarity >= 1.00:
        sentimiento = 'positivo'
        print("La frase ingresada presenta un sentimiento positivo")

    return sentimiento, frase_esta_en_df

df1 = pd.read_csv('script.csv') 
#df2 = pd.read_csv('Dialogue.en.es.csv')




