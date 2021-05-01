# %%
data = []
reader = open('81.in', 'r')
for line in reader.readlines():
    data.append([int(i) for i in line.rstrip().split(',')])
reader.close()
# %%
for n in reversed(range(158)):  # sum
    for j in range(max(0, n - 79), min(n+1, 80)):
        i = n-j
        if i == 79:
            data[i][j] += data[i][j + 1]
        elif j == 79:
            data[i][j] += data[i + 1][j]
        else:
            data[i][j] += min(data[i][j + 1], data[i + 1][j])
print(data[0][0])
