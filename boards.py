# A function which prints all possible Tic-tac-toe boards.
# Any cell may be empty, X or O.
# Possible results include
# - an empty board,
# - a board in which all cells are set to O,
# - a board in which all cells are set to X,
# - and all variants in between.


def board():
    full_board = []

    def step(full_board):
        if len(full_board) == 9:
            print("---")
            x = "".join(full_board)
            print(x[0:3])
            print(x[3:6])
            print(x[6:9])
        else:
            for n in [" ", "X", "O"]:
                full_board.append(n)
                step(full_board)
                full_board.pop()

    step(full_board)
    return full_board


board()
