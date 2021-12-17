from pathlib import Path
from typing import Generator
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


def parse_input() -> list[list[int]]:
    input_file = Path(__file__).parent / "input.txt"
    return [[int(c) for c in line.strip()] for line in input_file.open()]


def add_one(grid: list[list[int]]) -> bool:
    flash = False
    # Rows
    for row in grid:
        # Columns
        for j in range(len(row)):
            row[j] += 1
            if row[j] == 10:
                flash = True
    return flash


# TODO: Complete rewrite
def generate_points(point: Point, limits: Point) -> Generator[Point, None, None]:
    if point.y > 0:
        # Oben
        yield Point(point.x, point.y - 1)
        if point.x < limits.x:
            # Oben Rechts
            yield Point(point.x + 1, point.y - 1)
    if point.x < limits.x:
        # Rechts
        yield Point(point.x + 1, point.y)
    if point.y < limits.y:
        if point.x < limits.x:
            # Unten Rechts
            yield Point(point.x + 1, point.y + 1)
        # Unten
        yield Point(point.x, point.y + 1)
        if point.x > 0:
            # Unten Links
            yield Point(point.x - 1, point.y + 1)
    if point.x > 0:
        # Links
        yield Point(point.x - 1, point.y)
        if point.y > 0:
            # Oben Links
            yield Point(point.x - 1, point.y - 1)


def calculate_flashes(grid: list[list[int]], iteration: int) -> int:
    height = len(grid)
    width = len(grid[0])
    limit = Point(width - 1, height - 1)
    counter: int = 0
    for i in range(height):
        for j in range(width):
            if grid[i][j] >= 10:
                # print(f"{iteration=} x: {j}, y: {i}")
                counter += 1
                for point in generate_points(Point(j, i), limit):
                    # print(f"{point}")
                    if grid[point.y][point.x] != 0:
                        grid[point.y][point.x] += 1
                # print_grid(grid, iteration)
                grid[i][j] = 0
                counter += calculate_flashes(grid, iteration)
    return counter


def print_grid(grid: list[list[int]], iteration: int):
    print(f"Round: {iteration}")
    for row in grid:
        print(row)


def part2(grid: list[list[int]]):
    for row in grid:
        for col in row:
            if col != 0:
                return False
    return True


def part1(grid: list[list[int]], rounds: int) -> int:
    rounds_flashes: list[int] = []
    for i in range(rounds):
        if add_one(grid):
            flashes = calculate_flashes(grid, i)
            rounds_flashes.append(flashes)
            if part2(grid):
                return i + 1
    return sum(rounds_flashes)


def main():
    data = parse_input()
    grid1 = [row.copy() for row in data]
    print(f"Part 1: {part1(grid1, 100)}")
    grid2 = [row.copy() for row in data]
    print(f"Part 2: {part1(data.copy(), 500)}")


if __name__ == "__main__":
    main()
