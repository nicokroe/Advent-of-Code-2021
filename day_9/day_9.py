from pathlib import Path
from math import prod, sqrt
from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int


def parse_input():
    input_file = Path(__file__).parent / "input.txt"
    return [line.strip() for line in input_file.open()]


def generate_points(point: Point, limits: Point) -> set[Point]:
    points: set[Point] = set()
    if point.x != 0:
        points.add(Point(point.x - 1, point.y))
    if point.x < limits.x:
        points.add(Point(point.x + 1, point.y))
    if point.y != 0:
        points.add(Point(point.x, point.y - 1))
    if point.y < limits.y:
        points.add(Point(point.x, point.y + 1))
    return points


def part1(data: list[str]) -> tuple[int, set[Point], set[Point]]:
    limit_point = Point(len(data[0]) - 1, len(data) - 1)
    result: int = 0
    low_points: set[Point] = set()
    nines: set[Point] = set()
    for i, date in enumerate(data):
        for j, value in enumerate(date):
            curr_point = Point(j, i)
            if value == "9":
                nines.add(curr_point)
                continue
            points = generate_points(curr_point, limit_point)
            value = int(value)
            if all(value < int(data[point.y][point.x]) for point in points):
                result += 1 + value
                low_points.add(curr_point)
    return result, low_points, nines


def part2(data: list[str], low_points: set[Point], nines: set[Point]) -> int:
    grid = [list(line) for line in data]
    limit_point = Point(len(data[0]) - 1, len(data) - 1)
    basins: list[int] = []
    for low_point in low_points:
        counter: int = 0
        queue: list[Point] = [low_point]
        while queue:
            curr_point = queue.pop(0)
            if curr_point not in nines:
                grid[curr_point.y][curr_point.x] = "-1"
                counter += 1
                points = generate_points(curr_point, limit_point)
                queue.extend(
                    [
                        point
                        for point in points
                        if grid[point.y][point.x] != "-1" and point not in queue
                    ]
                )
        basins.append(counter)
    basins.sort()
    return prod(basins[-3:])


def main():
    data = parse_input()
    part1res, low_points, nines = part1(data)
    part2res = part2(data, low_points, nines)
    print(f"{part1res=}")
    print(f"{part2res=}")


if __name__ == "__main__":
    main()
