import math


def parse(fn: str):
    lines = open(fn).readlines()
    numbers = [[int(x) for x in line.strip().split()] for line in lines[:-1]]
    ops = lines[-1].split()
    return lines[:-1], list(zip(*numbers)), ops


def solve(lines, numbers, ops) -> tuple[int, int]:
    ans1, ans2 = 0, 0
    for nums, op in zip(numbers, ops):
        ans1 += sum(nums) if op == "+" else math.prod(nums)

    ops_gen = iter(ops)
    op = next(ops_gen)
    temp_ans = 0 if op == "+" else 1
    for nums in list(zip(*lines))[:-1]:
        if all(n == " " for n in nums):
            op, ans2 = next(ops_gen), ans2 + temp_ans
            temp_ans = 0 if op == "+" else 1
        elif op == "+":
            temp_ans += int("".join(nums))
        else:
            temp_ans *= int("".join(nums))

    return ans1, ans2 + temp_ans


if __name__ == "__main__":
    print(solve(*parse("inputs/day06.txt")))