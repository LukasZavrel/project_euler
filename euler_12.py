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
def generate_primes(n):
    r = [False, True] * (n//2) + [True]
    r[1], r[2] = False, True
    for i in range(3, int(1 + n**0.5), 2):
        if r[i]:
            r[i*i::2*i] = [False] * ((n+2*i-1-i*i)/(2*i))
    return r
#%%
def number_of_divisors(num):
    if num in prime_numbers:
        return 1
    result = 1
    counter = 0
    while num>1:
        curr_prime = primes[counter]
        exponent_counter = 1
        while not num % curr_prime:
            num = num // curr_prime
            exponent_counter += 1
        result *= exponent_counter
        counter += 1
    return result


#%%
triangle = 1
addition = 1
while True:
    addition += 1
    triangle += addition
    if number_of_divisors(triangle) > 500:
        print(triangle)
        break
