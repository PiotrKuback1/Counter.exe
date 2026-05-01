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

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            Smolfont = pygame.font.SysFont("freesansbold",15,False,False)
            text = Smolfont.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position as tuple of (x,y) coordinates
        mousePressed = pygame.mouse.get_pressed()
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                if mousePressed[0]:
                    return True
        return False

def drawScreen(screen,counterVal):
    screen.fill("orange")
    IncButton.draw(screen, (0,0,0))
    DecButton.draw(screen, (0,0,0))
    ResetButton.draw(screen, (0,0,0))
    font = pygame.font.SysFont("freesansbold", 30, True, False)
    text = font.render(str(counterVal), True, (255,255,255))
    counterRect = text.get_rect(topleft=(100, 30))
    screen.blit(text, counterRect)


def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 212))
    clock = pygame.time.Clock()
    running = True

    #checkinf if file exists
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
    IncButton = button((255,255,255),     70,70,200,140,"Increment")
    DecButton = button((255,255,255),     280,70,110,70,"Decrement")
    ResetButton = button((255,255,255),   280,140,110,70,"Reset")

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
                pygame.event.wait(10)
                if mousePress[0]:
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