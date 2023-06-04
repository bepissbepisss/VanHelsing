import re
global inventory
inventory = {}
global command
command = input

def end_game():
    action = input('Your Adventure Has Just Begun, Wanna See What Else Is There?  (y/n)')
    if re.match(r'^(yes|y|ye)$', action.lower()) != None:
        print('Great! Talk To  That Spooky Ghost, Bet He\'s Got More Stuff For Ya To Do...')
        inventory['MORE!'] = 6
        entrance()
    elif re.match(r'^(no|n|nah)$', action.lower()) != None:
        print('Fine! Have It Your Way. Hmph')
    else:
        print('Please Input A Valide Answer.')
        end_game()

def entrance():
    print('The room is dark and cold. There isn\'t much here. To your left is what seems to be a living room, there is also an intersection in the hallway in front of you.')
    action = input('?')
    if re.match(r'^(w|west|left|living_room|living room)$', action.lower()) != None:
        living_room()
    elif re.match(r'^(hallway|intersection|n|north|straight|forward)$', action.lower()) != None:
        hallway1()
    elif re.match(r'^(door|unlock|unlock door|entrance door|exit)$', action.lower()) != None:
        if 'key2' in inventory:
            inventory.pop('key2', None)
            print('<<Congragulation! You Beat The Game!>>')
            end_game()
        elif 'admin' in inventory:
            print('<<Congragulation! You Beat The Game!>>')
            end_game()
        else:
            print('<<Requires Key>>')
            entrance()
    else:
        print('Please Input A Valide Answer.')
        entrance()

def living_room():
    print('There is a door leading to the basement and a staircase leading up to the second floor. Behind you is the entrance.')
    action = input('?')
    if re.match(r'^(staircase|upstairs|second floor|second_floor|up)$', action.lower()) != None:
        second_floor_LR()
    elif re.match(r'^(s|south|back|entrance|backwards)$', action.lower()) != None:
        entrance()
    elif re.match(r'^(use key|key|unlock|basement|right|east|e|down)$', action.lower()) != None:
        if 'key1' in inventory:
            print("<<You Unlocked The Basement Door!>>")
            basement()
        elif 'admin' in inventory:
            print("<<You Unlocked The Basement Door!>>")
            basement()
        else:
            print("<<Requires Key>>")
            living_room()
    else:
        print('Please Input A Valide Answer.')
        living_room()

def hallway1():
    print('The hallway splits off into an intersection. To your right is the kitchen, however going straight will bring you to the dining room.')
    action = input ('?')
    if re.match(r'^(n|north|straight|forward|dining room|dining_room)$', action.lower()) != None:
        dining_room()
    elif re.match(r'^(e|east|right|kitchen)$', action.lower()) != None:
        kitchen()
    elif re.match(r'^(s|south|back|entrance|backwards)$', action.lower()) != None:
        entrance()
    else:
        print('Please Input A Valide Answer.')
        hallway1()

def dining_room():
    print('In the dining room are multiple chairs, plates, utensiles, napkins, etc. One of the walls looks like it\'s got something writen on it. Left of the room is a pathway which leads to the second floor. Further more, there is a hallway that goes to the kitchen. The hallway from which you came from is behind you.')
    action = input ('?')
    if re.match(r'^(second floor|second_floor|left|west|w|up|upstairs|staircase)$', action.lower()) != None:
        second_floor_DR()
    elif re.match(r'^(kitchen)$', action.lower()) != None:
        kitchen()
    elif re.match(r'^(s|south|back|hallway|backwards|intersection)$', action.lower()) != None:
        hallway1_DR()
    elif re.match(r'^(wall|look at wall|look wall)$', action.lower()) != None:
        print('1521')
        dining_room()
    else:
        print('Please Input A Valide Answer.')
        dining_room()

