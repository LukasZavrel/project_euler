#%%
data = []
reader = open('99.in', 'r')
for line in reader.readlines():
    data.append(line.rstrip().split(","))
reader.close()
#%%
import math
maximum = (0,0)
for i in range(1000):
    curr_value = int(data[i][1])*math.log(int(data[i][0]))
    if curr_value>maximum[1]:
        maximum = (i,curr_value)
print(maximum[0]+1)
