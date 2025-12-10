from itertools import combinations


def parse(fn: str) -> list[tuple[float]]:
    return [eval(p) for p in open(fn).readlines()]


def solve(coords) -> tuple[float, float]:
    pairs = sorted(combinations(coords, 2), key=lambda x: sum((a - b) ** 2 for a, b in zip(*x)))
    sets = []
    for i, (p1, p2) in enumerate(pairs):
        set_a = next((s for s in sets if p1 in s), None)
        set_b = next((s for s in sets if p2 in s), None)
        match set_a, set_b:
            case None, None:
                sets.append({p1, p2})
            case _set_a, None:
                _set_a.add(p2)
            case None, _set_b:
                _set_b.add(p1)
            case _set_a, _set_b if _set_a != _set_b:
                set_a |= set_b
                sets.remove(set_b)

        if i == 999:
            lens = sorted((len(x) for x in sets), reverse=True)
            ans1 = lens[0] * lens[1] * lens[2]
        if len(sets[0]) == len(coords):
            return ans1, p1[0] * p2[0]


if __name__ == "__main__":
    print(solve(parse("inputs/day08.txt")))
