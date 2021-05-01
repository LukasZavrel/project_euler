#%%
def decimal_division_1(dividend):
    result = ''
    remainder = 0
    divisor = 1
    max_len = 1000
    for _ in range(2*max_len):
        result += str(divisor // dividend)
        divisor = (divisor % dividend)*10
    searched_cycle = result[-max_len:]
    mover = 0
    while True:
        mover +=1
        if result[-max_len-mover:-mover] == searched_cycle:
            return mover


#%%
periode_len = {}
for i in range(1,1000):
    periode_len[i] = decimal_division_1(i)
#%%
sorted_dict = {k: v for k, v in sorted(periode_len.items(), key=lambda item: -item[1])}