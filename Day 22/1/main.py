input_path = '../input.txt'

blocks = [list(map(int, line.replace("~", ",").split(","))) for line in open(input_path)]
blocks.sort(key=lambda block: block[2])

def has_overlap(block1, block2):
    return max(block1[0], block2[0]) <= min(block1[3], block2[3]) and max(block1[1], block2[1]) <= min(block1[4], block2[4])

for index, block in enumerate(blocks):
    max_height = 1
    for check_block in blocks[:index]:
        if has_overlap(block, check_block):
            max_height = max(max_height, check_block[5] + 1)
    block[5] -= block[2] - max_height
    block[2] = max_height

blocks.sort(key=lambda block: block[2])

k_supports_v = {i: set() for i in range(len(blocks))}
v_supports_k = {i: set() for i in range(len(blocks))}

for j, upper_block in enumerate(blocks):
    for i, lower_block in enumerate(blocks[:j]):
        if has_overlap(lower_block, upper_block) and upper_block[2] == lower_block[5] + 1:
            k_supports_v[i].add(j)
            v_supports_k[j].add(i)

total_supported_blocks = 0

for i in range(len(blocks)):
    if all(len(v_supports_k[j]) >= 2 for j in k_supports_v[i]):
        total_supported_blocks += 1

print(total_supported_blocks)
