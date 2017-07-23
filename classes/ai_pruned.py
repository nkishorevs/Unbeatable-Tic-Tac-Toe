from classes import board

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

    def getBestMove(self, curr_board, player, alpha = -INF, beta = INF):
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
        v = int()
        #depth+=1
        #check all possible moves and score them
        for i in range(board.BOARD_SIZE):
            for j in range(board.BOARD_SIZE):
                if curr_board.board[i][j] == board.BLANK_MOVE:
                    #print(depth, "in IF",winner, i, j)
                    curr_board.setMove(i,j,player)
                    move = Move()
                    move.x = i
                    move.y = j
                    if player == board.AI_MOVE:
                        v = -INF
                        tempMove = self.getBestMove(curr_board, board.PLAYER_MOVE, alpha,beta)
                        move.score = tempMove.score
                        if v<move.score:
                            v = move.score
                        if alpha < v:
                            alpha = v
                    else:
                        v = INF
                        tempMove = self.getBestMove(curr_board, board.AI_MOVE, alpha, beta)
                        move.score = tempMove.score
                        if v > move.score:
                            v  = move.score
                        if beta > v:
                            beta = v
                    #print("Appending :",move.x, move.y, move.score)
                    moves.append(move)
                    #print("len",len(moves))
                    curr_board.setMove(i,j,board.BLANK_MOVE)
                    if (player == board.AI_MOVE and v>beta) or (player == board.AI_MOVE and v <alpha):
                        #print("Pruned at ",i, j)
                        break;
            if (player == board.AI_MOVE and v>beta) or (player == board.AI_MOVE and v <alpha):
                break;


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
        #print(str(depth)+"th",moveInd, len(moves), winner)
        return moves[moveInd] if moveInd!=-1 else Move(v)
