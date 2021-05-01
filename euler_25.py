# %%
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
# %%
smaller = '1'
bigger = '1'
bigger_index = 2
while len(bigger)<1000:
    smaller, bigger = bigger, sum_strings(smaller, bigger)
    bigger_index += 1
print(bigger_index)

