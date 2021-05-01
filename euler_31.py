#%%
from collections import defaultdict

coins = [1,2,5,10,20,50,100,200]
possibilities = defaultdict(int)
possibilities[0] = 1
for coin in coins:
    for i in range(200):
        if i+coin < 201:
            possibilities[i+coin] += possibilities[i]
print(possibilities[200])
