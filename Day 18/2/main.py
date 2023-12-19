
path = '../input.txt'

lines = [line.strip() for line in open(path).readlines()]


class Instruction:
    def __init__(self, color, dir, depth):
        if dir == "U":
            self.dir = (-1,0)
        elif dir == "D":
            self.dir = (1,0)
        elif dir == "R":
            self.dir = (0,1)
        elif dir == "L":
            self.dir = (0,-1)
        self.color = color
        self.depth = depth


instructions = []
for line in lines:
    arr = line.split(" ")
    l = {0:"R",1:"D",2:"L",3:"U"}
    hex = arr[2][:-1][2:]
    print(arr)
    color = hex
    depth = int(hex[:-1], 16)
    dir = l[int(hex[-1])]
    instructions.append(Instruction(color, dir, depth))

points = []


start = (0,0)
points.append(start)
borders = 0
for ins in instructions:
    for d in range(ins.depth):
        borders += 1
        x, y = start
        dx, dy = ins.dir
        start = (x + dx, y + dy)
    points.append(start)



area = abs(sum(points[i][0] * (points[i-1][1] - points[(i+1)%len(points)][1]) for i in range(len(points)))) / 2
i = area - borders // 2 + 1
print(borders)
print(i+borders)

