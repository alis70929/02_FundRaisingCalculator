import math 

# rounds up to multiple of round_to
def round_up(amount, round_to):
    return int(math.ceil(amount/round_to)) * round_to
    

print(round_up(1,4))
