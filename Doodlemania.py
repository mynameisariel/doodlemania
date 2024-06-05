"""
Doodlemania
Final project - Partner drawing game inspired by Pictionary and Skribblio
ICS3U
Ariel Liu
History:
03-28-2023 Creation
04-03-2023 Created buttons! :D
04-25-2023 Timer further implementations and more customization on drawing program buttons
05-11-2023 Implemented Screen changes between Welcome, Prompt Generation, and Drawing
05-15-2023 Prompt Generation screen works
05-16-2023 Text Input Pt1
05-24-2023 Improved Timer + Text Input Pt2
05-30-2023 Major changes to the background screens by importing self created pngs as the background

References in Reference Tracking sheet in my google drive folder - https://docs.google.com/document/d/1U6q2FkQX9J0cRqsPUBtdRr3EAt6j9fwroVqS6X7gBbA/edit?usp=sharing

IEEE Citations
[1] R. Sharma, “42 exciting Python Project Ideas & Topics for beginners in 2023 [latest],” upGrad blog, https://www.upgrad.com/blog/python-projects-ideas-topics-beginners/ (accessed Jun. 3, 2023).
[2] S. Gyger, “How to make a drawing program in Python,” Python Code, https://www.thepythoncode.com/article/make-a-drawing-program-with-python (accessed Jun. 3, 2023).
[3] M. Maeder, “How to make buttons in PyGame,” Python Code, https://www.thepythoncode.com/article/make-a-button-using-pygame-in-python (accessed Jun. 3, 2023).
[4] G. A. Hjelle, “Python timer functions: Three ways to monitor your code,” Real Python, https://realpython.com/python-timer/ (accessed Jun. 3, 2023).
[5] D. Potato, “Menus - pygame tutorial,” YouTube, https://www.youtube.com/watch?v=0RryiSjpJn0 (accessed Jun. 3, 2023).
[6] B. Tech, “How to make a menu screen in PYGAME!,” YouTube, https://www.youtube.com/watch?v=GMBqjxcKogA (accessed Jun. 3, 2023).
[7] Ankthon, “Python: Display text to Pygame Window,” GeeksforGeeks, https://www.geeksforgeeks.org/python-display-text-to-pygame-window/ (accessed Jun. 3, 2023).
[8] “Welcome to making apps with Pygame!,” Welcome to making apps with Pygame! - Pygame tutorial 2019 documentation, https://pygame.readthedocs.io/en/latest/index.html (accessed Jun. 3, 2023).
[9] “HTML color codes,” HTML Color Codes, https://htmlcolorcodes.com/ (accessed Jun. 4, 2023).
[10] B. Weber, “Python enumerate(): Simplify looping with counters,” Real Python, https://realpython.com/python-enumerate/ (accessed Jun. 4, 2023).
[11] “More sugar font,” 1001 Free Fonts, https://www.1001freefonts.com/more-sugar.font (accessed Jun. 4, 2023).
[12] Edu GrandoEdu Grando                    41511 gold badge44 silver badges55 bronze badges et al., “What fonts can I use with pygame.font.font?,” Stack Overflow, https://stackoverflow.com/questions/38001898/what-fonts-can-i-use-with-pygame-font-font (accessed Jun. 4, 2023).
[13] “HANGMAN CODE,” Chapter 8 - writing the Hangman Code, https://inventwithpython.com/invent4thed/chapter8.html (accessed Jun. 4, 2023).
[14] C. Edwards, “changeScreens.py,” Google drive, https://drive.google.com/file/d/1r77x1Sm-X_ze-i3m8iXF8kXYSBgdek8u/view?pli=1 (accessed Jun. 4, 2023).
[15] C. Edwards, “Pygamebuttons,” replit, https://replit.com/@CourtneyEdwards/pygameButtons#main.py (accessed Jun. 4, 2023).
[16] C. Code, “Python / pygame tutorial: Getting text input,” YouTube, https://www.youtube.com/watch?v=Rvcyf4HsWiw&ab_channel=ClearCode (accessed Jun. 4, 2023).
[17] C. Edwards, “Timerpause,” replit, https://replit.com/@CourtneyEdwards/timerPause#main.py (accessed Jun. 4, 2023).
[18] Canva, “Free design tool: Presentations, video, social media | CANVA,” Canva, https://www.canva.com/ (accessed Jun. 5, 2023). 
"""

