# Very similar to Part A. We keep a list of uncompleted boards, 
# and remove a board from it as soon as it has won until only 
# one remains.
import sys
import time
from dataclasses import dataclass
from typing import List


@dataclass
class Cell:
    num: int
    is_marked: bool


@dataclass
class Board:
    rows: List[Cell]

    def __init__(self, board_str):
        self.rows = [[Cell(int(num), False) for num in row.split()] for row in board_str]

    def mark(self, num):
        self.rows = [[Cell(cell.num, cell.is_marked or cell.num == num) for cell in row] for row in self.rows]

    def has_won(self):
        for row in (self.rows):
            if all(cell.is_marked for cell in row):
                return True

        for col_idx in range(len(self.rows[0])):
            if all(self.rows[row_idx][col_idx].is_marked for row_idx in range(len(self.rows))):
                return True

        return False

    def score(self):
        score = 0
        for row in self.rows:
            for cell in row:
                if not cell.is_marked:
                    score += cell.num

        return score


if __name__ == "__main__":
    t = time.time()
    with open("inputs/04.txt") as f:
        data = list(filter(lambda line: line.strip(), f))

        called_numbers = [int(num) for num in data[0].split(",")]
        boards = [Board(data[i:i+5]) for i in range(1, len(data), 5)]

    for num in called_numbers:
        new_boards = []
        for idx, board in enumerate(boards):
            board.mark(num)
            if board.has_won():
                if len(boards) == 1:
                    ans = board.score() * num
                    print(f"Ans - {ans}, Time - {time.time() - t}s")
                    sys.exit(0)
            else:
                new_boards.append(board)
        boards = new_boards
