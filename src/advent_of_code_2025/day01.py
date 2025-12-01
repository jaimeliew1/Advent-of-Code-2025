def parse(fn: str) -> list[str]:
    return open(fn).read().splitlines()


def solve(rotations: list[str]) -> tuple[int, int]:
    angle, pass1, pass2 = 50, 0, 0
    for rot in rotations:
        match rot[0], int(rot[1:]):
            case "R", x:
                angle_new = angle + x
                pass2 += angle_new // 100
            case "L", x:
                angle_new = angle - x
                pass2 += abs(angle_new // 100) + int(angle_new % 100 == 0) - int(angle == 0)
        angle = angle_new % 100
        pass1 += angle == 0

    return pass1, pass2


if __name__ == "__main__":
    print(solve(parse("inputs/day01.txt")))