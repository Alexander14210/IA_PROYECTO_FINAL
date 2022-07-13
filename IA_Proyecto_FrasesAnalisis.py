# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 22:40:16 2022

@author: Karl Grey, Luis Tapia, Alejandro Santamaría, Leonardo Castillo
"""

import pandas as pd
from textblob import TextBlob

def encontrar_info_tlor(frase: str):
    df_tlor = pd.read_csv('df_TLOR.csv', encoding='cp1252')
    filtro_dialog = df_tlor['dialog'] == frase
    char_pd_series = df_tlor[filtro_dialog]['char']
    char_name_list = list(char_pd_series)
    char_name = char_name_list[0]

    return char_name.capitalize()

def encontrar_info_hp(frase: str):
    df_hp_dialog = pd.read_csv('Dialogue.csv')
    df_hp_char = pd.read_csv('Characters.csv')

    #Filtrar registro al que pertenece la frase
    filtro_dialog = df_hp_dialog['Dialogue'] == frase

    char_id = df_hp_dialog[filtro_dialog]['Character ID'].sum()
    char_name = df_hp_char['Character Name'][char_id - 1]

    return char_name.capitalize()



def encontrar_polaridad(frase_inicial: str):
    df_tlor = pd.read_csv('df_TLOR.csv', encoding='cp1252')
    df_hp = pd.read_csv('Dialogue.csv')
    
    output = {}

    frase = TextBlob(frase_inicial)

    frase_es__de_tlor = (df_tlor['dialog'] == frase_inicial).any()
    frase_es_de_hp = (df_hp['Dialogue'] == frase_inicial).any()

    frase_esta_en_df = (df_tlor['dialog'] == frase_inicial).any() or (df_hp['Dialogue'] == frase_inicial).any()
    sentimiento = ''

    if frase_es__de_tlor:
        nombre_personaje = encontrar_info_tlor(frase_inicial)
        output['serie'] =  "tlor"
        output['nombre'] = nombre_personaje
    elif frase_es_de_hp:
        nombre_personaje = encontrar_info_hp(frase_inicial)
        output['serie'] = "hp"
        output['nombre'] = nombre_personaje

    else:
        output['serie'] = ''
        output['nombre'] = ''



    if frase.polarity >= -1.00 and frase.polarity <= -0.01:
        sentimiento = 'negativo 😕'
        output['sentimiento'] = sentimiento
        print("La frase ingresada presenta un sentimiento negativo")

    elif frase.polarity >= 0.00 and frase.polarity <= 0.99:
        sentimiento = 'neutral 😐'
        output['sentimiento'] = sentimiento
        print("La frase ingresada presenta un sentimiento neutral")

    elif frase.polarity >= 1.00:
        sentimiento = 'positivo 😄'
        output['sentimiento'] = sentimiento
        print("La frase ingresada presenta un sentimiento positivo")

    return output





