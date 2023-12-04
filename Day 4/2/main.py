from functools import reduce
data_path = '../input.txt'

with open(data_path, 'r') as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]


class Card:
    def __init__(self, winners, nums, index):
        self.index = index
        self.winners = winners
        self.nums = nums

    def calculate_matches(self):
        matches = list(set(self.winners) & set(self.nums))
        return len(matches)
    
cards = []
for i, line in enumerate(lines):
    line = line.split(':')[1]
    winners_str_arr = line.split('|')[0].split(" ")
    winners = [int(w) for w in winners_str_arr if w]
    nums_str_arr = line.split('|')[1].split(" ")
    nums = [int(w) for w in nums_str_arr if w]
    cards.append(Card(winners, nums, i))


sum = 0

def add_under_index(cards, index, new_card):
    updated_cards = []
    for card in cards:
        updated_cards.append(card)
        if card.index == index:
            updated_cards.append(new_card)  
    return updated_cards

reference_cards = cards.copy()
for i, card in enumerate(cards):
    matches = card.calculate_matches()
    for j in range(0, matches):
        idx = card.index + j + 1
        if idx < len(reference_cards):
            cards = add_under_index(cards, card.index, reference_cards[idx])


        
print(len(cards))
