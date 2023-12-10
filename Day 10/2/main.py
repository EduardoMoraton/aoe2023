
# RESOURCES https://en.wikipedia.org/wiki/Point_in_polygon
# TODO: Method to get the pipe shape on "S"


data_path = '../input.txt'

data_str = []

with open(data_path, 'r') as file:
    data_str = file.readlines()

data_str = [line.strip() for line in data_str]

class Pipe:
    def __init__(self, icon, pos):
        self.icon = icon
        self.pos = pos
        self.exits = self.calculate_exits()
        self.pipes = []

    def calculate_exits(self):
        x, y = self.pos
        exits = []
        
        if self.icon == '|':
            exits.extend([(x, y-1), (x, y+1)])  # North and South
        elif self.icon == '-':
            exits.extend([(x-1, y), (x+1, y)])  # West and East
        elif self.icon == 'L':
            exits.extend([(x, y-1), (x+1, y)])  # North and East
        elif self.icon == 'J':
            exits.extend([(x, y-1), (x-1, y)])  # North and West
        elif self.icon == '7':
            exits.extend([(x, y+1), (x-1, y)])  # South and West
        elif self.icon == 'F':
            exits.extend([(x, y+1), (x+1, y)])  # South and East

        return exits

    def calculate_pipes(self, pipes):
        for pipe in pipes:
            if pipe.pos in self.exits:
                self.pipes.append(pipe)

        

    def show(self):
        print(f"{self.icon} {str(self.pos)} Exits: {self.exits} Pipes: {[str(pipe.pos) for pipe in self.pipes]}")

pipes = []

for y in range(len(data_str)):
    for x in range(len(data_str[y])):
        pos = (x, y)
        icon = data_str[y][x]
        if icon != "." and icon != "S":
            pipe = Pipe(icon, pos)
            pipes.append(pipe)
        if icon == "S":
            start_pos = pos

for pipe in pipes:
    pipe.calculate_pipes(pipes)

posible_starts = []

for pipe in pipes:
    if start_pos in pipe.exits:
        posible_starts.append(pipe)
start_pipe = posible_starts[0]

curr_pos = start_pipe.pos
curr_pipe = start_pipe



steps = 0
max_distance = 0
max_steps = 0

loop_pipes=[]
loop_pipes.append(curr_pipe)

while curr_pos != start_pos:
    steps+= 1
    exits = curr_pipe.pipes
    next_pipe = None
    if exits:
        for pipe in exits:
            pipe.pipes.remove(curr_pipe)
            next_pipe = pipe
        
        curr_pipe = next_pipe
        loop_pipes.append(curr_pipe)
        curr_pos = curr_pipe.pos


    else:
        curr_pos = start_pos
print((steps+1)/2)



s_icon = input("Tell the s_icon do CTRL+F")

s_pipe = Pipe(s_icon, start_pos)
loop_pipes.append(s_pipe)




def fill_white_spaces(objects):
    max_x = max(obj.pos[0] for obj in objects) + 1
    max_y = max(obj.pos[1] for obj in objects) + 1

    grid = [[' ' for _ in range(max_x)] for _ in range(max_y)]

    for obj in objects:
        x, y = obj.pos
        grid[y][x] = obj.icon  
        for row in grid:
        print(' '.join(str(cell) for cell in row))

fill_white_spaces(loop_pipes)

total = 0
for y in range(len(data_str)):
    print(data_str[y])
    for x in range(len(data_str[y])):
        icon = data_str[y][x]
        curr_pos = (x, y)   
        count = 0

        if all(curr_pos != p.pos for p in loop_pipes):
            line = [pipe for pipe in loop_pipes if pipe.pos[1] == y]
            line_icons = [pipe.icon for pipe in line if pipe.pos[0]<x]
            
            if line_icons:
                for pipe_icon in line_icons:
                    if pipe_icon in ["J", "|", "L"]:
                        count += 1
                if count > 0 and count % 2 == 1:
                    total += 1
        else:
            continue


print(total)

