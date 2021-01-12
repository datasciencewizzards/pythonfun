# Python alternative to excel and MatLab
# language compatibility
# can easily work with Big Data

import pandas as pd

df = pd.read_csv("pokemon_data.csv")

print(df)

# Look at the top 3 rows
print(df.head(3))

# Look at the bottom 3 rows
print(df.tail(3))

# Print the headers
print("Headers {}".format(df.columns))

# Printing specific columns
print("Name column from csv {}".format(df["Name"]))

# Name column values from 0 to 5(exluding)
print("Name column from csv {}".format(df["Name"][0:5]))
# Name column values from last row to last -10(excluding)
print("Name column from csv {}".format(df["Name"][-10:-1]))

# What is the type of the data ?
print("Name column from csv {}".format(type(df["Name"][-10:-1])))

# Multi Columns
print("Name column from csv {}".format(df[["Name","Type 1"]]))

# Integer location (iLoc)
print("Data @ 0th row {}".format(df.iloc[0]))
# Multiple rows
print("Data @ 0-5(excluding) th row {}".format(df.iloc[0:5]))

# Multiple rows ex 2
print("Data @ 0,2 th row {}".format(df.iloc[2,1]))

# Iterating all the rows
for index, row in df.iterrows():
    print(index,row)

# Iterating all the rows
for index, row in df.iterrows():
    print(index,row["Name"])

# Finding the data
print("Find the data where Type 1 is fire {}".format(df.loc[df['Type 1'] == "Fire"]))

# Statistics

print("Basic statistics {}".format(df.describe()))

# Sorting the values
# Descending on Name and Ascending on Type1
print("Sorting Example {}".format(df.sort_values(["Name","Type 1"],ascending=[0,1])))
