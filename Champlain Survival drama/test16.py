bread = 5
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
def amount(x):
    pay_for = input(bcolors.OKCYAN + 'How many do you want to buy?' + bcolors.ENDC)
    if isinstance(int(pay_for), int):
        cost = int(pay_for) * x
        print(cost)

amount(bread)
