#%%
from collections import Counter
counter = Counter()
i=0
counter[''.join(sorted(str(i)))] +=1
while counter.most_common(1)[0][1] < 5:
    i += 1
    counter[''.join(sorted(str(i**3)))] +=1
    if '012334556789' == ''.join(sorted(str(i**3))):
        print(i**3)
print(counter.most_common(1))