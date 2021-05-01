last_ten = 0
for i in range(1,1001):
    partial = 1
    for _ in range(i):
        partial = (partial * i) % (10**10)
    last_ten += partial
    last_ten %= (10**10)
print(last_ten)