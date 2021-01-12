# Statistics with Python
import pandas as pd

df = pd.read_csv("pokemon_data.csv")
df = df.groupby(['Type 1']).mean().sort_values('Defense',ascending=False)
