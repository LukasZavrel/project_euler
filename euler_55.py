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

def is_palindrome(nr_str:str) -> bool:
    if nr_str == nr_str[::-1]:
        return True
    return False

def is_lychrel(nr) -> bool:
    str_nr = str(nr)
    for _ in range(50):
        str_nr = sum_strings(str_nr, str_nr[::-1])
        if is_palindrome(str_nr):
            return False
    return True

#%%
counter = 0
for i in range(10**4):
    counter += is_lychrel(i)*1
print(counter)