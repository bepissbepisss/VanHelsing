import string
import random
import re
import copy


monsters = {}
dic1 = {"name":"dic1", "var1":1, "var2":2}

dic2 = {"name":"dic2", "var3":3, "var4":4}

dic3 = {'dic3':'val1'}

dic4 = {'dic4':'val2'}

monsters = {**dic1, **dic2, **dic3, **dic4}

res = key, val = random.choice(list(monsters.items()))

print(res)
