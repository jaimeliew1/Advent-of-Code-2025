from itertools import combinations
from scipy.optimize import linprog


def parse(fn: str) -> list:
    out = []
    for line in open(fn).readlines():
        parts = line.split()
        target = [1 if c == "#" else 0 for c in parts[0][1:-1]]
        buttons = [[c for c in map(int, p[1:-1].split(","))] for p in parts[1:-1]]
        joltage = list(map(int, parts[-1][1:-1].split(",")))
        out.append((target, buttons, joltage))
    return out


def min_buttons(target, buttons) -> int:
    for n in range(len(buttons)):
        for pressed in combinations(buttons, n):
            result = [sum(i in p for p in pressed) % 2 for i in range(len(target))]
            if result == target:
                return n


def solve(inputs: list) -> tuple[float, float]:
    ans1, ans2 = 0, 0
    for target, buttons, joltage in inputs:
        ans1 += min_buttons(target, buttons)
        c = [1 for _ in buttons]
        Aeq = [[int(i in b) for b in buttons] for i in range(len(joltage))]
        ans2 += int(linprog(c, A_eq=Aeq, b_eq=joltage, integrality=1).x.sum())
    return ans1, ans2


if __name__ == "__main__":
    print(solve(parse("inputs/day10.txt")))
