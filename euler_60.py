# %%
import numpy as np
# %%
import numpy as np

max_prime = 10000
prime_numbers = set([i for i in range(2, max_prime)])
current = 0
primes = []
while current < np.sqrt(max_prime):
    current = min(prime_numbers)
    for i in range(current * current, max_prime + 1, current):
        prime_numbers.discard(i)
    prime_numbers.discard(current)
    primes.append(current)
primes.extend(prime_numbers)


# %%
def generate_primes(n):
    r = [False, True] * (n // 2) + [True]
    r[1], r[2] = False, True
    for i in range(3, int(1 + n ** 0.5), 2):
        if r[i]:
            r[i * i::2 * i] = [False] * ((n + 2 * i - 1 - i * i) // (2 * i))
    return r


# %%
prime_list = generate_primes(10 ** 8 + 41)
# %%
table = np.zeros([168, 168])
for i in range(168):
    for j in range(i + 1, 168):
        if prime_list[int(f'{str(primes[i])}{str(primes[j])}')] and prime_list[
            int(f'{str(primes[j])}{str(primes[i])}')]:
            table[i, j] = 1
# %%
x_1, x_2, x_3, x_4 = 0, 0, 0, 0
while x_1 < 168:
    while x_2 < 168:
        if sum(np.concatenate(table[np.ix_([x_1, x_2], [x_1, x_2])])) == 1:
            while x_3 < 168:
                if sum(np.concatenate(table[np.ix_([x_1, x_2, x_3], [x_1, x_2, x_3])])) == 3:
                    while x_4 < 168:
                        if sum(np.concatenate(table[np.ix_([x_1, x_2, x_3, x_4], [x_1, x_2, x_3, x_4])])) == 6:
                            print(primes[x_1], primes[x_2], primes[x_3], primes[x_4])
                        x_4 += 1
                x_3 += 1
                x_4 = x_3 + 1
        x_2 += 1
        x_3 = x_2 + 1
    x_1 += 1
    x_2 = x_1 + 1
#%%
table = np.zeros([1229, 1229])
for i in range(1229):
    for j in range(i + 1, 1229):
        if prime_list[int(f'{str(primes[i])}{str(primes[j])}')] and prime_list[
            int(f'{str(primes[j])}{str(primes[i])}')]:
            table[i, j] = 1
#%%
x_1, x_2, x_3, x_4, x_5 = 0, 0, 0, 0, 0
while x_1 < 168:
    while x_2 < 1229:
        if sum(np.concatenate(table[np.ix_([x_1, x_2], [x_1, x_2])])) == 1:
            while x_3 < 1229:
                if sum(np.concatenate(table[np.ix_([x_1, x_2, x_3], [x_1, x_2, x_3])])) == 3:
                    while x_4 < 1229:
                        if sum(np.concatenate(table[np.ix_([x_1, x_2, x_3, x_4], [x_1, x_2, x_3, x_4])])) == 6:
                            while x_5 < 1229:
                                if sum(np.concatenate(table[np.ix_([x_1, x_2, x_3, x_4, x_5], [x_1, x_2, x_3, x_4, x_5])])) == 10:
                                    print(primes[x_1], primes[x_2], primes[x_3], primes[x_4], primes[x_5])
                                x_5 += 1
                        x_4 += 1
                        x_5 = x_4 + 1
                x_3 += 1
                x_4 = x_3 + 1
        x_2 += 1
        x_3 = x_2 + 1
    x_1 += 1
    x_2 = x_1 + 1
