#%%
import numpy as np
import pandas as pd
data = []
reader =  open('11.in', 'r')
for line in reader.readlines():
    map_object = map(int, line.split(' '))
    data.append(list(map_object))
data = pd.DataFrame(data)
#%%
highest = 0
n = len(data)
for i in range(n):
    for j in range(n-4):
        product = np.prod(data.iloc[i, j:j+4])
        if product>highest:
            highest = product
        product = np.prod(data.iloc[j:j+4, i])
        if product>highest:
            highest = product

#%%
for i in range(n-4):
    for j in range(n-4):
        product = 1
        for k in range(4):
            product *= data.iloc[i+k,j+k]
        if product>highest:
            highest = product
        product = 1
        for k in range(4):
            product *= data.iloc[i+k,j+4-k]
        if product>highest:
            highest = product

