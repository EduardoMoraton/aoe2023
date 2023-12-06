from functools import reduce
data_path = '../input.txt'

with open(data_path, 'r') as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]


class Card:
    def __init__(self, winners, nums):
        self.winners = winners
        self.nums = nums

    def calculate_points(self):
        matches = list(set(self.winners) & set(self.nums))
        res = (2 ** (len(matches) - 1)) if len(matches) >= 1 else 0
        return res
    
cards = []
for line in lines:
    line = line.split(':')[1]
    winners_str_arr = line.split('|')[0].split(" ")
    winners = [int(w) for w in winners_str_arr if w]
    nums_str_arr = line.split('|')[1].split(" ")
    nums = [int(w) for w in nums_str_arr if w]
    cards.append(Card(winners, nums))


sum = 0
for card in cards:
    sum += card.calculate_points()
print(sum)
