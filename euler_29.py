# %%
distinct_powers = set()
max_boarder = 100
for a in range(2, max_boarder + 1):
    power_old = str(a)
    power_new = ''
    product = 0
    for b in range(2, max_boarder + 1):
        for j in reversed(power_old):
            product += int(j) * a
            power_new = f'{product % 10}{power_new}'
            product //= 10
        if product:
            power_new = f'{product}{power_new}'
            product = 0
        power_old = power_new
        distinct_powers.add(power_new)
        power_new = ''

print(len(distinct_powers))
