import re
import string

thing = input('money')
if re.match(r'^(5)$', thing.lower()) != None:
    stuff = 3 * int(thing)
    print(stuff)
