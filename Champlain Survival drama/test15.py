type (1)
isinstance(1.5, int)
print(type(1))
print(isinstance(1.5, int))
print(isinstance(1.5, (int, float)))

import re
import string

thing = input('money')
if isinstance(int(thing), int) == True:
    stuff = 3 * int(thing)
    print(stuff)
