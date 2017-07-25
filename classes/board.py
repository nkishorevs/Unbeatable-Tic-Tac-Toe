BOARD_SIZE = 3
PLAYER_MOVE = 1
AI_MOVE = 2
TIE = 3
BLANK_MOVE = 0

class Board:

    def __init__(self):
        self.board = [[ BLANK_MOVE for i in range(BOARD_SIZE)] for j in range(BOARD_SIZE)]

    def setMove(self, x, y, player = PLAYER_MOVE):
        self.board[x][y] = player

    def checkWin(self):
        winner = 0
        for row in range(BOARD_SIZE):
            winner = self.board[row][0]
            for each in range(1,BOARD_SIZE):
                winner = winner & self.board[row][each]
            if winner:
                return winner

        for col in range(BOARD_SIZE):
            winner = self.board[0][col]
            for each in range(1,BOARD_SIZE):
                winner = winner & self.board[each][col]
            if winner:
                return winner

        winner = self.board[0][0]
        for i in range(1,BOARD_SIZE):
            winner = winner&self.board[i][i]
        if winner:
            return winner

        winner = self.board[0][BOARD_SIZE-1]
        for i,j in zip(range(BOARD_SIZE-1,-1,-1), range(0,BOARD_SIZE)):
            winner = winner&self.board[i][j]
        if winner:
            return winner

        isTie = True
        for row in self.board:
            for move in row:
                if move == BLANK_MOVE:
                    isTie = False
                    break
        if isTie:
            return TIE
        else:
            return -1
