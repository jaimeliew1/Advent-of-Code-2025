def parse(fn: str) -> list[tuple[float]]:
    out = []
    for line in open(fn).readlines():
        a, b = line.strip().split(",")
        out.append((int(a), int(b)))
    return out


def solve(coords: list[tuple[float]]) -> tuple[float, float]:
    ans1 = 0
    for i, (a, b) in enumerate(coords):
        for aa, bb in coords[i + 1 :]:
            ans1 = max(ans1, abs((a - aa + 1) * (b - bb + 1)))
    return ans1, 0


if __name__ == "__main__":
    print(solve(parse("inputs/day09.txt")))
