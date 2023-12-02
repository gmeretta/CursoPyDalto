import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos_problemas_graficos\\keyped.csv")

sns.lineplot(x="fecha", y="keyped", data=df)

plt.plot("01-10", 9, "o")
plt.show()


