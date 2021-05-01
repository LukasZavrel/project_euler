#%%
for i in range(1,100000):
    nr = f"{i*1}{i*2}"
    if len(nr) == 9 and set([int(j) for j in nr]) == set(range(1,10)):
        print(nr)