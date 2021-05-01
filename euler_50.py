#%%
import numpy as np
max_prime = 10**6
prime_numbers = set([i for i in range(2, max_prime)])
current = 0
primes = []
while current<np.sqrt(max_prime):
    current = min(prime_numbers)
    for i in range(current*current,max_prime+1,current):
        prime_numbers.discard(i)
    prime_numbers.discard(current)
    primes.append(current)
primes.extend(prime_numbers)
primes_list = sorted(list(primes))
#%%
longest_len = 0
for start in range(len(primes_list)):
    for end in range(start+longest_len+1, len(primes_list)):
        curr_sum = sum(primes_list[start:end])
        if curr_sum > 10**6:
            break
        if curr_sum in primes:
            print(f'len in {end-start}, prime is {curr_sum}')
            longest_len = end-start
