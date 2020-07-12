'''
File:
    jordanui.py

Student Name:
    Jordan McCann - 23571144
    
Purpose: 
    To draw and render UI elements to the application based on context    
'''

# Library Imports
import cv2
import numpy as np

# Global Fonts
font = cv2.FONT_HERSHEY_SIMPLEX

# Global Render Booleans
shouldRenderMainMenu = False
shouldRenderHelloWorld = False
shouldRenderConditionals = False
shouldRenderLoops = False
shouldRenderFunctions = False

# Global States
## Button States
RunClicked = False
BackClicked = False
StatusRed = False
StatusGreen = False

# Selection States
## Hello World Screen
HelloWorld_PythonClicked = False
HelloWorld_JavaClicked = False
HelloWorld_ElixirClicked = False

## Conditonals Screen
Conditionals_PythonClicked = False
Conditionals_JavaClicked = False
Conditionals_LispClicked = False

## Loops Screen
Loops_PythonClicked = False
Loops_JavaClicked = False
Loops_JavascriptClicked = False

## Functions Screen
Functions_PythonClicked = False
Functions_JavaClicked = False
Functions_RustClicked = False

# CheckBackClicked function
## To check if the backbutton is clicked, if so, render the main menu
def CheckBackClicked():
    # Marked as global for assignment
    global shouldRenderMainMenu
    global shouldRenderHelloWorld
    global shouldRenderConditionals
    global shouldRenderLoops
    global shouldRenderFunctions
    global BackClicked
        
    if(BackClicked == True):
        shouldRenderMainMenu = True
        shouldRenderHelloWorld = False
        shouldRenderConditionals = False
        shouldRenderLoops = False
        shouldRenderFunctions = False
        BackClicked = False

# checkRenderScreens Function
# Function that Checks If something should be rendered to the screen
def checkRenderScreens(img):
    if shouldRenderMainMenu == True:
            renderMainMenu(img)
    elif shouldRenderHelloWorld == True:
        renderHelloWorldExample(img)
    elif shouldRenderConditionals == True:
        renderConditionalsExample(img)
    elif shouldRenderLoops == True:
        renderLoopsExample(img)
    elif shouldRenderFunctions == True:
        renderFunctionsExample(img)
    # Show Error if nothing is rendering
    else:
        cv2.rectangle(img, (0, 0), (1600, 900), (0, 0, 0), -1)
        cv2.putText(img, "Error: There is nothing rendering...", (100, 300), font, 2, (0, 0, 255), 5, cv2.LINE_AA)

# renderWindowBasics Function
# Function that draws the basic window features such as background and borders
def renderWindowBasics(img):
    # Border
    cv2.rectangle(img, (0, 0), (1600, 900), (196, 196, 196), -1)
    # Background
    cv2.rectangle(img, (50, 50), (1550, 850), (255, 255, 255), -1) 
    # Run Check Every render
    CheckBackClicked()

def renderInteractionButtonsAndStatus(img):
    # Buttons
    ## Back Button
    cv2.rectangle(img, (50, 675), (500, 850), (101, 101, 231), -1)
    cv2.putText(img, "BACK", (175, 780), font, 2, (0, 0, 0), 2, cv2.LINE_AA)
    ## Run Button
    cv2.rectangle(img, (1100, 675), (1550, 850), (120, 154, 102), -1)
    cv2.putText(img, "RUN", (1280, 780), font, 2, (0, 0, 0), 2, cv2.LINE_AA)
    ## Status Area
    # Check Current status and rerender the status component
    if(StatusRed == False and StatusGreen == False):
        cv2.rectangle(img, (600, 780), (1000, 850), (196, 196, 196), -1)
    elif(StatusRed == True and StatusGreen == False):
        cv2.rectangle(img, (600, 780), (1000, 850), (0, 0, 255), -1)
    elif(StatusRed == False and StatusGreen == True):
        cv2.rectangle(img, (600, 780), (1000, 850), (0, 255, 0), -1)
        
    
################################ Screens
    
    
    
