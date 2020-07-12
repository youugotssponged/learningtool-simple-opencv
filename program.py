'''
File:
    program.py

Student Name:
    Antony Bennett - 21119996

Hand Detection Code Provided by Dr. Ardhendu Behera

Date:
    09/04/2020

Last Modified:
    13/04/2020    

Purpose: 
    To draw and render UI elements to the application based on context    
'''

# Library Imports
import cv2
import numpy as np

# Jordan's UI functions and variables import
import jordanui

# Click detection variables
isClicked = False

# Hand coordinate variables
hand_x = 0
hand_y = 0
hand_x2 = 0
hand_y2 = 0

# Click range check variables
pointer_x = (0, 0)
pointer_y = (0, 0)

# Setup the Camers
camera = cv2.VideoCapture(0)
camera.set(0, 100)
# Sets the camera resolution - Window size is 1600 by 900
camera.set(3, 1920)
camera.set(4, 1080)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1600)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 900)


# load classifiers from file
hand = cv2.CascadeClassifier('haarcascades/Hand.Cascade.1.xml')

jordanui.shouldRenderMainMenu = True # Initial Window State

### Function to change display when corresponding button is clicked ###

def button_click (button_name, x_start, x_end, y_start, y_end):
    
    global isClicked
    
     # Check to see if the the x and y point of the pointer is within range of the Hello World Button
    if (isClicked and jordanui.shouldRenderMainMenu):
        
        # Loop between the range of the x points of the Hello World Button
        for x_check in range(x_start, x_end):
            
            # If pointer_X has the same current value as i then check for the y point
            if (pointer_x == x_check):
                
                # Loop in range of Hello World Y points
                for y_check in range (y_start, y_end):
                    
                    # If both pointer_X and pointer_Y points are within the defined ranges, then change screens
                    if (pointer_y == y_check):
                        
                        # Disable Main Menu bool
                        jordanui.shouldRenderMainMenu = False
                        
                        # When hand detection occurs within the range of a button...
                        
                        if (button_name == "Hello World"): # Change page to Hello World screen
                            
                            # Enable Hello World bool
                            jordanui.shouldRenderHelloWorld = True
                            
                        elif (button_name == "Conditionals"): # Change page to Conditionals screen
                            
                            # Enable Conditionals bool
                            jordanui.shouldRenderConditionals = True
                        
                        elif (button_name == "Loops"): # Change page to Loops screen
                            
                            # Enable Loops bool
                            jordanui.shouldRenderLoops = True
                            
                        elif (button_name == "Functions"): # Change page to Functions screen
                            
                            # Enable Functions bool
                            jordanui.shouldRenderFunctions = True
        
                        # Turn off the isClicked bool
                        isClicked = False
    
    # When the Back button or Run button is clicked, return to the Main Menu screen                   
    if (isClicked and jordanui.shouldRenderMainMenu == False):
        
        # Loop for checking the x range
        for x_check in range(x_start, x_end):
            
            if (pointer_x == x_check):
                
                # Loop for checking the y range
                for y_check in range (y_start, y_end):
                    
                    if (pointer_y == y_check):
                        
                        # Hello world answers                        
                        if (jordanui.shouldRenderHelloWorld):
                            
                            # Enter Python code into the answer section
                            if (button_name == "Python Code"):
                                
                                # Turn off any other answers
                                jordanui.HelloWorld_JavaClicked = False
                                jordanui.HelloWorld_ElixirClicked = False
                                
                                # Turn on the selected answer
                                jordanui.HelloWorld_PythonClicked = True
                                
                                # Remove any previous attempt visualisation (via the status bar booleans)
                                jordanui.StatusGreen = False
                                jordanui.StatusRed = False
                            
                            # Enter Java Code into the answer section
                            elif (button_name == "Java Code"):
                                
                                # Turn off any other answers
                                jordanui.HelloWorld_PythonClicked = False
                                jordanui.HelloWorld_ElixirClicked = False
                                
                                # Turn on the selected answer
                                jordanui.HelloWorld_JavaClicked = True
                                
                                # Remove any previous attempt visualisation (via the status bar booleans)
                                jordanui.StatusGreen = False
                                jordanui.StatusRed = False
                                
                            elif (button_name == "Other Code"):
                                
                                # Turn off any other answers
                                jordanui.HelloWorld_PythonClicked = False
                                jordanui.HelloWorld_JavaClicked = False
                                
                                # Turn on the selected answer
                                jordanui.HelloWorld_ElixirClicked = True
                                
                                # Remove any previous attempt visualisation (via the status bar booleans)
                                jordanui.StatusGreen = False
                                jordanui.StatusRed = False
                                
                        # Conditionals answers                        
                        elif (jordanui.shouldRenderConditionals):
                            
                            # Enter Python code into the answer section
                            if (button_name == "Python Code"):
                                
                                # Turn off any other answers
                                jordanui.Conditionals_JavaClicked = False
                                jordanui.Conditionals_LispClicked = False
                                
                                # Turn on the selected answer
                                jordanui.Conditionals_PythonClicked = True
                                
                                # Remove any previous attempt visualisation (via the status bar booleans)
                                jordanui.StatusGreen = False
                                jordanui.StatusRed = False
                            
                            # Enter Java Code into the answer section
                            elif (button_name == "Java Code"):
                                
                                # Turn off any other answers
                                jordanui.Conditionals_PythonClicked = False
                                jordanui.Conditionals_LispClicked = False
                                
                                # Turn on the selected answer
                                jordanui.Conditionals_JavaClicked = True
                                
                                # Remove any previous attempt visualisation (via the status bar booleans)
                                jordanui.StatusGreen = False
                                jordanui.StatusRed = False
                                
                            elif (button_name == "Other Code"):
                                
                                # Turn off any other answers
                                jordanui.Conditionals_PythonClicked = False
                                jordanui.Conditionals_JavaClicked = False
                                
                                # Turn on the selected answer
                                jordanui.Conditionals_LispClicked = True
                                
                                # Remove any previous attempt visualisation (via the status bar booleans)
                                jordanui.StatusGreen = False
                                jordanui.StatusRed = False
                                
                        # Loops answers                        
                        elif (jordanui.shouldRenderLoops):
                            
                            # Enter Python code into the answer section
                            if (button_name == "Python Code"):
                                
                                # Turn off any other answers
                                jordanui.Loops_JavaClicked = False
                                jordanui.Loops_JavascriptClicked = False
                                
                                # Turn on the selected answer
                                jordanui.Loops_PythonClicked = True
                                
                                # Remove any previous attempt visualisation (via the status bar booleans)
                                jordanui.StatusGreen = False
                                jordanui.StatusRed = False
                            
                            # Enter Java Code into the answer section
                            elif (button_name == "Java Code"):
                                
                                # Turn off any other answers
                                jordanui.Loops_PythonClicked = False
                                jordanui.Loops_JavascriptClicked = False
                                
                                # Turn on the selected answer
                                jordanui.Loops_JavaClicked = True
                                
                                # Remove any previous attempt visualisation (via the status bar booleans)
                                jordanui.StatusGreen = False
                                jordanui.StatusRed = False
                                
                            elif (button_name == "Other Code"):
                                
                                # Turn off any other answers
                                jordanui.Loops_PythonClicked = False
                                jordanui.Loops_JavaClicked = False
                                
                                # Turn on the selected answer
                                jordanui.Loops_JavascriptClicked = True
                                
                                # Remove any previous attempt visualisation (via the status bar booleans)
                                jordanui.StatusGreen = False
                                jordanui.StatusRed = False
                                
                        # Functions answers                        
                        elif (jordanui.shouldRenderFunctions):
                            
                            # Enter Python code into the answer section
                            if (button_name == "Python Code"):
                                
                                # Turn off any other answers
                                jordanui.Functions_JavaClicked = False
                                jordanui.Functions_RustClicked = False
                                
                                # Turn on the selected answer
                                jordanui.Functions_PythonClicked = True
                                
                                # Remove any previous attempt visualisation (via the status bar booleans)
                                jordanui.StatusGreen = False
                                jordanui.StatusRed = False
                            
                            # Enter Java Code into the answer section
                            elif (button_name == "Java Code"):
                                
                                # Turn off any other answers
                                jordanui.Functions_PythonClicked = False
                                jordanui.Functions_RustClicked = False
                                
                                # Turn on the selected answer
                                jordanui.Functions_JavaClicked = True
                                
                                # Remove any previous attempt visualisation (via the status bar booleans)
                                jordanui.StatusGreen = False
                                jordanui.StatusRed = False
                                
                            elif (button_name == "Other Code"):
                                
                                # Turn off any other answers
                                jordanui.Functions_PythonClicked = False
                                jordanui.Functions_JavaClicked = False
                                
                                # Turn on the selected answer
                                jordanui.Functions_RustClicked = True
                                
                                # Remove any previous attempt visualisation (via the status bar booleans)
                                jordanui.StatusGreen = False
                                jordanui.StatusRed = False
                        
                        # If the button clicked is the back button, return to the main menu screen
                        if (button_name == "Back"):
                            
                            # Return back to the main menu screen
                            jordanui.BackClicked = True
                            
                            # Remove any previous attempt visualisation (via the status bar booleans)
                            jordanui.StatusGreen = False
                            jordanui.StatusRed = False
                            
                            # Remove any previous button states
                            # Hello World
                            jordanui.Functions_PythonClicked = False
                            jordanui.Functions_JavaClicked = False
                            jordanui.Functions_ElixirClicked = False
                            # Conditionals
                            jordanui.Functions_PythonClicked = False
                            jordanui.Functions_JavaClicked = False
                            jordanui.Functions_LispClicked = False
                            # Loops
                            jordanui.Functions_PythonClicked = False
                            jordanui.Functions_JavaClicked = False
                            jordanui.Functions_JavascriptClicked = False
                            # Functions
                            jordanui.Functions_PythonClicked = False
                            jordanui.Functions_JavaClicked = False
                            jordanui.Functions_RustClicked = False
                        
                        # Else if the button clicked is the run button, check the answer
                        elif (button_name == "Run"):
                            
                            # Switch the RunClicked bool to True
                            jordanui.RunClicked = True

