#%%
import math
def next_nr(nr):
    return sum([math.factorial(int(i)) for i in str(nr)])

total_sum = 0
loop_dict = {}
for i in range(10**6):
    if i not in loop_dict:
        curr_loop = []
        loop_len = 0
        while i not in curr_loop:
            curr_loop.append(i)
            i = next_nr(i)
            if i in loop_dict:
                loop_len = loop_dict[i] + len(curr_loop)
                break
        if not loop_len:
            loop_len = len(curr_loop)
        repeated = False
        for pos, j in enumerate(curr_loop):
            if j == i:
                repeated = True
                loop_len = loop_len-pos
            if not repeated:
                loop_dict[j] = loop_len-pos
            else:
                loop_dict[j] = loop_len
#%%
for i in range(10**6):
    if loop_dict[i] == 60:
        total_sum +=1
print(total_sum)