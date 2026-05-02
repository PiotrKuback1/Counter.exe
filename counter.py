import pygame
import os.path

class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def drawButton(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            Smolfont = pygame.font.SysFont("freesansbold",50,False,False)
            text = Smolfont.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position as tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

def drawScreen(screen,counterVal):
    screen.fill("orange")
    IncButton.drawButton(screen, (0,0,0))
    DecButton.drawButton(screen, (0,0,0))
    ResetButton.drawButton(screen, (0,0,0))
    font = pygame.font.SysFont("freesansbold", 30, True, False)
    text = font.render(str(counterVal), True, (255,255,255))
    counterRect = text.get_rect(topleft=(25, 17))
    screen.blit(text, counterRect)


def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 200))
    clock = pygame.time.Clock()
    running = True
    # pygame.event.set_grab(True)    #if uncommented this will lock your mouse in the window use alt f4 to kill

    #checking if file exists
    if os.path.isfile("./save.txt"):
        with open("save.txt", "r") as saveFile:
            #if exists make the counter value the read number
            counterVal = int(saveFile.readline())
            saveFile.close()
    else:
        #else make it 0
        counterVal = 0

    pygame.display.set_caption('Counter.exe')

    pygame.event.set_allowed([pygame.MOUSEBUTTONDOWN])

    #declare all buttons 
    global ResetButton,IncButton, DecButton
    IncButton = button((255,255,255),     0    ,50  ,200  ,150 ,"+")
    DecButton = button((255,255,255),     200  ,50  ,200  ,75  ,"-")
    ResetButton = button((255,255,255),   200  ,125 ,200  ,75  ,"0")

    while running:
        drawScreen(screen,counterVal)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                #saving sequence
                with open("save.txt", "w") as saveFile:
                    saveFile.write(str(counterVal) + "\n")
                    saveFile.close()
            else:
                mousePos = pygame.mouse.get_pos()
                mousePress = pygame.mouse.get_pressed()
                keyPress = (event.type == pygame.KEYDOWN)

                pygame.event.wait(10)
                if mousePress[0] or keyPress:
                    if IncButton.isOver(mousePos):
                        counterVal += 1

                    elif DecButton.isOver(mousePos):
                        counterVal -= 1

                    elif ResetButton.isOver(mousePos):
                        counterVal = 0

        pygame.display.flip()
        clock.tick(60) 
    pygame.quit()

#start
main()