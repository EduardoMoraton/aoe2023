
data_path = '../input.txt'


class Cube:
    def __init__(self, color, num):
        self.color = color
        self.num = num

class Game:
    total_sets = []
    def __init__(self, id, game_sets):
        self.id = id
        self.game_sets = game_sets
        
    def verify(self, cube_set):
        for game_set in self.game_sets:
            for cube in game_set:
                if (cube.num > next(cu.num for cu in cube_set if cu.color == cube.color)):
                    return False

    def power_of_min_possible(self):
        min_red = max(cube.num for cube_set in self.game_sets for cube in cube_set if cube.color == "red")
        min_green = max(cube.num for cube_set in self.game_sets for cube in cube_set if cube.color == "green")
        min_blue = max(cube.num for cube_set in self.game_sets for cube in cube_set if cube.color == "blue")
        return min_red * min_green * min_blue
    
        return True

    def show(self):
        print("=====")
        print("id: " + str(self.id))
        for game_set in self.game_sets:
            print("--")
            for cube in game_set:
                
                print(cube.color + ": " + str(cube.num))
        print("=====")


lines = []
with open(data_path, 'r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

reds = Cube("red", 12)
greens = Cube("green", 13)
blues = Cube("blue", 14)
cube_set = [reds, greens, blues]
sets_of_sets = [cube_set, cube_set.copy(), cube_set.copy()]

games = []
for line in lines:
    line_arr = line.split(":")
    game_id = int(line_arr[0].split(" ")[1])
    sets = line_arr[1].split(";")
    game_sets = []
    for s in sets:
        game_set = []
        aux = s.split(",")
        for a in aux:
            a = a.split(" ")
            cube = Cube(a[2], int(a[1]))
            game_set.append(cube)
        game_sets.append(game_set)
    games.append(Game(game_id, game_sets))


power_sum = 0
for game in games:
    power_sum += game.power_of_min_possible()

print(power_sum)
