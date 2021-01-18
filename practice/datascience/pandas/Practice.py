# Mandatory imports

import numpy as np
import pandas as pd

#  Series creations

pd_series = pd.Series([1 , 3 , 5 , np.nan , 6 , 8])

print("Basic Series Panda \n" , pd_series)

dates = pd.date_range("20130101" , periods=6)

print("Dates produced \n" , dates)
#  DataFrame creation
#                   matrix(6x4)         rowIndices      Columns
df = pd.DataFrame(np.random.randn(6 , 4) , index=dates , columns=list("ABCD"))

print("DataFrame \n" , df)

# Data Frame Creation with dictionary of objects
df2 = pd.DataFrame(
    {
        "A": 1.0 ,
        "B": pd.Timestamp("20130102") ,
        "C": pd.Series(1 , index=list(range(4)) , dtype="float32") ,
        "D": np.array([3] * 4 , dtype="int32") ,
        "E": pd.Categorical(["test" , "train" , "test" , "train"]) ,
        "F": "foo" ,
    }
)

print("DataFrame produced using a dictionary\n",df2)


