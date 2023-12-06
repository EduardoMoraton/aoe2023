import concurrent.futures
import numpy as np
data_path = "../input.txt"

with open(data_path) as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]




seeds = lines[0].split(":")[1].split(" ")
seeds = [int(seed) for seed in seeds if seed]
seed_ranges = []
for i in range(0,len(seeds),2):
    seed_ranges.append(range(seeds[i], seeds[i] + seeds[i+1]))

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


min_seed = float('inf')

def map_it(min_seed, seed):
    for map in maps:
        for line in map:
            dest, source, lenght = line
            source_range = range(source, source+lenght)
            if seed in source_range:
                seed = dest + (seed - source)
                break
    if seed < min_seed:
        min_seed = seed
    return min_seed

full_seeds = []

print("start")



smallest_start, maximum_stop = min(r[0] for r in seed_ranges), max(r[1] for r in seed_ranges)

print(smallest_start)
print(maximum_stop)

full_range = range(smallest_start, maximum_stop)

n = 10000  

step = len(range(full_range.start, full_range.stop)) // n + 1
subranges = []

start = full_range.start
for i in range(n):
    print("created range: " + str(i))
    subrange = range(start, start + step)
    subranges.append(subrange)
    start += step

min_seed = 99999999999999999
for i, ran in enumerate(subranges):
    print(ran)
    print("procesing range: " + str(i))
    for seed in ran:
        min_seed = map_it(min_seed, seed)
    print("procesed range: " + str(i))
    print(min_seed)
print(min_seed)