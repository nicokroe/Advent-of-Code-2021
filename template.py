from pathlib import Path


def parse_input():
    input_file = Path(__file__).parent / "input.txt"
    return [line.strip() for line in input_file.open()]


def part1(data: list[str]):
    pass


def part2(data: list[str]):
    pass


def main():
    data = parse_input()
    print(f"{part1(data)=}")
    print(f"{part2(data)=}")


if __name__ == "__main__":
    main()
