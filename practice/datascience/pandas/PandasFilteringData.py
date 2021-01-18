# Pandas data filters are covered here

import pandas as pd

df = pd.read_csv("pokemon_data.csv")

print(df.head(5))

print(df.columns)
print(df.index)

filtered_df = df.loc[(df['Type 1']=='Grass') & (df['Type 2']=='Poison') & (df['HP']>70)]


# It has indexes from the original dataset
filtered_df = filtered_df.reset_index()
filtered_df.to_csv("filtered.csv")
print("Filtered df \n",filtered_df)

# RegEx based filtering
filtered_df = df.loc[~df['Name'].str.contains('Mega')]

print("Names which doesn't contain Mega\n",filtered_df)

import re

filtered_df = df.loc[df['Type 1'].str.contains('Fire|Grass',flags=re.I,regex=True)]

print("Names which contain Fire|Grass",filtered_df)

df.loc[df['Type 1']=='Fire' , 'Type 1'] = 'Flammer'

print ("Fire changed to Flamer\n",df)

# Make Legendary True
df.loc[df['Type 1']=='Flamer' , 'Legendary'] = 'True'

print ("Legendary set to True\n",df)

# Change multiple values
df.loc[df['Type 1']=='Flamer' , ['Legendary','Generation']] = ['True','New Value']

print ("Legendary set to True\n",df)

