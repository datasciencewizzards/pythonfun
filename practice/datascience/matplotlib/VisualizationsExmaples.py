# Generalized random data in normal distribution

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))

df = pd.DataFrame(
   np.random.randn(1000, 4), index=ts.index, columns=["A", "B", "C", "D"]
   )

ts = ts.cumsum()

# plt.plot(ts)

# plt.show()

# Example 2 : Plotting using the dataframe

df = pd.DataFrame(
   np.random.randn(1000, 4), index=ts.index, columns=["A", "B", "C", "D"])

df = df.cumsum()

plt.figure()

plt.legend(loc='best')

plt.plot(df)

plt.show()
