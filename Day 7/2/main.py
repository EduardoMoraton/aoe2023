
from itertools import groupby
data_path = '../input.txt'


with open(data_path, 'r') as file:
    lines = file.readlines()
lines = [line.strip() for line in lines]



hands = []

def get_card_type(hand):
    card_counts = {card: hand.count(card) for card in set(hand)}

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


class Hand:
    def __init__(self, hand, value):
        self.hand = hand
        self.value = value
        self.hand_type = self.get_card_type_joker()
    
    def get_card_type_joker(self):
        high = 0
        hand_set = set(self.hand)
        hand = self.hand
        if 'J' in hand_set and len(hand_set) > 1:
            cus = "AKQT98765432"
            new_hands = []
            for c in hand:
                if c != 'J':
                    hand = hand.replace("J", c)
                    val = get_card_type(hand)
                    hand = self.hand
                    if val>high:
                        high = val
            return high
        else:
            return get_card_type(self.hand)

    def __str__(self):
        return f"{self.hand} type: {str(self.hand_type)} bid: {str(self.value)}"

hands = []

for line in lines:
    hands.append(Hand(line.split(" ")[0], int(line.split(" ")[1])))

hands.sort(key=lambda x: x.hand_type)
grouped_hands = {key: list(group) for key, group in groupby(hands, key=lambda x: x.hand_type)}

custom_order = "AKQT98765432J"
for hand_type, group in grouped_hands.items():
    group.sort(key=lambda hand: [custom_order.index(card) for card in hand.hand], reverse=True) 
    grouped_hands[hand_type] = group

full_hands = []
for hand_type, hands in grouped_hands.items():
    for hand in hands:
        full_hands.append(hand)
total = 0
for i, hand in enumerate(full_hands):
    print(str(hand))
    total += hand.value*(i+1)
print(total)
