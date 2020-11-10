import pygame
import math

import buttons as bt

class sudokusolver:
    def __init__(self, board=[
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]):
        self.board = board

        self.solveButton = bt.button(100,100,(400,400))
        
        


    def getEmpty(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return (i, j)

    def getCandidates(self,emptyPosition):
        candidate = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        #get blocked numbers in row
        for i in range(8):
            candidate.discard(
                self.board[(emptyPosition[0]+1 + i) % 9][emptyPosition[1]])
        #get blocked numbers in column
        for i in range(8):
            candidate.discard(self.board[emptyPosition[0]]
                              [(emptyPosition[1]+1 + i) % 9])
        #get blocked numbers in 3x3
        for i in range(3):
            for j in range(3):
                candidate.discard(self.board[emptyPosition[0]+i-emptyPosition[0] %
                                        3][emptyPosition[1]+j-emptyPosition[1] % 3])

        return candidate

    def solver(self):
            #board should be 9x9 list of numbers between 0-9
        index = self.getEmpty()
        if index == True:
            return True
        possibilities = self.getCandidates(index)
        if len(possibilities) == 0:
            return False
        for i in possibilities:
            self.board[index[0]][index[1]] = i
            if self.solver():
                return True
            else:
                self.board[index[0]][index[1]] = 0

        return False

class displaySudoku:
    def __init__(self): 
        pygame.init()
        self.sudoku=sudokusolver()

        self.screen = pygame.display.set_mode((800, 640))
        pygame.display.set_caption("Sudoku Solver")

    def __del__(self):
        pygame.quit()

    def numberSurface(self,posX,posY,number,font='bold',size=50,color=(0,0,0)):
        font=pygame.font.SysFont(font,size)

        surface=font.render(number,1,color)
        self.screen.blit(surface,(posX,posY))

    def drawBoard(self,size,offset):
        self.screen.fill((255, 255, 255))
        pygame.draw.line(self.screen, (0, 0, 0),
                     (-1/4*size+offset, (-1/4)*size+offset), ((9-1/4)*size+offset, (-1/4)*size+offset))
        pygame.draw.line(self.screen, (0, 0, 0),
                     (-1/4*size+offset, (-1/4)*size+offset), ((-1/4)*size+offset, (9-1/4)*size+offset))

        for i in range(9):
            if((i+1) % 3 == 0):
                pygame.draw.line(self.screen, (0, 0, 0),
                             ((i+3/4)*size+offset, -1/4*size+offset), ((i+3/4)*size+offset, (9-1/4)*size+offset))

                pygame.draw.line(self.screen, (0, 0, 0),
                             (-1/4*size+offset, (i+3/4)*size+offset), ((9-1/4)*size+offset, (i+3/4)*size+offset))
            else:
                pygame.draw.line(self.screen, (200, 200, 200),
                             ((i+3/4)*size+offset, -1/4*size+offset), ((i+3/4)*size+offset, (9-1/4)*size+offset))

                pygame.draw.line(self.screen, (200, 200, 200),
                             (-1/4*size+offset, (i+3/4)*size+offset), ((9-1/4)*size+offset, (i+3/4)*size+offset))

            for j in range(9):
                if(self.sudoku.board[i][j] != 0):
                    self.numberSurface(
                        i*size+offset, j*size+offset, '{}'.format(self.sudoku.board[i][j]))

    def ask(self,positionX,positionY):
        asking=True
        number=0
        print(0)
        while(asking):
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_0:
                        asking=False
                    elif event.key==pygame.K_1:
                        number=1
                        print(number)
                        asking=False
                    elif event.key == pygame.K_2:
                        number = 2
                        asking = False
                    elif event.key == pygame.K_2:
                        number = 2
                        asking = False
                    elif event.key == pygame.K_3:
                        number = 3
                        asking = False
                    elif event.key == pygame.K_4:
                        number = 4
                        asking = False
                    elif event.key == pygame.K_5:
                        number = 5
                        asking = False
                    elif event.key == pygame.K_6:
                        number = 6
                        asking = False
                    elif event.key == pygame.K_7:
                        number = 7
                        asking = False
                    elif event.key == pygame.K_8:
                        number = 8
                        asking = False
                    elif event.key == pygame.K_9:
                        number = 9
                        asking = False
                    elif event.key == pygame.K_ESCAPE:
                        asking=False
                
                if event.type==pygame.MOUSEBUTTONDOWN:
                    asking=False

                
        print(number)
        return number

    def display(self):

        
        pygame.display.update()

        
def main():
    size=50
    offset=50

    running=True
    sudoku=displaySudoku()
    
    sudoku.drawBoard(size,offset)
    
    sudoku.display()

    while(running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                
                position=pygame.mouse.get_pos()
                x = math.floor((position[0]-offset)/size)
                y = math.floor((position[1]-offset)/size)
                if(x<9 and y<9):
                    #sudoku.sudoku.board[math.floor((position[0]-offset)/size)][math.floor((position[1]-offset)/size)]=input('enter a number')
                    print(1)
                    sudoku.sudoku.board[x][y]=sudoku.ask(x,y)
                    
                
                    sudoku.drawBoard(size, offset)
                    sudoku.display()
                    
        

        
        
    del sudoku

main()









