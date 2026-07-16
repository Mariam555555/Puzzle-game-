# state.py
class State:
    def __init__(self, board, parent=None, move=None):
        self.board = board
        self.parent = parent
        self.move = move
        self.g = 0 if parent is None else parent.g + 1

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(str(self.board))

def find_zero(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j
    return None
