path = "../input.txt"
block1, block2 = open(path).read().split("\n\n")



workflows = {}



for line in block1.split("\n"):
    line = line.strip()
    arr = line.split("{")
    name = arr[0]
    conditions = arr[1][:-1]
    workflows[name] = conditions


wf = "in"
total_sum = 0
for line in block2.split("\n")[:-1]:
    line = line.strip()
    line = line[1:-1]
    arr = line.split(",")
    ratings = {}
    for a in arr:
        a = a.split("=")
        ratings[a[0]] = a[1]
    
    res = ""
    total = 0
    wf = "in"
    while res != "A" and res != "R":
        conditions = workflows[wf]
        for c in conditions.split(","):
            if c == "A" or c == "R":
                res = c
                break
            if not ":" in c:
                wf = c
                continue
            
            for_eval = c.split(":")[0]
            expr = ratings[for_eval[0]]+for_eval[1:]
            if eval(expr):
                r = c.split(":")[1]
                if r == "A" or r == "R":
                    res = r
                    break
                else:
                    wf = r
                    break
            else:
                continue
    if res == "A":
        total_sum += sum(map(int, ratings.values()))
print(total_sum)


        
