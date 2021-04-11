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

    'Item Name' = item_list,
    'Amount' = quantity_list,
    'Price' = price_list,

}

product_name = not_blank("Product name: ",
                         "The product name can't be blank")

item_name = ""
while item_name != "xxx":
    print()

    item_name = not_blank("Item name: ",
                          "The component name can't be blank")

    if item.name.lower() = "xxx":
        break

        amount = num_check("Amount: ",
                           "The amount must be a whole number greater than zero",
                           int)
        price = num_check("Price:",
                          "The amount must be greater than zero",
                          float)

        item_list.appen

