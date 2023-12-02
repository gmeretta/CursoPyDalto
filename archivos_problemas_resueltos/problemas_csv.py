import pandas as pd

df = pd.read_csv("archivos_problemas_resueltos\\datos.csv")
print(df)

# convertir a string los datos de una columna

df['edad'] = df['edad'].astype(str)
print(f"\n{type(df['edad'][0])}\n")

#df['apellido'].replace("dalto", "maestro", inplace=True)
df['apellido'].replace("dalto", "maestro")
print("\nSin inplace\n")
print(df['apellido'])
df['apellido'].replace("dalto", "maestro", inplace=True)
print("\nCon inplace\n")
print(df['apellido'])


print("\nCon datos faltantes\n")
print(df)
# sacando datos faltantes
df=df.dropna()
print("\nCon datos faltantes borrados !!! \n")
print(df)

print("\nCon datos repetidos\n")
print(df)
df = df.drop_duplicates()
print("\nsin datos repetidos\n")
print(df)

# escribiendo csv a file

df.to_csv("archivos_problemas_resueltos\\datos_limpios.csv")