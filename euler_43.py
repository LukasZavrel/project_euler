#%%
import itertools
pandigit = list(itertools.permutations(range(10)))
primes = [2,3,5,7,11,13,17]
total_sum = 0
for tup in pandigit:
    interesting = True
    for i in range(1,len(primes)+1):
        if int(f'{tup[i]}{tup[i+1]}{tup[i+2]}') % primes[i-1]:
            interesting = False
            break
    if interesting:
        print(int("".join([str(k) for k in tup])))
        total_sum += int("".join([str(k) for k in tup]))
print(f'total sum is {total_sum}')

