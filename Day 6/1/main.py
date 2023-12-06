data_path = '../input.txt'
from functools import reduce


with open(data_path, 'r') as file:
    lines = file.readlines()
lines = [line.strip() for line in lines]
t = [line for line in lines[0].split(' ') if line]
d = [line for line in lines[1].split(' ') if line]

data = []
for i in range(1, len(t)):
    data.append((int(t[i]), int(d[i])))
print(data)



def calculate_win_times(data):
    time, distance = data
    
    times_beaten = 0
    for vel in range(time+1):
        time_left = time - vel
        if (time_left * vel) > distance:
            times_beaten += 1
    return times_beaten


res = []
for i, record in enumerate(data):
    print("record: " + str(i))
    res.append(calculate_win_times(record))
final_res = reduce(lambda a, b: a*b, res)
print(final_res)
