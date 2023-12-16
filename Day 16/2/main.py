from collections import deque
path = '../input.txt'

grid = open(path).read().splitlines()

def process(row, col, drow, dcol):
    a = [(row,col, drow, dcol)]

    seen = set()
    q = deque(a)

    while q:
        row, col, drow, dcol = q.popleft()

        row += drow
        col += dcol

        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            continue

        cell = grid[row][col]

        if cell == "." or (cell == "-" and dcol != 0) or (cell == "|" and drow != 0):
            if (row, col, drow, dcol) not in seen:
                seen.add((row, col, drow, dcol))
                q.append((row, col, drow, dcol))
        elif cell == "/":
            drow, dcol = -dcol, -drow
            if (row, col, drow, dcol) not in seen:
                seen.add((row, col, drow, dcol))
                q.append((row, col, drow, dcol))
        elif cell == "\\":
            drow, dcol = dcol, drow
            if (row, col, drow, dcol) not in seen:
                seen.add((row, col, drow, dcol))
                q.append((row, col, drow, dcol))
        else:
            for drow, dcol in [(1, 0), (-1, 0)] if cell == "|" else [(0, 1), (0, -1)]:
                if (row, col, drow, dcol) not in seen:
                    seen.add((row, col, drow, dcol))
                    q.append((row, col, drow, dcol))             
    coords = {(r, c) for (r, c, _, _) in seen}
    return len(coords)
max_val = 0

for r in range(len(grid)):
    max_val = max(max_val, process(r, -1, 0, 1))
    max_val = max(max_val, process(r, len(grid[0]), 0, -1))
for c in range(len(grid)):
    max_val = max(max_val, process(-1, c, 1, 0))
    max_vañ = max(max_val, process(len(grid), c, -1, 0))
print(max_val)
