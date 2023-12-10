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
        loop_pipes.append(loop_pipes)
        curr_pos = curr_pipe.pos


    else:
        curr_pos = start_pos
print((steps+1)/2)





