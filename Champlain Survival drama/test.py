stringvar = "mod"
dictvar = {'key1': 1,
           'key2': 2}

def foo():
    dictvar['key1'] += 1

def bar():
    global stringvar
    stringvar = "bar"
    print(stringvar)

print(dictvar)
foo()
print(dictvar)

print(stringvar)
bar()
print(stringvar)
