EMPTY = 'empty'
BLACK = 'black'
WHITE = 'white'
class board():

    def __init__(self):
        self.b = [[EMPTY for x in range(8)] for y in range(8)]  # Create 2d board
        self.b[3][3] = WHITE
        self.b[4][4] = WHITE
        self.b[3][4] = BLACK
        self.b[4][3] = BLACK
        self.turn = BLACK
        self.legal_moves = []
        self.calc_legal_moves()

    def display_board(self):
        for i in range(8):
            for j in range(8):
                if(self.b[i][j] == EMPTY):
                    print('.',end = ' ')
                elif(self.b[i][j] == BLACK):
                    print('X',end = ' ')
                elif(self.b[i][j] == WHITE):
                    print('O',end = ' ')
            print('')

    def is_legal_move(self,mov):
        (x, y) = mov
        if mov in self.legal_moves:
            return True
        else:
            return False

    def change_turn(self):
        if self.turn == BLACK:
            self.turn = WHITE
        else :
            self.turn = BLACK

    def is_game_over(self):
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
        a = sum(l.count(BLACK) for l in self.b)
        b = sum(l.count(WHITE) for l in self.b)
        if a > b:
            print('Black Wins!!')
        else:
            print('White Wins!!')

    def calc_legal_moves(self):
        self.legal_moves = []
        for i in range(8):
            for j in range(8):
                if self.b[i][j] == self.turn:
                    self.check_pos(i,j)

    def check_pos(self, row, col):

        # Horizontal right check
        x = row
        y = col + 1
        count = 0
        while y < 8 and y > -1 and x > -1 and x < 8:
            if self.b[x][y] == EMPTY and count != 0:
                self.legal_moves.append((x, y))
                break
            if self.b[x][y] == EMPTY:
                break;
            if self.b[x][y] == self.turn:
                break
            else :
                count += 1
            y += 1
        # Horizontal left check
        x = row
        y = col - 1
        count = 0
        while y < 8 and y > -1 and x > -1 and x < 8:
            if self.b[x][y] == EMPTY and count != 0:
                self.legal_moves.append((x, y))
                break
            if self.b[x][y] == EMPTY:
                break;
            if self.b[x][y] == self.turn:
                break
            else :
                count += 1
            y -= 1
        # Vertical down check
        x = row + 1
        y = col
        count = 0
        while y < 8 and y > -1 and x > -1 and x < 8:
            if self.b[x][y] == EMPTY and count != 0:
                self.legal_moves.append((x, y))
                break
            if self.b[x][y] == EMPTY:
                break;
            if self.b[x][y] == self.turn:
                break
            else :
                count += 1
            x += 1
        # Vertical up check
        x = row - 1
        y = col
        count = 0
        while y < 8 and y > -1 and x > -1 and x < 8:
            if self.b[x][y] == EMPTY and count != 0:
                self.legal_moves.append((x, y))
                break
            if self.b[x][y] == EMPTY:
                break;
            if self.b[x][y] == self.turn:
                break
            else :
                count += 1
            x -= 1
        # Diagonal NW check
        x = row - 1
        y = col - 1
        count = 0
        while y < 8 and y > -1 and x > -1 and x < 8:
            if self.b[x][y] == EMPTY and count != 0:
                self.legal_moves.append((x, y))
                break
            if self.b[x][y] == EMPTY:
                break;
            if self.b[x][y] == self.turn:
                break
            else :
                count += 1
            x -= 1
            y -= 1
        # Diagonal NE check
        x = row - 1
        y = col + 1
        count = 0
        while y < 8 and y > -1 and x > -1 and x < 8:
            if self.b[x][y] == EMPTY and count != 0:
                self.legal_moves.append((x, y))
                break
            if self.b[x][y] == EMPTY:
                break;
            if self.b[x][y] == self.turn:
                break
            else :
                count += 1
            x -= 1
            y += 1

        # Diagonal SW check
        x = row + 1
        y = col - 1
        count = 0
        while y < 8 and y > -1 and x > -1 and x < 8:
            if self.b[x][y] == EMPTY and count != 0:
                self.legal_moves.append((x, y))
                break
            if self.b[x][y] == EMPTY:
                break;
            if self.b[x][y] == self.turn:
                break
            else :
                count += 1
            x += 1
            y -= 1

        # Diagonal SE check
        x = row + 1
        y = col + 1
        count = 0
        while y < 8 and y > -1 and x > -1 and x < 8:
            if self.b[x][y] == EMPTY and count != 0:
                self.legal_moves.append((x, y))
                break
            if self.b[x][y] == EMPTY:
                break;
            if self.b[x][y] == self.turn:
                break
            else :
                count += 1
            x += 1
            y += 1

    def shift_color(self, l):
        for pos in l:
            self.b[pos[0]][pos[1]] = self.turn

    def make_move(self, row, col):
        self.b[row][col] = self.turn

        # Horizontal right check
        x = row
        y = col + 1
        count = []
        while y < 8 and y > -1 and x > -1 and x < 8:
            if self.b[x][y] == EMPTY:
                break;
            if self.b[x][y] == self.turn:
                self.shift_color(count)
                break
            else :
                count.append((x, y))
            y += 1
        # Horizontal left check
        x = row
        y = col - 1
        count = []
        while y < 8 and y > -1 and x > -1 and x < 8:
            if self.b[x][y] == EMPTY:
                break;
            if self.b[x][y] == self.turn:
                self.shift_color(count)
                break
            else :
                count.append((x, y))
            y -= 1
        # Vertical down check
        x = row + 1
        y = col
        count = []
        while y < 8 and y > -1 and x > -1 and x < 8:
            if self.b[x][y] == EMPTY:
                break;
            if self.b[x][y] == self.turn:
                self.shift_color(count)
                break
            else :
                count.append((x, y))
            x += 1
        # Vertical up check
        x = row - 1
        y = col
        count = []
        while y < 8 and y > -1 and x > -1 and x < 8:
            if self.b[x][y] == EMPTY:
                break;
            if self.b[x][y] == self.turn:
                self.shift_color(count)
                break
            else :
                count.append((x, y))
            x -= 1
        # Diagonal NW check
        x = row - 1
        y = col - 1
        count = []
        while y < 8 and y > -1 and x > -1 and x < 8:
            if self.b[x][y] == EMPTY:
                break;
            if self.b[x][y] == self.turn:
                self.shift_color(count)
                break
            else :
                count.append((x, y))
            x -= 1
            y -= 1
        # Diagonal NE check
        x = row - 1
        y = col + 1
        count = []
        while y < 8 and y > -1 and x > -1 and x < 8:
            if self.b[x][y] == EMPTY:
                break;
            if self.b[x][y] == self.turn:
                self.shift_color(count)
                break
            else :
                count.append((x, y))
            x -= 1
            y += 1

        # Diagonal SW check
        x = row + 1
        y = col - 1
        count = []
        while y < 8 and y > -1 and x > -1 and x < 8:
            if self.b[x][y] == EMPTY:
                break;
            if self.b[x][y] == self.turn:
                self.shift_color(count)
                break
            else :
                count.append((x, y))
            x += 1
            y -= 1

        # Diagonal SE check
        x = row + 1
        y = col + 1
        count = []
        while y < 8 and y > -1 and x > -1 and x < 8:
            if self.b[x][y] == EMPTY:
                break;
            if self.b[x][y] == self.turn:
                self.shift_color(count)
                break
            else :
                count.append((x, y))
            x += 1
            y += 1



