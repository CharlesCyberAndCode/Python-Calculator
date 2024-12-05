##### Calculator V.1
import math
import tkinter as tk
from tkinter import *
import sys
from PIL import ImageTk
## MAKE EXCEPTION HANDLING FOR EVERYTHING

# GUI

window = tk.Tk()
window.title("Charles' Calculator")
canvas= tk.Canvas (window , width = 300 , height = 600 , bg = "light blue")
image = ImageTk.PhotoImage(file = r"C:\python\Calculator\GUI Calculator\test.png")
canvas.create_image(150, 450, image = image)
canvas.pack()

# Globals

historyList = []
nums = []
currentNum = 0
# Functions for calculations
def addition():
    for i in range(len(nums[1:])):
        finalCalc = finalCalc + nums[i+1]
        print("Answer: ", finalCalc)
        historyList.append(float(finalCalc))

def subtraction():
    for i in range(len(nums[1:])):
        finalCalc = finalCalc - nums[i+1]
        print("Answer: ", finalCalc)
        historyList.append(float(finalCalc))

def multiply():
    for i in range(len(nums[1:])):
        finalCalc = finalCalc * nums[i+1]
        print("Answer: ", finalCalc)
        historyList.append(float(finalCalc))

def division():
    for i in range(len(nums[1:])):
        finalCalc = finalCalc / nums[i+1]
        print("Answer: ", finalCalc)
        historyList.append(float(finalCalc))

def exponent():
    power = float(input(""))
    finalCalc = nums[0]
    finalCalc = finalCalc ** power
    print("Answer: ", finalCalc)
    historyList.append(float(finalCalc))

def sqrt():
    finalCalc = math.sqrt(nums[0])
    print("Answer: ", finalCalc)
    historyList.append(float(finalCalc))

def Plus():
    t

def Subtract():
    t

def Multiply():
    t

def Divide():
    t

def Square():
    t

def Squareroot():
    t

def Quit(evnet):
    sys.exit()

# Buttons etc.

addButton = tk.Button(window , text = " + " , command = Plus)
addButton.pack(padx=5)

subtractButton = tk.Button(window , text = " - " , command = Subtract)
subtractButton.pack(padx=5)

multiplyButton = tk.Button(window , text = " * " , command = Multiply)
multiplyButton.pack(padx=5)

divideButton = tk.Button(window , text = " / " , command = Divide)
divideButton.pack(padx=5)

squareButton = tk.Button(window , text = " ^2 " , command = Square)
squareButton.pack(padx=5)

squareRootButton = tk.Button(window , text = " √ " , command = Squareroot)
squareRootButton.pack(padx=5)

addButtonWindow = canvas.create_window(20 , 75 , window = addButton)
subtractButtonWindow = canvas.create_window(43 , 75 , window = subtractButton)
multiplyButtonWindow = canvas.create_window(64 , 75 , window = multiplyButton)
divideButtonWindow = canvas.create_window(85 , 75 , window = divideButton)
squareButtonWindow = canvas.create_window(110 , 75 , window = squareButton)
sqrtButtonWindow = canvas.create_window(136 , 75 , window = squareRootButton)
# addButtonWindow = canvas.create_window(145 , 75 , window = addButton)
# addButtonWindow = canvas.create_window(12 , 75 , window = addButton)


##### KEYBOARD FUNCTIONS IN CANVAS

canvas.bind("<Escape>" , Quit)
canvas.bind("" , )
canvas.bind("" , )
canvas.bind("" , )
canvas.bind("" , )
canvas.bind("" , )
canvas.bind("" , )
canvas.bind("" , )

canvas.focus_set()


while True:
    # Setting up variables/list for use. Using list so user can add as many values as necessary
    
    while True:       

# Allows user to input as many numbers as they like, del/delete upper or lower will delete last number
# Allows user to enter 0 to progress to doing calculation
        while True:
            inputNum1 = 1
            while inputNum1 != "":
                print("Choose a number to input")
                print("To delete last number type 'delete' or 'del'")
                print("To continue to calculation hit enter")
                inputNum1 = (input("")) 
                #"Backspace function"
                if inputNum1.lower() == "del" or inputNum1.lower() == 'delete':
                    nums.pop()
                    print(nums)
                # Allows user to move on to calculation.
                elif (inputNum1 == ""): 
                    break
                # Adds number entered into the 'nums' list for later use
                elif True:
                    nums.append(float(inputNum1))
                    print(nums)
            
            # Declaring after setting up nums list so no exceptions
            finalCalc = nums[0] 
            
            # Calculation functionality seperated by opperator      
            while True:
            
                
                print("Sorry, you did not enter an accepted operator. Try again.")
                print(nums)   
                break                
               
            # History functionality to see previous answers. Make show nums and operators used in future.            
            print("Type 1 to see a history of previous calculations.")
            print("Type anything else to continue.")
            history = input("")
            if history == "1":
                print(historyList[0:])            
            break
                
            ## Make a dictionary to retain the numbers and opperator used for calculation with the finalCalc?




# Main Loop
window.mainloop()