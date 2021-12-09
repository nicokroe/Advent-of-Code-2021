from pathlib import Path


def parse_input() -> tuple[list[int], list[list[list[int]]]]:
    input_file = Path(__file__).parent / "input.txt"
    boards = []
    with input_file.open() as ifile:
        first_line = ifile.readline()
        draws = [int(number) for number in first_line.strip().split(",")]
        next(ifile)
        data = ifile.read().split("\n")
        board = []
        for row in data:
            if len(row) != 0:
                row = [int(number) for number in row.split()]
                board.append(row)
            else:
                boards.append(board)
                board = []
        boards.append(board)
    return draws, boards


def calc_board_sum(board: list[list[int]], winning_number: int) -> int:
    res = sum(sum(number for number in row if number != -1) for row in board)
    return res * winning_number


def part1(draws: list[int], boards: list[list[list[int]]]) -> tuple[int, int]:
    winners: dict[int, tuple[int, int]] = {i: tuple() for i in range(len(boards))}
    for board_index, board in enumerate(boards):
        winners[board_index] = check_bingo(draws, board)
    tmp = float("inf")
    winner_board = 0
    winning_number = 0
    for board, values in winners.items():
        if values[0] < tmp:
            tmp = values[0]
            winner_board = board
            winning_number = values[1]
    last_winning_board = part2(boards, winners)
    return calc_board_sum(boards[winner_board], winning_number), last_winning_board


def check_bingo(draws, board):
    winning_number: int = 0
    winning_index: int = 0
    for draw_index, draw in enumerate(draws):
        for row_index, row in enumerate(board):
            for col_index, number in enumerate(row):
                if number == draw:
                    board[row_index][col_index] = -1
            if sum(row) == -5:
                winning_index = draw_index
                winning_number = draw
                return winning_index, winning_number
        for i in range(5):
            col_sum = sum(board[j][i] for j in range(5))
            if col_sum == -5:
                winning_index = draw_index
                winning_number = draw
                break
    return winning_index, winning_number


def part2(boards: list[list[list[int]]], winners: dict[int, tuple[int, int]]):
    tmp = 0
    last_board = 0
    last_board_number = 0
    for board, values in winners.items():
        if values[0] > tmp:
            tmp = values[0]
            last_board = board
            last_board_number = values[1]
    return calc_board_sum(boards[last_board], last_board_number)


def main():

    draws, boards = parse_input()
    part1res, part2res = part1(draws, boards)
    print(f"{part1res=}\n{part2res=}")


if __name__ == "__main__":
    main()
