from pathlib import Path


def parse_input():
    input_file = Path(__file__).parent / "input.txt"
    return [line.strip() for line in input_file.open()]


def part1(commands: list[str]):
    submarine = {"position": 0, "depth": 0}
    for command in commands:
        match command.split():
            case ["forward", value]:
                submarine["position"] += int(value)
            case ["up", value]:
                submarine["depth"] -= int(value)
            case ["down", value]:
                submarine["depth"] += int(value)
            case _:
                print(command)
    return submarine["depth"]*submarine["position"]

def part2(commands: list[str]):
    submarine = {"position": 0, "depth": 0, "aim": 0}
    for command in commands:
        match command.split():
            case ["forward", value]:
                submarine["position"] += int(value)
                submarine["depth"] += submarine["aim"] * int(value)
            case ["up", value]:
                submarine["aim"] -= int(value)
            case ["down", value]:
                submarine["aim"] += int(value)
            case _:
                print(command)
    return submarine["depth"]*submarine["position"]

def main():
    data = parse_input()
    print(f"{part1(data)=}")
    print(f"{part2(data)=}")


if __name__ == "__main__":
    main()
