#%%
import math
nr = 999999
to_use = [0,1,2,3,4,5,6,7,8,9]
final_nr = ''
#%%
while to_use:
    pos = nr // math.factorial(len(to_use)-1)
    final_nr += str(to_use[pos])
    nr %= math.factorial(len(to_use)-1)
    to_use.pop(pos)
print(final_nr)