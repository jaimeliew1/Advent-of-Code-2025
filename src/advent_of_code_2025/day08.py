import math


def parse(fn: str) -> list[tuple[float]]:
    out = []
    for line in open(fn).readlines():
        a, b, c = line.split(",")
        out.append((int(a), int(b), int(c)))
    return out


def solve(coords) -> tuple[float, float]:
    pairs = []
    for i, (a, b, c) in enumerate(coords):
        for j, (aa, bb, cc) in enumerate(coords[i + 1 :]):
            pairs.append((i, i + j + 1, (a - aa) ** 2 + (b - bb) ** 2 + (c - cc) ** 2, a * aa))
    pairs.sort(key=lambda x: x[2])

    sets = []
    for i, (a, b, _, xx) in enumerate(pairs):
        set_a = next((s for s in sets if a in s), None)
        set_b = next((s for s in sets if b in s), None)
        match set_a, set_b:
            case None, None:
                sets.append({a, b})
            case _set_a, None:
                _set_a.add(b)
            case None, _set_b:
                _set_b.add(a)
            case _set_a, _set_b if _set_a == _set_b:
                pass
            case _set_a, _set_b:
                set_a |= set_b
                sets.remove(set_b)

        if i == 999:
            lengths_sorted = sorted((len(x) for x in sets), reverse=True)
            ans1 = math.prod(lengths_sorted[:3])
        if len(sets[0]) == len(coords):
            ans2 = xx
            break

    return ans1, ans2


if __name__ == "__main__":
    print(solve(parse("inputs/day08.txt")))