def kitchen():
    print('You find broken bottles, expired food, and dead mice.There is also a cupboard, a fridge, and a drawer in the table. On the right is the hallway, and behind you is the dining room.')
    action = input('?')
    if re.match(r'^(right|e|east|hallway|intersection)$', action.lower()) != None:
        hallway1()
    elif re.match(r'^(s|south|back|backwards|dining room|dining_room)$', action.lower()) != None:
        dining_room()
    elif re.match(r'^(cupboard|open cupboard)$', action.lower()) != None:
        print('It\'s empty.')
        kitchen()
    elif re.match(r'^(fridge|open fridge)$', action.lower()) != None:
        print('It\'s empty.')
        kitchen()
    elif re.match(r'^(table|look at table)$', action.lower()) != None:
        print('It\'s empty.')
        kitchen()
    elif re.match(r'^(drawer|open drawer)$', action.lower()) != None:
        print('There is a key')
        action1 = input('?')
        if re.match(r'^(pick up key|key|take key)$', action1.lower()) != None:
            inventory["key1"] = 1
            print("<<You Picked Up A Key!>>")
            kitchen()
        else:
            print('Please Input A Valide Answer.')
            kitchen()
    else:
        print('Please Input A Valide Answer.')
        kitchen()

def second_floor_DR():
    print('The hallway on the second has stairs on the right going to the attic, and stairs on the left leading to the living room. There is also a fuse box.')
    action = input('?')
    if re.match(r'^(right|e|east|attic|up|upstairs|staircase)$', action.lower()) != None:
        attic_DR()
    elif re.match(r'^(left|west|w|living_room|living room)$', action.lower()) != None:
        living_room()
    elif re.match(r'^(fusebox|fuse box)$', action.lower()) != None:
        print('You take a better look, the fuse box appears to be broken.')
        action1 = input('?')
        if re.match(r'^(fusebox|fuse box|use|fix)$', action1.lower()) != None:
            if 'Tape' in inventory:
                inventory.pop('Tape', None)
                print("<<You Fixed The Fuse Box!>>")
                inventory['power'] = 2
                print('The moment you fix the box, the house comes to life with all the lights begining to turn on.')
                second_floor_DR()
            elif 'power' in inventory:
                print('The fuse box is already fixed.')
                second_floor_DR()
            elif 'admin' in inventory:
                print("<<You Fixed The Fuse Box!>>")
                inventory['power'] = 2
                print('The moment you fix the box, the house comes to life with all the lights begining to turn on.')
                second_floor_DR()

            else:
                print("<<Requires Tape>>")
                second_floor_DR()
    else:
        print('Please Input A Valide Answer.')
        second_floor_DR()

def attic_DR():
    print('The door has a number lock on it.')
    action = input('?')
    if action == '1521':
        print('<<You Unlocked The Door!>>')
        unlocked_attic()
    else:
        print('<<Requires code>>')
        second_floor_DR()

def attic_LR():
    print('The door has a number lock on it.')
    action = input('?')
    if action == '1521':
        print('<<You Unlocked The Door!>>')
        unlocked_attic()
    else:
        print('<<Requires code>>')
        second_floor_LR()

def basement():
    if 'power' in inventory:
        action = input('?')
        print('You see a ghost at the center of the room. He hasn\'t noticed you.')
        if re.match(r'^(ghost|talk|talk ghost|talk to ghoast)$', action.lower()) != None:
            spooky_ghost()
        elif re.match(r'^(up|s|south|living room|living_room|back|backwards)$', action.lower()) != None:
            living_room()
        else:
            print('Please Input A Valide Answer.')
            basement()
    elif 'admin' in inventory:
        print('You see a ghost at the center of the room. He hasn\'t noticed you.')
        if re.match(r'^(ghost|talk|talk ghost|talk to ghoast)$', action.lower()) != None:
            spooky_ghost()
        elif re.match(r'^(up|s|south|living room|living_room|back|backwards)$', action.lower()) != None:
            living_room()
        else:
            print('Please Input A Valide Answer.')
            basement()
    else:
        print('You can\'t see anything, due to the power being off.')
        action1 = input('?')
        if re.match(r'^(up|s|south|living room|living_room|back|backwards)$', action1.lower()) != None:
            living_room()
        else:
            print('Please Input A Valide Answer.')
            basement()

