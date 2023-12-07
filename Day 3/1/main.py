import re
data_path = '../input.txt'

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
    


nums = []



results = []

def find_all_numbers(input_string):
    pattern = re.compile(r'\b(?:\d+|\d+\.\d+)\b')
    line_match = [(match.start(), match.end(), match.group()) for match in pattern.finditer(input_string)]
    return line_match

for i in range(len(arr)):
    line = ""
    for j in range(len(arr)):
        curr_char = arr[i][j]

        line += curr_char
    results.append(find_all_numbers(line))

    

for y in range(len(results)):
    for start_idx, end_idx, value in results[y]:
        nums.append(Number(value, [start_idx, y], [end_idx, y]))

sum = 0
for num in nums:
    if num.is_symbol_around(arr):
        print(num.value)
        sum += int(num.value)

print(sum)