#================ IMPORTS & SETUP ================

# Imports
from datetime import datetime
import sys
import pygame
import ctypes # enables mouse sensitivity awareness to make window look sharper
import random

# increase dots per inch for better sharper quality
ctypes.windll.shcore.SetProcessDpiAwareness(True)

# initialize pygame
pygame.init()

#================ CONFIGURATION ================

# constants
FPS = 300
SCREENWIDTH = 1600
SCREENHEIGHT = 900 

# restrain the max amount of fps
CLOCK = pygame.time.Clock()

# screen + font setup
screen = pygame.display.set_mode([SCREENWIDTH, SCREENHEIGHT], pygame.RESIZABLE)

#each screen will be a background image that is loaded into the program
welcomeBg = pygame.image.load("Background Screens/Welcome Screen.png").convert()
instructionsBg = pygame.image.load("Background Screens/Instructions Screen.png").convert()
promptBg = pygame.image.load("Background Screens/Prompt Screen.png").convert()
attentionBg = pygame.image.load("Background Screens/Attention Screen.png").convert()
drawingBg = pygame.image.load("Background Screens/Drawing Screen.png").convert()
finishBg = pygame.image.load("Background Screens/Finish Screen.png").convert()
thankYouBg = pygame.image.load("Background Screens/Thank You Screen.png").convert()

#different font sizes
mainFont = pygame.font.Font("Fonts/MoreSugar-Regular.ttf", 20)
typeFont = pygame.font.Font("Fonts/MoreSugar-Regular.ttf", 40)
titleFont = pygame.font.Font("Fonts/MoreSugar-Regular.ttf", 100)
hugeTitleFont = pygame.font.Font("Fonts/MoreSugar-Regular.ttf", 180)

#================ CLASSES ================

