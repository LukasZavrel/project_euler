# %%
data = []
reader = open('54.in', 'r')
for line in reader.readlines():
    data.append(line.rstrip().split())
reader.close()

# %%
import numpy as np

basic_hand = np.array([[False for _ in range(4)] for _ in range(14)])

# %%
import copy


def read_hand(hand):
    hand_1 = copy.deepcopy(basic_hand)
    for i in range(5):
        card = hand[i]
        if card[0] == "A":
            pos = [0, 13]
        elif card[0] == "2":
            pos = [1]
        elif card[0] == "3":
            pos = [2]
        elif card[0] == "4":
            pos = [3]
        elif card[0] == "5":
            pos = [4]
        elif card[0] == "6":
            pos = [5]
        elif card[0] == "7":
            pos = [6]
        elif card[0] == "8":
            pos = [7]
        elif card[0] == "9":
            pos = [8]
        elif card[0] == "T":
            pos = [9]
        elif card[0] == "J":
            pos = [10]
        elif card[0] == "Q":
            pos = [11]
        elif card[0] == "K":
            pos = [12]
        if card[1] == "S":
            color = 0
        if card[1] == "C":
            color = 1
        if card[1] == "D":
            color = 2
        if card[1] == "H":
            color = 3
        for po in pos:
            hand_1[po, color] = True

    hand_2 = copy.deepcopy(basic_hand)
    for i in range(5, 10):
        card = hand[i]
        if card[0] == "A":
            pos = [0, 13]
        elif card[0] == "2":
            pos = [1]
        elif card[0] == "3":
            pos = [2]
        elif card[0] == "4":
            pos = [3]
        elif card[0] == "5":
            pos = [4]
        elif card[0] == "6":
            pos = [5]
        elif card[0] == "7":
            pos = [6]
        elif card[0] == "8":
            pos = [7]
        elif card[0] == "9":
            pos = [8]
        elif card[0] == "T":
            pos = [9]
        elif card[0] == "J":
            pos = [10]
        elif card[0] == "Q":
            pos = [11]
        elif card[0] == "K":
            pos = [12]
        if card[1] == "S":
            color = 0
        if card[1] == "C":
            color = 1
        if card[1] == "D":
            color = 2
        if card[1] == "H":
            color = 3
        for po in pos:
            hand_2[po, color] = True
    return hand_1, hand_2


# %%
def straight_flush(hand):
    for i in range(4):
        for j in range(0, 14 - 4):
            if sum(hand[i, j:j + 5]) == 5:
                return j + 5
    return -1


def four(hand):
    for j in reversed(range(14)):
        if sum(hand[j, :]) == 4:
            return j
    return -1


def full_house(hand):
    for j in reversed(range(14)):
        if sum(hand[j, :]) == 3:
            for k in range(14):
                if sum(hand[k, :]) == 2:
                    return j
    return -1


def flush(hand):
    for i in range(4):
        if sum(hand[1:, i]) == 5:
            return 1
    return -1


def straight(hand):
    for j in reversed(range(4, 14)):
        if sum(hand[j, :]) == True == sum(hand[j - 1, :]) == sum(hand[j - 2, :]) == sum(hand[j - 3, :])== sum(hand[j - 4, :]):
            return 1
    return -1


def three(hand):
    for j in reversed(range(14)):
        if sum(hand[j, :]) == 3:
            return j
    return -1


def two_two(hand):
    for j in reversed(range(14)):
        if sum(hand[j, :]) == 2:
            for k in range(14):
                if sum(hand[k, :]) == 2 and k != j:
                    return j
    return -1


def two(hand):
    for j in reversed(range(14)):
        if sum(hand[j, :]) == 2:
            return j
    return -1


def high_card(hand):
    to_return = []
    for j in reversed(range(14)):
        for k in range(sum(hand[j, :])):
            to_return.append(j)
    return to_return


def compare_hands(hand_1, hand_2):
    # straight flush
    res_1, res_2 = straight_flush(hand_1), straight_flush(hand_2)
    if res_1 > res_2:
        return 1
    elif res_2 > res_1:
        return 0
    # four of a kind
    res_1, res_2 = four(hand_1), four(hand_2)
    if res_1 > res_2:
        return 1
    elif res_2 > res_1:
        return 0
    # fullhouse
    res_1, res_2 = full_house(hand_1), full_house(hand_2)
    if res_1 > res_2:
        return 1
    elif res_2 > res_1:
        return 0
    # flush
    res_1, res_2 = flush(hand_1), flush(hand_2)
    if res_1 > res_2:
        return 1
    elif res_2 > res_1:
        return 0
    # straight
    res_1, res_2 = straight(hand_1), straight(hand_2)
    if res_1 > res_2:
        return 1
    elif res_2 > res_1:
        return 0
    # three of a kind
    res_1, res_2 = three(hand_1), three(hand_2)
    if res_1 > res_2:
        return 1
    elif res_2 > res_1:
        return 0
    # two pairs
    res_1, res_2 = two_two(hand_1), two_two(hand_2)
    if res_1 > res_2:
        return 1
    elif res_2 > res_1:
        return 0
    # one pair
    res_1, res_2 = two(hand_1), two(hand_2)
    if res_1 > res_2:
        return 1
    elif res_2 > res_1:
        return 0
    # high card
    res_1, res_2 = high_card(hand_1), high_card(hand_2)
    for card_nr in range(5):
        if res_1[card_nr] > res_2[card_nr]:
            return 1
        elif res_2[card_nr] > res_1[card_nr]:
            return 0
    print('mistake')
    return None


# %%
# hand = read_hand(data[0])
# print(compare_hands(*read_hand(['2D', '9C', 'AS', 'AH', 'AC', '3D', '6D', '7D', 'TD', 'QD'])))
# # %%
# print(compare_hands(*read_hand(['2H', '2D', '4C', '4D', '4S', '3C', '3D', '3S', '9S', '9D'])))
# # %%
# print(compare_hands(*read_hand(['2D', '9C', 'AS', 'AH', 'AC', '3D', '6D', '7D', 'TD', 'QD'])))
# %%
total_sum = 0
for i in range(1000):
    total_sum += compare_hands(*read_hand(data[i]))
print(total_sum)
