import pandas as pd

# print (type (pd) )

df = pd.read_csv("archivos\\datos.csv")
# df = pd.read_csv("archivos\\datos.csv", names=["name", "lastname", "age"])
# nombres = df["nombre"]

# print(nombres)

print(df)

