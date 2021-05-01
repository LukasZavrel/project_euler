#%%
def is_curious(a,b):
    a_part, b_part = str(a)[0], str(b)[1]
    if b_part != '0' and int(a_part)/int(b_part) == a/b:
        return True
    a_part, b_part = str(a)[1], str(b)[0]
    if b_part != '0' and int(a_part) / int(b_part) == a / b:
        return True
    return False
for a in range(10,100):
    for b in range(a+1,100):
        if is_curious(a,b):
            print(f"pair {a} and {b}")
# pair 49 and 98
# pair 16 and 64
# pair 19 and 95
# pair 26 and 65
print(1/2*1/4*1/5*2/5)