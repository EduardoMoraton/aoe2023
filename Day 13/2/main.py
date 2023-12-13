import numpy as np
data_path = "../input.txt"

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

print(len(panels))
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
            if top != bot:
                print(top)
                top_str = ''.join(top)
                bot_str = ''.join(bot)
                s = sum(1 for char1, char2 in zip(top_str, bot_str) if char1 != char2)
                if s == 1:
                    print(abobe)
                    print(s)
                    print(top_str)
                    print(bot_str)


                    return abobe
    return -1
        
        


def summarize(panel):
    r = reflect(panel)
    if r == -1:
        panel = [list(line) for line in panel]
        panel = np.array(panel).T.tolist()
        print(panel)
        panel = [''.join(p) for p in panel]
        return reflect(panel)
    else:
        return r * 100

total = 0
for i, panel in enumerate(panels, 1):
    curr_sum = summarize(panel)
    total += curr_sum
print(total)