#################### Main Loop ####################

# While the camera is open and recieving feed
while camera.isOpened():
    
    # Program Display
    ret, img = camera.read() # Read from the camera
    
    img = cv2.resize(img, (1600, 900), fx=0.5, fy=0.5)
    
    # Add light blur to improve image detection and text lines
    post_processing = cv2.GaussianBlur(img, (1, 1), 5)
    
    flip_img = cv2.flip(post_processing, 1) # Flip Image
    
    # Open another window for the camera Feed
    ret2, img2 = camera.read() # Read from the camera
    
    img2 = cv2.resize(img2, (600, 350), fx=0.5, fy=0.5)
    
    flip_img2 = cv2.flip(img2, 1) # Flip Image
    
    # If ret is true
    if(ret):
        gray = cv2.cvtColor(flip_img, cv2.COLOR_BGR2GRAY) # Set the colour scale
                
        # Render Screens based on if they should or not - will update
        jordanui.checkRenderScreens(flip_img)
        
        # Turn all button clicked variables False
        isClicked = False
        jordanui.RunClicked = False
        jordanui.BackClicked = False
        
        # Display the pointer

        pointer = cv2.circle(flip_img, (int((hand_x + hand_x+hand_x2)/2), int((hand_y + hand_y+hand_y2)/2)), 30, (0, 0, 0), 2)
        
        # Hand and Fist
        palms = hand.detectMultiScale(gray, 1.305, 16)
        
        #################### Hand Detection ####################
        
        for (x,y,x2,y2) in palms:
            
            hand_x = x
            hand_y = y
            hand_x2 = x2
            hand_y2 = y2
            
            # Inform the User that a hand has been detected -- Displayed on the camera feed window
            cv2.putText(flip_img2, "Hand Detected", (30,30), cv2.FONT_HERSHEY_DUPLEX, 1, (235, 206, 135), 1)
            
            # Update the pointer position
            pointer
            
            # Update the pointer posistion check
            pointer_x = ((hand_x + hand_x+hand_x2)/2)
            pointer_y = ((hand_y + hand_y+hand_y2)/2)
            
            # Button click
            isClicked = True
    
        #################### Buttons ####################
        
        # When on the Main Munu screen
        
        if (jordanui.shouldRenderMainMenu):
            
            # Hello World Screen
            button_click("Hello World", 100, 400, 600, 750)
            
            # Conditionals Screen
            button_click("Conditionals", 450, 750, 600, 750)
            
            # Loops Screen
            button_click("Loops", 850, 1150 , 600, 750)
            
            # Functions Screen
            button_click("Functions", 1200, 1500 , 600, 750)
        
        #  When any of the other screens
        else:
        
            # Back Button (To Main Menu Screen)
            button_click("Back", 50, 500 , 675, 850)
            
            # Run Button (check answer)
            button_click("Run", 1100, 1550 , 675, 850)
            
            # Three Possible Answers:
            #   - Python Code
            #   - Java Code
            #   - Other Code
            #       - Elixir
            #       - Lisp
            #       - Javascript
            #       - Rust
            button_click("Python Code", 100, 600 , 150, 250)
            button_click("Java Code", 100, 600 , 350, 450)
            button_click("Other Code", 100, 600 , 550, 650)
            
        #################### Render Image ####################
        
        #cv2.resize(flip_img, (1600, 900))
        cv2.imshow('Interface Programming CW2 - Buzz Programming', flip_img)
        
        cv2.imshow('Interface Programming CW2 - Camera Feed', flip_img2)
        
        # Check if the escape key was pressed
        k = cv2.waitKey(10)
        if k == 27: # Exit loop if escape was pressed
            break
    else:
        break

# Exit Cleanup
camera.release()
cv2.destroyAllWindows()
