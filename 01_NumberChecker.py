def intcheck(question):
    valid = False
    # Error messages

    error = "please enter a whole number greater than 0"

    while not valid:
        try:
            # Gets user input
            response = int(input(question))
            # Checks number is not below zero
            if response <= 0:
                print(error)
                print()
            else:
                return response



        # If input is not a number or is a decimal then display error
        except ValueError:
            print(error)
            print()

def NumberInRangeCheck(low, high,numtocheck):

    # Error messages
    if low is not None and high is not None: # Error message if variables are given
        error = "Please enter a whole number between {} and {} (Inclusive) ".format(low,high)
    elif low is not None and high is None: # Error message if only low variable is given
        error = "Please enter a whole number equal to or above {} ".format(low)
    elif low is not None and high is None: # Error message if only high variable is given
        error = "Please enter a whole number equal to or below {} ".format(high)
    else: # Error message if no variables are given
        error = "please enter a whole number"

    if low is not None and numtocheck < low:
        print(error)  # If its too low  display error
        return False
    # Checks number is not too high
    if high is not None and numtocheck > high:
        print(error)  # If it is too high print error
        return False
    
    return True

    
valid = False
while valid == False:
    response = float(input("Product Cost: "))
    print(response)