
data_path = '../input.txt'



with open(data_path, 'r') as file:
    lines = file.readlines()

data = []
for line in lines:
    data.append([int(num.strip()) for num in line.split(" ")])


def predict(history):
    differences = [next - curr for curr, next in zip(history, history[1:])]

    if all(dif == 0 for dif in differences):
        return history[-1] + differences[-1]
    else:
        return history[-1] + predict(differences)


print(data)
sum = 0
for hist in data:
    sum += predict(hist)

print(sum)

