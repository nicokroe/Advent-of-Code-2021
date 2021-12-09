from pathlib import Path


def parse_input():
    input_file = Path(__file__).parent / "input.txt"
    all_patterns: list[list[str]] = []
    outputs: list[list[str]] = []
    with input_file.open() as file:
        for line in file:
            patterns, output = line.split("|")
            patterns = patterns.strip().split()
            output = output.strip().split()
            all_patterns.append(patterns)
            outputs.append(output)
    return all_patterns, outputs


def part1(outputs: list[list[str]]) -> int:
    counter: int = 0
    for output in outputs:
        for digit in output:
            length = len(digit)
            if length in {2, 3, 4, 7}:
                counter += 1
    return counter


def find_common_characters(a: str, b: str) -> int:
    return sum(c in b for c in a)

def find_number(display, patterns, one, four, case11, case12, case2):
    for pattern in patterns:
        match find_common_characters(four, pattern):
            case 2:
                display[pattern] = case2
            case 3:
                matches = find_common_characters(one, pattern)
                display[pattern] = case11 if matches == 2 else case12
            case 4:
                display[pattern] = case2

def part2(all_patterns: list[list[str]], outputs: list[list[str]]) -> int:
    results: list[int] = []
    for patterns, output in zip(all_patterns, outputs):
        display: dict[str, str] = {}
        number: str = ""
        patterns.sort(key=len)
        fives: list[str] = patterns[3:6]
        sixes: list[str] = patterns[6:-1]
        display[patterns[0]] = "1"
        display[patterns[1]] = "7"
        display[patterns[2]] = "4"
        display[patterns[-1]] = "8"
        one = patterns[0]
        four = patterns[2]
        find_number(display, fives, one, four, "3", "5", "2")
        find_number(display, sixes, one, four, "0", "6", "9")
        for value in output:
            for k, v in display.items():
                matches = find_common_characters(value, k)
                if matches == len(value) and len(value) == len(k):
                    number += v
        results.append(int(number))
    return sum(results)


def main():
    all_patterns, outputs = parse_input()
    print(f"{part1(outputs)=}")
    print(f"{part2(all_patterns, outputs)=}")


if __name__ == "__main__":
    main()