# Main Menu Screen Function
def renderMainMenu(img):
    renderWindowBasics(img)
    
    # Title and text
    cv2.rectangle(img, (400, 75), (1200, 300), (196, 196, 196), -1) # Title Box
    # Title Text
    cv2.putText(img, "Welcome to BUZZ", (440, 175), font, 2.5, (0, 0, 0), 5, cv2.LINE_AA)
    cv2.putText(img, "programming.", (580, 250), font, 2, (0, 0, 0), 5, cv2.LINE_AA)
    # Subtitle text
    cv2.putText(img, "Please touch a program to get started with Python!", (180, 400), font, 1.5, (0, 0, 0), 2, cv2.LINE_AA)
    
    # Buttons and text
    cv2.rectangle(img, (100, 600), (400, 750), (196, 196, 196), -1) # Hello World Button
    cv2.putText(img, "Hello World", (100, 690), font, 1.7, (0, 0, 0), 2, cv2.LINE_AA)
    
    
    cv2.rectangle(img, (450, 600), (750, 750), (196, 196, 196), -1) # Conditionals Button
    cv2.putText(img, "Conditionals", (450, 690), font, 1.6, (0, 0, 0), 2, cv2.LINE_AA)
    
    cv2.rectangle(img, (850, 600), (1150, 750), (196, 196, 196), -1) # Loops Button
    cv2.putText(img, "Loops", (910, 690), font, 2, (0, 0, 0), 2, cv2.LINE_AA)
    
    
    cv2.rectangle(img, (1200, 600), (1500, 750), (196, 196, 196), -1) # Loops Button
    cv2.putText(img, "Functions", (1200, 690), font, 2, (0, 0, 0), 2, cv2.LINE_AA)



