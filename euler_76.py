# %%
dynamic_dict = {}


def how_many_ways(max_used, remaining_sum):
    if (max_used, remaining_sum) not in dynamic_dict:
        if max_used == 1 or remaining_sum == 0:
            dynamic_dict[(max_used, remaining_sum)] = 1
        else:
            dynamic_dict[(max_used, remaining_sum)] = sum(
                [how_many_ways(i, remaining_sum - i) for i in range(1, min(remaining_sum, max_used)+1)])
    return dynamic_dict[(max_used, remaining_sum)]

n = 100
print(how_many_ways(n-1, n))
