def parse(fn: str) -> dict[complex, str]:
    out = {}
    for i, line in enumerate(open(fn, "r").readlines()):
        for j, c in enumerate(line.strip()):
            out[complex(j, i)] = c
    return out


def removable(map: dict[complex, str]) -> list[complex]:
    can_be_removed = []
    for p in [_p for _p in map.keys() if map[_p] == "@"]:
        n_neighbors = 0
        for dir in [1, 1 + 1j, 1j, -1 + 1j, -1, -1 - 1j, -1j, 1 - 1j]:
            n_neighbors += map.get(p + dir) == "@"
        if n_neighbors < 4:
            can_be_removed.append(p)
    return can_be_removed


def solve(map: dict[complex, str]) -> tuple[int, int]:
    ans1, ans2 = len(removable(map)), 0
    while len(can_be_removed := removable(map)) > 0:
        for p in can_be_removed:
            map[p] = "."
        ans2 += len(can_be_removed)
    return ans1, ans2


if __name__ == "__main__":
    print(solve(parse("inputs/day04.txt")))
