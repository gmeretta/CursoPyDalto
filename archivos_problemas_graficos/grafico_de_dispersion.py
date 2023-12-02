import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos_problemas_graficos\\dispersion.csv")

sns.scatterplot(x="tiempo", y="dinero", data=df)
#total_ingresos =  df['ingresos'].sum()
#print(f"El total de ingresos es de {total_ingresos}")
plt.show()