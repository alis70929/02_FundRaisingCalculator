import math 

# rounds up to multiple of round_to
def round_up(amount, round_to):
    amount = int(math.ceil(amount/round_to) * round_to)
    return amount

print(round(1,30))
