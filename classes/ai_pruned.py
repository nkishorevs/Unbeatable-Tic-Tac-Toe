from classes import board

INF = 9999

class Move:
    def __init__(self, score=-1):
        self.x= -1
        self.y = -1
        self.score = score


class AI_Player:

    def getBestMove(self, curr_board, player, alpha = -INF, beta = INF):
        #alpha -> the best score so far along the path to root for the maximizer node(i.e., the AI player)
        #beta -> the best score so far along the path to root for minimizer node.
        # v -> score at current node
        winner = curr_board.checkWin()
        
        if winner == board.AI_MOVE:
            return Move(10)
        elif winner == board.PLAYER_MOVE:
            return Move(-10)
        elif winner == board.NO_VAL:
            return Move(0)

        #moves will store the list of possible moves and their score
        moves = list()
        v = int()
        
        for i in range(board.BOARD_SIZE):
            for j in range(board.BOARD_SIZE):
                #find a possible move,i.e., a blank place
                if curr_board.board[i][j] == board.BLANK_MOVE:
                    curr_board.setMove(i,j,player)
                    move = Move()
                    move.x = i
                    move.y = j
                    if player == board.AI_MOVE:
                        #initialise v to worst case for maximiser
                        v = -INF
                        move.score = self.getBestMove(curr_board, board.AI_MOVE, alpha, beta).score
                        if v<move.score:
                            v = move.score
                        if alpha < v:
                            alpha = v
                    else:
                        #initialise v to worst case for minimiser
                        v = INF
                        move.score = self.getBestMove(curr_board, board.AI_MOVE, alpha, beta).score
                        if v > move.score:
                            v  = move.score
                        if beta > v:
                            beta = v

                    #add move to the moves list
                    moves.append(move)
                    curr_board.setMove(i,j,board.BLANK_MOVE)    #bactrack the move
                    
                    #check the condition for pruning
                    if (player == board.AI_MOVE and v>beta) or (player == board.AI_MOVE and v <alpha):
                        #print("Pruned at ",i, j)
                        break;
            if (player == board.AI_MOVE and v>beta) or (player == board.AI_MOVE and v <alpha):
                break;


        #find the best move from moves list
        bestMove = Move()
        if player == board.AI_MOVE:
            for i in range(len(moves)):
                if moves[i].score > bestMove.score:
                    bestMove = moves[i]
        else:
            bestScore = INF
            for i in range(len(moves)):
                if moves[i].score < bestMove.score:
                    bestMove = moves[i]
        
        #return the best move if any move found, if pruned before that return v as the score
        return bestMove if bestMove.score!=-1 else Move(v)
