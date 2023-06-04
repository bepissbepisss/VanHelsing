import string
import random
import re
import copy

keychain = {}

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

def func(a, b):
    if 'key1' in keychain:
        dic2 = a.copy()
        return dic2
    elif 'key2' in keychain:
        dic2 = b.copy()
        return dic2

rand()
print (dic2)
print (func(dic1, dic3))
print (dic2)
