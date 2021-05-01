multiples = set()
for i in range(1000//3):
    multiples.add(3*(i+1))
for i in range(1000//5):
    multiples.add(5*i)
print(sum(multiples))
