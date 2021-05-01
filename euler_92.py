#%%
def square_digit_chain(nr):
    while True:
        if nr == 1:
            return 0
        if nr == 89:
            return 1
        nr = sum((int(i)**2 for i in str(nr)))

total_sum = 0
for j in range(1,10_000_000):
    total_sum += square_digit_chain(j)
print(total_sum)