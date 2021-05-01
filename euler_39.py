#%%
import math
from collections import defaultdict
triangles = defaultdict(int)
for a in range(334):
    for b in range(a, 500):
        if math.sqrt(a**2+b**2) == int(math.sqrt(a**2+b**2)):
            triangles[a+b+int(math.sqrt(a**2+b**2))]+=1
print({k: v for k, v in sorted(triangles.items(), key=lambda item: -item[1])})
#%%
triangles[120]