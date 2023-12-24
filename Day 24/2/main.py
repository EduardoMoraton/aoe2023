import sympy

def read_hailstones(path):
    return [tuple(map(int, line.replace("@", ",").split(","))) for line in open(path)]

def create_symbols():
    return sympy.symbols("xr, yr, zr, vxr, vyr, vzr")

def create_equations(hailstones, symbols):
    xr, yr, zr, vxr, vyr, vzr = symbols
    equations = []

    for i, (sx, sy, sz, vx, vy, vz) in enumerate(hailstones):
        equations.append((xr - sx) * (vy - vyr) - (yr - sy) * (vx - vxr))
        equations.append((yr - sy) * (vz - vzr) - (zr - sz) * (vy - vyr))
        if i >= 2:
            break

    return equations

def find_solution(equations):
    return [soln for soln in sympy.solve(equations) if all(x % 1 == 0 for x in soln.values())]

def main():
    path = '../input.txt'
    hailstones = read_hailstones(path)
    symbols = create_symbols()
    equations = create_equations(hailstones, symbols)

    for equ in equations:
        print(equ)

    answers = find_solution(equations)
    answer = answers[0]

    print(answer[symbols[0]] + answer[symbols[1]] + answer[symbols[2]])
    print(len(hailstones) - 1)

if __name__ == "__main__":
    main()
