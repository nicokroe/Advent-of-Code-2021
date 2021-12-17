from pathlib import Path


def parse_input():
    input_file = Path(__file__).parent / "input.txt"
    return [line.strip() for line in input_file.open()]


def part1(source: list[str]) -> tuple[int, int]:
    corrupted_counter: dict[str, int] = {")": 0, "]": 0, "}": 0, ">": 0}
    corrupted_points: list[int] = [3, 57, 1197, 25137]
    part2_scores: list[int] = []
    for line in source:
        stack: list[str] = []
        for token in line:
            match token:
                case ("(" | "[" | "{" | "<"):
                    stack.append(token)
                case ")":
                    prev_token = stack.pop()
                    if not (ord(token) - 1 == ord(prev_token)):
                        corrupted_counter[token] += 1
                        stack.clear()
                        break
                case _:
                    prev_token = stack.pop()
                    if not (ord(token) - 2 == ord(prev_token)):
                        corrupted_counter[token] += 1
                        stack.clear()
                        break
        if len(stack):
            res = part2(stack)
            part2_scores.append(res)
    part2_scores.sort()    
    part1res = sum(amount * point for amount, point in zip(corrupted_counter.values(), corrupted_points))
    return part1res, part2_scores[int(len(part2_scores) / 2)]

def part2(stack) -> int:
    points: dict[str, int] = {")": 1, "]": 2, "}": 3, ">": 4}
    closing_tokens: list[str] = []
    score: int = 0
    while len(stack):
        token = stack.pop()
        match token:
            case "(":
                closing_token = chr(ord(token) + 1)
                closing_tokens.append(closing_token)
            case _:
                closing_token = chr(ord(token) + 2)
                closing_tokens.append(closing_token)
    for closing_token in closing_tokens:
        score *= 5
        score += points[closing_token]
    return score


def main():
    data = parse_input()
    part1res, part2res = part1(data)
    print(f"{part1res=}\n{part2res=}")


if __name__ == "__main__":
    main()
