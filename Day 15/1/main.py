
path = '../test.txt'

line = open(path).readlines()[0]

line = line.strip()

steps = []

for step in line.split(","):
    steps.append(step)

def hash(s):
    val = 0
    for c in s:
        val += ord(c)
        val *= 17
        val %= 256
    return val

print(sum([hash(step) for step in steps]))
