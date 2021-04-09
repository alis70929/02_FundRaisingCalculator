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


for item in range(0, 6):
    want_help = yes_no("Do you want to read the instructions: ")
    print("You said {}".format(want_help))