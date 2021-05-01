#%%
import math
greater_10_6 = 0
for n in range(1,101):
    for r in range(math.ceil(n/2)+1):
        if math.comb(n,r)>10**6:
            greater_10_6 += n+1-2*r
            break
print(greater_10_6)