#%%
data = []
reader = open('13.in', 'r')
for line in reader.readlines():
    data.append(line.rstrip())
reader.close()
#data = [['99'], ['99'], ['99'], ['99'], ['99'], ['99'], ['99'], ['99'], ['99'], ['99'], ['99'], ['99'], ['99']]
#%%
summation = 0
final_number = ""
for position in range(1, len(data[0])+1):
    for number in data:
        summation += int(number[-position])
    final_number = f"{summation % 10}{final_number}"
    summation = summation // 10
final_number = f"{summation}{final_number}"
print(final_number[:10])