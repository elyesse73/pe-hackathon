import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 



fichier = "PS_2024.10.29_06.17.42.csv"

df = pd.read_csv(fichier, skiprows = 96)
df.head()
df.drop_duplicates(subset=["pl_name"], keep="last",inplace = True)
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
df.head(10)

# +
#graphe radius = f(orbital period) 

couleurs = {'Radial Velocity': 'blue', 'Imaging': 'orange', 'Eclipse Timing Variations': 'green', 'Transit': 'red', 'Microlensing': 'gray', 'Astrometry': 'pink', 'Transit Timing Variations': 'purple'}


for categorie in df['discoverymethod'].unique():
    subset = df[df['discoverymethod'] == categorie]
    plt.scatter(subset['pl_orbper'], subset['pl_rade'],  
                label=categorie, 
                marker='o')


# Définir l'échelle logarithmique
plt.xscale('log')
plt.yscale('log')
# Ajouter des labels et un titre
plt.xlabel('Orbital period (days)')
plt.ylabel('Planet Radius [earth radius]')
plt.title('Graphique en échelle logarithmique')
plt.legend()
plt.grid(True)

# Afficher le graphique
plt.show()
# +
#graphe planet Mass or Mass*sin(i) = f(orbital period) 

for categorie in df['discoverymethod'].unique():
    subset = df[df['discoverymethod'] == categorie]
    plt.scatter(subset['pl_orbper'], subset['pl_bmassj'],  
                label=categorie, 
                marker='o')


# Définir l'échelle logarithmique
plt.xscale('log')
plt.yscale('log')
# Ajouter des labels et un titre
plt.xlabel('Orbital period (days)')
plt.ylabel('Planet Mass or Mass*sin(i) [jupyter mass]')
plt.title('Graphique en échelle logarithmique')
plt.legend()
plt.grid(True)

# Afficher le graphique
plt.show()

# +
#graphe insolation flux [earth flux] = f(orbital period) 

for categorie in ['Radial Velocity','Transit','Transit Timing Variations']:
    subset = df[df['discoverymethod'] == categorie]
    plt.scatter(subset['pl_orbper'], subset['pl_insol'],  
                label=categorie,
                marker='o', 
                s=4)


# Définir l'échelle logarithmique
plt.xscale('log')
plt.yscale('log')
# Ajouter des labels et un titre
plt.xlabel('Orbital period (days)')
plt.ylabel('Insolation Flux [Earth flux]')
plt.title('Graphique en échelle logarithmique')
plt.legend()
plt.grid(True)

# Afficher le graphique
plt.show()

# +
#graphe insolation eccentricity = f(orbital period) 

for categorie in df['discoverymethod'].unique():
    subset = df[df['discoverymethod'] == categorie]
    plt.scatter(subset['pl_orbper'], subset['pl_orbeccen'],  
                label=categorie,
                marker='o', 
                s=4)


# Définir l'échelle logarithmique
plt.xscale('log')

# Ajouter des labels et un titre
plt.xlabel('Orbital period (days)')
plt.ylabel('Eccentricity')
plt.title('Ecentricity en fonction de la période orbite')
plt.legend()
plt.grid(True)

# Afficher le graphique
plt.show()
# -


df['releasedatenew'] = pd.to_datetime(df['releasedate'], errors='coerce')
df['annee'] = df['releasedatenew'].dt.year
df.head()

# +
#histogramme sur l'année de découverte

# Créer un histogramme
plt.figure(figsize=(10, 6))
plt.hist(df['annee'], bins=df['annee'].nunique(), color='blue', edgecolor='black', alpha=0.7)


# Ajouter des labels et un titre
plt.xlabel('Valeurs')
plt.ylabel('Fréquence')
plt.title('')

# Afficher la grille
plt.grid(axis='y')

# Afficher le graphique
plt.show()
# -

#tableau classement par rayon 
#j'ai essayé de faire un tableau croisé complexe avec des masques j'ai légérement manqué de temps 
df['categorierade'] = pd.cut(df['pl_rade'], bins=[0,50,100])
df['categorieinsol'] = df[(df['pl_insol'] >= 0.32) & (df['pl_insol'] <= 1.78)]
df.pivot_table(index='categorierade', columns='pl_insol', aggfunc='count')












