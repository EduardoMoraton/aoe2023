data_path = '../input.txt'



with open(data_path, 'r') as file:
    lines = file.readlines()

data = []
for line in lines:
    data.append([int(num.strip()) for num in line.split(" ")])


def predict(history):
    differences = [curr-next for curr, next in zip(history, history[1:])]

    if all(dif == 0 for dif in differences):
        res = differences[-1] + history[-1]
        return res
    else:
        res = history[-1] - predict(differences)
        return res


print(data)
sum = 0
for hist in data:
    hist.reverse()
    val = predict(hist)
    sum += val 
print(sum)

