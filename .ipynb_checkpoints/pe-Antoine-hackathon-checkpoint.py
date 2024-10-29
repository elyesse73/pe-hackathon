import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 



fichier = "PS_2024.10.29_06.17.42.csv"

df = pd.read_csv(fichier, skiprows = 96)
df.head()

#cohérence types
df.dtypes



# +
#df.describe
# -

#taille du data set 
df.shape

# +
#Bilan valeurs manquantes 
#df.value_counts()
# -

#on enlève les colonnes inutiles
df.drop(["default_flag", "soltype","pl_controv_flag", "pl_refname","ttv_flag"], axis=1, inplace = True)
df.head()

# +
#graphe radius = f(orbital period) 


plt.scatter(df['pl_orbper'], df['pl_rade'], marker='o')

# Définir l'échelle logarithmique
plt.xscale('log')

# Ajouter des labels et un titre
plt.xlabel('Orbital period (days)')
plt.ylabel('Planet Radius [earth radius]')
plt.title('Graphique en échelle logarithmique')
plt.grid(True)

# Afficher le graphique
plt.show()
# -






