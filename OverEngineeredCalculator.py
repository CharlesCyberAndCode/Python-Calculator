##### Calculator V.1

## MAKE EXCEPTION HANDLING FOR EVERYTHING
while True:
    # Setting up variables/list for use. Using list so user can add as many values as necessary
    
    historyList = []
    while True:
        nums = []       

# Allows user to input as many numbers as they like, del/delete upper or lower will delete last number
# Allows user to enter 0 to progress to doing calculation
        while True:
            inputNum1 = 1
            while inputNum1 != 0:
                print("Choose a number to input")
                print("To delete last number type 'delete' or 'del'")
                print("To continue to calculation type 0")
                inputNum1 = (input("")) 
                #"Backspace function"
                if inputNum1.lower() == "del" or inputNum1.lower() == 'delete':
                    nums.pop()
                    print(nums)
                # Allows user to move on to calculation.
                elif (inputNum1 == "0"): 
                    break
                # Adds number entered into the 'nums' list for later use
                elif True:
                    nums.append(float(inputNum1))
                    print(nums)
            
            # Declaring after setting up nums list so no exceptions
            finalCalc = nums[0] 
            
            # Calculation functionality seperated by opperator      
            while True:
                math = input("Choose operator to use. Ex. +, /, *, -: ")
                if math == "+":
                    for i in range(len(nums[1:])):
                        finalCalc = finalCalc + nums[i+1]
                    print("Answer: ", finalCalc)
                    historyList.append(float(finalCalc))
                    break
                elif math == "/":  
                    for i in range(len(nums[1:])):
                        finalCalc = finalCalc / nums[i+1]
                    print("Answer: ", finalCalc)
                    historyList.append(float(finalCalc))
                    break
                elif math == "*" or math == "x":  
                    for i in range(len(nums[1:])):
                        finalCalc = finalCalc * nums[i+1]
                    print("Answer: ", finalCalc)
                    historyList.append(float(finalCalc))
                    break
                elif math == "-":  
                    for i in range(len(nums[1:])):
                        finalCalc = finalCalc - nums[i+1]
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





