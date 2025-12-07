def parse(fn: str) -> dict[complex, str]:
    out = {}
    for i, line in enumerate(open(fn, "r").readlines()):
        for j, c in enumerate(line.strip()):
            out[complex(j, i)] = c
    return out


def solve(map: dict[complex, str]) -> tuple[int, int]:
    ans1, start = 0, [k for k, v in map.items() if v == "S"][0]
    frontier = [start]
    while frontier:
        k, to_add = frontier.pop(), []
        match map.get(k + 1j):
            case "|" | None:
                continue
            case ".":
                to_add.extend([k + 1j])
            case "^":
                to_add.extend([k + 1j + 1, k + 1j - 1])
                ans1 += 1
        for _k in to_add:
            map[_k] = "|"
            frontier.append(_k)

    row_max = int(max(k.imag for k in map.keys()))
    timelines = {}

    for row in range(row_max, -1, -1):
        for k, v in [(k, v) for k, v in map.items() if k.imag == row]:
            if v not in ["|", "S"]:
                continue
            match map.get(k + 1j - 1), map.get(k + 1j), map.get(k + 1j + 1):
                case _, None, _:
                    timelines[k] = 1
                case _, "|", _:
                    timelines[k] = timelines[k + 1j]
                case "|", _, "|":
                    timelines[k] = timelines[k + 1j - 1] + timelines[k + 1j + 1]

    return ans1, timelines[start]


if __name__ == "__main__":
    print(solve(parse("inputs/day07.txt")))
