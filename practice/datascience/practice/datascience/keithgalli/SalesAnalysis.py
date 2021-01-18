# Task 1 Merge all months of data into a single file

# (1) Load all the files from a directory

import os
import pandas as pd

pd.set_option('display.max_columns' , None)

files = [file for file in os.listdir("data")]

# print(files)

if os.path.exists("data/all_data.csv"):
    all_data = pd.read_csv("data/all_data.csv")
else:
    all_data = pd.DataFrame()
    for file in files:
        df = pd.read_csv("data/" + file)
        all_data = pd.concat([all_data , df])

    all_data.to_csv("data/all_data.csv" , index=False)

# Write all months data to final csv


# Data analysis

# all_data = pd.read_csv("data/all_data.csv")

print("First 5 rows of the all loaded data\n",all_data.head(5))

# Step (2) : Preparing data for the data analysis
# Augment data with Month for the monthly reports : Add "Month" to all data

print("all_data['Order Date'].str[0:2]!='Or'",all_data['Order Date'].str[0:2]!='Or')

all_data = all_data.dropna(how='all')
all_data = all_data[all_data['Order Date'].str[0:2]!='Or']
all_data['Month'] = all_data['Order Date'].str[0:2]
all_data['Month'] = all_data['Month'].astype('int32')


print("First 5 rows of the all loaded data after adding the Month column\n",all_data.head(5))

# nan_df = all_data[all_data.isna().any(axis=1)]

# print("NAN columns\n",nan_df)

print ("Data dimensions\n",all_data.shape)

print ("All months \n",all_data[:7:])



