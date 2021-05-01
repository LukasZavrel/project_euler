#%%
i = 0
product = 1
positions = [10**j for j in range(7)]
curr_length = 0
while positions:
    i+=1
    if positions[0]<=curr_length+len(str(i)):
        product *=int(str(i)[positions[0]-curr_length-1])
        positions.pop(0)
    curr_length += len(str(i))
print(product)
