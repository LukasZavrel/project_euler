import numpy as np
prime_numbers = set([i for i in range(2, 2000000)])
final_sum = 0
current = 0
while current<np.sqrt(2000000):
    current = min(prime_numbers)
    for i in range(current*current,2000001,current):
        prime_numbers.discard(i)
    prime_numbers.discard(current)
    final_sum += current
    print(current)
final_sum+=sum(prime_numbers)
print(final_sum)
