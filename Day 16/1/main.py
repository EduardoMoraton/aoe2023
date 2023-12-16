from collections import deque
path = '../input.txt'

grid = open(path).read().splitlines()


a = [(0,-1, 0, 1)]

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
print(len(coords))
