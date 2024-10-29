import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fichier = "PS_2024.10.29_06.17.42.csv"

df = pd.read_csv(fichier, skiprows = 96)
df.head()

df2 = df.drop_duplicates(subset=["pl_name"], keep="last")
df2.head()

df2["pl_name"].value_counts()

df2.shape

df3 = df2[["pl_orbsmax","pl_orbper","pl_bmasse"]]
T = df3["pl_orbper"]
a = df3["pl_orbsmax"]
G = 6.67430/(10**11)
M = df3["pl_bmasse"]
df3["Kepler"] = (2*a*149597870700)**3/(T/86400)**2
df3.head()

X = 4*np.pi**2/(G*df3["pl_bmasse"]*5.972*10**24)
Y = df3["Kepler"]
plt.scatter(X,Y);


