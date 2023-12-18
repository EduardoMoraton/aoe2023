
from heapq import heappush, heappop

path = "../input.txt"

grid = [list(map(int, line.strip())) for line in open(path)]

seen = set()

heat_loss = 0
sx = 0
sy = 0
dx = 0
dy = 0
same_dir = 0
pq = [(heat_loss, sx, sy, dx, dy, same_dir)]

while pq:
    hl, row, col, drow, dcol, n = heappop(pq)

    if row == len(grid) - 1 and col == len(grid[0]) - 1 and n >= 4:
        print(hl)
        break

    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
        continue
    if (row, col, drow, dcol, n) in seen:
        continue

    seen.add((row, col, drow, dcol, n))

    if n < 10 and (drow, dcol) != (0, 0):
        next_row = row + drow
        next_col = col + dcol
        if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]):
            heappush(pq, (hl + grid[next_row][next_col], next_row, next_col, drow, dcol, n + 1))
    
    if n >= 4 or (drow, dcol) == (0,0):
        for nei_row, nei_col in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if (nei_row, nei_col) != (drow, dcol) and (nei_row, nei_col) != (-drow, -dcol):
                next_row = row + nei_row
                next_col = col + nei_col
                if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]):
                    heappush(pq, (hl + grid[next_row][next_col], next_row, next_col, nei_row, nei_col, 1))

