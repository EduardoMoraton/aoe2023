
import re
from functools import reduce
data_path = '../test.txt'

with open(data_path, 'r') as file:
    lines = file.readlines()
    arr = [list(line.strip()) for line in lines]



class Number:
    def __init__(self, value, start_pos, end_pos):
        self.value = value
        self.start_pos = start_pos
        self.end_pos = end_pos

    def is_symbol_around(self, arr):
        start_x, start_y = self.start_pos
        end_x, end_y = self.end_pos


        for i in range(start_y - 1, end_y + 2):
            line = ""
            for j in range(start_x - 1, end_x + 1):
                if (i<0) or (i >= len(arr)) or (j < 0) or (j>=len(arr[0])):
                    char = "O"
                else:
                    char = arr[i][j]
                if char != "." and char != "O" and not char.isdigit():
                    return True
        return False
    def __str__(self):
        return self.value + ' start: ' + str(self.start_pos) + ' end: ' + str(self.end_pos)
    
class Gear:
    def __init__(self, pos):
        self.pos = pos    

    def numbers_arround(self, numbers):
        x, y = self.pos
        nums = []


        for i in range(y - 1, y+2):
            for j in range(x - 1, x + 2):
                for num in numbers:   
                    x1 = num.start_pos[0]
                    y1 = num.start_pos[1]
                    x2 = num.end_pos[0]
                    y2 = num.end_pos[1]
                    if ((i == y1) and (j == x1)) or ((i == y2) and (j == x2-1)):
                        nums.append(int(num.value))
                        numbers.remove(num)
                        
                        
        return nums
    def __str__(self):
        return str(self.pos)


def find_all_numbers(input_string):
    pattern = re.compile(r'\b(?:\d+|\d+\.\d+)\b')
    line_match = [(match.start(), match.end(), match.group()) for match in pattern.finditer(input_string)]
    return line_match

def find_all_gears(input_string):
    pattern = re.compile(r'\*')
    line_match = [(match.start(), match.end(), match.group()) for match in pattern.finditer(input_string)]
    return line_match

results = []
results_gears = []
# Parse
for i in range(len(arr)):
    line = ""
    for j in range(len(arr)):
        curr_char = arr[i][j]

        line += curr_char
    results.append(find_all_numbers(line))
    results_gears.append(find_all_gears(line))


nums = []
## Create Numbers
for y in range(len(results)):
    for start_idx, end_idx, value in results[y]:
        nums.append(Number(value, [start_idx, y], [end_idx, y]))

gears = []
## Create Gears
for y in range(len(results_gears)):
    for start_idx, end_idx, value in results_gears[y]:
        gears.append(Gear([start_idx, y]))

sum = 0
for gear in gears:
    l = gear.numbers_arround(nums)
    if (len(l)>=2):
        res = reduce((lambda x, y: x*y), l)
        sum += res
print(sum)
