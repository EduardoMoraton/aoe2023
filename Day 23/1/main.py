path = '../input.txt'
grid_lines = open(path).read().splitlines()

start_point = (0, grid_lines[0].index("."))
end_point = (len(grid_lines) - 1, grid_lines[-1].index("."))

points_list = [start_point, end_point]

for row_index, row in enumerate(grid_lines):
    for col_index, char in enumerate(row):
        if char == "#":
            continue
        neighbors_count = 0
        for n_row, n_col in [(row_index - 1, col_index), (row_index + 1, col_index), (row_index, col_index - 1), (row_index, col_index + 1)]:
            if 0 <= n_row < len(grid_lines) and 0 <= n_col < len(grid_lines[0]) and grid_lines[n_row][n_col] != "#":
                neighbors_count += 1
        if neighbors_count >= 3:
            points_list.append((row_index, col_index))

graph = {point: {} for point in points_list}

directions = {
    "^": [(-1, 0)],
    "v": [(1, 0)],
    "<": [(0, -1)],
    ">": [(0, 1)],
    ".": [(-1, 0), (1, 0), (0, -1), (0, 1)],
}

for s_row, s_col in points_list:
    stack = [(0, s_row, s_col)]
    visited = {(s_row, s_col)}

    while stack:
        distance, row, col = stack.pop()
        
        if distance != 0 and (row, col) in points_list:
            graph[(s_row, s_col)][(row, col)] = distance
            continue

        for d_row, d_col in directions[grid_lines[row][col]]:
            new_row = row + d_row
            new_col = col + d_col
            if 0 <= new_row < len(grid_lines) and 0 <= new_col < len(grid_lines[0]) and grid_lines[new_row][new_col] != "#" and (new_row, new_col) not in visited:
                stack.append((distance + 1, new_row, new_col))
                visited.add((new_row, new_col))

visited_set = set()

def dfs(current_point):
    if current_point == end_point:
        return 0

    max_distance = -float("inf")

    visited_set.add(current_point)
    for next_point in graph[current_point]:
        if next_point not in visited_set:
            max_distance = max(max_distance, dfs(next_point) + graph[current_point][next_point])
    visited_set.remove(current_point)

    return max_distance

print(dfs(start_point))
