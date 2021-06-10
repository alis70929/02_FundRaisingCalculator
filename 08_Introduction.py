# checks if answer is yes or no
def yes_no(question):
    to_check = ["yes", "no"]

    valid = False
    while not valid:

        response = input(question).lower()

        for item in to_check:
            if response == item:
                return item
            elif response == item[0]:
                return item

        print("Please enter yes or no")


def instructions():
    show_help = 'invalid choice'
    while show_help == 'invalid choice':
        show_help = input("Do you want to read the instructions: ")
        show_help = yes_no(show_help)

        if show_help == "Yes":
            print("****** Instructions ******* ")
            print("To use this program you must - ")
            print(" - put in a customers name")
            print(" - put in a customers age")
            print(" - while entering snacks type in xxx or n to finish inputting snacks ")
            print(" - put number of snacks wanted infront of of that snack \n E.g 2 pita chips")
            print(" - then enter whether the user is paying with cash or credit")
            print(" when finished inputting customers type in xxx to finish \n the program will show you a short summary and put all inputted customer data in a .csv file")
            print()
            input("press enter to continue")


instructions()
