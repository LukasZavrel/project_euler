#%%
nr = 28433
for i in range(7830457):
    nr = nr * 2 % 10**10
print(nr+1)