# %%
import numpy as np

prime_numbers = set([i for i in range(2, 2000000)])
current = 0
primes = []
while current < np.sqrt(2000000):
    current = min(prime_numbers)
    for i in range(current * current, 2000001, current):
        prime_numbers.discard(i)
    prime_numbers.discard(current)
    primes.append(current)
primes.extend(prime_numbers)


# %%
def sum_of_divisors(num):
    to_substract = num
    if num in prime_numbers or num==1:
        return 1
    all_divisors = set([1])
    counter = 0
    while num > 1:
        curr_prime = primes[counter]
        exponent_counter = 0
        while not num % curr_prime:
            num = num // curr_prime
            exponent_counter += 1
        if exponent_counter:
            to_add = set()
            for number in all_divisors:
                for exponent in range(exponent_counter):
                    to_add.add(number * curr_prime ** (exponent + 1))
            all_divisors.update(to_add)
        counter += 1
    return sum(all_divisors) - to_substract

#%%
abundant = set()
sum_of_two_abundants = set()
for i in range(1, 28123):
    if sum_of_divisors(i)>i:
        to_add = set()
        abundant.add(i)
        for abundat_nr in abundant:
            to_add.add(abundat_nr + i)
        sum_of_two_abundants.update(to_add)
print(sum(set(range(1, 28123))-sum_of_two_abundants))
