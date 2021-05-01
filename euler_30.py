total_sum = 0
for i in range(6 * 9 ** 5):
    curr_nr = str(i)
    partial_sum = 0
    for nr in curr_nr:
        partial_sum += int(nr) ** 5
    if partial_sum == i:
        print(i)
        total_sum += i
print(total_sum-1)
