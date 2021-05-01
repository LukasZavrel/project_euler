#%%
data = []
reader = open('67.in', 'r')
for line in reader.readlines():
    data.append([int(i) for i in line.rstrip().split()])
reader.close()
#%%
for i in reversed(range(1,len(data))):
    for j in range(len(data[i-1])):
        data[i-1][j] += max(data[i][j], data[i][j+1])
print(data[0][0])