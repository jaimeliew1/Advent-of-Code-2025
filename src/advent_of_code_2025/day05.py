def parse(fn: str):
    ranges_raw, ing = open(fn, "r").read().split("\n\n")
    ranges = []
    for line in ranges_raw.splitlines():
        a, b = line.split("-")
        ranges.append((int(a), int(b)))
    return ranges, [int(x) for x in ing.splitlines()]


def solve(ranges, ingredients) -> tuple[int, int]:
    ans1 = sum(any(a <= ing <= b for a, b in ranges) for ing in ingredients)
    points = sorted([x for xs in ranges for x in xs])

    ans2 = points[-1] - points[0] + 1
    for i, p in enumerate(points[:-1]):
        if any(a <= p + 1 <= b for a, b in ranges) or any(
            a <= points[i + 1] - 1 <= b for a, b in ranges
        ):  
            continue
        ans2 -= points[i+1] - p - 1
    return ans1, ans2


if __name__ == "__main__":
    print(solve(*parse("inputs/day05.txt")))
