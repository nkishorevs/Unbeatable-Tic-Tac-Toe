import classes.board
INF = 9999

class Move:
    def __init__(self, score=-1):
        self.x= -1
        self.y = -1
        self.score = score

    def copy(self, move):
        self.x= move.x
        self.y = move.y
        self.score = move.score

class AI_Player:

    def getBestMove(self, curr_board, player):
        #print("function getBestMove: ")
        #base case
        #for move in curr_board.board:
        #    print(move,end="-")
        winner = curr_board.checkWin()
        #print("winner: ", winner)
        if winner == board.AI_MOVE:
            #for move in curr_board.board:
            #    print(move,end="-")
            #print(winner)
            return Move(10)
        elif winner == board.PLAYER_MOVE:
            #for move in curr_board.board:
            #    print(move,end="-")
            #print(winner)
            return Move(-10)
        elif winner == board.NO_VAL:
            #for move in curr_board.board:
            #    print(move,end="-")
            #print(winner)
            return Move(0)

        moves = list()

        #check all possible moves and score them
        for i in range(board.BOARD_SIZE):
            for j in range(board.BOARD_SIZE):
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

                    #print("Appending :",move.x, move.y, move.score)
                    moves.append(move)
                    curr_board.setMove(i,j,board.BLANK_MOVE)

        #find the best move
        moveInd = -1
        if player == board.AI_MOVE:
            bestScore = -INF
            for i in range(len(moves)):
                #print(moves[i].x,moves[i].y, moves[i].score, bestScore,moveInd, end =" : ")
                if moves[i].score > bestScore:
                    moveInd = i
                    bestScore = moves[i].score
        else:
            bestScore = INF
            for i in range(len(moves)):
                if moves[i].score < bestScore:
                    moveInd = i
                    bestScore = moves[i].score
        #print("")
        return moves[moveInd]
