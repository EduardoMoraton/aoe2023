from itertools import cycle
import time
import copy
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

def loop(map_data, direction):

    key = (tuple(tuple(row) for row in map_data), direction)


    while True:
        new_map = [row[:] for row in map_data]

        for rock in rocks:
            new_map_result = rock.move(new_map, direction)
            if new_map_result is not None:
                new_map = new_map_result

        if new_map == map_data:
            break

        map_data = new_map
        
    return map_data



def iterate(map_data):
    map_data2 = loop(map_data, "up")
    map_data3 = loop(map_data2, "left")
    map_data4 = loop(map_data3, "down")
    map_data5 = loop(map_data4, "right")
    return map_data5
maps = []
interval = 10000

goal_i = 1000000000
period = None

for i in range(goal_i):
    map_data = iterate(map_data)
    if map_data not in maps:
        maps.append(map_data)
    else:
        before_period = maps.index(map_data)
        period = i - before_period
        break
i_1000000000 = (goal_i - before_period) % period + before_period - 1
matrix = maps[i_1000000000]     
    
count = 0



for y in range(len(matrix)):
    for char in matrix[y]:
        if char == "O":
            count += len(matrix)-y


print(count)