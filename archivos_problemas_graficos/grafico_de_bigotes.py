import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos_problemas_graficos\\bigotes.csv")

sns.boxplot(x="categoria", y="valor", data=df)
#total_ingresos =  df['ingresos'].sum()
#print(f"El total de ingresos es de {total_ingresos}")
plt.show()