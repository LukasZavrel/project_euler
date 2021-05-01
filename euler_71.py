#%%
import math
greatest = 2/7

for d in reversed(range(10**6)):
    for n in reversed(range(int(greatest*d), int(3*d/7)+1)):
        if math.gcd(d,n) == 1:
            if n/d < 3/7 and n/d > greatest:
                greatest = n/d
                great_pair = (n,d)
                break
print(great_pair)
