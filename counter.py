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
        #Pos is the mouse position or a tuple of (x,y) coordinates
        mousePressed = pygame.mouse.get_pressed()
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                if mousePressed[0]:
                    return True
        return False

def drawScreen(screen,counterVal):
    screen.fill("orange")
    PlusButton.draw(screen, (0,0,0))
    MinusButton.draw(screen, (0,0,0))
    MultiplyButton.draw(screen, (0,0,0))
    DivideButton.draw(screen, (0,0,0))
    ResetButton.draw(screen, (0,0,0))
    OneButton.draw(screen, (0,0,0))
    TwoButton.draw(screen, (0,0,0))
    ThreeButton.draw(screen, (0,0,0))
    FourButton.draw(screen, (0,0,0))
    FiveButton.draw(screen, (0,0,0))
    SixButton.draw(screen, (0,0,0))
    SevenButton.draw(screen, (0,0,0))
    EightButton.draw(screen, (0,0,0))
    NineButton.draw(screen, (0,0,0))
    TenButton.draw(screen, (0,0,0))
    IncButton.draw(screen, (0,0,0))
    DecButton.draw(screen, (0,0,0))
    ResetButton.draw(screen, (0,0,0))
    font = pygame.font.SysFont("freesansbold", 30, True, False)
    text = font.render(str(counterVal), True, (255,255,255),(0,0,0))
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

    # default values
    counterInc = 1;
    counterOp = "+";
    pygame.display.set_caption('Counter.exe')

    pygame.event.set_allowed([pygame.MOUSEBUTTONDOWN])

    #declare all buttons 
    global PlusButton, MinusButton, MultiplyButton, DivideButton, ResetButton, OneButton, TwoButton, ThreeButton, FourButton, FiveButton, SixButton, SevenButton, EightButton, NineButton, TenButton, IncButton, DecButton, ResetButton
    PlusButton = button((255,255,255),    0,0,30,30,"+")
    MinusButton = button((255,255,255),   30,0,30,30,"-")
    MultiplyButton = button((255,255,255),0,30,30,30,"x")
    DivideButton = button((255,255,255),  30,30,30,30,"÷")

    OneButton = button((255,255,255),     0,60,30,30,"1")
    TwoButton = button((255,255,255),     30,60,30,30,"2")
    ThreeButton = button((255,255,255),   0,90,30,30,"3")
    FourButton = button((255,255,255),    30,90,30,30,"4")
    FiveButton = button((255,255,255),    0,120,30,30,"5")
    SixButton = button((255,255,255),     30,120,30,30,"6")
    SevenButton = button((255,255,255),   0,150,30,30,"7")
    EightButton = button((255,255,255),   30,150,30,30,"8")
    NineButton = button((255,255,255),    0,180,30,30,"9")
    TenButton = button((255,255,255),     30,180,30,30,"10")

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
                        if counterOp == "+":
                            counterVal += counterInc
                        elif counterOp == "-":
                            counterVal -= counterInc
                        elif counterOp == "*":
                            counterVal = counterVal * counterInc
                        elif counterOp == "/":
                            counterVal = counterVal / counterInc

                        counterVal = int(counterVal)

                    elif DecButton.isOver(mousePos):
                        if counterOp == "+":
                            counterVal -= counterInc
                        elif counterOp == "-":
                            counterVal += counterInc
                        elif counterOp == "*":
                            counterVal = counterVal / counterInc
                        elif counterOp == "/":
                            counterVal = counterVal * counterInc

                    elif ResetButton.isOver(mousePos):
                        counterVal = 0
                    elif PlusButton.isOver(mousePos):
                        counterOp = "+"
                    elif MinusButton.isOver(mousePos):
                        counterOp = "-"
                    elif MultiplyButton.isOver(mousePos):
                        counterOp = "*"
                    elif DivideButton.isOver(mousePos):
                        counterOp = "/"
                    elif OneButton.isOver(mousePos):
                        counterInc = 1
                    elif TwoButton.isOver(mousePos):
                        counterInc = 2
                    elif ThreeButton.isOver(mousePos):
                        counterInc = 3
                    elif FourButton.isOver(mousePos):
                        counterInc = 4
                    elif FiveButton.isOver(mousePos):
                        counterInc = 5
                    elif SixButton.isOver(mousePos):
                        counterInc = 6
                    elif SevenButton.isOver(mousePos):
                        counterInc = 7
                    elif EightButton.isOver(mousePos):
                        counterInc = 8
                    elif NineButton.isOver(mousePos):
                        counterInc = 9
                    elif TenButton.isOver(mousePos):
                        counterInc = 10
        pygame.display.flip()
        clock.tick(60) 
    pygame.quit()

#start
main()