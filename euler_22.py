# %%
reader = open('22.in', 'r')
data = sorted([name[1:-1] for name in reader.readline().split(sep=',')])
reader.close()


# %%
def name_value(name):
    value = 0
    for letter in name:
        value += ord(letter) - 64
    return value
#%%
print(sum([name_value(name)*(position+1) for position, name in enumerate(data)]))