from pathlib import Path


def parse_input():
    input_file = Path(__file__).parent / "input.txt"
    return [int(line.strip()) for line in input_file.open()]


def part1(data: list[int]) -> int:
    tmp: int = data[0]
    counter: int = 0
    for depth in data[1:]:
        if depth > tmp:
            counter += 1
        tmp = depth
    return counter


def part2(data: list[int]):
    window_a: int = sum(data[:3])
    counter: int = 0
    for i in range(1, len(data) - 2):
        window_b = sum(data[i : i + 3])
        if window_b > window_a:
            counter += 1
        window_a = window_b
    return counter


def main():
    data = parse_input()
    print(f"{part1(data)=}")
    print(f"{part2(data)=}")


if __name__ == "__main__":
    main()
