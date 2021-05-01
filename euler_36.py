total_sum=0
for i in range(1,10**6,2):
    if str(i) == str(i)[::-1]:
        if bin(i)[2:] == bin(i)[:1:-1]:
            total_sum += i
            print(i)
print(f'result is {total_sum}')