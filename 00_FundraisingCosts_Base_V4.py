import pandas


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


def get_expenses(var_fixed):
    item_list = []
    quantity_list = []
    price_list = []

    expenses_dict = {

        'Item Name': item_list,
        'Quantity': quantity_list,
        'Price': price_list,
    }

    item_name = ""
    while item_name != "xxx":
        print()

        item_name = not_blank("Item name: ",
                              "The component name can't be blank")

        if item_name.lower() == "xxx":
            break

        if var_fixed == "variable":

            quantity = num_check("Quantity: ",
                                 "The amount must be a whole number greater than zero",
                                 int)
        else:
            quantity = 1

        price = num_check("Price:",
                          "The amount must be greater than zero",
                          float)

        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)

    expenses_frame = pandas.DataFrame(expenses_dict)
    expenses_frame = expenses_frame.set_index('Item Name')

    expenses_frame['Cost'] = expenses_frame['Quantity'] * expenses_frame['Price']

    expenses_sub = expenses_frame['Cost'].sum()

    add_dollars = ['Price', "Cost"]
    for item in add_dollars:
        expenses_frame[item] = expenses_frame[item].apply(currency)

    return [expenses_frame, expenses_sub]


def currency(x):
    return '${:.2f}'.format(x)


def not_blank(question, error_message):
    valid = False

    while not valid:
        response = input(question)
        if response != "":
            return response
        else:
            print(error_message)


def display_frame(heading, frame, sub_total):
    print()
    print("**** {} ****".format(heading))
    print()
    print(frame)
    print()
    print("Sub Total: ${:.2f}".format(sub_total))


# ***************** Main Routine **************
want_help = yes_no("Do you want to read the instructions: ")
print("You said {}".format(want_help))

product_name = not_blank("Product name: ",
                         "The product name can't be blank")

# Get Variable Costs
print()
print("**** Variable Costs *****")
variable_cost_data = get_expenses("variable")
variable_cost_frame = variable_cost_data[0]
variable_cost_sub = variable_cost_data[1]

have_fixed = yes_no("Do you have fixed costs (y/n)")
if(have_fixed == yes):
    # get fixed costs
    print()
    print("**** Fixed Costs *****")
    fixed_cost_data = get_expenses("fixed")
    fixed_cost_frame = fixed_cost_data[0]
    fixed_cost_sub = fixed_cost_data[1]
else:
    fixed_cost_sub = 0

print()
print("**** {} ****" .format(product_name))
print()
# Variable Cost
display_frame("Variable Costs", variable_cost_frame, variable_cost_sub)

if(have_fixed == yes):
    # Fixed Cost Display
    display_frame("Fixed Costs", fixed_cost_frame[['Cost']], fixed_cost_sub)

# Total
print()
total_expenses = fixed_cost_sub + variable_cost_sub
print("Total Expenses: ${:.2f}".format(total_expenses))
