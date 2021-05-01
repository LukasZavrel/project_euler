#%%
max_nr = 10**6
triangle = set([n*(n+1)//2 for n in range(max_nr)])
pentagonal = set([n*(3*n-1)//2 for n in range(max_nr)])
hexagonal = set([n*(2*n-1) for n in range(max_nr)])
print(set.intersection(triangle, pentagonal, hexagonal))