def main():

    def quest1():
    #Given a number n, return ```True``` if n is in the range 1..10, inclusive.
    #Unless outside_mode is ```True```, in which case return True if the number is less or equal to 1, or greater or equal to 10.
    #Print the result returned from your function.
        numinput=int(input("Please enter a number. "))
        booleaninput=input("If you believe the number is outside the scope of 1 to 10 enter 'T' for true. Otherwise enter 'F' for false. ")
        booleaninput=booleaninput.upper()
        def in1to10(number,boolean):
            if boolean == 'T':        #If they believe the number is outside the range; 'T' is used to avoid confusion with True
                if number in range(11):   #if they are wrong, return false
                    return False
                else:                   #If they are right, return true
                    return True
            elif boolean == 'F':         #If they believe their number is inside the range; 'F' is used to avoid confusion with False
                if number in range(11):
                    return True          #If they are right, return true
                else:
                    return False         #If they are wrong, return false
        # print(in1to10(5,'T'))
        # print(in1to10(5,'F'))
        # print(in1to10(10,'T'))
        print(in1to10(numinput,booleaninput))
    def quest2():
    #Create a function that has a loop that quits with the equal sign. If the user doesn't enter the equal sign, ask them to input another string.
    #Once the user enters the equal sign to quit, print all the strings that were entered as one line with each word separated by a comma and space.
        def Ihopeeveryonegetsthisright():  #function for the question
            escapeWithequal=""
            randomstring=""
            while (escapeWithequal!="="):
                escapeWithequal= input ("Please enter '=' to escape. Otherwise it will return what you input.")

                if escapeWithequal.lower()=='q': #another easter egg
                    print("Did you mean '='?")
                if escapeWithequal == "=":        #escapes loops to prevent '=' from entering the string
                    print("Do you think I copy and pasted this code?")
                else:
                    randomstring= randomstring +", " +escapeWithequal    #add strings together

            randomstring= randomstring[2:] #removes the first 2 characters; "" and ,

            print(f"You entered: \n{randomstring}")

        Ihopeeveryonegetsthisright()   #calls function

    def quest3():
    #Given a non-negative number "num", return ```True``` if num is within ```2``` of a *multiple of 10*. Print the result from your function.
    #BONUS: Get the number from User input instead of hardcoding it

        def checkWithin2():
            num = int(input ("Please enter a non-negative number, This will return true if you number is within 2 of a multiple of 10 "))
            if ((num%10==2 and num>2) or num%10==8 or num%10==9 or (num%10==1 and num>1) or num%10==0 and num>=10):
                #The First condition covers all numbers that end in 2 and are greater than 2.
                #The Second condition covers all numbers that end in 8.
                #The Third condition covers all numbers that end in 9.
                #The Forth conditions cover all numbers that end in 1 and are greater than 1.
                #The final conditions covers all numbers divisible by 10.
                return True
            else:
                return False
        print(checkWithin2())

    def quest4():
    #Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array.
    # Note: There isn't any restriction on how your approach determining what the min and max values are.
        array=[1,10,9,5,3,7]
        least=array[0] #sets the number to the first element of the array
        greatest=array[0] #sets the number to the first element of the array
        for x in range(len(array)):
            if least>array[x]:       #if there exist a number in the array less than "Least" it will replace the current "least"
                least=array[x]
        for y in range (len(array)):
            if(greatest<array[y]):    #if there exist a number in the array greather than "Greatest", it will replace the "current greatest"
                greatest=array[y]
        print(greatest-least)        #Takes the difference between the two








    quest1()
    #quest2()
    #quest3()
    #quest4()

if __name__ == '__main__':
    main()