data_path = "../input.txt"

with open(data_path) as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]




seeds = lines[0].split(":")[1].split(" ")
seeds = [int(seed) for seed in seeds if seed]



maps = []
maplist = []

for line in lines[1:]: 
    if line == "-":
        if maplist:
            maps.append(maplist)
            maplist = []  
        else:
            print("Empty maplist, skipping")

    else:
        maplist.append([int(num) for num in line.split()])

if maplist:
    maps.append(maplist)

final_seeds = []

for seed_index in range(len(seeds)):
    seed = seeds[seed_index] 
    for map in maps:
        for line in map:
            dest, source, lenght = line
            source_range = range(source, source+lenght)
            if seed in source_range:
                seed = dest + (seed - source)
                break
    final_seeds.append(seed)
print(min(final_seeds))


