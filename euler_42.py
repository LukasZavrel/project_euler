# %%
reader = open('42.in', 'r')
data = sorted([name[1:-1] for name in reader.readline().split(sep=',')])
reader.close()
#%%
def name_value(name):
    value = 0
    for letter in name:
        value += ord(letter) - 64
    return value
#%%
triangle_numbers = set([i*(i+1)//2 for i in range(1,200)])
#%%
counter = 0
for word in data:
    if name_value(word) in triangle_numbers:
        counter+=1
print(counter)