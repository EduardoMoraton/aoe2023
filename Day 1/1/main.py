import re
data_path = '../input.txt'


with open(data_path, 'r') as file:
    lines = file.readlines()

nums = [re.sub(r"[a-z]", "", l.strip()) for l in lines]

treated_nums = [int(num[0] + num[-1]) for num in nums]

print(sum(treated_nums))

