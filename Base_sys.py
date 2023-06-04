import os


run = True
menu = True
play = False
rules = False


        # x = 0    x = 1       x = 2      x = 3        x = 4
map = [['forest'],['forest'],['forest'],['mountain'],['mountain'], # y = 0
        ['forest'],['forest'],['forest'],['forest'],['mountain'],  # y = 1
        ['forest'],['forest'],['plains'],['plains'],['hills'],     # y = 2
        ['plains'],['plains'],['plains'],['plains'],['hills'],     # y = 3
        ['river'],['river'],['bridge'],['river'],['river'],        # y = 4
        ['fields'],['fields'],['town'],['shop'],['forest'],        # y = 5
        ['plains'],['fields'],['plains'],['forest'],['mountain']]  # y = 6


HP = 100
max_HP = 100
ATK = 20
POTION = 0
GOLD = 50
x_len = len(map) - 1
y_len = len(map[0]) - 1
x = 0
y = 0
location = map[y][x]



biom = {
    'forest' : {
        'text' : "FOREST",
        'enemies' : True},
    'plains' : {
        'text' : "PLAINS",
        'enemies' : True},
    'mountain' : {
        'text' : "MOUNTAIN",
        'enemies' : True},
    'hills' : {
        'text' : "HILLS",
        'enemies' : False},
    'river' : {
        'text' : "RIVER",
        'enemies' : True},
    'bridge' : {
        'text' : "BRIDGE",
        'enemies': False},
    'town' : {
        'text' : "TOWN",
        'enemies' : False},
    'fields' : {
        'text' : "FIELDS",
        'enemies' : False},
    'shop' : {
        'text' : "SHOP",
        'enemies' : False},
}

location_name = biom[location]['text']
location_enemy_status = biom[location]['enemies']

def draw():
    print('<~|-------------------------------------------------|~>')

def clear():
    os.system("cls")

def save():
    list = [
        name,
        str(HP),
        str(max_HP),
        str(ATK),
        str(POTION),
        str(GOLD),
        str(location),
        str(x),
        str(y),
    ]

    f = open("load.txt", "w")

    for item in list:
        f.write(item + "\n")
    f.close()


while run:
    while menu:
        clear()
        draw()
        print(location)
        print(location_name)
        print(location_enemy_status)
        print('1 -- New Game')
        print('2 -- Load Game')
        print('3 -- Rules')
        print('4 -- Quit')
        draw()


        if rules:
            clear()
            draw()
            print('Don\'t break the fucking game please')
            draw()
            rules = False
            choice = ''
        else:
            choice = input('> ')


        if choice == '1':
            clear()
            draw()
            name = input('> what\'s your name bozo?\nName: ')
            menu = False
            play = True

        elif choice == '2':
            f = open("load.txt", "r")
            load_list = f.readlines()
            name = load_list[0][:-1]
            HP = load_list[1][:-1]
            max_HP = load_list[2][:-1]
            ATK = load_list[3][:-1]
            POTION = load_list[4][:-1]
            GOLD = load_list[5][:-1]
            location = load_list[6][:-1]
            clear()
            draw()
            print ('You\'re back ""' + name + '"", finally...')
            print('here are your stats btw, not very impressive just saying')
            print('-HP:' + HP + '/' + max_HP + ' -ATK:' + ATK + ' -POTION:' + POTION + ' -GOLD:' + GOLD + ' -LOCATION:' + location)  #there's a syntax error here IDK why though, something to do with the location. ' -LOCATION:' + location)
            draw()
            input('> Press ENTER to return to menu...')

        elif choice == '3':
            rules = True

        elif choice == '4':
            quit()


    while play:
        save() #autosave
        clear()

        draw()
        print("LOCATION: " + biom[map[x][y]]["text"])
        draw()

        print("NAME: " + name)
        print("HP: " + str(HP) + "/" + str(max_HP))
        print("ATK: " + str(ATK))

        direct = input('> ')
        print(location) # I need to figure out how tf to make the position change in the map
        # also make sure I can check that the location has actually changed
        if direct == 'left':
            if x_position == 0:
                x_position = 4
                save()
            else:
                x_position -= 1
                save()

        elif direct == 'right':
            if x_position == 4:
                x_position = 0
                save()
            else:
                x_position +=1
                save()

        elif direct == 'up':
            if y_position == 0:
                y_position = 6
                print(location)
                save()
            else:
                y_position -= 1
                save()

        elif direct == 'down':
            if y_position == 6:
                y_position = 0
                save()
            else:
                y_position += 1
                save()

        elif direct == '0':
            play = False
            menu = True
            save() #autosave
