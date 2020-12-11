import pygame

class button():
    #superclass for event buttons
    def __init__(self, width, height, position):
        self.width=width
        self.height=height
        self.position=position #coordinate of the top left of the button
        self.buttonSurface=pygame.Rect(position[0],position[1],width,height)
        



            

    def checkPressed(self,x,y):
        if (x>self.position[0] and x<self.position[0]+self.width
            and y>self.position[1] and y<self.position[1]+self.height):
            print(True)
            return True

class solveButton(button):
    def __init__(self, position, width=105, height=50, img="solveButton1.png"):
        super().__init__(width, height, position)
        self.img = pygame.image.load(img)

    def makeButton(self,screen):
        screen.blit(self.img, self.position)
    
    
    
