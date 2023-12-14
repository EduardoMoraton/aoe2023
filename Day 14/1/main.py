class Rock:
    def __init__(self, shape, pos):
        self.shape = shape
        self.pos = pos

    def move(self, map, direction):
        vector = (0, 0)

        if direction == "up":
            vector = (0, -1)
        elif direction == "down":
            vector = (0, 1)
        elif direction == "left":
            vector = (-1, 0)
        elif direction == "right":
            vector = (1, 0)

        y = self.pos[1] + vector[1]
        x = self.pos[0] + vector[0]

        if y < 0 or y >= len(map) or x < 0 or x >= len(map[0]):
            return None

        if map[y][x] == ".":
            map[self.pos[1]][self.pos[0]] = "."
            self.pos = (x, y)
            map[y][x] = self.shape
            return map

        return None

    def __str__(self):
        return self.shape


def show(map):
    for line in map:
        print("".join(line))


path = '../input.txt'
data = open(path).readlines()
data = [line.strip() for line in data]

rocks = []

for y in range(len(data)):
    for x in range(len(data[y])):
        cell = (x, y)
        if data[y][x] == "O":
            r = Rock(data[y][x], cell)
            rocks.append(r)

map_data = [list(row) for row in data]

while True:
    print("---")
    show(map_data)
    new_map = [row[:] for row in map_data]

    for rock in rocks:
        new_map_result = rock.move(new_map, "up")
        if new_map_result is not None:
            new_map = new_map_result

    if new_map == map_data:
        break

    map_data = new_map

count = 0


for y in range(len(map_data)):
    for char in map_data[y]:
        if char == "O":
            count += len(map_data)-y

print(count)
