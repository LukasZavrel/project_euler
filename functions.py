data = []
reader = open('.in', 'r')
for line in reader.readlines():
    data.append(line.rstrip())
reader.close()

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

def generate_primes(n):
    r = [False, True] * (n//2) + [True]
    r[1], r[2] = False, True
    for i in range(3, int(1 + n**0.5), 2):
        if r[i]:
            r[i*i::2*i] = [False] * ((n+2*i-1-i*i)//(2*i))
    return r