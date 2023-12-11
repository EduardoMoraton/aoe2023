import numpy as np
data_path = '../input.txt'

with open(data_path, 'r') as file:
    lines = file.readlines()
lines = [list(line.strip()) for line in lines]
expanded = []



def show(universe):
    for line in universe:
        print(line)


#Expand X
for line in lines:
    expanded.append(line)
    if not "#" in line:
        expanded.append(line)
#Expand Y
expanded = np.array(expanded).T.tolist()
full_expanded = []

for line in expanded:
    full_expanded.append(line)
    if not "#" in line:
        full_expanded.append(line)

full_expanded = np.array(full_expanded).T.tolist()

print("EXPANDED")



uni = full_expanded
galaxies = []


def distance(a,b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

for y, line in enumerate(uni):
    for x in range(len(line)):
        if line[x] == "#":
            galaxies.append((x,y))
print(galaxies)

sum = 0
for gal_index, gal in enumerate(galaxies):
    for gal2_index, gal2 in enumerate(galaxies):
        if gal != gal2:
            d = distance(gal, gal2)
            # print(str(gal_index+1) + ' : ' + str(gal2_index+1) + ' => ' + str(d))
            sum += d
print(sum/2)

