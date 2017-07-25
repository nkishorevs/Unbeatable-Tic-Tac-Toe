import pygame
import random
from classes import board
from classes import ai_pruned #change this: 'ai'  -> MiniMax without pruning
                                #       'ai_pruned' -> MiniMax with Alpha-Beta pruning
#constants
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 656
WHITE = (255,255,255)
GREEN = (34,177,76)
BLACK = (0,0,0)
RED = (237, 28, 36)
GREY = (127,127,127)
MSG_BY = "Developed by Nanda Kishore V S"
MSG_PLAYAGAIN = "Press P to Play again"
FPS = 60
BLOCK_SIZE = 200
MAP_TO_PIX = {(0,0):(126,76), (0,1):(308,76), (0,2):(486,76),
              (1,0):(126,258), (1,1):(308,258), (1,2):(486,258),
              (2,0):(126,436), (2,1):(308,436), (2,2):(486,436)}

#pygame initialising
pygame.init()
running = True
XLFont = pygame.font.SysFont("consolas", 46)
MFont = pygame.font.SysFont("consolas", 15)
pygame.display.set_caption("UnBeatable Tic-Tac-Toe!")
clock = pygame.time.Clock()
imgX = pygame.image.load("images/X.png")
imgO = pygame.image.load("images/O.png")
imgGrid = pygame.image.load("images/grid.png")
imgHead = pygame.image.load("images/header.png")
gameDisplay = pygame.display.set_mode([DISPLAY_WIDTH,DISPLAY_HEIGHT])


class Game:
    def __init__(self):
        gameDisplay.fill(WHITE)
        gameDisplay.blit(imgGrid, (126,76))
        gameDisplay.blit(imgHead, (88,10))
        txtBy = MFont.render(MSG_BY, True, BLACK)
        gameDisplay.blit(txtBy,(DISPLAY_WIDTH-txtBy.get_width()-6, DISPLAY_HEIGHT-txtBy.get_height()))
        self.turn = 0
        self.board = board.Board()
        self.bot = ai_pruned.AI_Player() ## change 'ai/ai_pruned' here also to change algo
        pygame.display.update()

    def reset(self):
        gameDisplay.fill(WHITE)
        gameDisplay.blit(imgGrid, (126,76))
        gameDisplay.blit(imgHead, (88,10))
        txtBy = MFont.render(MSG_BY, True, BLACK)
        gameDisplay.blit(txtBy,(DISPLAY_WIDTH-txtBy.get_width()-6, DISPLAY_HEIGHT-txtBy.get_height()))
        self.turn = 0
        self.board = board.Board()
        self.bot = ai_pruned.AI_Player()    ## change 'ai/ai_pruned' here also to change algo
        pygame.display.update()

    def checkPlace(self, x,y):
        return not self.board.board[x][y]

    def setMove(self, x, y, player = board.PLAYER_MOVE):
        self.board.setMove(x,y, player)
        self.turn+=1

    def checkWin(self):
        return self.board.checkWin()

    def play_ai_move(self):
        move = self.bot.getBestMove(self.board, board.AI_MOVE)
        #print(move.x,move.y,move.score)
        self.board.setMove(move.x,move.y, board.AI_MOVE)
        self.drawMove(move)
        self.turn+=1

    def drawMove(self, move):
        gameDisplay.blit(imgO, MAP_TO_PIX[(move.x,move.y)])

    def endGame(self, message):
        txt = XLFont.render(message, True, GREEN)
        txtRect = txt.get_rect()
        txtRect.center = (246 + int(295/2) , 201 + int(244/2))
        txtAgain = MFont.render(MSG_PLAYAGAIN, True, BLACK)
        txtAgainRect = txtAgain.get_rect()
        txtAgainRect.center = (246 + int(295/2) , 221 + int(244/2)+20)
        gameDisplay.fill(GREY, (242,217,302,251))
        gameDisplay.fill(WHITE, (254, 232, 278,222))
        gameDisplay.blit(txt, txtRect)
        gameDisplay.blit(txtAgain, txtAgainRect)
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.reset()
                        return True


if __name__ == '__main__':
    game = Game()

    def eventhandling():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                #print(pos)
                if pos[0]>126 and pos[0]<300 and pos[1]>76 and pos[1]<250 and game.checkPlace(0,0): #0
                    game.setMove(0,0)
                    gameDisplay.blit(imgX, (126,76))
                elif pos[0]>308 and pos[0]<478 and pos[1]>76 and pos[1]<250 and game.checkPlace(0,1): #1
                    game.setMove(0,1)
                    gameDisplay.blit(imgX, (308,76))
                elif pos[0]>486 and pos[0]<660 and pos[1]>76 and pos[1]<250 and game.checkPlace(0,2): #2
                    game.setMove(0,2)
                    gameDisplay.blit(imgX, (486,76))
                elif pos[0]>126 and pos[0]<300 and pos[1]>258 and pos[1]<428 and game.checkPlace(1,0): #3
                    game.setMove(1,0)
                    gameDisplay.blit(imgX, (126,258))
                elif pos[0]>308 and pos[0]<478 and pos[1]>258 and pos[1]<428 and game.checkPlace(1,1): #4
                    game.setMove(1,1)
                    gameDisplay.blit(imgX, (308,258))
                elif pos[0]>486 and pos[0]<660 and pos[1]>258 and pos[1]<428 and game.checkPlace(1,2): #5
                    game.setMove(1,2)
                    gameDisplay.blit(imgX, (486,258))
                elif pos[0]>126 and pos[0]<300 and pos[1]>436 and pos[1]<610 and game.checkPlace(2,0): #6
                    game.setMove(2,0)
                    gameDisplay.blit(imgX, (126,436))
                elif pos[0]>308 and pos[0]<478 and pos[1]>436 and pos[1]<610 and game.checkPlace(2,1): #7
                    game.setMove(2,1)
                    gameDisplay.blit(imgX, (308,436))
                elif pos[0]>486 and pos[0]<660 and pos[1]>436 and pos[1]<610 and game.checkPlace(2,2): #8
                    game.setMove(2,2)
                    gameDisplay.blit(imgX, (486,436))


    while running and game.turn<9:
        clock.tick(FPS)
        if game.turn&1:
            game.play_ai_move()
        else:
            eventhandling()
        winner =  game.checkWin()
        if winner==board.AI_MOVE:
            running = game.endGame("AI Wins!!")
        elif winner == board.PLAYER_MOVE:
            running = game.endGame("You Win!!")
        elif winner == board.TIE:
            running = game.endGame("Its a TIE!")

        pygame.display.update()

    pygame.quit()
    quit()
