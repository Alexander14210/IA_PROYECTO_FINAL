#Limpiar los dataset, quitar caracteres speciales
import pandas as pd

#Verificar encoding
with open('script.csv') as f:
  print(f)

#Abrir dataset TLOR
df = pd.read_csv('script.csv', encoding='cp1252')

print('Columna de Dialogos')
print(df['dialog'].head(20))

#Reemplazar caracter especial por un espacio vacio
df['dialog'] = df['dialog'].str.replace('Â','')

#Quitar leading and trailing whitespaces
df['dialog']= df['dialog'].str.strip().replace(r'\s+',' ', regex=True)

#Quitar espacios entre las palabras de la oracion


print("Columna modificada")
print(df['dialog'].head(20))

print("Guardar nuevo dataset")
df.to_csv('df_TLOR.csv', encoding='cp1252')


