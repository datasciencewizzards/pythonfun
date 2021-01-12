# Pandas Sum
import pandas as pd

df = pd.read_csv("data.csv")

print("Before adding the values :: \n",df)

# Axis is unclear
df['Total'] = df.iloc[:,4:10].sum(axis=1)

print("After adding the values :: \n",df)

# More tryouts
data = {'Month': ['Jan ','Feb ','Mar ','Apr ','May ','Jun '],
        'Bill Commission': [1500,2200,3500,1800,3000,2800],
        'Maria Commission': [3200,4100,2500,3000,4700,3400],
        'Jack Commission': [1700,3100,3300,2700,2400,3100]
        }

df = pd.DataFrame(data,columns=['Month','Bill Commission','Maria Commission','Jack Commission'])
print (df)

sum_column = df.sum(axis=0)
print (sum_column)

# Axis if we try to store , it says not a NAN
df['sum_column'] = df.sum(axis=1)
print (df)

