#%%
import math

total_sum = 0
for n in range(1, 100):
    for i in range(math.ceil((10 ** (n - 1)) ** (1 / n)), 10):
        total_sum +=1
        print(n)
print(total_sum)
