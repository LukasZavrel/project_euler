#%%
power_old = '1'
for i in range(2, 100+1):
    power_new = ''
    product = 0
    for j in reversed(power_old):
        product += int(j) * i
        power_new = f'{product%10}{power_new}'
        product //= 10
    if product:
        power_new = f'{product}{power_new}'
    power_old = power_new
print(sum([int(i) for i in power_new]))