from classes import board
INF = 9999

class Move:
    def __init__(self, score=-1):
        self.x= -1
        self.y = -1
        self.score = score

class AI_Player:

    def getBestMove(self, curr_board, player):
        
        #base case
        winner = curr_board.checkWin()
        if winner == board.AI_MOVE:
            return Move(10)
        elif winner == board.PLAYER_MOVE:
            return Move(-10)
        elif winner == board.TIE:
            return Move(0)

        #moves list will store the list of possible moves and their score
        moves = list()

        #check all possible moves and score them
        for i in range(board.BOARD_SIZE):
            for j in range(board.BOARD_SIZE):
                #find a possible move, ie, a blank place
                if curr_board.board[i][j] == board.BLANK_MOVE:
                    curr_board.setMove(i,j,player)
                    move = Move()
                    move.x = i
                    move.y = j
                    if player == board.AI_MOVE:
                        tempMove = self.getBestMove(curr_board, board.PLAYER_MOVE)
                        move.score = tempMove.score
                    else:
                        tempMove = self.getBestMove(curr_board, board.AI_MOVE)
                        move.score = tempMove.score
                        
                    moves.append(move)
                    curr_board.setMove(i,j,board.BLANK_MOVE)

        #find the best move
        bestMove = Move()
        if player == board.AI_MOVE:
            bestMove.score = -INF
            for i in range(len(moves)):
                if moves[i].score > bestMove.score:
                    bestMove = moves[i]
        else:
            bestMove.score = INF
            for i in range(len(moves)):
                if moves[i].score < bestMove.score:
                    bestMove = moves[i]
        #return best move
        return bestMove
