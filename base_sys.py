import os
import pygame
run = True
menu = True
play = False
rules = False

HP = 100
ATK = 20
POTION = 0
GOLD = 50


def clear():
    os.system("cls")

def save():
    list = [
        name,
        str(HP),
        str(ATK),
        str(POTION),
        str(GOLD)
    ]

    f = open("load.txt", "w")

    for item in list:
        f.write(item + "\n")
    f.close()


while run:
    while menu:
        clear()
        print('1 -- New Game')
        print('2 -- Load Game')
        print('3 -- Rules')
        print('4 -- Quit')


        if rules:
            clear()
            print('Don\'t break the fucking game please')
            rules = False
            choice = ''
        else:
            choice = input('>')


        if choice == '1':
            clear()
            name = input('> what\'s your name bozo?')
            menu = False
            play = True

        elif choice == '2':
            f = open("load.txt", "r")
            load_list = f.readlines()
            name = load_list[0][:-1]
            HP = load_list[1][:-1]
            ATK = load_list[2][:-1]
            POTION = load_list[3][:-1]
            GOLD = load_list[4][:-1]
            clear()
            print ('You\'re back ' + name + ', finally...')
            print('here are your stats btw, not very impressive just saying')
            print('-HP:' + HP + ' -ATK:' + ATK + ' -POTION:' + POTION + ' -GOLD:' + GOLD)

        elif choice == '3':
            rules = True

        elif choice == '4':
            quit()


    while play:
        save() #autosave

        direct = input('> ')

        if direct == '0':
            play = False
            menu = True
            save() #autosave
