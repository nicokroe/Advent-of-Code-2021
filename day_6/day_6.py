from pathlib import Path
from collections import defaultdict


def parse_input():
    input_file = Path(__file__).parent / "input.txt"
    return [int(number) for number in input_file.open().read().strip().split(",")]


def part1(data: list[int], days: int = 80):
    population: list[int] = [0] * 9
    for fish in data:
        population[fish] += 1
    for _ in range(days):
        tmp_population: list[int] = [0] * 9
        for day, amount in enumerate(population):
            match day:
                case 0:
                    tmp_population[8] += amount
                    tmp_population[6] += amount
                case _:
                    tmp_population[day-1] += amount
        population = tmp_population
    return sum(population)
    
    


def part2(data: list[int]):
    return part1(data, 256)


def main():
    data = parse_input()
    print(f"{part1(data)=}")
    print(f"{part2(data)=}")


if __name__ == "__main__":
    main()
