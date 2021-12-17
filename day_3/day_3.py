from pathlib import Path
from itertools import filterfalse
from enum import Enum


class Mode(Enum):
    MOST = 1
    LEAST = 0


def parse_input():
    input_file = Path(__file__).parent / "input.txt"
    return [line.strip() for line in input_file.open()]


def part1(data: list[str]) -> int:
    width = len(data[0])
    counter: dict[int, int] = {i: 0 for i in range(width)}
    for number in data:
        for i, c in enumerate(number):
            if c == "1":
                counter[i] += 1
    gamma: int = 0
    data_len = len(data)
    for k, v in counter.items():
        if v > data_len // 2:
            # Bitwise or on gamma with 1 and shift to the left to the
            # right position. Substract 1 since width is not 0-based.
            gamma |= 0x01 << width - k - 1
    epsilon = ~gamma & ((1 << gamma.bit_length()) - 1)
    return gamma * epsilon


def filter_ratings(ratings: list[str], mode: Mode, index: int) -> str:
    # There should be only one rating left
    if len(ratings) == 1:
        return ratings[0]
    # Count "1" to see if there are more "1"s than "0"s
    counter: int = sum(rating[index] == "1" for rating in ratings)
    match mode:
        case mode.MOST:
            # Keep all with "1" in case counter is exactl half of len(ratings)
            filter_char = "1" if counter >= len(ratings) / 2 else "0"
        case mode.LEAST:
            # Keep all with "0" in case counter is exactly half of len(ratings)
            filter_char = "1" if counter < len(ratings) / 2 else "0"
    ratings = [rating for rating in ratings if rating[index] == filter_char]
    return filter_ratings(ratings, mode, index + 1)


def part2(o2: list[str]) -> int:
    # Make a copy for co2
    co2 = o2.copy()
    o2ret = filter_ratings(o2, Mode.MOST, 0)
    co2ret = filter_ratings(co2, Mode.LEAST, 0)
    return int(o2ret, 2) * int(co2ret, 2)


def main():
    data = parse_input()
    print(f"{part1(data)=}")
    print(f"{part2(data)=}")


if __name__ == "__main__":
    main()
