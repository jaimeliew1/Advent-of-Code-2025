def parse(fn: str) -> list[str]:
    return [x.strip() for x in open(fn).readlines()]


def max_jolt(bank: str, right_offset: int = 0) -> tuple[int, str]:
    i_max, val_max = 0, 0
    clipped = bank[:-right_offset] if right_offset > 0 else bank
    for i, val in enumerate(clipped):
        if int(val) > val_max:
            i_max, val_max = i, int(val)
    return val_max, bank[i_max + 1 :]


def max_jolt_combo(bank: str, n_digits: int) -> int:
    out = 0
    for n in range(n_digits):
        digit, bank = max_jolt(bank, n_digits - n - 1)
        out += digit * (10 ** (n_digits - n - 1))
    return out


def solve(banks: list[str]) -> tuple[int, int]:
    ans1 = sum(max_jolt_combo(b, 2) for b in banks)
    ans2 = sum(max_jolt_combo(b, 12) for b in banks)
    return ans1, ans2


if __name__ == "__main__":
    print(solve(parse("inputs/day03.txt")))
