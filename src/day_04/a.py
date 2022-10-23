# Simple data-classes to keep track of the Bingo board, and whether
# a cell has been marked. Marking a new number, calculating if 
# a board won, and computing the score are done through simple 
# iterations / list comprehensions.
# We simply iterate through the numbers being called out, and
# marking numbers and checking we a board has won. 
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
    t_start = time.perf_counter()
    with open("inputs/04.txt") as f:
        data = list(filter(lambda line: line.strip(), f))

        called_numbers = [int(num) for num in data[0].split(",")]
        boards = [Board(data[i:i+5]) for i in range(1, len(data), 5)]

    for num in called_numbers:
        for board in boards:
            board.mark(num)
            if board.has_won():
                ans = board.score() * num
                print(f"Ans - {ans}, Time - {(time.perf_counter() - t_start) * 1000}ms")
                sys.exit(0)
