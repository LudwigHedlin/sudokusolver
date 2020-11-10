import pygame

class button():
    #superclass for event buttons
    def __init__(self,width,height,position):
        self.width=width
        self.height=height
        self.position=position #coordinate of the top left of the button
        self.buttonSurface=pygame.rect(position[0],position[1],self.width,self.height)

    def makeButton(self,screen):
        screen.blit(self.buttonSurface,screen)

            

    def checkPressed(self,x,y):
        if (x>self.position[0] and x<self.position[0]+self.width
            and y>self.position[1] and y<self.position[1]+self.height):
            return True
    