# Hello World Example Screen Function
def renderHelloWorldExample(img):
    # Declare Scoping for flags for global assignment
    global StatusGreen
    global StatusRed
        
    renderWindowBasics(img)
    
    # Window Title box and text
    cv2.rectangle(img, (100, 20), (300, 100), (196, 196, 196), -1)
    cv2.putText(img, "Hello World", (110, 80), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
    
    # Code Area
    ## Border Area
    cv2.rectangle(img, (800, 80), (1500, 500), (0, 0, 0), 1)
    cv2.putText(img, "# Make Python Run Hello World", (850, 150), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
    
    ### SELECTION STUFF
    cv2.rectangle(img, (850, 200), (1450, 300), (196, 196, 196), -1)
    
    if(HelloWorld_PythonClicked == False):
        # Python Answer
        cv2.rectangle(img, (100, 150), (600, 250), (196, 196, 196), -1)
        cv2.putText(img, "print('hello world')", (105, 215), font, 1.7, (0, 0, 0), 2, cv2.LINE_AA)
    elif(HelloWorld_PythonClicked == True):
        cv2.putText(img, "print('hello world')", (850, 270), font, 1.7, (0, 0, 0), 2, cv2.LINE_AA)
        
    if(HelloWorld_JavaClicked == False):
        # Java Answer
        cv2.rectangle(img, (100, 350), (600, 450), (196, 196, 196), -1)
        cv2.putText(img, "System.println(\"Hello World\");", (105, 415), font, 1.07, (0, 0, 0), 2, cv2.LINE_AA)
    elif(HelloWorld_JavaClicked == True):
        cv2.putText(img, "System.println(\"Hello World\");", (850, 270), font, 1.07, (0, 0, 0), 2, cv2.LINE_AA)
    
    # Elixir Answer
    if(HelloWorld_ElixirClicked == False):
        cv2.rectangle(img, (100, 550), (600, 650), (196, 196, 196), -1)
        cv2.putText(img, "IO.puts(\"Hello World\")", (105, 610), font, 1.4, (0, 0, 0), 2, cv2.LINE_AA)
    elif(HelloWorld_ElixirClicked == True):
        cv2.putText(img, "IO.puts(\"Hello World\")", (850, 270), font, 1.4, (0, 0, 0), 2, cv2.LINE_AA)
    
    if(HelloWorld_PythonClicked == True and RunClicked == True):
        StatusGreen = True
        StatusRed = False
    elif(HelloWorld_JavaClicked == True or HelloWorld_ElixirClicked == True and RunClicked == True):
        StatusGreen = False
        StatusRed = True
    
    # BUTTONS
    renderInteractionButtonsAndStatus(img)
    
    
    
# Conditional Example Screen Function
def renderConditionalsExample(img):
    # Declare Scoping for flags for global assignment
    global StatusGreen
    global StatusRed
    
    renderWindowBasics(img)
    
    # Window Title box and text
    cv2.rectangle(img, (100, 20), (300, 100), (196, 196, 196), -1)
    cv2.putText(img, "Conditionals", (110, 80), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
    
    # Code Area 
    ## Border Area
    cv2.rectangle(img, (800, 80), (1500, 500), (0, 0, 0), 1)
    
    ### SELECTION STUFF
    cv2.rectangle(img, (850, 200), (1450, 300), (196, 196, 196), -1)
    cv2.putText(img, "# Check to see if X and Y are equal", (850, 150), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(img, "    print(\"X is Equal to Y\")", (850, 350), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
    
    if(Conditionals_PythonClicked == False):
        # Python Answer
        cv2.rectangle(img, (100, 150), (600, 250), (196, 196, 196), -1)
        cv2.putText(img, "if x == y:", (105, 215), font, 1.7, (0, 0, 0), 2, cv2.LINE_AA)
    elif(Conditionals_PythonClicked == True):
        cv2.putText(img, "if x == y:", (850, 270), font, 1.7, (0, 0, 0), 2, cv2.LINE_AA)
        
    if(Conditionals_JavaClicked == False):
        # Java Answer
        cv2.rectangle(img, (100, 350), (600, 450), (196, 196, 196), -1)
        cv2.putText(img, "if(x == y) {", (105, 415), font, 1.07, (0, 0, 0), 2, cv2.LINE_AA)
    elif(Conditionals_JavaClicked == True):
        cv2.putText(img, "if(x == y) {", (850, 270), font, 1.07, (0, 0, 0), 2, cv2.LINE_AA)
    
    # Lisp Answer
    if(Conditionals_LispClicked == False):
        cv2.rectangle(img, (100, 550), (600, 650), (196, 196, 196), -1)
        cv2.putText(img, "(if x == y)", (105, 610), font, 1.4, (0, 0, 0), 2, cv2.LINE_AA)
    elif(Conditionals_LispClicked == True):
        cv2.putText(img, "(if x == y)", (850, 270), font, 1.4, (0, 0, 0), 2, cv2.LINE_AA)
    
    # Check Answer and update status component state
    if(Conditionals_PythonClicked == True and RunClicked == True):
        StatusGreen = True
        StatusRed = False
    elif(Conditionals_JavaClicked == True or Conditionals_LispClicked == True and RunClicked == True):
        StatusGreen = False
        StatusRed = True
    
    # BUTTONS
    renderInteractionButtonsAndStatus(img)




# Loops Example Screen Function
def renderLoopsExample(img):
    # Declare Scoping for flags for global assignment
    global StatusGreen
    global StatusRed
    
    renderWindowBasics(img)
    
    # Window Title box and text
    cv2.rectangle(img, (100, 20), (300, 100), (196, 196, 196), -1)
    cv2.putText(img, "Loops", (110, 80), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
    
    # Code AreA
    ## Border Area
    cv2.rectangle(img, (800, 80), (1500, 500), (0, 0, 0), 1)
    
    ### SELECTION STUFF
    cv2.rectangle(img, (850, 200), (1450, 300), (196, 196, 196), -1)
    cv2.putText(img, "# Choose the correct for loop", (850, 150), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(img, "    print(i)", (850, 350), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
    
    if(Loops_PythonClicked == False):
        # Python Answer
        cv2.rectangle(img, (100, 150), (600, 250), (196, 196, 196), -1)
        cv2.putText(img, "for i in range(10):", (105, 215), font, 1.7, (0, 0, 0), 2, cv2.LINE_AA)
    elif(Loops_PythonClicked == True):
        cv2.putText(img, "for i in range(10):", (850, 270), font, 1.7, (0, 0, 0), 2, cv2.LINE_AA)
        
    if(Loops_JavaClicked == False):
        # Java Answer
        cv2.rectangle(img, (100, 350), (600, 450), (196, 196, 196), -1)
        cv2.putText(img, "for(int i = 0; i < 10; i++) {", (105, 415), font, 1.07, (0, 0, 0), 2, cv2.LINE_AA)
    elif(Loops_JavaClicked == True):
        cv2.putText(img, "for(int i = 0; i < 10; i++) {", (850, 270), font, 1.07, (0, 0, 0), 2, cv2.LINE_AA)
    
    # Lisp Answer
    if(Loops_JavascriptClicked == False):
        cv2.rectangle(img, (100, 550), (600, 650), (196, 196, 196), -1)
        cv2.putText(img, "for(var i = 0; i < 10; i++) {", (105, 610), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
    elif(Loops_JavascriptClicked == True):
        cv2.putText(img, "for(var i = 0; i < 10; i++) {", (850, 270), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
    
    # Check Answer and update status component state
    if(Loops_PythonClicked == True and RunClicked == True):
        StatusGreen = True
        StatusRed = False
    elif(Loops_JavaClicked == True or Loops_JavascriptClicked == True and RunClicked == True):
        StatusGreen = False
        StatusRed = True
    
    # BUTTONS
    renderInteractionButtonsAndStatus(img)



# Functions Example Screen Function 
def renderFunctionsExample(img):
    # Declare Scoping for flags for global assignment
    global StatusGreen
    global StatusRed
    
    renderWindowBasics(img)
    
    # Window Title box and text
    cv2.rectangle(img, (100, 20), (300, 100), (196, 196, 196), -1)
    cv2.putText(img, "Functions", (110, 80), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
    
    # Code Area
    ## Border Area
    cv2.rectangle(img, (800, 80), (1500, 500), (0, 0, 0), 1)
        
    ### SELECTION STUFF
    cv2.rectangle(img, (850, 200), (1450, 300), (196, 196, 196), -1)
    cv2.putText(img, "# Choose the correct function declaration", (850, 150), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(img, "    return x + y", (850, 350), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
    
    if(Functions_PythonClicked == False):
        # Python Answer
        cv2.rectangle(img, (100, 150), (600, 250), (196, 196, 196), -1)
        cv2.putText(img, "def add(x, y): ", (105, 215), font, 1.7, (0, 0, 0), 2, cv2.LINE_AA)
    elif(Functions_PythonClicked == True):
        cv2.putText(img, "def add(x, y):", (850, 270), font, 1.7, (0, 0, 0), 2, cv2.LINE_AA)

    # Java Answer        
    if(Functions_JavaClicked == False):
        cv2.rectangle(img, (100, 350), (600, 450), (196, 196, 196), -1)
        cv2.putText(img, "void add(int x, int y) {", (105, 415), font, 1.07, (0, 0, 0), 2, cv2.LINE_AA)
    elif(Functions_JavaClicked == True):
        cv2.putText(img, "void add(int x, int y) {", (850, 270), font, 1.07, (0, 0, 0), 2, cv2.LINE_AA)
    
    # Rust Answer
    if(Functions_RustClicked == False):
        cv2.rectangle(img, (100, 550), (600, 650), (196, 196, 196), -1)
        cv2.putText(img, "fn add(x: i32, y: i32){ ", (105, 610), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
    elif(Functions_RustClicked == True):
        cv2.putText(img, "fn add(x: i32, y: i32){", (850, 270), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
    
    # Check Answer and update status component state
    if(Functions_PythonClicked == True and RunClicked == True):
        StatusGreen = True
        StatusRed = False
    elif(Functions_JavaClicked == True or Functions_RustClicked == True and RunClicked == True):
        StatusGreen = False
        StatusRed = True
    
    # BUTTONS
    renderInteractionButtonsAndStatus(img)
    
    
################################### End of Screens
    
    
    
    
    