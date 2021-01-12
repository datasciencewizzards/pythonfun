# Pandas Sum
import pandas as pd

df = pd.read_csv("data.csv")

print("Before adding the values :: \n",df)

df['Total'] = df.iloc[:,4:10].sum(axis=1)

print("After adding the values :: \n",df)