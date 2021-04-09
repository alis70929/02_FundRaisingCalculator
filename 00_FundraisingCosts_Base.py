def num_check(question, error, num_type):
    valid = False
    while not valid:
        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


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


# ***************** Main Routine **************
for item in range(0, 6):
    want_help = yes_no("Do you want to read the instructions: ")
    print("You said {}".format(want_help))

get_int = num_check("How many do you need? ",
                    "Please enter a whole number more than 0 \n",
                    int)

get_cost = num_check("How much does it cost? ",
                     "Please enter an amount more than 0 \n",
                     float)
