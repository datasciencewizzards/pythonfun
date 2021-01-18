import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# plot(x axis, y axis)
X = [0 , 1 , 2 , 3 , 4]
Y = [0 , 2 , 4 , 6 , 8]
# plt.plot(X , Y,label='y=2x', color='red', linewidth=2,marker='.',linestyle='--',markersize=10, markeredgecolor='blue')

plt.figure(figsize=(5 , 3) , dpi=200)
# Shorthand notation for setting visual properties 'r.--'
plt.plot(X , Y , 'r.--' , label='y=2x')

# Lets generate a quadratic data
x2 = np.arange(0 , 4.5 , .5)
plt.plot(x2 , x2 ** 2)

plt.title("Our First Graph!" , fontdict={'fontname': 'Comic Sans MS' , 'fontsize': 20})
plt.xlabel("X axis")
plt.ylabel("Y axis")

# Don't show the decimal places but integers only
plt.xticks([0 , 1 , 2 , 3])
# plt.yticks([0 , 2 , 4 , 6 , 8 , 10])

plt.legend()

plt.savefig('mygraph.png' , dpi=200)

# Dont show but the save in a file
# plt.show()

# Bar chart
labels = ['A' , 'B' , 'C']
values = [1 , 4 , 2]

bars = plt.bar(labels , values)

patterns = ['/' , 'o' , '*']

for bar in bars:
    bar.set_hatch(patterns.pop(0))

# plt.figure(figsize=(6,4))
plt.savefig('mygraph.png' , dpi=200)
