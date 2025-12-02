def parse(fn: str) -> list[tuple[int, int]]:
    return [(x.split("-")[0], x.split("-")[1]) for x in open(fn).read().split(",")]


def solve(ranges: list[tuple[int, int]]) -> tuple[int, int]:
    ans1_set, ans2_set = set(), set()
    for a, b in ranges:
        for x in range(int(a), int(b) + 1):
            n = len(str(x))
            divisors = [i for i in range(1, n) if n % i == 0]

            for div in divisors:
                x_str = str(x)
                parts = [x_str[i : i + div] for i in range(0, n, div)]
                if all(part == parts[0] for part in parts):
                    ans2_set.add(x)
                    if len(parts) == 2:
                        ans1_set.add(x)

    return sum(ans1_set), sum(ans2_set)


if __name__ == "__main__":
    print(solve(parse("inputs/day02.txt")))
