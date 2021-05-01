#%%
for exponent in range(10):
    print(f'current exponent is {exponent}')
    for i in range(10**exponent, 10**(exponent + 1)//6):
        if sorted([j for j in str(i)]) == sorted([j for j in str(2*i)]) == sorted([j for j in str(3*i)]) == sorted([j for j in str(4*i)]) == sorted([j for j in str(5 *i)]) == sorted([j for j in str(6*i)]):
            print(i)