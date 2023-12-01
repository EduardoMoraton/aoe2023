import re
data_path = '../input.txt'


with open(data_path, 'r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

num_arr = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


treated_lines = []

for line in lines:
    print(line)
    line_list = list(line)
    for num in num_arr:
        matches = re.finditer(num, line)
        for match in matches:
            line_list[match.start()] = str(num_arr.index(num)+1)
    treated_lines.append(''.join(line_list))
      

nums = [re.sub(r"[a-z]", "", l.strip()) for l in treated_lines]
treated_nums = [int(num[0] + num[-1]) for num in nums]

print(sum(treated_nums))
 
