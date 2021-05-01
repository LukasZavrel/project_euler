#%%
'''
1 digit * 4 digit = 4 digit

2 digit * 3 digit = 4 digit
'''

all_products = set()

#
for i in range(1,10):
    for j in range(1000,10000):
        used_numbers = set([str(i),*str(j)])
        if len(used_numbers) == 5 and len(set(used_numbers)) == 5:
            if set([str(k) for k in range(1,10)]) - set([*str(i*j)]) == set(used_numbers) and len([*str(i*j)]) == 4:
                all_products.add(i*j)
                print(i,j,i*j)

for i in range(10,100):
    for j in range(100,1000):
        used_numbers = [*str(i),*str(j)]
        if len(used_numbers) == 5 and len(set(used_numbers)) == 5:
            if set([str(k) for k in range(1,10)]) - set([*str(i*j)]) == set(used_numbers) and len([*str(i*j)]) == 4:
                all_products.add(i*j)
                print(i,j,i*j)
print(f'sum of all products is {sum(all_products)}')
