import string
import random
import re
import copy




monsters = {
    "dic1" : {"name":"dic1", "var1":1, "var2":2},
    "dic2" : {"name":"dic2", "var3":3, "var4":4}
    }
keyIdx = random.randrange(0, len(monsters))
key = dict(monsters.keys())[keyIdx]

print(key)
