##### Calculator V.1

## MAKE EXCEPTION HANDLING FOR EVERYTHING
print("Overly Engineered Calculator v1.4")
print("Square root can only affect single numbers, exponents also only affect single numbers")
input("Accept: ")
print("")
print("")
print("")

while True:
    import math
    # Setting up variables/list for use. Using list so user can add as many values as necessary
    
    historyList = []
    while True:
        nums = []       

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
                numIn = input("Choose operator to use. Ex. +, /, *, -, ^2, Square root: ")
                if numIn == "+":
                    for i in range(len(nums[1:])):
                        finalCalc = finalCalc + nums[i+1]
                    print("Answer: ", finalCalc)
                    historyList.append(float(finalCalc))
                    break
                elif numIn == "/":  
                    for i in range(len(nums[1:])):
                        finalCalc = finalCalc / nums[i+1]
                    print("Answer: ", finalCalc)
                    historyList.append(float(finalCalc))
                    break
                elif numIn == "*" or numIn.lower() == "x":  
                    for i in range(len(nums[1:])):
                        finalCalc = finalCalc * nums[i+1]
                    print("Answer: ", finalCalc)
                    historyList.append(float(finalCalc))
                    break
                elif numIn == "-":  
                    for i in range(len(nums[1:])):
                        finalCalc = finalCalc - nums[i+1]
                    print("Answer: ", finalCalc)
                    historyList.append(float(finalCalc))
                    break
                elif numIn == "^2":
                    print("What power would you like to raise to?")
                    power = float(input(""))
                    finalCalc = nums[0]
                    finalCalc = finalCalc ** power
                    print("Answer: ", finalCalc)
                    historyList.append(float(finalCalc))
                    break
                elif numIn.lower() == "square root" or numIn.lower() == "sqrt" or numIn.lower() == "sqr rt" or numIn.lower() == "sqr root":
                    finalCalc = math.sqrt(nums[0])
                    print("Answer: ", finalCalc)
                    historyList.append(float(finalCalc))
                    break
                else:
                    print("Sorry, you did not enter an accepted operator. Try again.")
                    print(nums)                   
               
            # History functionality to see previous answers. Make show nums and operators used in future.            
            print("Type 1 to see a history of previous calculations.")
            print("Type anything else to continue.")
            history = input("")
            if history == "1":
                print(historyList[0:])            
            break
                
            ## Make a dictionary to retain the numbers and opperator used for calculation with the finalCalc?





