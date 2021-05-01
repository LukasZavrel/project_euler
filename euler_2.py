fibonacci = [1, 2]
even_sum = 2
while True:
    next_fib = fibonacci[-1] + fibonacci[-2]
    if next_fib < 4 * 10 ** 6:
        fibonacci.append(next_fib)
        if next_fib % 2 == 0:
            even_sum += next_fib
    else:
        break
print(fibonacci)
print(even_sum)
