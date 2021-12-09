from pathlib import Path
from collections import defaultdict
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


def parse_input():
    input_file = Path(__file__).parent / "input.txt"
    lines: list[list[Point]] = []
    with input_file.open() as ifile:
        for line in ifile:
            line = line.strip().split()
            start, end = line[0], line[-1]
            tmp = start.split(",")
            start = Point(x=int(tmp[0]), y=int(tmp[1]))
            tmp = end.split(",")
            end = Point(x=int(tmp[0]), y=int(tmp[1]))
            lines.append([start, end])
    return lines


def part1(lines: list[list[Point]]) -> int:
    coords: dict[tuple[int, int], int] = defaultdict(int)
    counter: int = 0
    for line in lines:
        generated_coords = []
        start, end = line
        if start.x == end.x:
            if start.y > end.y:
                start, end = end, start
            generated_coords = [Point(start.x, y) for y in range(start.y, end.y + 1)]
        elif start.y == end.y:
            if start.x > end.x:
                start, end = end, start
            generated_coords = [Point(x, start.y) for x in range(start.x, end.x + 1)]
        for coord in generated_coords:
            coords[(coord.x, coord.y)] += 1
            if coords[(coord.x, coord.y)] == 2:
                counter += 1
    return counter


def distance(a: Point, b: Point) -> int:
    return abs(a.x - b.x)


def part2(lines: list[list[Point]]):
    coords: dict[tuple[int, int], int] = defaultdict(int)
    counter: int = 0
    for line in lines:
        generated_coords = []
        start, end = line
        if start.x == end.x:
            if start.y > end.y:
                start, end = end, start
            generated_coords = [Point(start.x, y) for y in range(start.y, end.y + 1)]
        elif start.y == end.y:
            if start.x > end.x:
                start, end = end, start
            generated_coords = [Point(x, start.y) for x in range(start.x, end.x + 1)]
        elif start.x == start.y and end.x == end.y:
            if start.x > end.x:
                start, end = end, start
            generated_coords = [Point(x, y) for x, y in enumerate(range(start.x, end.x + 1))]
        else:
            dist = distance(start, end)
            if start.x > end.x and start.y < end.y:
                generated_coords = [Point(start.x - i, start.y + i) for i in range(dist + 1)]
            elif start.x < end.x and start.y > end.y:
                generated_coords = [Point(start.x + i, start.y - i) for i in range(dist + 1)]
            elif start.x > end.x and start.y > end.y:
                generated_coords = [Point(start.x - i, start.y - i) for i in range(dist + 1)]
            else:
                generated_coords = [Point(start.x + i, start.y + i) for i in range(dist + 1)]
        for coord in generated_coords:
            coords[(coord.x, coord.y)] += 1
            if coords[(coord.x, coord.y)] == 2:
                counter += 1
    return counter


def main():
    data = parse_input()
    print(f"{part1(data)=}")
    print(f"{part2(data)=}")


if __name__ == "__main__":
    main()
