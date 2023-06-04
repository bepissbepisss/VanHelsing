import random
enemies = ['WJ', 'PQ', 'JVA', 'SP', 'JA', 'C', 'gus', 'MY', 'bear', 'Ifs', 'Ia', 'Is']

#This function determines which enemie you will fight
key = 0
def bruh():
    key = random.randrange(0, len(enemies))


#This function copies over the chosen enemies dictionary to the dictionary that we're going to use in our applications

def dict_copy(a):
    a += 1
    return a

bruh()
print(key)
print(dict_copy(key))