# Button Class
class Button():
    """
    Represents buttons on the screen
    Attributes:
        x: button's x coordinate
        y: button's y coordinate
        width: button's width
        height: button's height
        colours: list of the button colours (normal, hover, pressed)
        onclickFunction: function that button calls when clicked (boolean)
        onePress: defines whether the button continuously calls function while pressed, or only once (boolean)
        alreadyPressed: button state (boolean)
        font: specific font that the button text uses
        doSomething: used to toggle the timer button to start or pause it  (boolean)
        
    """
    def __init__(self, x, y, width, height, colours, font, buttonText = "Button", onclickFunction = None, onePress = False):
        """
        Initializes Button attributes
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False
        self.font = font
        self.doSomething = False
        
        #different colours for different states of the button - need to be the colour hex code
        self.fillColours = {
            "normal": colours[0],
            "hover": colours[1],
            "pressed": colours[2]
            }
        
        #use values defined above to create button surface and button rect
        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))
        
        #creating the ability for the text button to wrap text
        self.textList = []
        splitText = buttonText.split("\n")
        
        #find the longest line
        self.longestText = 0
        for i in range(1, len(splitText)):
            if len(splitText[i]) > len(splitText[self.longestText]):
                self.longestText = i #keep track of the longest line in the loop
        
        #render each line
        for line in splitText:
            line = self.font.render(line, True, (20, 20, 20))
            self.textList.append(line)
        
        #warnings if button isnt long or wide enough
        self.requiredHeight = (len(splitText))*self.font.get_height()
        if self.requiredHeight > self.height:
            print("Warning: Button height is too small for text.")
            
        if self.textList[self.longestText].get_rect().width > self.width:
            print("Warning: Button width is too small for text.")

        
    def process(self):
        """
        Process function that is called every frame to check for the mouse and clicking of button.
        Args:
            self: Button
        """
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColours["normal"]) #fill with the regular button colour
        
        #check if mouse touches button to fill with other colours
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColours["hover"])
            
            #get_pressed returns states of three mouse buttons [0] is the left mouse button that we want to get
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColours["pressed"])
                #onePress variable lets us control whether we want to call the function after the mouse clicks immediately or for as long as the mouse is pressed
                
                if self.onePress:
                    self.onclickFunction() #run the click function
                
                elif not self.alreadyPressed: #making sure that it has not been pressed already, then running the function and making alreadyPressed True
                    self.onclickFunction()
                    self.alreadyPressed = True
                    self.doSomething = True #set doSomething to True when it has been clicked to keep track of whether the button is being toggled to start or pause
                
                else:
                    self.doSomething = False #doSomething mimics alreadyPressed, but just is a separate attribute that will be only become True when the button is pressed at first and then False afterwards
    
            else:
                self.alreadyPressed = False
                self.doSomething = False
                
        #blit text on surface and screen
        tempHeight = 0 #temp variable for y-placement of text line on button

        #For each line of text, blit to screen, centered over the 
        for line in self.textList:
            self.buttonSurface.blit(line, [
                #The x placement is optimized for the longest line of text. 
                #The y-placement is optimized for centering top to bottom, so long as the text isn't too large for the button height.
                self.buttonRect.width/2 - self.textList[self.longestText].get_rect().width/2,
                self.buttonRect.height/2 - self.requiredHeight/2 + tempHeight
            ])
            tempHeight += self.font.get_height()

        screen.blit(self.buttonSurface, self.buttonRect)

# Timer Class
class Timer():
    """
    Custom Timer class that is able to keep track of time and start and stop elapsed time.
    Attributes:
        _start_time: tracks when the timer has started - has the value None when the timer has not started yet (float)
        _paused: tracks if the timer has been paused (boolean)
        _pausedStart: tracks the start time after the timer has been pasued  - None value if this hasn't happened yet (float)
        _elapsed: tracks the time elapsed - None value if the timer has not started yet (float)
    """
    
    def __init__(self):
        """
        Initializes Timer attributes
        Args:
            self: Timer
        """
        self._start_time = None 
        self._paused = False
        self._pausedStart = None
        self._elapsed = None

    def start(self, pause = False):
        """
        Starting a new timer.
        Args:
            self: Timer
            pause: boolean
        """
        self._start_time = datetime.now() #the time value of now is stored in _start_time

    def get(self):
        """
        Getting the current time of the timer constantly.
        Args:
            self: Timer
        """
        getTime = datetime.now() #constantly getting the current time
        self._elapsed = (getTime - self._start_time).total_seconds() #allowing us to get the total seconds of the amount of time that has passed since the current time and the start time
        if self._elapsed <= 0: #making sure that the elapsed time can't go negative when toggling the button
            self._elapsed = 0


#================ VARIABLES ================

# COLOURS - three different shades for each colour for the buttons 
red = ["#FF0000", "#CD0000", "#970000"]
orange = ["#FF9800", "#D47600", "#AD6000"]
yellow = ["#FFD200", "#D8B200", "#BB9A00"]
lightGreen = ["#3BC800", "#33AD00", "#2B9100"]
darkGreen = ["#006F0C", "#015B0A", "#004007"]
lightBlue = ["#0091FF", "#0275CC", "#005FA7"]
darkBlue = ["#0048BF", "#003C9F", "#002F7C"]
purple = ["#9900F7", "#8000CF", "#62009F"]
pink = ["#F562D3", "#BB439F", "#A03988"]
black = ["#000000", "#000000", "#000000"]
white = ["#FFFFFF", "#D1D1D1", "#D1D1D1"]
grey = ["#939393", "#777777", "#4F4F4F"]

# OBJECT LISTS
#list for each objects/buttons in each screen - the buttons will be appended to each of these lists
dObjects = [] 
pObjects = []
wObjects = []
aObjects = []
fObjects = []
iObjects = []

# BUTTON SIZE VARIABLES

#welcome screen
playButtonSize = [300, 150]
instructionsButtonSize = [300, 100]

#instructions screen
gotItButtonSize = [180, 70]

#attention screen
nextButtonSize = [300, 140]

#prompt screen
okButtonSize = [200, 140]

#drawing screen
handlerButtonWidth = 90
handlerButtonHeight = 58
colourButtonWidth = 40
colourButtonHeight = 40
clickButtonSize = [100, 50]

#finish screen
thankYouButtonSize = [500, 270]
exitButtonSize = [250, 130]

# TEXT INPUT VARIABLES
userText = ""
inputRect = pygame.Rect(170, 320, 200, 60)
active = False
textBoxColour = lightBlue

# DRAWING VARIABLES
drawColour = [0, 0, 0] # initial colour the brush starts with
brushSize = 20
brushSizeSteps = 3 # how many pixels the brush increases by
canvasSize = [800, 700]

#================ FUNCTIONS ================


# Handler functions to adjust the colour and brush size
def changeColour(colour):
    """
    Changes the colour of drawColour variable to the desired colour.
    Args: 
        colour: str
    """
    global drawColour #global variable used to access the drawColour variable and change it through the click of the button
    #changing drawColour that is used to paint depending on user choice
    drawColour = colour

def changeBrushSize(dir):
    """
    Changes the brush size smaller or larger depending on the dir variable.
    Args:
        dir: str
    """
    global brushSize #global variable used to access the brushSize variable and change it through the click of the button
    #making brush size bigger or smaller depending on button that the user clicks
    if (dir == "greater"):
        brushSize += brushSizeSteps
    else:
        brushSize -= brushSizeSteps

# Text function
def displayText(text, font, textcolour, surface, x, y):
    """
    This function displays text to screen.
    Args:
        text: str
        font: Sysfont
        textcolour: list
        surface: rect
        x: int
        y: int
    """
    
    textObj = font.render(text, True, textcolour) #rendering text
    textRect = textObj.get_rect() #creating a surface for the text
    textRect.center = (x, y) #finding the centre of the rect
    surface.blit(textObj, textRect) #blit the text onto screen
    
# Button Actions
def startGame():
    """
    This function starts the timer. Used when the start button is pressed.
    Args: None
    """
    timer.start()


def doNothing():
    """
    This function allows buttons to change screens by doing nothing.
    Args: None
    """
    pass

# prompt generation

def generatePrompt():
    """
    This function counts the number of characters in a word and prints underscores for the amount of characters. 
    Args:
        None
    """

    #list of possible prompts
    prompts = [
        "ice cream",
        "Captain America",
        "MHS",
        "koala",
        "Tim Hortons",
        "Lion King",
        "frozen yogurt",
        "tennis",
        "popcorn",
        "geography",
        "fluffy sheep",
        "Ottawa",
        "rhino",
        "Rick Astley",
        "science fair"
        ]
    
    finalPrompt = random.choice(prompts) #randomly choose from list
    return finalPrompt

def hidePrompt(word):
    """
    This function counts the number of characters in a word and prints underscores for the amount of characters, hiding the prompt. 
    Args:
        word: str
    """
    
    count = len(word) #count the number of characters in the string
    for i in word:
        if (i == " "):
            count -= 1 #remove the count if there is a space

    blanks = "__ " * count #create the __ for the number of characters
    return blanks

#================ INTERFACE CREATION ================

# For each interface/screen I have various buttons and text that need to be set up or displayed so I create them here and they are processed onto the screen in the program later. For each button, I use constants for their size that I defined earlier. Their placement can therefore be properly done on the screen.

# Drawing Screen 
# list of lists for each button (displayed text and the function)
handlerButtons = [
    ['Brush \nLarger', lambda: changeBrushSize('greater')],
    ['Brush \nSmaller', lambda: changeBrushSize('smaller')],
]

#colour list, change colour function to the specific colour
colourButtons = [
    [red, lambda: changeColour(red[0])],
    [orange, lambda: changeColour(orange[0])],
    [yellow, lambda: changeColour(yellow[0])],
    [lightGreen, lambda: changeColour(lightGreen[0])],
    [darkGreen, lambda: changeColour(darkGreen[0])],
    [lightBlue, lambda: changeColour(lightBlue[0])],
    [darkBlue, lambda: changeColour(darkBlue[0])],
    [purple, lambda: changeColour(purple[0])],
    [pink, lambda: changeColour(pink[0])],
    [black, lambda: changeColour(black[0])],
    [white, lambda: changeColour(white[0])],
    [grey, lambda: changeColour(grey[0])]
]

# setting up the buttons on screen 10 pixels apart
for index, buttonName in enumerate(handlerButtons): # enumerate allows each item in list to receive an index (number)
    handlerButton = Button(SCREENWIDTH - 95, (index * (handlerButtonHeight + 10) + 10) + 100, handlerButtonWidth, handlerButtonHeight, pink, mainFont, buttonName[0], buttonName[1])
    dObjects.append(handlerButton) #we append all the buttons to a list for the specific screen that is used to process them onto the screen

#same with colour buttons
for index, paintColour in enumerate(colourButtons):
    colourButton = Button(SCREENWIDTH - 70, (index * (colourButtonHeight + 10) + 10) + 230, colourButtonWidth, colourButtonHeight, paintColour[0], mainFont, "", paintColour[1], True)
    dObjects.append(colourButton)

#timer buttons
startButton = Button(SCREENWIDTH - (clickButtonSize[0] + 100), SCREENHEIGHT - (clickButtonSize[1] + 10), clickButtonSize[0], clickButtonSize[1], lightBlue, mainFont, "START", startGame) 
stopButton = Button(SCREENWIDTH - (clickButtonSize[0] + 100), SCREENHEIGHT - (clickButtonSize[1] + 10), clickButtonSize[0], clickButtonSize[1], red, mainFont, 'PAUSE', doNothing)
dObjects.append(startButton) #append startButton only so that it is processed to screen at the beginning (we append stopButton later)

# Welcome Screen 
playButton = Button(SCREENWIDTH/2 - playButtonSize[0]/2, SCREENHEIGHT - 320, playButtonSize[0], playButtonSize[1], pink, titleFont, 'PLAY', doNothing)
instructionsButton = Button(300, SCREENHEIGHT - 290, instructionsButtonSize[0], instructionsButtonSize[1], yellow, typeFont, "How To Play", doNothing)
wObjects.append(playButton)
wObjects.append(instructionsButton)

# Instructions Screen
gotItButton = Button(SCREENWIDTH - gotItButtonSize[0] - 20, SCREENHEIGHT - gotItButtonSize[1] - 20, gotItButtonSize[0], gotItButtonSize[1], orange, typeFont, "GOT IT", doNothing)
iObjects.append(gotItButton)

# Prompt Screen
chosenPrompt = generatePrompt()
okButton = Button(SCREENWIDTH/2 - okButtonSize[0]/2, SCREENHEIGHT - 300, okButtonSize[0], okButtonSize[1], orange, titleFont, "OK", doNothing)
pObjects.append(okButton)
hiddenPrompt = hidePrompt(chosenPrompt)

# Attention Screen
nextButton = Button(SCREENWIDTH/2 - nextButtonSize[0]/2, SCREENHEIGHT - 150, nextButtonSize[0], nextButtonSize[1], lightGreen, titleFont, "NEXT", doNothing)
aObjects.append(nextButton)

# Finish Screen
thankYouButton = Button(SCREENWIDTH/2 - thankYouButtonSize[0]/2, SCREENHEIGHT - thankYouButtonSize[1] - 50, thankYouButtonSize[0], thankYouButtonSize[1], purple, titleFont, "THANK\n  YOU", doNothing)
exitButton = Button(SCREENWIDTH - exitButtonSize[0] - 30, SCREENHEIGHT - exitButtonSize[1] - 30, exitButtonSize[0], exitButtonSize[1], orange, titleFont, "EXIT", doNothing)
fObjects.append(thankYouButton)
fObjects.append(exitButton)

# Canvas 
canvas = pygame.Surface(canvasSize)
canvas.fill((255, 255, 255))

# Timer initialization
timer = Timer()

#================ MAIN GAME SCREENS ================
# Different game screens

# Menu
def main():
    """
    This function is the main driver for the program.
    Args: none
    Returns: None
    """
    run = True
    status = "w" #starting the screen at welcome
    
    # for each status, there is a different function that runs its own small program within - allows the switching of screens
    while run:
        if (status == "w"):
            status = welcome()
        if (status == "i"):
            status = instructionsScreen()
        if (status == "p"):
            status = promptGeneration()
        if (status == "d"):
            status = drawingScreen(startButton)
        if (status == "f"):
            status = finish()
        if (status == "a"):
            status = attentionScreen()
        if (status == "t"):
            status = thankYouScreen()
        if (status == "q"):
            run = False
        
        #generating the pygame display
        pygame.display.flip()
        CLOCK.tick(FPS)


# Welcome screen
def welcome():
    """
    This function is the welcome screen. Allows the user to navigate to different parts of the game.
    Args: None
    """
    choice = "w"
    #blit background image/screen
    screen.blit(welcomeBg, (0, 0))
    
    #allow user to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    #create buttons
    for object in wObjects:
        object.process()
    
    #check if buttons are pressed to switch screens
    if playButton.alreadyPressed:
        choice = "a"
    
    if instructionsButton.alreadyPressed:
        choice = "i"
    
    return choice

# Instructions Screen
def instructionsScreen():
    """
    This function is the instructions screen. Displays instructions for how to play the game.
    Args: None
    """

    choice = "i"
    screen.blit(instructionsBg, (0, 0))
    
    #allow user to quit
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()

    #create button
    for object in iObjects:
        object.process()

    #check to switch screens
    if gotItButton.alreadyPressed:
        print("got it")
        choice = "a"

    return choice

# Attention Screen
def attentionScreen():
    """
    This function is the attention screen. It gives a warner for the guesser to not look at the next screen since it will show the prompt.
    Args:
        None
    """
    
    choice = "a"
    screen.blit(attentionBg, (0, 0))
    
    #allow user to quit
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()
           
    for object in aObjects:
        object.process()
        
    if nextButton.alreadyPressed:
        choice = "p"
        
    return choice
    

# Prompt Generator
def promptGeneration():
    """
    This function is the prompt screen. It gives a randomly generated prompt for the drawer to draw.
    Args:
        None
    """

    choice = "p"
    screen.blit(promptBg, (0, 0))
    
    #allow user to quit
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()  
    
    for object in pObjects:
        object.process()

    #display chosen prompt using the displayText function that was created earlier
    displayText(chosenPrompt, hugeTitleFont, black[0], screen, SCREENWIDTH/2, SCREENHEIGHT/2)

    #switch screens
    if okButton.alreadyPressed:
        choice = "d"
    
    return choice
    
    
# Main Drawing Screen
def drawingScreen(startButton):
    """
    This function is the main drawing screen. Allows the user to handle the drawing functions.
    Args:
        startButton: Button
    """
    choice = "d"
    screen.blit(drawingBg, (0, 0))

    #allow user to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # text input
        #check if the user has pressed on the textbox
        if event.type == pygame.MOUSEBUTTONDOWN:
            if inputRect.collidepoint(event.pos):
                global active #global variable used to keep track of the state for active - was not able to figure out how to avoid using this global variable - program would run into bugs if the variable was passed as an argument 
                active = True
            else:
                active = False

        if event.type == pygame.KEYDOWN:
            #when the user types stuff, we need to make sure they have pressed the box first 
            if active:
                global userText #same issue: global variable used since passing the argument and keeping track of its state resulted in problems with the code :(
                if event.key == pygame.K_BACKSPACE:
                    userText = userText[:-1] #allowing the user to use the backspace key

                elif event.key == pygame.K_RETURN:
                    userText = userText
                    active = False #finishing the typing when return key is pressed
                    if (userText.lower() == chosenPrompt.lower()):
                        choice = "f" #change screens if the guesser guesses correct
                else:
                    userText += event.unicode #this method allows the user to type text
                
    # drawing buttons / checking if they are pressed
    for object in dObjects:
        object.process()

    # text input - if the box is clicked on, the box colour will become darker
    if active:
        boxColour = textBoxColour[1]
    else:
        boxColour = textBoxColour[0]
    pygame.draw.rect(screen, boxColour, inputRect, 2)

    textSurface = typeFont.render(userText, True, black[0])
    screen.blit(textSurface, (inputRect.x + 5, inputRect.y + 5)) #if the user text input is becoming too long, the rectangle will follow the text

    inputRect.w = max(200, textSurface.get_width() + 10) #having a starting width and height before it follows the text length
        
    # drawing canvas on right of screen
    cx = SCREENWIDTH - canvasSize[0] - 100
    cy = SCREENHEIGHT - canvasSize[1] - 70
    screen.blit(canvas, [cx, cy])
    
    # timer stuff
    
    if startButton in dObjects and not startButton.alreadyPressed: #this prevents the user from drawing before they have pressed START
        timer._paused = True #prevents timer from running 
        timer._elapsed = 0
        
    elif startButton in dObjects and startButton.alreadyPressed: #making sure that the stop button does not get pressed as well
        dObjects.remove(startButton) #this allows the first START button to not be processed since it is removed from the list
        timer._start_time = datetime.now() #keep track of when the timer first starts to determine the time elapsed
        dObjects.append(stopButton) #process the stopButton onto the screen
        stopButton.alreadyPressed = True #avoid having to press the stop button twice so need to set it to True when timer starts running
        timer._paused = False

    elif stopButton.doSomething: #the timer is able to track if the stop button is pressed to in order to "doSomething"
        if (timer._paused == False):
            #set paused to true
            timer._paused = True
            timer._pausedStart = datetime.now() #keep track of time at paused
        
        #basically toggling the timer on and off - checking whether the timer_paused is true or not and either pausing it or starting it again
        else:
            timer._paused = False
            timer._start_time = datetime.now() - (timer._pausedStart - timer._start_time) #able to make timer start where it left off

    # this runs the actual timer
    if not timer._paused:
        if (timer._start_time != None):
            timer.get() # constantly keeps track of the current time elapsed
        else:
            timer._elapsed = 0
    
    # allowing player to draw

    if timer._paused == False: #making sure they only draw after they press START
        if pygame.mouse.get_pressed()[0]:             
                mx, my = pygame.mouse.get_pos()

                # calculate actual drawing pos on canvas
                dx = mx - (SCREENWIDTH - canvasSize[0] - 100)
                dy = my - (SCREENHEIGHT / 2) + (canvasSize[1] / 2 - 15) #get a good height for the position of stroke on canvas 

                # the brush on the screen will be a circle that continues to process when the mouse is clicked
                pygame.draw.circle(
                    canvas,
                    drawColour,
                    [dx, dy],
                    brushSize
                )
                
                
    # reference dot - able to allow the user to see the colour and brush size
    pygame.draw.circle(
        screen, 
        drawColour,
        [screen.get_size()[0] - 50, 50],
        brushSize
    )
    
    # display time elapsed
    displayText(str(round(timer._elapsed, 2)), mainFont, black[0], screen, (cx + (canvasSize[0] - 50)), (cy + (canvasSize[1] - 40)))

    # display the amqount of letters in the prompt as a clue for guesser
    displayText(hiddenPrompt, mainFont, black[0], screen, SCREENWIDTH - 600, SCREENHEIGHT - 30)

    return choice

def finish():
    """
    This is the finishing screen for when the guesser has guessed the prompt correctly".
    Args:
        None
    Returns:
        choice: str
    """
    
    choice = "f"
    screen.blit(finishBg, (0,0))
    
    #allow user to quit
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()
           
    for object in fObjects:
        object.process()
        
    if thankYouButton.alreadyPressed:
        choice = "t"
    if exitButton.alreadyPressed:
        choice = "q"

    points = round(500 - timer._elapsed, 1)
    displayText(str(points), titleFont, black[0], screen, 230, SCREENHEIGHT - 170)
    
    return choice

def thankYouScreen():
    """
    This function is the thank you screen.
    Args:
        None
    """
    
    # due to the fact that i wasn't able to figure out how to allow the user to navigate back to previous screens and reset the whole game to play again, i provided this thank you screen that let the players know to rerun the program if they want to play again - a bit of a hassle, but is able to communicate this to the players and avoid running into issues with bugs
    choice = "t"
    screen.blit(thankYouBg, (0,0))
    
    #allow user to quit
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()
    
    return choice


#================ CALLING MAIN FUNCTION ================
#this allows the whole game to run
main() 