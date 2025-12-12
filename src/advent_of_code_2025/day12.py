def solve(fn: str) -> int:
    ans = 0
    for _space in open(fn).read().split("\n\n")[-1].splitlines():
        prod, *counts = _space.split()
        ans += (int(prod[:2]) // 3) * (int(prod[3:5]) // 3) >= sum(map(int, counts))
    return ans


if __name__ == "__main__":
    print(solve("inputs/day12.txt"))
