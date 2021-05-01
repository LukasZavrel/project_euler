#%%
pentagonal_list = [n*(3*n-1)/2 for n in range(1,10**5)]
pentagonal_set = set(pentagonal_list)

min_difference = 10**10
for i in range(10**5):
    for j in range(i):
        if pentagonal_list[i]-pentagonal_list[j] in pentagonal_set and pentagonal_list[i]+pentagonal_list[j] in pentagonal_set:
            if pentagonal_list[i]-pentagonal_list[j] < min_difference:
                min_difference = pentagonal_list[i]-pentagonal_list[j]
                print(min_difference)