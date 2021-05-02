# functions go here

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

# Gets how much profit is wanted
def profit_goal(total_costs):

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
            print (error)

        if profit_type == "unknown" and amount >= 100:
            dollar_type = yes_no("Do you mean ${:.2f}. ie {:.2f} dollars? (Y/N)".format(amount,amount))

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
            goal = (amount/100) * total_costs
            return goal


all_costs = 200
for item in range(0,6):
    
    profit_target = profit_goal(all_costs)
    print("Profit Target ${:.2f}".format(profit_target))
    print("Target Sales ${:.2f}".format(all_costs + profit_target))
