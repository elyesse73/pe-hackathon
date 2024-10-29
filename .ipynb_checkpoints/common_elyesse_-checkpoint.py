import numpy as np
import pandas as pd

fichier = "PS_2024.10.29_06.17.42.csv"

df = pd.read_csv(fichier, skiprows = 96)
df.head()


