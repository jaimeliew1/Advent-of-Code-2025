from itertools import combinations, pairwise


def parse(fn: str) -> list[tuple[float]]:
    out = []
    for line in open(fn).readlines():
        a, b = line.strip().split(",")
        out.append((int(a), int(b)))
    out.append(out[0])
    return out


def area(a, b, aa, bb) -> int:
    return (aa - a + 1) * (bb - b + 1)


def solve(polygon: list[tuple[float]]) -> tuple[float, float]:
    pairs = []
    for (a, b), (aa, bb) in combinations(polygon, r=2):
        pairs.append((min(a, aa), min(b, bb), max(a, aa), max(b, bb)))
    pairs = sorted(pairs, key=lambda x: area(*x), reverse=True)

    for a, b, aa, bb in pairs:
        for (p, q), (r, s) in pairwise(polygon):
            if p < aa and r > a and q < bb and s > b:
                break
        else:
            return area(*pairs[0]), area(a, b, aa, bb)


if __name__ == "__main__":
    print(solve(parse("inputs/day09.txt")))
