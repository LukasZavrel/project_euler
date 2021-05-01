# %%
from itertools import cycle

reader = open('59.in', 'r')
data = [chr(int(i)) for i in reader.read().split(",")]
reader.close()

# %%
frequency_capital = {
    'E': 529117365,
    'T': 390965105,
    'A': 374061888,
    'O': 326627740,
    'I': 320410057,
    'N': 313720540,
    'S': 294300210,
    'R': 277000841,
    'H': 216768975,
    'L': 183996130,
    'D': 169330528,
    'C': 138416451,
    'U': 117295780,
    'M': 110504544,
    'F': 95422055,
    'G': 91258980,
    'P': 90376747,
    'W': 79843664,
    'Y': 75294515,
    'B': 70195826,
    'V': 46337161,
    'K': 35373464,
    'J': 9613410,
    'X': 8369915,
    'Z': 4975847,
    'Q': 4550166,
}
suma = sum(frequency_capital.values())
frequency_lower = {key.lower(): value / suma for key, value in frequency_capital.items()}

# %%
key = 'exp'
#data = [i for i in 'ahoj']
encrypted_message = [chr(ord(a) ^ ord(b)) for (a, b) in zip(data, cycle(key))]
decrypted_message = [chr(ord(a) ^ ord(b)) for (a, b) in zip(encrypted_message, cycle(key))]

# %%
data2 = [[data[i] for i in range(len(data)) if i % 3 == j] for j in range(3)]

# %%
import math

for j in range(3):
    for key in range(97, 123):
        log_prob = 0
        decrypted_message = [chr(ord(a) ^ b) for (a, b) in zip(data2[j], cycle([key]))]
        for letter in frequency_lower:
            occur = decrypted_message.count(letter)
            log_prob += math.log(math.comb(len(decrypted_message), occur) * (frequency_lower[letter] ** occur) * (
                        (1 - frequency_lower[letter]) ** (len(encrypted_message) - occur)))
        print(f'letter {chr(key)} with a log probability of {log_prob}')

#%%
print(sum([ord(i) for i in encrypted_message]))
