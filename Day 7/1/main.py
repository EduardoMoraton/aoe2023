from itertools import groupby
data_path = '../input.txt'


with open(data_path, 'r') as file:
    lines = file.readlines()
lines = [line.strip() for line in lines]



hands = []


class Hand:
    def __init__(self, hand, value):
        self.hand = hand
        self.value = value
        self.hand_type = self.get_card_type()
    
    def get_card_type(self):
        card_counts = {card: self.hand.count(card) for card in set(self.hand)}

        if 5 in card_counts.values():
            return 7
        if 4 in card_counts.values():
            return 6
        if 3 in card_counts.values() and 2 in card_counts.values():
            return 5
        if 3 in card_counts.values():
            return 4
        if list(card_counts.values()).count(2) == 2:
            return 3      
        if 2 in card_counts.values():
            return 2
        return 1

    def __str__(self):
        return f"{self.hand} type: {str(self.hand_type)} bid: {str(self.value)}"

hands = []

for line in lines:
    hands.append(Hand(line.split(" ")[0], int(line.split(" ")[1])))

hands.sort(key=lambda x: x.hand_type)
grouped_hands = {key: list(group) for key, group in groupby(hands, key=lambda x: x.hand_type)}

custom_order = "AKQJT98765432"
for hand_type, group in grouped_hands.items():
    group.sort(key=lambda hand: [custom_order.index(card) for card in hand.hand], reverse=True) 
    grouped_hands[hand_type] = group

full_hands = []
for hand_type, hands in grouped_hands.items():
    print(f'Hand Type: {hand_type}')
    for hand in hands:
        print(f'    {hand}')
        full_hands.append(hand)
total = 0
for i, hand in enumerate(full_hands):
    print(str(hand))
    total += hand.value*(i+1)
print(total)
