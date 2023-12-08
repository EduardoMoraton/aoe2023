from itertools import cycle

data_path = '../input.txt'

with open(data_path, 'r') as file:
    lines = file.readlines()


class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def show(self):
        print(self.name)
        for child in self.children:
            print("    " + child.name)

instr_arr = list(lines[0].strip())


instr = cycle(list(lines[0].strip()))

nodes = []


def find_in_nodes(nodes, name):
    for node in nodes:
        if node.name == name:
            return node
    return None


for line in lines[2:]:
    line = line.strip()
    arr = line.split("=")
    name = arr[0].strip()
    node = find_in_nodes(nodes, name)
    if node is None:
        node = Node(name)
        nodes.append(node)

    chd_arr = arr[1].replace(")", "").replace("(", "").split(",")
    children_str = [c.strip() for c in chd_arr]
    for c in children_str:
        chl = find_in_nodes(nodes, c)
        if chl is None:
            child_node = Node(c)
            nodes.append(child_node)
            node.children.append(child_node)
        else:
            node.children.append(chl)



print("------------")
curr_node = find_in_nodes(nodes, "AAA")
steps = 0
while curr_node.name != "ZZZ":
    curr_instr = next(instr)
    steps += 1
    if curr_instr == "L":
        curr_node = curr_node.children[0]
    else:
        curr_node = curr_node.children[1]

print(steps)
