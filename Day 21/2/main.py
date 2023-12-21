from collections import deque

def read_grid(path):
    return open(path).read().splitlines()

def find_starting_position(grid):
    return next((r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == "S")

def traverse(sr, sc, ss, grid):
    result_set = set()
    seen_set = {(sr, sc)}
    queue = deque([(sr, sc, ss)])

    while queue:
        r, c, s = queue.popleft()

        if s % 2 == 0:
            result_set.add((r, c))
        if s == 0:
            continue

        for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if (
                nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0])
                or grid[nr][nc] == "#" or (nr, nc) in seen_set
            ):
                continue
            seen_set.add((nr, nc))
            queue.append((nr, nc, s - 1))

    return len(result_set)

def main():
    input_path = '../input.txt'
    grid_data = read_grid(input_path)

    start_row, start_col = find_starting_position(grid_data)
    grid_size = len(grid_data)
    total_steps = 26501365

    assert len(grid_data) == len(grid_data[0])
    assert start_row == start_col == grid_size // 2
    assert total_steps % grid_size == grid_size // 2

    grid_width = total_steps // grid_size - 1

    odd_size = (grid_width // 2 * 2 + 1) ** 2
    even_size = ((grid_width + 1) // 2 * 2) ** 2

    odd_points = traverse(start_row, start_col, grid_size * 2 + 1, grid_data)
    even_points = traverse(start_row, start_col, grid_size * 2, grid_data)

    corner_top = traverse(grid_size - 1, start_col, grid_size - 1, grid_data)
    corner_right = traverse(start_row, 0, grid_size - 1, grid_data)
    corner_bottom = traverse(0, start_col, grid_size - 1, grid_data)
    corner_left = traverse(start_row, grid_size - 1, grid_size - 1, grid_data)

    small_top_right = traverse(grid_size - 1, 0, grid_size // 2 - 1, grid_data)
    small_top_left = traverse(grid_size - 1, grid_size - 1, grid_size // 2 - 1, grid_data)
    small_bottom_right = traverse(0, 0, grid_size // 2 - 1, grid_data)
    small_bottom_left = traverse(0, grid_size - 1, grid_size // 2 - 1, grid_data)

    large_top_right = traverse(grid_size - 1, 0, grid_size * 3 // 2 - 1, grid_data)
    large_top_left = traverse(grid_size - 1, grid_size - 1, grid_size * 3 // 2 - 1, grid_data)
    large_bottom_right = traverse(0, 0, grid_size * 3 // 2 - 1, grid_data)
    large_bottom_left = traverse(0, grid_size - 1, grid_size * 3 // 2 - 1, grid_data)

    result = (
        odd_size * odd_points +
        even_size * even_points +
        corner_top + corner_right + corner_bottom + corner_left +
        (grid_width + 1) * (small_top_right + small_top_left + small_bottom_right + small_bottom_left) +
        grid_width * (large_top_right + large_top_left + large_bottom_right + large_bottom_left)
    )

    print(result)

if __name__ == "__main__":
    main()
