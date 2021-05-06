import math

# rounds up to multiple of round_to
def round_up(amount, var_round_to):
    amount = int(math.ceil(amount/round_to) * round_to)
    return amount

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
    
# main routine
how_many = 50
total = 200
profit_goal = 100
round_to = 5

sales_needed = total + profit_goal

print("Total: ${:.2f}".format(total))
print("Profit Goal: ${:.2f}".format(profit_goal))

selling_price = sales_needed/how_many
print("Selling Price (Unrounded): ${:.2f}".format(selling_price))

recommended_price = round_up(selling_price,round_to)
print("Recommended Price: ${:.2f}".format(recommended_price))
