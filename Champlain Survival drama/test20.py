global thing
thing = 0

def func():
    global thing
    thing = thing + 1

print(thing)
func()
print(thing)
