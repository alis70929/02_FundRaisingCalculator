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


item_list = []
quantity_list = []
price_list = []

variable_cost_dict = {

    'Item Name': item_list,
    'Quantity': quantity_list,
    'Price': price_list,

}

product_name = not_blank("Product name: ",
                         "The product name can't be blank")

item_name = ""
while item_name != "xxx":
    print()

    item_name = not_blank("Item name: ",
                          "The component name can't be blank")

    if item_name.lower() == "xxx":
        break

    quantity = num_check("Quantity: ",
                         "The amount must be a whole number greater than zero",
                         int)
    price = num_check("Price:",
                      "The amount must be greater than zero",
                      float)

    item_list.append(item_name)
    quantity_list.append(quantity)
    price_list.append(price)

variable_cost_frame = pandas.DataFrame(variable_cost_dict)
variable_cost_frame = variable_cost_frame.set_index('Item Name')

variable_cost_frame['Cost'] = variable_cost_frame['Quantity'] * variable_cost_frame['Price']

variable_cost_sub = variable_cost_frame['Cost'].sum()

add_dollars = ['Price', "Cost"]
for item in add_dollars:
    variable_cost_frame[item] = variable_cost_frame[item].apply(currency)

print(variable_cost_frame)
print()
print("Sub Total: ${:.2f}".format(variable_cost_sub))
