"""
Module which contains the definition of board and board constants
"""
import random
EMPTY = 'empty'
BLACK = 'black'
WHITE = 'white'
# Simple constant weightage
# TODO: Apply better weights
WEIGHTS = [[1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 1]]

def other(color):
    """
    Returns opposite color of color
    Useful for flipping
    """
    if color == WHITE:
        return BLACK
    else:
        return WHITE


class Move():
    """
    Class representating a move:
    One token placed
    And the rest flipped
    """
    def __init__(self):
        self.placed = (-1, -1)
        self.flipped = []

    def set_placed(self, mov):
        """
        Sets placed to this move
        """
        self.placed = mov

    def add_to_flipped(self, list_moves):
        """
        Adds this list to the list of flipped tokens
        """
        self.flipped.extend(list_moves)

    def get_placed(self):
        """
        Get placed
        """
        return self.placed

    def get_flipped(self):
        """
        get flipped
        """
        return self.flipped

    def __str__(self):
        return str(self.placed) + "\t" + str(self.flipped)

    def __repr__(self):
        return str(self.placed) + "\t" + str(self.flipped)

class board():
    """
    Class representating the reversi board in memory
    """
    def __init__(self):
        # Create 2d board
        self.b = [[EMPTY for row in range(8)] for col in range(8)]
        self.b[3][3] = WHITE
        self.b[4][4] = WHITE
        self.b[3][4] = BLACK
        self.b[4][3] = BLACK
        self.turn = BLACK
        self.legal_moves = []
        self.calc_legal_moves()
        self.winner = None
        self.moves = []

    def is_legal_move(self, mov):
        """
        Checks if a move is legal
        """
        return mov in self.legal_moves

    def change_turn(self):
        """
        Switches current player
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
        Calculates legal moves by checking every position
        """
        self.legal_moves = []
        for i in range(8):
            for j in range(8):
                if self.b[i][j] == self.turn:
                    self.check_pos(i, j)

    def check_pos(self, row, col):
        """
        Checks whether current pos is at the end of any line
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

    # def shift_color(self, list_moves):
        # """
        # Flips token at a certain positions to current color
        # """
        # for pos in list_moves:
            # self.b[pos[0]][pos[1]] = self.turn
    def shift_color(self, list_moves):
        """
        Flips token at a certain positions to current color
        """
        self.flip_tokens(list_moves)

    def make_move(self, row, col):
        """
        Makes move at a certain position
        """
        current_move = Move()
        current_move.set_placed((row, col))
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
                current_move.add_to_flipped(count)
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
                current_move.add_to_flipped(count)
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
                current_move.add_to_flipped(count)
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
                current_move.add_to_flipped(count)
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
                current_move.add_to_flipped(count)
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
                current_move.add_to_flipped(count)
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
                current_move.add_to_flipped(count)
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
                current_move.add_to_flipped(count)
                break
            else:
                count.append((current_row, current_col))
            current_row += 1
            current_col += 1
        self.moves.append(current_move)

    def flip_tokens(self, list_moves):
        """
        Flips token at a certain positions to current color
        """
        for pos in list_moves:
            self.b[pos[0]][pos[1]] = other(self.b[pos[0]][pos[1]])

    def undo_move(self):
        """
        Undo last move
        """
        mov = self.moves.pop()
        self.b[mov.placed[0]][mov.placed[1]] = EMPTY
        self.flip_tokens(mov.flipped)

    def evaluate_board(self):
        """
        Evaluates the board taking into account the weights
        """
        score = 0
        for i in range(8):
            for j in range(8):
                if self.b[i][j] == BLACK:
                    score += WEIGHTS[i][j]
                else:
                    score -= WEIGHTS[i][j]
        return score

    def _get_random_move(self):
        """
        Returns a random move from the list of available moves
        """
        return random.choice(self.legal_moves)

    def computer_move(self):
        """
        Makes a move
        """
        # (row, col) = self._get_random_move()
        (row, col) = self._get_best_move(0, 3)
        self.make_move(row, col)

    def _get_best_move(self, depth, max_depth):
        """
        Fetches best move
        """
        if self.is_game_over() or depth == max_depth:
            return self.evaluate_board()
        bmov = None
        # As low as possible
        score = -1000
        for move in self.legal_moves:
            self.make_move(move[0], move[1])
            self.change_turn()
            self.calc_legal_moves()
            sco = self._get_best_move(depth + 1, max_depth)
            sco = -sco
            if sco > score:
                score = sco
                bmov = move
            self.undo_move()
            self.change_turn()
            self.calc_legal_moves()
        if depth == 0:
            return bmov
        else:
            return score