def second_floor_LR():
    print('The hallway on the second has stairs on the right going to the dining room, and stairs on the straight leading to the attic. There is also a fuse box.')
    action = input('?')
    if re.match(r'^(n|north|straight|attic|up|upstairs|staircase)$', action.lower()) != None:
        attic_LR()
    elif re.match(r'^(right|e|east|dining room|dining_room)$', action.lower()) != None:
        dining_room()
    elif re.match(r'^(back|backwards|s|south|living_room|living room)$', action.lower()) != None:
        living_room()
    elif re.match(r'^(fusebox|fuse box)$', action.lower()) != None:
        print('You take a better look, the fuse box appears to be broken.')
        action1 = input('?')
        if re.match(r'^(fusebox|fuse box|use|fix)$', action1.lower()) != None:
            if 'Tape' in inventory:
                inventory.pop('Tape', None)
                print("<<You Fixed The Fuse Box!>>")
                inventory['power'] = 2
                print('The moment you fix the box, the house comes to life with all the lights begining to turn on.')
                second_floor_LR()
            elif 'power' in inventory:
                print('The fuse box is already fixed.')
                second_floor_LR()
            elif 'admin' in inventory:
                print("<<You Fixed The Fuse Box!>>")
                inventory['power'] = 2
                print('The moment you fix the box, the house comes to life with all the lights begining to turn on.')
                second_floor_LR()
            else:
                print("<<Requires Tape>>")
                second_floor_LR()
    else:
        print('Please Input A Valide Answer.')
        second_floor_LR()

def hallway1_DR():
    print('The hallway splits off into an intersection. To your left is the kitchen, however going straight will bring you to the entrance.')
    action = input('?')
    if re.match(r'^(entrance|n|north|straight|forward)$', action.lower()) != None:
        entrance()
    elif re.match(r'^(w|west|left|kitchen)$', action.lower()) != None:
        kitchen()
    elif re.match(r'^(s|south|back|backwards|dining_room|dining room)$', action.lower()) != None:
        dining_room()
    else:
        print('Please Input A Valide Answer.')
        hallway1_DR()

def unlocked_attic():
    print('Cobwebs fill the room. While old boxes touch the cieling.')
    action1 = input('?')
    if re.match(r'^(back|backwards|down|second floor|s|south)$', action1.lower()) != None:
        second_floor_DR()
    elif re.match(r'^(box|old box|open box|boxes)$', action1.lower()) != None:
        print('You find tape.')
        action2 = input('?')
        if re.match(r'^(tape|take tape|take)$', action2.lower()) != None:
            inventory['Tape'] = 3
            print('<<You Obtained Tape!>>')
            unlocked_attic()
        else:
            print('Please Input A Valide Answer.')
            unlocked_attic()
    else:
        print('Please Input A Valide Answer.')
        unlocked_attic()

def spooky_ghost():
    print('The ghost appears to pocess the finnest tophat, while maintaining a moist mustash. He has a golden monocle and gives off a spooky atmosphere.')
    print('He turns around and notices you."OH! Sorry, didn\'t see you there. You must be the poor fellow who\'s been wandering this cursed house(it keeps locking the attic door even when i already unlocked iy...). Anyway, I bet you wanna get out of here eh? Well don\'t worry, I\'ve got the entrance key right here! All you have to do is answer a riddle and i\'ll give it to you. However if you get it wrong, i\'ll have to eat ya soul. Even spooky ghost such as myself get hungry sometimes ya know!"')
    spooky_ghost_riddle()

def spooky_ghost_riddle():
    print('"Anyway, do you want to hear the riddle, don\'t worry, you can come back anytime."')
    action = input('?')
    if re.match(r'^(leave|go|back|living room)$', action.lower()) != None:
        print('"Hope I see you soon!"')
        living_room()
    elif re.match(r'^(riddle|yes|continue|keep going)$', action.lower()) != None:
        print('"Alright then! So here\'s the riddle. <<Is this the best game ever? Yes or No?>>"')
        action1 = input('?')
        if re.match(r'^(yes)$', action1.lower()) != None:
            print('"Right-O! Alrght then, er ya go chap!"')
            inventory['key2'] = 4
            print('<<Entrance Key Unlocked!>>')
            living_room()
        else:
            print('"Oof mate, looks like you chose the wrong answer. Welp, looks like bottoms up for me!"')
            game_over()
    else:print('Please Input A Valide Answer.')
    spooky_ghost_riddle()

def game_over():
    print('<<GAME OVER>>')
    print('bruh')
    start()

def start():
    print('Welcome To Dungeon Adventure!')
    action = input('Would You Like To Play? <yes/no>')
    if action == 'no':
        print ('Okay, See You Soon!')
    elif action == 'yes':
        print('<<You wake up in a strange house. The door behind you is locked and you have no other way out!>>')
        entrance()
    elif action == 'admin 1521':
        print('Welcome Back Kordia -> [Kai]!')
        inventory['admin'] = 420
    else:
        print('Please Input A Valide Answer.')
        start()

start()
