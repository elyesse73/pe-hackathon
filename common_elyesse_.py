import numpy as np
import pandas as pd

fichier = "PS_2024.10.29_06.17.42.csv"

df = pd.read_csv(fichier, skiprows = 96)
df.head()

df2 = df.copy()
df2 = df.drop_duplicates(subset=["pl_name"], keep="last")
df2.head()

df2["pl_name"].value_counts()

df2.shape


