#%%
total_sum = 0
e_sequence = [1 for i in range(100)]
e_sequence[0] = 2
for i in range(1, 34):
    e_sequence[3 * i - 1] = 2 * i
nominator = 0
denominator = 1
for i in reversed(range(100)):
    denominator, nominator = e_sequence[i]*denominator+nominator, denominator
print(sum([int(i) for i in str(denominator)]))