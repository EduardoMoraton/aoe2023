import numpy as np
data_path = "../test.txt"

lines = open(data_path).readlines()
lines = [line.strip() for line in lines]

panels = []
current_panel = []
for line in lines:
    if not line:
        if current_panel:
            panels.append(current_panel)
            current_panel = []
    else:
        current_panel.append(line)


if current_panel:
    panels.append(current_panel)
def reflect(panel):
    for i in range(len(panel)):
        top = panel[:i]
        bot = panel[i:]

        abobe = len(top) 

        top.reverse()
        min_length = min(len(top), len(bot))
        top = top[:min_length]
        bot = bot[:min_length]
        
        


        if top and bot:
            if bot == top:

                return abobe
    return -1
        
        


def summarize(panel):
    r = reflect(panel)
    if r == -1:
        panel = [list(line) for line in panel]
        panel = np.array(panel).T.tolist()
        
        return reflect(panel)
    else:
        return r * 100

total = 0
for i, panel in enumerate(panels, 1):
    curr_sum = summarize(panel)
    total += curr_sum
print(total)
