import math
total_sum = 0
for i in range(10,10**7):
    curr_nr = str(i)
    partial_sum = 0
    for nr in curr_nr:
        partial_sum += math.factorial(int(nr))
    if partial_sum == i:
        print(i)
        total_sum += i
print(total_sum)
