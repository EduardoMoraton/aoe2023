from collections import deque


path = '../input.txt'

grid = open(path).read().splitlines()

start_row, start_col = next((row, col) for row, r, in enumerate(grid) for col, c in enumerate(r) if  c == "S")


res = set()
seen = {(start_row, start_col)}
q = deque([(start_row, start_col, 64)])

while q:
    row, col, steps = q.popleft()

    if steps % 2 == 0: 
        res.add((row, col))
    if steps == 0:
        continue
    
    for nr, nc in [(row + 1, col), (row -1, col), (row, col + 1), (row, col -1)]:
        if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]) or grid[nr][nc] == "#" or (nr,nc) in seen:
            continue
        seen.add((nr,nc))
        q.append((nr,nc,steps-1))



print(len(res))
