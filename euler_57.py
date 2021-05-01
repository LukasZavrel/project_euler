#%%
def sum_strings(a: str, b: str) -> str:
    # b should not be shorter
    if len(b) < len(a):
        a, b = b, a
    c = ''
    summation = 0
    for i in range(1, len(a) + 1):
        summation += int(a[-i]) + int(b[-i])
        c = f'{summation % 10}{c}'
        summation //= 10
    for i in range(len(a) + 1, len(b)+1):
        summation += int(b[-i])
        c = f'{summation % 10}{c}'
        summation //= 10
    if summation:
        c = f'{summation}{c}'
    return c

nominator = '1'
denominator = '2'

total_sum = 0
for i in range(1000):
    new_nr = sum_strings(nominator, denominator)
    if len(new_nr)>len(denominator):
        total_sum += 1
    nominator, denominator = denominator, sum_strings(sum_strings(nominator, denominator), denominator)
    # print(nominator, denominator)
print(total_sum)