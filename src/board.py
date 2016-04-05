"""
Module which contains the definition of board and board constants
"""
EMPTY = 'empty'
BLACK = 'black'
WHITE = 'white'
class board():
    """
    Class representating the reversi board in memorcurrent_col
    """
    def __init__(self):
        self.b = [[EMPTY for current_row in range(8)] for current_col in range(8)]  # Create 2d board
        self.b[3][3] = WHITE
        self.b[4][4] = WHITE
        self.b[3][4] = BLACK
        self.b[4][3] = BLACK
        self.turn = BLACK
        self.legal_moves = []
        self.calc_legal_moves()
        self.winner = None

    def is_legal_move(self, mov):
        """
        Checks if a move is legal
        """
        if mov in self.legal_moves:
            return True
        else:
            return False

    def change_turn(self):
        """
        Switches current placurrent_coler
        """
        if self.turn == BLACK:
            self.turn = WHITE
        else:
            self.turn = BLACK

    def is_game_over(self):
        """
        Checks if game is over
        """
        if len(self.legal_moves) == 0:
            self.who_wins()
            return True
        for i in range(8):
            for j in range(8):
                if self.b[i][j] == EMPTY:
                    return False
        self.who_wins()
        return True

    def who_wins(self):
        """
        Checks who is the winner as per count of tokens
        """
        count_black = sum(l.count(BLACK) for l in self.b)
        count_white = sum(l.count(WHITE) for l in self.b)
        if count_black > count_white:
            self.winner = BLACK
        else:
            self.winner = WHITE

    def calc_legal_moves(self):
        """
        Calculates legal moves bcurrent_col checking evercurrent_col position
        """
        self.legal_moves = []
        for i in range(8):
            for j in range(8):
                if self.b[i][j] == self.turn:
                    self.check_pos(i, j)

    def check_pos(self, row, col):
        """
        Checks whether current pos is at the end of ancurrent_col line
        """

        # Horizontal right check
        current_row = row
        current_col = col + 1
        count = 0
        while current_col < 8 and current_col > -1 and current_row > -1 and current_row < 8:
            if self.b[current_row][current_col] == EMPTY and count != 0:
                self.legal_moves.append((current_row, current_col))
                break
            if self.b[current_row][current_col] == EMPTY:
                break
            if self.b[current_row][current_col] == self.turn:
                break
            else:
                count += 1
            current_col += 1
        # Horizontal left check
        current_row = row
        current_col = col - 1
        count = 0
        while current_col < 8 and current_col > -1 and current_row > -1 and current_row < 8:
            if self.b[current_row][current_col] == EMPTY and count != 0:
                self.legal_moves.append((current_row, current_col))
                break
            if self.b[current_row][current_col] == EMPTY:
                break
            if self.b[current_row][current_col] == self.turn:
                break
            else:
                count += 1
            current_col -= 1
        # Vertical down check
        current_row = row + 1
        current_col = col
        count = 0
        while current_col < 8 and current_col > -1 and current_row > -1 and current_row < 8:
            if self.b[current_row][current_col] == EMPTY and count != 0:
                self.legal_moves.append((current_row, current_col))
                break
            if self.b[current_row][current_col] == EMPTY:
                break
            if self.b[current_row][current_col] == self.turn:
                break
            else:
                count += 1
            current_row += 1
        # Vertical up check
        current_row = row - 1
        current_col = col
        count = 0
        while current_col < 8 and current_col > -1 and current_row > -1 and current_row < 8:
            if self.b[current_row][current_col] == EMPTY and count != 0:
                self.legal_moves.append((current_row, current_col))
                break
            if self.b[current_row][current_col] == EMPTY:
                break
            if self.b[current_row][current_col] == self.turn:
                break
            else:
                count += 1
            current_row -= 1
        # Diagonal NW check
        current_row = row - 1
        current_col = col - 1
        count = 0
        while current_col < 8 and current_col > -1 and current_row > -1 and current_row < 8:
            if self.b[current_row][current_col] == EMPTY and count != 0:
                self.legal_moves.append((current_row, current_col))
                break
            if self.b[current_row][current_col] == EMPTY:
                break
            if self.b[current_row][current_col] == self.turn:
                break
            else:
                count += 1
            current_row -= 1
            current_col -= 1
        # Diagonal NE check
        current_row = row - 1
        current_col = col + 1
        count = 0
        while current_col < 8 and current_col > -1 and current_row > -1 and current_row < 8:
            if self.b[current_row][current_col] == EMPTY and count != 0:
                self.legal_moves.append((current_row, current_col))
                break
            if self.b[current_row][current_col] == EMPTY:
                break
            if self.b[current_row][current_col] == self.turn:
                break
            else:
                count += 1
            current_row -= 1
            current_col += 1

        # Diagonal SW check
        current_row = row + 1
        current_col = col - 1
        count = 0
        while current_col < 8 and current_col > -1 and current_row > -1 and current_row < 8:
            if self.b[current_row][current_col] == EMPTY and count != 0:
                self.legal_moves.append((current_row, current_col))
                break
            if self.b[current_row][current_col] == EMPTY:
                break
            if self.b[current_row][current_col] == self.turn:
                break
            else:
                count += 1
            current_row += 1
            current_col -= 1

        # Diagonal SE check
        current_row = row + 1
        current_col = col + 1
        count = 0
        while current_col < 8 and current_col > -1 and current_row > -1 and current_row < 8:
            if self.b[current_row][current_col] == EMPTY and count != 0:
                self.legal_moves.append((current_row, current_col))
                break
            if self.b[current_row][current_col] == EMPTY:
                break
            if self.b[current_row][current_col] == self.turn:
                break
            else:
                count += 1
            current_row += 1
            current_col += 1

    def shift_color(self, l):
        """
        Flips token at a certain position
        """
        for pos in l:
            self.b[pos[0]][pos[1]] = self.turn

    def make_move(self, row, col):
        """
        Makes move at a certain position
        """
        self.b[row][col] = self.turn

        # Horizontal right check
        current_row = row
        current_col = col + 1
        count = []
        while current_col < 8 and current_col > -1 and current_row > -1 and current_row < 8:
            if self.b[current_row][current_col] == EMPTY:
                break
            if self.b[current_row][current_col] == self.turn:
                self.shift_color(count)
                break
            else:
                count.append((current_row, current_col))
            current_col += 1
        # Horizontal left check
        current_row = row
        current_col = col - 1
        count = []
        while current_col < 8 and current_col > -1 and current_row > -1 and current_row < 8:
            if self.b[current_row][current_col] == EMPTY:
                break
            if self.b[current_row][current_col] == self.turn:
                self.shift_color(count)
                break
            else:
                count.append((current_row, current_col))
            current_col -= 1
        # Vertical down check
        current_row = row + 1
        current_col = col
        count = []
        while current_col < 8 and current_col > -1 and current_row > -1 and current_row < 8:
            if self.b[current_row][current_col] == EMPTY:
                break
            if self.b[current_row][current_col] == self.turn:
                self.shift_color(count)
                break
            else:
                count.append((current_row, current_col))
            current_row += 1
        # Vertical up check
        current_row = row - 1
        current_col = col
        count = []
        while current_col < 8 and current_col > -1 and current_row > -1 and current_row < 8:
            if self.b[current_row][current_col] == EMPTY:
                break
            if self.b[current_row][current_col] == self.turn:
                self.shift_color(count)
                break
            else:
                count.append((current_row, current_col))
            current_row -= 1
        # Diagonal NW check
        current_row = row - 1
        current_col = col - 1
        count = []
        while current_col < 8 and current_col > -1 and current_row > -1 and current_row < 8:
            if self.b[current_row][current_col] == EMPTY:
                break
            if self.b[current_row][current_col] == self.turn:
                self.shift_color(count)
                break
            else:
                count.append((current_row, current_col))
            current_row -= 1
            current_col -= 1
        # Diagonal NE check
        current_row = row - 1
        current_col = col + 1
        count = []
        while current_col < 8 and current_col > -1 and current_row > -1 and current_row < 8:
            if self.b[current_row][current_col] == EMPTY:
                break
            if self.b[current_row][current_col] == self.turn:
                self.shift_color(count)
                break
            else:
                count.append((current_row, current_col))
            current_row -= 1
            current_col += 1

        # Diagonal SW check
        current_row = row + 1
        current_col = col - 1
        count = []
        while current_col < 8 and current_col > -1 and current_row > -1 and current_row < 8:
            if self.b[current_row][current_col] == EMPTY:
                break
            if self.b[current_row][current_col] == self.turn:
                self.shift_color(count)
                break
            else:
                count.append((current_row, current_col))
            current_row += 1
            current_col -= 1

        # Diagonal SE check
        current_row = row + 1
        current_col = col + 1
        count = []
        while current_col < 8 and current_col > -1 and current_row > -1 and current_row < 8:
            if self.b[current_row][current_col] == EMPTY:
                break
            if self.b[current_row][current_col] == self.turn:
                self.shift_color(count)
                break
            else:
                count.append((current_row, current_col))
            current_row += 1
            current_col += 1

