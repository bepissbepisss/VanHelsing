import random
enemies = ['WJ', 'PQ', 'JVA', 'SP', 'JA', 'C', 'gus', 'MY', 'bear', 'Ifs', 'Ia', 'Is']

#This function determines which enemie you will fight

def random_monster():
    key = random.randrange(0, len(enemies))
    return key

#This function copies over the chosen enemies dictionary to the dictionary that we're going to use in our applications

def dict_copy(a):
    a += 1
    return a

print(random_monster())
print(dict_copy(random_monster()))
