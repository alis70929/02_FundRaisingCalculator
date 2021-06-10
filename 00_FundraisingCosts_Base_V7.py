import math
import pandas


# loops till number is valid(integer or float) and greater than 0
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


# loops till response is yes or no
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


# Get variable or fixed costs from user
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


# Currency formatting function
def currency(x):
    return '${:.2f}'.format(x)


# lopps till answer is not blank
def not_blank(question, error_message):
    valid = False

    while not valid:
        response = input(question)
        if response != "":
            return response
        else:
            print(error_message)


# Formatting data frames(returns a string)
def format_frame(var_heading, frame, sub_total):
    heading = "**** {} ****\n\n".format(var_heading)
    frame = pandas.DataFrame.to_string(frame)
    sub_total = "\nSub Total: ${:.2f}\n\n".format(sub_total)

    return heading + frame + sub_total


# rounds up to multiple of round_to
def round_up(var_amount, var_round_to):
    amount = int(math.ceil(var_amount / var_round_to) * var_round_to)
    return amount


# Get profit goal(% or $)
def profit_goal(total_costs):

    error = "Please enter a valid profit goal \n"
    valid = False
    while not valid:

        response = input("What is your profit goal (eg $500 or 50%)")

        if response[0] == "$":
            profit_type = "$"
            amount = response[1:]

        elif response[-1] == "%":
            profit_type = "%"
            amount = response[:-1]

        else:
            profit_type = "unknown"
            amount = response

        try:
            amount = float(amount)

            if amount <= 0:
                print(error)

        except ValueError:
            print(error)
            continue

        if profit_type == "unknown" and amount >= 100:
            dollar_type = yes_no("Do you mean ${:.2f}. ie {:.2f} dollars? (Y/N)".format(amount, amount))

            if dollar_type == "yes":
                profit_type = "$"
            else:
                profit_type = "%"
        elif profit_type == "unknown" and amount < 100:
            dollar_type = yes_no("Do you mean {:.2f}%. (Y/N)".format(amount))

            if dollar_type == "yes":
                profit_type = "%"
            else:
                profit_type = "$"

        if profit_type == "$":
            return amount
        else:
            goal = (amount / 100) * total_costs
            return goal


# formats strings with **** surronding them
def heading_format(text_to_format):
    return "****{}****".format(text_to_format)


# Asks user iif they want to read thge intstuctions
def instructions():
    show_help = 'invalid choice'
    while show_help == 'invalid choice':
        show_help = "Do you want to read the instructions: "
        show_help = yes_no(show_help)

        if show_help == "yes":
            print("****** Instructions ******* ")
            print(" Intructions go here")
            input("\npress enter to continue")


# ***************** Main Routine **************
instructions()

product_name = not_blank("Product name: ",
                         "The product name can't be blank")

how_many = num_check("How many items will you be producing",
                     "The number of items must be a whole number greater than 0 ", int)
# Get Variable Costs
print()
print("**** Variable Costs *****")
# get variable costs
variable_cost_data = get_expenses("variable")
variable_cost_frame = variable_cost_data[0]
variable_cost_sub = variable_cost_data[1]

# Ask if user has fixed costs
have_fixed = yes_no("Do you have fixed costs (y/n)")
if(have_fixed == "yes"):
    # get fixed costs
    print()
    print("**** Fixed Costs *****")
    # Get fixed costs list(dataframe, subtotal)
    fixed_cost_data = get_expenses("fixed")
    # get dtata frame from list
    fixed_cost_frame = fixed_cost_data[0]
    # gets subtotal from list
    fixed_cost_sub = fixed_cost_data[1]
else:
    # Sets fixed sub total to zero for later calculations
    fixed_cost_sub = 0

# work out total costs and profit target
total_expenses = fixed_cost_sub + variable_cost_sub
profit_target = profit_goal(total_expenses)

# calculate total sales needed
sales_needed = total_expenses + profit_target

# Ask user for rounding
round_to = num_check("Round to nearest...? $",
                     "Cant be 0 or lower",
                     int)

# Get how many each thing you sell will have to sell for(bare minimum)
selling_price = sales_needed / how_many

# get recomended price
Recommended_price = round_up(selling_price, round_to)

# Format stuff for printing/writing to file
heading = heading_format(product_name)
total_expenses_sentence = "Total Expenses: {:.2f}".format(total_expenses)
profit_target_sentence = "Profit Target: {:.2f}".format(profit_target)
sales_needed_sentence = "Required Sales: {:.2f}".format(sales_needed)
recommended_price_sentence = "Recommended Sales: {:.2f}".format(Recommended_price)

# Chnage data frame to string so it can be written to txt file with proper formatting
variable_cost_txt = format_frame("Variable Costs", variable_cost_frame, variable_cost_sub)
if have_fixed == "yes":
    fixed_cost_txt = format_frame("Fixed Cost", fixed_cost_frame, fixed_cost_sub)
else:
    fixed_cost_txt = heading_format("No Fixed Costs")

# store what you want to print/write to file
to_write = [heading,
            variable_cost_txt,
            fixed_cost_txt,
            total_expenses_sentence,
            profit_target_sentence,
            sales_needed_sentence,
            recommended_price_sentence]

# Wirte to file
# create file to hold data add .txt extension
file_name = "{}.txt".format(product_name)
text_file = open(file_name, "w+")

# write items to file
for item in to_write:
    text_file.write(item)
    text_file.write("\n")

# Close Text File
text_file.close()

# Print the items
for item in to_write:
    print(item)
