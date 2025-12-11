from functools import cache


def parse(fn: str) -> dict:
    map = {"out": []}
    for line in open(fn):
        key, *vals = line.split()
        map[key[:-1]] = vals
    return map


def solve(map: dict) -> tuple[float, float]:
    @cache
    def npaths(start: str, end: str) -> int:
        return 1 if end in map[start] else sum(npaths(x, end) for x in map[start])

    ans2a = npaths("svr", "dac") * npaths("dac", "fft") * npaths("fft", "out")
    ans2b = npaths("svr", "fft") * npaths("fft", "dac") * npaths("dac", "out")
    return npaths("you", "out"), ans2a + ans2b


if __name__ == "__main__":
    print(solve(parse("inputs/day11.txt")))
