import string
import random
import re
import copy

keychain = {}

monsters = {
    "dic1" : {"name":"dic1", "var1":1, "var2":1},
    "dic2" : {"var1":1, "var2":1},
    "dic3" : {"var1":1, "var2":1},
    "dic4" : {"var1":1, "var2":1},
}

dic1 = {'var1' : 1,
        'var2' : 2}

dic2 = {}

dic3 = {'var1' : 3,
        'var2' : 4}
def rand():
    key = random.randrange(1,3)
    if key == 1:
        keychain['key1'] = 1
    elif key == 2:
        keychain['key2'] = 2

def change():
    dic2['var1'] += 1

def rand2():
    keyIdx = random.randrange(0, len(monsters))
    key = list(monsters.keys())[keyIdx]
    return key

rand()
if 'key1' in keychain:
    dic2 = dic1.copy()
elif 'key2' in keychain:
    dic2 = dic3.copy()

print (dic2)
change()
print (dic2)
print (rand2())
