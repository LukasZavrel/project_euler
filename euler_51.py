# %%
def generate_primes(n):
    r = [False, True] * (n // 2) + [True]
    r[1], r[2] = False, True
    for i in range(3, int(1 + n ** 0.5), 2):
        if r[i]:
            r[i * i::2 * i] = [False] * ((n + 2 * i - 1 - i * i) // (2 * i))
    return r


primes = generate_primes(10 ** 6)
# %%
from collections import Counter
from itertools import combinations

suspects = Counter()
primes = generate_primes(10 ** 6)
for i in range(10 ** 5, 10 ** 6):
    if primes[i]:
        str_prime = str(i)
        counter = Counter(str_prime)
        key, value = counter.most_common(1)[0]
        positions = []
        counter_extension = set()
        if value >= 3:
            for pos, nr in enumerate(str_prime):
                if nr == key:
                    positions.append(pos)
            for variant in combinations(positions, 3):
                counter_extension.add(''.join([nr if pos not in variant else 'x' for pos, nr in enumerate(str_prime)]))
        for value in counter_extension:
            suspects[value]+=1
#%%
suspects.most_common(3)