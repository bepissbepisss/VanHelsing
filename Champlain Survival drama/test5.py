dic1 = {'var1':1,
        'var2':2}

dic2 = {'var3':3,
        'var4':4}

dest = {**dic1, **dic2}

def change():
    dic1['var1'] += 1

print(dest) #dic merged
change() #var1 value change
print(dest) #var1 vale doesn't change in this dictionary, because the change happened after the dictioanry was assigned
print(dic1) #value has changed
dest = {**dic1, **dic2} #reassigne the new dictioanry
print(dest) #the value changed
