
path = '../input.txt'

line = open(path).readlines()[0]

line = line.strip()

steps = []

for step in line.split(","):
    steps.append(step)

map = [[] for _ in range(256)] 
focal = {}

def hash_it(s):
    val = 0
    for c in s:
        val += ord(c)
        val *= 17
        val %= 256
    return val



for step in steps:
    if "-" in step:
        label, num = step.split("-")
        print(label)
        idx = hash_it(label)
        if label in map[idx]:
            map[idx].remove(label)
    else:
        label, num = step.split("=")
        idx = hash_it(label)
        if label not in map[idx]:
            map[idx].append(label)

        focal[label] = int(num)
total = 0
for i, box in enumerate(map, 1):
    for j, label in enumerate(box, 1):
        total += i * j * focal[label]
print(total)

