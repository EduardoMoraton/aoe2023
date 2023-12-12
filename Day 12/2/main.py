
import re
from itertools import product
from multiprocessing import Pool

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

memo = {}

def count_combinations(spring_condition, replacements):
    if spring_condition == "":
        return 1 if not replacements else 0

    if not replacements:
        return 0 if "#" in spring_condition else 1

    if (spring_condition, replacements) in memo:
        return memo[spring_condition, replacements]
    
    result = 0

    if spring_condition[0] in ".?":
        result += count_combinations(spring_condition[1:], replacements)

    if spring_condition[0] in "#?":
        if replacements[0] <= len(spring_condition) and "." not in spring_condition[:replacements[0]] and (
                replacements[0] == len(spring_condition) or spring_condition[replacements[0]] != "#"):
            result += count_combinations(spring_condition[replacements[0] + 1:], replacements[1:])
    memo[(spring_condition, replacements)] = result
    return result





if __name__ == "__main__":
    total = 0
    for record, info in rows:
        record5 = ""
        for i in range(5):
            record5 += record + "?"
        record5 = record5[:-1]
        info = tuple(map(int, info))
        info *= 5
        correct_count = count_combinations(record5, info)
        print(correct_count)
        total += correct_count
print(total)