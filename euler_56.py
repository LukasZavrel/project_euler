#%%
maximal_digit_sum = 0
for i in range(100):
    power_old = '1'
    for j in range(100):
        power_new = ''
        product = 0
        for j in reversed(power_old):
            product += int(j) * i
            power_new = f'{product%10}{power_new}'
            product //= 10
        if product:
            power_new = f'{product}{power_new}'
        power_old = power_new
        if sum([int(i) for i in power_new]) > maximal_digit_sum:
            maximal_digit_sum = sum([int(i) for i in power_new])
            print(maximal_digit_sum)
