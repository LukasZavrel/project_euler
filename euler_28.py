#%%
corners = [3, 5, 7, 9]
size = 1
curr_sum = 1 + 3 + 5 + 7 + 9
to_add = 8
for i in range(499):
    for j in range(4):
        to_add += 2
        corners[j] += to_add
        curr_sum += corners[j]
print(curr_sum)