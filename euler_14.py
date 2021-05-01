collatz_dict = {1: 1}


# %%
def collatz(num):
    if num in collatz_dict:
        return collatz_dict[num]
    elif num % 2:
        next_seq = collatz(3 * num + 1)
        collatz_dict[num] = next_seq + 1
        return next_seq + 1
    else:
        next_seq = collatz(num // 2)
        collatz_dict[num] = next_seq + 1
        return next_seq + 1


# %%
for i in range(1, 10 ** 6):
    a = collatz(i)

# %%
max_length = 1
for i in range(1, 10 ** 6):
    curr = collatz_dict[i]
    if curr > max_length:
        max_length = curr
        max_arg = i

print(max_arg)