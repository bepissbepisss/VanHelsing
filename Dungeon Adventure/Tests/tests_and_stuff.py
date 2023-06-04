global player_atk_buff
player_atk_buff = player_weapons


player_weapons = {
            'sword': 5
                }

print (player_atk_buff)







start = input('Would You Like To Play? <yes/no>')
if start == 'no':
      print ('Okay, See You Soon!')
elif start == 'yes':
    entrance = input('The room is dark and cold. There isn\' much here. To your left is what seems to be a living room, there is also an intersection in the hallway in front of you.')
    if entrance == 'w':
        living_room = input('bruh')

#It appears that when using this method of "if" statments within each other proves to be troblesaome. However there seems to be a solution for such an issue. By simply utilsing functions, we can allow the program to run without being stuck in a one way input.



def entrance():
    print('The room is dark and cold. There isn\' much here. To your left is what seems to be a living room, there is also an intersection in the hallway in front of you.')
    action = input('?')
    if action == 'living_room':
        living_room()
    elif action == 'hallway' or action == 'intersection':
        hallway1()

#Using functions seems to work fine, but since I want to make the players input work not simply as just one answer I have to make a list of "if" statements. Thsi can be reduce to a certain extent via the method of applying "or" within the statement. As shown above.


import re

def entrance():
    print('The room is dark and cold. There isn\'t much here. To your left is what seems to be a living room, there is also an intersection in the hallway in front of you.')
    action = input('?')
    if re.match(r'^(w|west|left|living_room|living room)$', action.lower()) != None:
        living_room()
    elif re.match(r'^(hallway|intersection|n|north|straight|forward)$', action.lower()) != None:
        hallway1()
    else:
        print('Please Input A Valide Answer.')
        entrance()

#This allows me to let all the answers in the brackets to be aloowed in all kinds of caps. Ex. "wheel" would be the same as if you typed "WhEel".

import re

global inventory = {}
inventory['key1'] = 1

if 'key1' in inventory:
    inventory.pop('key1', None)



def entrance():
    print('The room is dark and cold. There isn\'t much here. To your left is what seems to be a living room, there is also an intersection in the hallway in front of you.')
    action = input('?')
    if re.match(r'^(w|west|left|living_room|living room)$', action.lower()) != None:
        living_room()
    elif re.match(r'^(hallway|intersection|n|north|straight|forward)$', action.lower()) != None:
        hallway1()
    elif re.match(r'^(pick up key|key|take key)$', action.lower()) != None:
        inventory['key1'] = 1
        print("You Picked Up A Key!")
    else:
        print('Please Input A Valide Answer.')
        entrance()
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def living_room():
    print('There is a door leading to the basement and a staircase leading up to the second floor. Behind you is the entrance.')
    action = input('?')
    if re.match(r'^(staircase|upstairs|second floor|second_floor|up)$', action.lower()) != None:
        second_floor_LR()
    elif re.match(r'^(s|south|back|entrance|backwards)$', action.lower()) != None:
        entrance()
    elif re.match(r'^(use key|key|unlock|basement|right|east|e|down)$', action.lower()) != None:
        if 'key1' in inventory:
            inventory.pop('key1', None)
            print("You Unlocked The Basement Door!")
            basement()
        else:
            print("Requires Key")
            living_room()
    else:
        print('Please Input A Valide Answer.')
        living_room()
