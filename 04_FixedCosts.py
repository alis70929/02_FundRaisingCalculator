import pandas


def not_blank(question, error_message):
    valid = False

    while not valid:
        response = input(question)
        if response != "":
            return response
        else:
            print(error_message)


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


def currency(x):
    return '${:.2f}'.format(x)


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


# Main Routine
fixed_cost_data = get_expenses("fixed")
fixed_cost_frame = fixed_cost_data[0]
fixed_cost_sub = fixed_cost_data[1]

print(fixed_cost_frame[['Cost']])
print()
print("Sub Total: ${:.2f}".format(fixed_cost_sub))
