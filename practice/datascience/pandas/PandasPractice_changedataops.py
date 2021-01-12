# Python alternative to excel and MatLab
# language compatibility
# can easily work with Big Data

import pandas as pd

df = pd.read_csv("pokemon_data.csv")

print(df.head(5))

print(df.columns)

# Create an additional column called "Total" which is the sum of
# 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed'
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

print("After creating one more column Total \n" , df.head(5))

print("Statistics after total\n" , df.describe())

# Drop column Type 1

# df = df.drop(columns=['Type 1'])
print("DataFrame after dropping the column 'Total 1'\n" , df)

# Another way of doing the same
# df['Total'] = df['HP']+df['Attack']+df[ 'Defense']+df[ 'Sp. Atk']+df[ 'Sp. Def']+df[ 'Speed']
# df['Total'] is the sum of all the columns from column 4-9
# (1) Locate the data from all rows and 4 to 9 rows : iloc
# (2) Sum up all the columns from (1) df.loc.sum
# (3) Put back the sum in the df['Total']

df['Total'] = df.iloc[: , 4:10].sum(axis=1)
print("After creating one more column Total \n" , df.head(5))

# Moving total column from the last to middle somewhere
cols = list(df.columns)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]
print("Dataframe after moving the Total in the middle\n" , df.head(5))

df.to_csv("modified.csv")
