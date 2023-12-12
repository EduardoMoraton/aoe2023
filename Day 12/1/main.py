import re
from itertools import product

data_path = "../input.txt"

with open(data_path, 'r') as file:
    lines = file.readlines()
lines = [line.strip() for line in lines]

rows = []
for line in lines:
    arr = line.split(" ")
    rows.append((arr[0], list(map(int, arr[1].split(",")))))

def is_correct(string, info):
    arr = string.split(".")
    len_arrs = [len(a) for a in arr if "#" in a]

    return info == len_arrs

def generate_combinations(spring_condition):
    question_indices = [i for i, char in enumerate(spring_condition) if char == "?"]

    replacements = product("#.", repeat=len(question_indices))

    combinations = []
    for replacement in replacements:
        current_combination = list(spring_condition)
        for index, rep_char in zip(question_indices, replacement):
            current_combination[index] = rep_char
        combinations.append("".join(current_combination))

    return combinations

total = 0
for record, info in rows:
    combinations = generate_combinations(record)
    correct_count = sum(is_correct(com, info) for com in combinations)
    total += correct_count
print(total)
