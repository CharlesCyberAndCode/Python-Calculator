while True:
    ## Calculator V.1

    # Setting up variables/list for use. Using list so user can add as many values as necessary
    
    historyList = []
    while True:
        nums = []       
        #FIX THIS LATER OR YOURE A DICKHEAD
        #try:
       
        
        lengthOfCalc = int(input("How many numbers will you be using? "))
        #except ValueError:
        ### print("Must use numbers to enter value.")
        

        # This adds the user input into the list for use later.
        for i in range (lengthOfCalc):
            nums.append(float(input("Choose Number: "))) 
            print(nums[0:])

        #Declaring after setting up nums list
        finalCalc = nums[0]



        
           
        while True:
            math = input("Choose operator to use. Ex. +, /, *, -: ")
            if math == "+":
                for i in range(len(nums[1:])):
                    finalCalc = finalCalc + nums[i+1]
                print(finalCalc)
                historyList.append(int(finalCalc))
                break
            elif math == "/":  
                for i in range(len(nums[1:])):
                    finalCalc = finalCalc / nums[i+1]
                print(finalCalc)
                historyList.append(int(finalCalc))
                break
            elif math == "*" or math == "x":  
                for i in range(len(nums[1:])):
                    finalCalc = finalCalc * nums[i+1]
                print(finalCalc)
                historyList.append(int(finalCalc))
                break
            elif math == "-":  
                for i in range(len(nums[1:])):
                    finalCalc = finalCalc - nums[i+1]
                print(finalCalc)
                historyList.append(int(finalCalc))
                break
            else:
                print("Sorry, you did not enter an accepted operator. Try again.")
                
        print("Would you like to see a history of previous calculations?")
        print("1. Yes")
        print("2. No")
        print("Choose a number.")
        history = input("")
        if history == "1":
            print(historyList[0:])
        ## Make a dictionary to retain the numbers and opperator used for calculation with the finalCalc?







