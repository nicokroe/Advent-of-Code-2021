from pathlib import Path
from math import ceil


def parse_input():
    input_file = Path(__file__).parent / "input.txt"
    return [int(number) for number in input_file.open().readline().strip().split(",")]


def median(data: list[int]) -> int:
    data.sort()
    length = len(data)
    if not length % 2:
        return data[(length + 1) // 2]
    index_1, index_2 = length // 2, (length + 1) // 2
    return (data[index_1] + data[index_2]) // 2


def part1(data: list[int]):
    mean = median(data)
    return sum(abs(value - mean) for value in data)


def part2(data: list[int]) -> int:
    mean = sum(data) // len(data)
    values = []
    for value in data:
        n = abs(value - mean)
        values.append(((n ** 2) + n) // 2)
    return sum(values)


def main():
    data = parse_input()
    print(f"{part1(data)=}")
    print(f"{part2(data)=}")


if __name__ == "__main__":
    main()
