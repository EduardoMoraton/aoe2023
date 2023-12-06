
data_path = '../input.txt'
from functools import reduce


with open(data_path, 'r') as file:
    lines = file.readlines()
lines = [line.strip() for line in lines]
t = [line for line in lines[0].split(' ') if line]
d = [line for line in lines[1].split(' ') if line]

data = []
time = ''
distance = ''
for i in range(1, len(t)):
    time += t[i]
    distance += d[i]



def calculate_win_times(data):
    time, distance = data
    
    times_beaten = 0
    for vel in range(time+1):
        time_left = time - vel
        if (time_left * vel) > distance:
            times_beaten += 1
    return times_beaten
record = (int(time), int(distance))

win_times = calculate_win_times(record)
print(win_times)
