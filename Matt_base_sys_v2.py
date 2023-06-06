import os
import re
import random
import copy
import string


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


#This dictionary let's me store variables to tell me wether or not the player has completed an event or not
global variable
variable = {}


#This acts as the dictionary we'll be using in our applications
global mob
mob = {}



enemies = {
    0 : {
    'name' :'WOLF',
    'min_ATK' :15,
    'max_ATK' :25,
    'hp' :100,
    'reset hp' : 100,
    'luck' :0,
    'speed' :100,
    'experience' : 10,
    'item' : 'pelt',
    'chance': 50},

    1 : {
    'name' :'BAT',
    'min_ATK' :5,
    'max_ATK' :10,
    'hp' :10,
    'reset hp' : 10,
    'luck' :0,
    'speed' :150,
    'experience' : 5,
    'item' : 'wing',
    'chance': 50},

    2 : {
    'name' :'VAMPIRE',
    'min_ATK' :20,
    'max_ATK' :30,
    'hp' :150,
    'reset hp' : 150,
    'luck' :0,
    'speed' :80,
    'experience' : 15,
    'item' : 'fangs',
    'chance': 50},

    3 : {
    'name' :'Gypsie',
    'min_ATK' :10,
    'max_ATK' :15,
    'hp' :120,
    'reset hp' : 120,
    'luck' :0,
    'speed' :50,
    'experience' : 5,
    'item' : 'cloth',
    'chance': 50},
}


#List of dictrionaries that contain enemies
enemies_list = ['wolf','bat', 'vampire','gypsie']

inventory_status = False

#function which tells the user that the shit they put don't work
def invalid():
    print ('\033[1m \033[91m \033[4m' +  "~~~PLEASE INPUT A VALID RESPONSE~~~\n" + '\033[0m')



#This dictionary is the players inventory
global inventory
inventory = {
    'cooked meat' : {
        'duration' : 0,
        'healing' : 25,
        'quantity' : 5,
        'value' : 2.5,
        'trait' : 'weapon',
        'discription' : ('I knew cooking this was a good idea!')
                    },
    'arrow' : {
        'quantity' : 30,
        'value' : 1,
        'trait' : 'ammo',
        'discription' : ('Aim for the knees!')
               },
    'cloth' : {
        'duration' : 0,
        'healing' : 10,
        'quantity' : 5,
        'value' : 5,
        'trait' : 'weapon',
        'discription' : ('A little dirty, but hey, better than nothing.')
            },
    'bandage' : {
        'duration' : 0,
        'healing' : 50,
        'quantity' : 2,
        'value' : 20,
        'trait' : 'item',
        'discription' : ('Small cut or broken arm? Doesn\'t matter, this will patch you up.')
                },
    'knife' : {
        'min_ATK' : 10,
        'max_ATK' : 20,
        'HOLY' : 0,
        'quantity' : 1,
        'value' : 20,
        'trait' : 'weapon',
        'discription' : ('The knife. Light, sharp, effective.')
                },
    'crossbow' : {
        'min_ATK' : 25,
        'max_ATK' : 30,
        'HOLY' : 0,
        'quantity' : 1,
        'value' : 12.5,
        'trait' : 'weapon',
        'discription' : ('A powerful weapon, but requires <<Arrows>> to shoot. Make sure each shot counts...')
                },
    'cross' : {
        'min_ATK' : 1,
        'max_ATK' : 1,
        'HOLY' : 40,
        'quantity' : 1,
        'value' : 20,
        'trait' : 'weapon',
        'discription' : ('Deals <<Holy Damage>>. Does increased damage to vampires, but is just a cross against anything else.')
                },
    'shield' : {
        'block' : 100,
        'quantity': 1,
        'value' : 10,
        'trait' : 'shield',
        'discription' : ('Good at keeping the scary things away.')
                },
    'meat' : {
        'duration' : 0,
        'healing' : 5,
        'quantity' : 0,
        'value' : 3,
        'trait' : 'item',
        'discription' : ('Tasty, probably best to cook it though.')
            },
    'pelt' : {
        'quantity' : 0,
        'value' : 5,
        'trait' : 'misc.',
        'discription' : ('Cozy stuff!')
            },
    'bloody rag' : {
        'duration' : 15,
        'effect' : 5,
        'quantity' : 0,
        'value' : 15,
        'trait' : 'item',
        'discription' : ('Quintuples your chances of encounter wildlife. Last for 10 forest trips before drying out, also ew.')
                            },
    'wing' : {
        'quantity' : 0,
        'value' : 10,
        'trait' : 'misc.',
        'discription' : ('A little weird carrying this around.')
                    },
    'steak' : {
        'quantity' : 0,
        'value' : 15,
        'min_ATK' : 5,
        'max_ATK' : 10,
        'HOLY' : 25,
        'trait' : 'weapon',
        'discription' : ('Don\'t eat this, it might break the game.'),
        },
    'fang' : {
        'quantity' : 0,
        'value' : 10,
        'trait' : 'misc.',
        'discription' : ('Try not to poke yourself with it.')
                },
}


#This function lets the player use items
def use(x):
    global attractor
    if inventory[x]['healing'] > 0:
        player_stat['HP'] = player_stat['HP'] +  inventory[x]['healing']
        inventory[x]['quantity'] = inventory[x]['quantity'] - 1
        print(bcolors.OKGREEN + 'You recovered ({})hp!'.format(inventory[x]['healing']) + bcolors.ENDC)
        if player_stat['HP'] >= player_stat['max_HP']:
            player_stat['HP'] = player_stat['max_HP']
            inven()
    if inventory[x]['duration'] > 0:
        attractor = attractor + inventory[x]['duration']
        inventory[x]['quantity'] = inventory[x]['quantity'] - 1
        print(bcolors.OKGREEN + 'You added ({}) worth of stacks to your wildlife attractor effect!'.format(inventory[x]['duration']) + bcolors.ENDC)
        inven()




#This function will make the xp requirement go up, reset xp accordingly, and increase player lv.
def lv_up():
    global xp
    global req
    global lv
    if int(xp) >= req:
        lv = lv + 1
        xp = xp - req
        req = req * 2
        player_stat['min_ATK'] = player_stat['min_ATK']*1.5
        player_stat['max_ATK'] = player_stat['max_ATK']*1.5
        player_stat['max_HP'] = player_stat['max_HP']*1.5
        player_stat['SPEED'] = player_stat['SPEED']*1.5
        print(bcolors.OKGREEN + 'You <<Leveled Up>>!' + bcolors.ENDC)
        print('({})atk min'.format(player_stat['min_ATK']))
        print('({})atk max'.format(player_stat['max_ATK']))
        print('({})hp'.format(player_stat['max_HP']))
        print('({})speed'.format(player_stat['SPEED']))
    drop()


def drop():
    if mob['chance'] <= random.randrange(1,101):
        print(bcolors.OKGREEN + 'You Gained (1) <<{}>>!'.format(mob['item']) + bcolors.ENDC)
        item = mob['item']
        inventory[item]['quantity'] += 1


def game_over():
    global GOLD
    print('you are dead')
    player_stat['HP'] = player_stat['max_HP']
    lost = (int(GOLD))/2
    GOLD =  int(GOLD) - lost
    print(bcolors.FAIL + 'YOU LOST ({})g'.format(lost) + bcolors.ENDC)
    world(x, y)


def inven(combat = False):
    inventory_status = True
    while inventory_status == True:
        global xp
        global req
        global lv
        variable.pop('from forest', None)
        print(bcolors.OKGREEN + 'What would You like to View?' +  bcolors.ENDC)
        action = input(bcolors.OKCYAN + '(1) <<Health>> | (2) <<Gold>> | (3) <<Overall stats>> | (4) <<Inventory>> | (5) <<Experience>> | (6) <<EXIT>>' +  bcolors.ENDC)
        if re.match(r'^(1|health)$', action.lower()) != None:
            print("HP: " + str(player_stat['HP']) + '/' + str(player_stat['max_HP']))
            inven()
        elif re.match(r'^(2|gold)$', action.lower()) != None:
            print("GOLD: " + str(GOLD))
        elif re.match(r'^(3|overall stats|stats)$', action.lower()) != None:
            print("ATK: " + str(player_stat['min_ATK']) + "(+" + str(player_stat_bonus['min_ATK_bonus']) +  ") - " + str(player_stat['max_ATK']) + "(+" + str(player_stat_bonus['max_ATK_bonus']) + ')')
            print("HOLY: " + str(player_stat['HOLY']))
            print("LUCK: " + str(player_stat['LUCK']))
            print("SPEED: " + str(player_stat['SPEED']))
            inven()
        elif re.match(r'^(5|experience)$', action.lower()) != None:
            print('({})xp'.format(xp))
            print('({})req xp'.format(req))
            print('({})lv'.format(lv))
            inven()
        elif re.match(r'^(4|inventory)$', action.lower()) != None:
            print(bcolors.OKGREEN + 'Which Item do You wish to Look at?' +  bcolors.ENDC)
            print(bcolors.OKCYAN + '(1) <<Cooked meat [{}]>>'.format(inventory['cooked meat']['quantity']) +  bcolors.ENDC)
            print(bcolors.OKCYAN + '(2) <<Arrows [{}]>>'.format(inventory['arrow']['quantity']) +  bcolors.ENDC)
            print(bcolors.OKCYAN + '(3) <Crossbow [{}]>>' .format(inventory['crossbow']['quantity']) + bcolors.ENDC)
            print(bcolors.OKCYAN + '(4) <<Bandages [{}]>>'.format(inventory['bandage']['quantity']) +  bcolors.ENDC)
            print(bcolors.OKCYAN + '(5) <<Knife [{}]>>'.format(inventory['knife']['quantity']) +  bcolors.ENDC)
            print(bcolors.OKCYAN + '(6) <<Cross [{}]>>'.format(inventory['cross']['quantity']) +  bcolors.ENDC)
            print(bcolors.OKCYAN + '(7) <<Steak [{}]>>'.format(inventory['steak']['quantity']) +  bcolors.ENDC)
            print(bcolors.OKCYAN + '(8) <<Shield [{}]>>'.format(inventory['shield']['quantity']) +  bcolors.ENDC)
            print(bcolors.OKCYAN + '(9) <<Cloth [{}]>>'.format(inventory['cloth']['quantity']) +  bcolors.ENDC)
            print(bcolors.OKCYAN + '(10) <<pelt [{}]>>' .format(inventory['pelt']['quantity'])+  bcolors.ENDC)
            print(bcolors.OKCYAN + '(11) <<Bloody Rag[{}]>>'.format(inventory['bloody rag']['quantity']) +  bcolors.ENDC)
            print(bcolors.OKCYAN + '(12) <<Wings [{}]>>'.format(inventory['wing']['quantity']) +  bcolors.ENDC)
            print(bcolors.OKCYAN + '(13) <<Fangs [{}]>>'.format(inventory['fang']['quantity']) +  bcolors.ENDC)
            print(bcolors.OKCYAN + '(14) <<Meat [{}]>>'.format(inventory['meat']['quantity']) +  bcolors.ENDC)
            specification = input(bcolors.OKCYAN + '(15) <<EXIT>>' +  bcolors.ENDC)
            if re.match(r'^(1|cooked meat)$', specification.lower()) != None:
                print(inventory['cooked meat'])
                if inventory['cooked meat']['quantity'] > 0:
                    ask = input(bcolors.OKGREEN + 'Would you like to use this item?' +  bcolors.ENDC)
                    if re.match(r'^(yes|y|yeah|sure|use|yep)$', ask.lower()) != None:
                        use('cooked meat')
                    elif re.match(r'^(no|nope|nah|n|exit|cancel|leave)$', ask.lower()) != None:
                        inven()
            elif re.match(r'^(2|arrow|arrows)$', specification.lower()) != None:
                print(inventory['arrow'])
                inven()
            elif re.match(r'^(3|crossbow)$', specification.lower()) != None:
                print(inventory['crossbow'])
                if inventory['crossbow']['quantity'] > 0:
                    ask = input(bcolors.OKGREEN + 'Would you like to equip this item?' +  bcolors.ENDC)
                    if re.match(r'^(yes|y|yeah|sure|use|yep)$', ask.lower()) != None:
                        equip('crossbow')
                    elif re.match(r'^(no|nope|nah|n|exit|cancel|leave)$', ask.lower()) != None:
                        inven()
            elif re.match(r'^(4|bandages|bandage)$', specification.lower()) != None:
                print(inventory['bandage'])
                if inventory['bandage']['quantity'] > 0:
                    ask = input(bcolors.OKGREEN + 'Would you like to use this item?' +  bcolors.ENDC)
                    if re.match(r'^(yes|y|yeah|sure|use|yep)$', ask.lower()) != None:
                        use('bandage')
                    elif re.match(r'^(no|nope|nah|n|exit|cancel|leave)$', ask.lower()) != None:
                        inven()
            elif re.match(r'^(5|knife)$', specification.lower()) != None:
                print(inventory['knife'])
                if inventory['knife']['quantity'] > 0:
                    ask = input(bcolors.OKGREEN + 'Would you like to equip this item?' +  bcolors.ENDC)
                    if re.match(r'^(yes|y|yeah|sure|use|yep)$', ask.lower()) != None:
                        equip('knife')
                    elif re.match(r'^(no|nope|nah|n|exit|cancel|leave)$', ask.lower()) != None:
                        inven()
            elif re.match(r'^(6|cross)$', specification.lower()) != None:
                print(inventory['cross'])
                if inventory['cross']['quantity'] > 0:
                    ask = input(bcolors.OKGREEN + 'Would you like to equip this item?' +  bcolors.ENDC)
                    if re.match(r'^(yes|y|yeah|sure|use|yep)$', ask.lower()) != None:
                        equip('cross')
                    elif re.match(r'^(no|nope|nah|n|exit|cancel|leave)$', ask.lower()) != None:
                        inven()
            elif re.match(r'^(7|steak)$', specification.lower()) != None:
                print(inventory['steak'])
                if inventory['steak']['quantity'] > 0:
                    ask = input(bcolors.OKGREEN + 'Would you like to use this item?' +  bcolors.ENDC)
                    if re.match(r'^(yes|y|yeah|sure|use|yep)$', ask.lower()) != None:
                        use('steak')
                    elif re.match(r'^(no|nope|nah|n|exit|cancel|leave)$', ask.lower()) != None:
                        inven()
            elif re.match(r'^(8|shield)$', specification.lower()) != None:
                print(inventory['shield'])
                if inventory['shield']['quantity'] > 0:
                    ask = input(bcolors.OKGREEN + 'Would you like to equip this item?' +  bcolors.ENDC)
                    if re.match(r'^(yes|y|yeah|sure|use|yep)$', ask.lower()) != None:
                        equip('shield')
                    elif re.match(r'^(no|nope|nah|n|exit|cancel|leave)$', ask.lower()) != None:
                        inven()
            elif re.match(r'^(9|cloth)$', specification.lower()) != None:
                print(inventory['cloth'])
                if inventory['cloth']['quantity'] > 0:
                    ask = input(bcolors.OKGREEN + 'Would you like to use this item?' +  bcolors.ENDC)
                    if re.match(r'^(yes|y|yeah|sure|use|yep)$', ask.lower()) != None:
                        use('cloth')
                    elif re.match(r'^(no|nope|nah|n|exit|cancel|leave)$', ask.lower()) != None:
                        inven()
            elif re.match(r'^(10|pelt)$', specification.lower()) != None:
                print(inventory['pelt'])
                inven()
            elif re.match(r'^(11|bloody rag)$', specification.lower()) != None:
                print(inventory['bloody rag'])
                if inventory['bloody rag']['quantity'] > 0:
                    ask = input(bcolors.OKGREEN + 'Would you like to use this item?' +  bcolors.ENDC)
                    if re.match(r'^(yes|y|yeah|sure|use|yep)$', ask.lower()) != None:
                        use('bloody rag')
                    elif re.match(r'^(no|nope|nah|n|exit|cancel|leave)$', ask.lower()) != None:
                        inven()
            elif re.match(r'^(12|wings|wing)$', specification.lower()) != None:
                print(inventory['wing'])
                inven()
            elif re.match(r'^(13|fangs|fang)$', specification.lower()) != None:
                print(inventory['fang'])
                inven()
            elif re.match(r'^(14|meat|meats)$', specification.lower()) != None:
                print(inventory['meat'])
                inven()
                ask = input(bcolors.OKGREEN + 'Would you like to use this item?' +  bcolors.ENDC)
                if re.match(r'^(yes|y|yeah|sure|use|yep)$', ask.lower()) != None:
                    use('cloth')
                elif re.match(r'^(no|nope|nah|n|exit|cancel|leave)$', ask.lower()) != None:
                    inven()
            elif re.match(r'^(15|exit|leave|cancel|stop)$', specification.lower()) != None:
                inven()
        elif re.match(r'^(6|exit|leave|cancel|stop)$', action.lower()) != None:
            if combat == True:
                inputs()
            else:
                inventory_status = False


#This dictionary has all presently equiped player items
global equiped
equiped = {}


#this function equipes items
def equip(x):
    save()
    global player_stat
    global player_stat_bonus
    if 'weapon' in equiped:
        equiped.pop('weapon', None)
        y_value = player_stat['min_ATK']
        player_stat.update(('min_ATK', y_value - player_stat_bonus['min_ATK_bonus']) for x, y in player_stat.items())
        y_value = player_stat['max_ATK']
        player_stat.update(('max_ATK', y_value - player_stat_bonus['max_ATK_bonus']) for x, y in player_stat.items())
        y_value = player_stat['HOLY']
        player_stat.update(('HOLY', y_value - player_stat_bonus['HOLY_bonus']) for x, y in player_stat.items())
    if inventory[x]['trait'] == 'shield':
        equiped['shield'] = 0
        save()
    elif inventory[x]['trait'] == 'weapon':
        equiped['weapon'] = 1
        player_stat_bonus['min_ATK_bonus'] = inventory[x]['min_ATK']
        y_value = player_stat['min_ATK']
        player_stat.update(('min_ATK', y_value + player_stat_bonus['min_ATK_bonus']) for x, y in player_stat.items())
        player_stat_bonus['max_ATK_bonus'] = inventory[x]['max_ATK']
        y_value = player_stat['max_ATK']
        player_stat.update(('max_ATK', y_value + player_stat_bonus['max_ATK_bonus']) for x, y in player_stat.items())
        player_stat_bonus['HOLY_bonus'] =  inventory[x]['HOLY']
        y_value = player_stat['HOLY']
        player_stat.update(('HOLY', y_value + player_stat_bonus['HOLY_bonus']) for x, y in player_stat.items())
        save()




# clear function os option


print("Please select operating system: \n 0 -- Unix (macOS, Linux, BSD... \n 1 -- Windows")
operating_sys = input('> ')
if re.match(r'^(0|Unix|macOS|linux|BSD)$', operating_sys.lower()) != None:
    def clear():
        os.system("clear")
elif re.match(r'^(1|window|windows)$', operating_sys.lower()) != None:
    def clear():
        os.system("cls")


#This variable keeps track of active bloody rags effects
global attractor
attractor = 0


#This determines whether or not the player encounters an enemy
def check_encounter():
    global attractor
    global mob
    if attractor > 0:
        attractor = attractor - 1
        encounter = 50
        if random.randrange(1, 101) <= encounter:
            key = random.randrange(0, len(enemies_list))
            mob = enemies[key].copy()
            #print(mob)
            play = False
            combat_intro()
    else:
        encounter = 10
        if random.randrange(1, 101) <= encounter:
            #These lines determine which enemie you will fight
            key = random.randrange(0, len(enemies_list))
            mob = enemies[key].copy()
            #print(mob)
            play = False
            combat_intro()

#This function introduces the enemie
def combat_intro():
    global mob
    print(bcolors.WARNING + '<< You Engaged Comabt With ({}), They Have ({}hp)! >>'.format(mob['name'], mob['hp']) + bcolors.ENDC)
    inputs(True)


#This function asks for the player's input
def inputs(combat = True):
    global mob
    while combat:
        action = input(bcolors.BOLD + bcolors.UNDERLINE + '<< What Do You Want To Do? [Attack]--[Escape]--[Parry]--[Inventory] >>' + bcolors.ENDC)
        if re.match(r'^(attack|atk|1)$', action.lower()) != None:
            attack()
        elif re.match(r'^(run|2)$', action.lower()) != None:
            escape()
        elif re.match(r'^(parry|3)$', action.lower()) != None:
            if 'shield' in equiped:
                parry()
            else:
                print(bcolors.FAIL + 'YOU DON"T HAVE A SHIELD EQUIPED' + bcolors.ENDC)
                inputs()
        elif re.match(r'^(inventory|bag|sac|my stuff|4)$', action.lower()) != None:
            inven(combat = True)
        else:
            invalid()
            inputs()

#This function deals with applying player damage to enemies
def attack():
    clear()
    global mob
    is_crit = is_critical()
    hit_chance = (player_stat['SPEED']/mob['speed'])*100 + (player_stat['LUCK']/2) - (mob['luck']/2)
    if hit_chance <= 0:
        hit_chance = 1
    if mob['speed'] <= 0:
        hit_chance = 95
    attack_rsp = input('<< Would You Like To See Your Hit Chance? [Yes]--[No] >>')
    if re.match(r'^(yes|ye|y|1)$', attack_rsp.lower()) != None:
        clear()
        print(bcolors.FAIL + bcolors.UNDERLINE + '<< You Have a' + bcolors.OKCYAN + '({}%)'.format(hit_chance) + bcolors.FAIL + 'Chance To Hit! >>' + bcolors.ENDC)
        attack_confirm(hit_chance, is_crit)
    elif re.match(r'^(no|n|2)$', attack_rsp.lower()) != None:
        clear()
        attack_confirm(hit_chance, is_crit)
    else:
        invalid()
        attack()

#This function checks for crits for the damage function, for the player
def is_critical():
    crit = random.randrange(1,101)
    if crit <= player_stat['LUCK'] + ((player_stat_bonus['LUCK_bonus'])/2) :
        return True
    return False


#This function just reduces repetition, it's has the inputs and the function calls, that simply get repeated a few times, so I want to reduce the amount of lines im using with this function. This is used in the attack function.
def attack_confirm(hit_chance, is_crit=False):
    confirmation = input('<< Want To Proceed? [Yes]--[No] >>')
    if re.match(r'^(yes|ye|y|1)$', confirmation.lower()) != None:
        clear()
        damage(hit_chance, False, is_critical())
    elif re.match(r'^(no|n|2)$', confirmation.lower()) != None:
        clear()
        inputs()
    else:
        invalid()
        attack_confirm(hit_chance, False, is_critical())

#This function is for blocking
def parry():
    global mob
    parry = is_parry()
    is_crit = is_critical()
    hit_chance = (player_stat['SPEED']/mob['speed'])/2*100 + (player_stat['LUCK']/2) - (mob['luck']/2)
    if hit_chance <= 0:
        hit_chance = 1
    if mob['speed'] <= 0:
        hit_chance = 95
    attack_rsp = input('<< Would You Like To See Your Parry Chance? [Yes]--[No] >>')
    if re.match(r'^(yes|ye|y|1)$', attack_rsp.lower()) != None:
        print(bcolors.FAIL + bcolors.UNDERLINE + '<< You Have a' + bcolors.OKCYAN + '({}%)'.format(hit_chance) + bcolors.FAIL + 'Chance To Hit! >>' + bcolors.ENDC)
        parry_comfirm(hit_chance, parry, is_crit)
    elif re.match(r'^(no|n|2)$', attack_rsp.lower()) != None:
        parry_comfirm(hit_chance, parry, is_crit)
    else:
        invalid()
        parry()


#Same as attack comfirm
def parry_comfirm(hit_chance, parry=False, is_crit=False):
    comfirmation = input('<< Want To Proceed? [Yes]--[No] >>')
    if re.match(r'^(yes|ye|y|1)$', comfirmation.lower()) != None:
        print(bcolors.WARNING + 'You Prepare your Shield to parry...' + bcolors.ENDC)
        damage(hit_chance, parry, is_crit)
    elif re.match(r'^(no|n|2)$', comfirmation.lower()) != None:
        inputs()
    else:
        invalid()
        parry_comfirm(hit_chance, parry=False, is_crit=False)

#This function determines whether or not the pplayer parries
def is_parry():
    parry = (player_stat['SPEED']/mob['speed'])/2*100 + (player_stat['LUCK']/2) - (mob['luck']/2)
    if parry <= random.randrange(1, 101):
        return True
    return False


#This function does the damage calculations for the player's turn + the critical skips the monster's turn.
def damage(hit_chance, parry=False, is_crit=False):
    global mob
    damage = random.randrange(player_stat['min_ATK'], (player_stat['max_ATK'] + 1))
    if hit_chance >= random.randrange(1,101):
        if is_crit:
            damage = damage * 1.5
            mob['hp'] = mob['hp'] - damage
            print(bcolors.OKGREEN + bcolors.UNDERLINE + '<< You Dealt' + bcolors.OKCYAN + '({})'.format(damage) + bcolors.OKGREEN + 'Critical Damage To ({})! ({}) Health Is Now'.format(mob['name'], mob['name']) + bcolors.OKCYAN + '({}hp)'.format(mob['hp']) + bcolors.OKGREEN + '! >>' + bcolors.ENDC)
            check_death()
            if check_death() == False:
                almost_ded(parry)
            elif check_death() == True:
                world(x, y)
        if is_crit == False:
            mob['hp'] = mob['hp'] - damage
            print(bcolors.OKGREEN + '<< You Dealt' + bcolors.OKCYAN + '({})'.format(damage) + bcolors.OKGREEN + 'Damage To ({})! ({}) Health Is Now'.format(mob['name'], mob['name']) + bcolors.OKCYAN + '({}hp)'.format(mob['hp']) + bcolors.OKGREEN + '>>' + bcolors.ENDC)
            check_death()
            if check_death() == False:
                almost_ded(parry)
            elif check_death() == True:
                world(x, y)
        if is_crit and parry:
            damage = damage * 1.5
            mob['hp'] = mob['hp'] - damage
            print(bcolors.OKGREEN + bcolors.UNDERLINE + '<< You Parried the Attack and Dealt' + bcolors.OKCYAN + '({})'.format(damage) + bcolors.OKGREEN + 'Critical Damage To ({})! ({}) Health Is Now'.format(mob['name'], mob['name']) + bcolors.OKCYAN + '({}hp)'.format(mob['hp']) + bcolors.OKGREEN + '! >>' + bcolors.ENDC)
            check_death()
            if check_death() == False:
                almost_ded(parry)
            elif check_death() == True:
                world(x, y)
        if parry:
            mob['hp'] = mob['hp'] - damage
            print(bcolors.OKGREEN + '<< You Parried the Attack and Dealt' + bcolors.OKCYAN + '({})'.format(damage) + bcolors.OKGREEN + 'Damage To ({})! ({}) Health Is Now'.format(mob['name'], mob['name']) + bcolors.OKCYAN + '({}hp)'.format(mob['hp']) + bcolors.OKGREEN + '>>' + bcolors.ENDC)
            check_death()
            if check_death() == False:
                almost_ded(parry)
            elif check_death() == True:
                world(x, y)
    else:
        print(bcolors.WARNING + '<< You Didn\'t Land Your Hit... >>' + bcolors.ENDC)
        enemie_turn()


#here we check to see how low the enemy is, and how low we are
def check_death():
    global mob
    global xp
    if player_stat['HP'] <= 0:
        clear()
        print (bcolors.UNDERLINE + bcolors.WARNING + '~~~' + bcolors.FAIL +  "YOU DIED" + bcolors.WARNING + '~~~' + bcolors.ENDC)
        player_stat['HP'] = player_stat['max_HP']
        game_over()
        return True
    if mob['hp'] <= 0:
        clear()
        print(bcolors.OKGREEN + '<< You Killed ({}) and Gained ({})xp! >>'.format(mob['name'], mob['experience']) + bcolors.ENDC)
        xp = int(xp) + mob['experience']
        mob['hp'] = mob['hp'] + mob['reset hp']
        lv_up()
        play = True
        combat = False
        return True
    return False


#This function also for lower line count, man im doing a lot of these eh?
def almost_ded(x):
    global mob
    if mob['hp'] <= mob['hp']/3:
        print('<< It\'s Almost Dead! >>')
    if x == True:
        inputs()
    else:
        enemie_turn()


#this is the enemie's turn
def enemie_turn():
    global mob
    hit_chance = (mob['speed']/player_stat['SPEED'])*100 - (player_stat['LUCK']/2) + (mob['luck']/2)
    damage = random.randrange(mob['min_ATK'], (mob['max_ATK'] + 1))
    is_crit = enemie_crit()
    if hit_chance >= random.randrange(1,101):
        player_stat['HP'] = player_stat['HP'] - damage
        print(bcolors.FAIL + '<< ({}) Dealt'.format(mob['name']) + bcolors.WARNING + '({})'.format(damage) + bcolors.FAIL + 'Damage! Your Health Is Now' + bcolors.WARNING + '({}hp)'.format(player_stat['HP']) + bcolors.FAIL + '>>' + bcolors.ENDC)
        check_death()
        inputs()
    if is_crit:
        damage = damage * 1.5
        player_stat['HP'] = player_stat['HP'] - damage
        print(bcolors.FAIL + bcolors.UNDERLINE + '<< ({}) Dealt'.format(mob['name'])  + bcolors.WARNING + '({})'.format(damage) + bcolors.FAIL +  'Critical Damage! Your Health Is Now' + bcolors.WARNING + '({}hp)'.format(player_stat['HP']) + bcolors.FAIL + '>>'.format(mob['name'], damage, player_stat['HP']) + bcolors.ENDC)
        check_death()
        inputs()
    else:
        print(bcolors.OKGREEN + '<< ({}) Didn\'t Land It\'s Hit... >>'.format(mob['name']) + bcolors.ENDC)
        inputs()

#This function checks for enemie crits
def enemie_crit():
    global mob
    crit = random.randrange(1,101)
    if crit <= mob['luck']:
        return True
    return False

#This function performs the running action
def escape():
    clear()
    global mob
    run_chance = ((player_stat['SPEED']/mob['speed']/2))*100 + (player_stat['LUCK']/2) - (mob['luck']/2)
    escape = input('<< Would You Like To See Your Run Chance? [Yes]--[No] >>')
    if re.match(r'^(yes|ye|y|1)$', escape.lower()) != None:
        print('<< You Have a ({}%) Chance To Hit! >>'.format(run_chance))
        run_confirmation(run_chance)
    elif re.match(r'^(no|n|2)$', escape.lower()) != None:
        run_confirmation(run_chance)
    else:
        clear()
        invalid()
        escape()

#This function serves the same purpose as attack_comfirm, just lowering the line count.
def run_confirmation(run_chance):
    clear()
    confirmation = input('<< Want To Proceed? [Yes]--[No] >>')
    if re.match(r'^(yes|ye|y|1)$', confirmation.lower()) != None:
        run = random.randrange(1,101)
        if run <= run_chance:
            print('<< You Successfully Ran Away! >>')
            play = True
        else:
            print('<< Your Run Attempt Failed... >>')
            enemie_turn()
    elif re.match(r'^(no|n|2)$', confirmation.lower()) != None:
        inputs()
    else:
        clear()
        invalid()
        run_confirmation(run_chance)




combat = False
intro = True

while intro:
    clear()
    print("$$\    $$\                          $$\   $$\           $$\           $$\                  ")
    print("$$ |   $$ |                         $$ |  $$ |          $$ |          \__|                          ")
    print("$$ |   $$ |$$$$$$\  $$$$$$$\        $$ |  $$ | $$$$$$\  $$ | $$$$$$$\ $$\ $$$$$$$\   $$$$$$\       ")
    print("\$$\  $$  |\____$$\ $$  __$$\       $$$$$$$$ |$$  __$$\ $$ |$$  _____|$$ |$$  __$$\ $$  __$$\       ")
    print(" \$$\$$  / $$$$$$$ |$$ |  $$ |      $$  __$$ |$$$$$$$$ |$$ |\$$$$$$\  $$ |$$ |  $$ |$$ /  $$ |      ")
    print("  \$$$  / $$  __$$ |$$ |  $$ |      $$ |  $$ |$$   ____|$$ | \____$$\ $$ |$$ |  $$ |$$ |  $$ |            ")
    print("   \$  /  \$$$$$$$ |$$ |  $$ |      $$ |  $$ |\$$$$$$$\ $$ |$$$$$$$  |$$ |$$ |  $$ |\$$$$$$$ |       ")
    print("    \_/    \_______|\__|  \__|      \__|  \__| \_______|\__|\_______/ \__|\__|  \__| \____$$ |        ")
    print("                                                                                    $$\   $$ |         ")
    print("                                                                                    \$$$$$$  |       ")
    print("                                                                                     \______/             ")
    print("$$$$$$$$\ $$\                        $$$$$$\                                                    ")
    print("\__$$  __|$$ |                      $$  __$$\                                                         ")
    print("   $$ |   $$$$$$$\   $$$$$$\        $$ /  \__| $$$$$$\  $$$$$$\$$$$\   $$$$$$\                 ")
    print("   $$ |   $$  __$$\ $$  __$$\       $$ |$$$$\  \____$$\ $$  _$$  _$$\ $$  __$$\           ")
    print("   $$ |   $$ |  $$ |$$$$$$$$ |      $$ |\_$$ | $$$$$$$ |$$ / $$ / $$ |$$$$$$$$ |         ")
    print("   $$ |   $$ |  $$ |$$   ____|      $$ |  $$ |$$  __$$ |$$ | $$ | $$ |$$   ____|                          ")
    print("   $$ |   $$ |  $$ |\$$$$$$$\       \$$$$$$  |\$$$$$$$ |$$ | $$ | $$ |\$$$$$$$\              ")
    print("   \__|   \__|  \__| \_______|       \______/  \_______|\__| \__| \__| \_______|         ")
    print("Holly H, Matt L, Jill L, Kai YT\n Press <0> to continue...")
    print("Map system from video guide https://www.youtube.com/watch?v=i3j3iZNPUbI")
    selection = input('> ')
    if selection == '0':
        intro = False
        run = True
        menu = True
        play = False
        rules = False
    else:
        selection = input('> ')





#run = True
#menu = True
#play = False
#rules = False


        # x = 0    x = 1       x = 2      x = 3        x = 4
map = [['forest','forest','forest','mountain','mountain'], # y = 0
        ['forest','forest','forest','forest','mountain'],  # y = 1
        ['forest','forest','plains','plains','hills'],     # y = 2
        ['plains','plains','plains','plains','hills'],     # y = 3
        ['river','river','bridge','river','river'],        # y = 4
        ['fields','fields','town','shop','forest'],        # y = 5
        ['plains','fields','plains','forest','mountain']]  # y = 6



global player_stat_bonus
player_stat_bonus = {
    'min_ATK_bonus' : 0,
    'max_ATK_bonus' : 0,
    'max_HP_bonus' : 0,
    'LUCK_bonus' : 0,
    'SPEED_bonus' : 0,
    'HOLY_bonus'  : 0,
}

global player_stat
player_stat = {
    'HP' : 100,
    'min_ATK' : 20,
    'max_ATK' : 25,
    'max_HP' : 100,
    'LUCK' : 80,
    'SPEED' : 6,
    'HOLY'  : 0,
}
global lv
lv = 1
global xp
xp = 0
global req
req = 10
GOLD = 50
x_len = len(map)- 1
y_len = len(map[0])- 1
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


def world(x, y):
    draw()
    print("LOCATION: " + biom[map[x][y]]["text"])
    draw()

    print("NAME: " + name)
    print("HP: " + str(player_stat['HP']) + "/" + str(player_stat['max_HP']))
    print("ATK: " + str(player_stat['min_ATK']) + '-' + str(player_stat['max_ATK']))
    print("LUCK: " + str(player_stat['LUCK']))
    print("SPEED: " + str(player_stat['SPEED']))
    print("BLOODY RAGS: " + str(inventory['bloody rag']['quantity']))
    print("GOLD: " + str(GOLD))
    print(xp)
    #controls
    print("OPTIONS:")
    print("0 -- Menu")
    print("1 -- Left")
    print("2 -- Down")
    print("3 -- Up")
    print("4 -- Right")
    print("5 -- Inventory/Stats")
    print("COORDS", x, y)
    draw()

    dest = input("# ")

###--------------------------KAI----------------------------##
#        direct = input('> ')
#        print(location) # I need to figure out how tf to make the position change in the map
#        # also make sure I can check that the location has actually changed
#        if direct == 'left':
#            if x_position == 0:
#                x_position = 4
#                save()
#            else:
#                x_position -= 1
#                save()
#
#        elif direct == 'right':
#            if x_position == 4:
#                x_position = 0
#                save()
#            else:
#                x_position +=1
#                save()
#
#        elif direct == 'up':
#            if y_position == 0:
#                y_position = 6
#                print(location)
#                save()
#            else:
#                y_position -= 1
#                save()
#
#        elif direct == 'down':
#            if y_position == 6:
#                y_position = 0
#                save()
#            else:
#                y_position += 1
#                save()
#
#        elif direct == '0':
#            play = False
#            menu = True
#            save() #autosave

###-------------------MATT---------------------------##

    if re.match(r'^(0|menu|exit)$', dest.lower()) != None:
        play = False
        menu = True
        save()
    elif re.match(r'^(2|down)$', dest.lower()) != None:
        if y > 0:
            y -= 1
            if biom[map[x][y]]['enemies'] == True:
                check_encounter()
        else:
            y = y_len
            if biom[map[x][y]]['enemies'] == True:
                check_encounter()

    elif re.match(r'^(4|right)$', dest.lower()) != None:
        if x < x_len:
            x += 1
            if biom[map[x][y]]['enemies'] == True:
                check_encounter()
        else:
            x = 0
            if biom[map[x][y]]['enemies'] == True:
                check_encounter()

    elif re.match(r'^(3|up)$', dest.lower()) != None:
        if y < y_len:
            y += 1
            if biom[map[x][y]]['enemies'] == True:
                check_encounter()
        else:
            y = 0
            if biom[map[x][y]]['enemies'] == True:
                check_encounter()
    elif re.match(r'^(1|left)$', dest.lower()) != None:
        if x > 0:
            x -= 1
            if biom[map[x][y]]['enemies'] == True:
                check_encounter()
        else:
            x = x_len
            if biom[map[x][y]]['enemies'] == True:
                check_encounter()
    elif re.match(r'^(5|inventory|inven|bag|sac|stats|stat)$', dest.lower()) != None:
        inven()


def draw():
    print('<~|-------------------------------------------------|~>')

def save():
    list = [
        name,
        str(lv),
        str(xp),
        str(req),
        str(player_stat_bonus['min_ATK_bonus']),
        str(player_stat_bonus['max_ATK_bonus']),
        str(player_stat_bonus['max_HP_bonus']),
        str(player_stat_bonus['LUCK_bonus']),
        str(player_stat_bonus['SPEED_bonus']),
        str(player_stat_bonus['HOLY_bonus']),
        str(player_stat['HP']),
        str(player_stat['max_HP']),
        str(player_stat['min_ATK']),
        str(player_stat['max_ATK']),
        str(player_stat['HOLY']),
        str(player_stat['LUCK']),
        str(player_stat['SPEED']),
        str(inventory['bloody rag']['quantity']),
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
        #print(location)
        #print(location_name)
        #print(location_enemy_status)
        print('1 -- New Game')
        print('2 -- Load Game')
        print('3 -- Rules')
        print('4 -- Quit')
        draw()


        if rules:
            clear()
            draw()
            print('Don\'t break the game please') #this is getting cleared before poeple can read it because of line 884, the clear at the beggining of the while menu loop
            draw()
            rules = False
            choice = ''
        else:
            choice = input('> ')


        if re.match(r'^(1|new game|one|first)$', choice.lower()) != None:
            clear()
            draw()
            name = input('> What\'s your name hero?\nName: ')
            menu = False
            play = True

        elif re.match(r'^(2|load game|two|second)$', choice.lower()) != None:
            f = open("load.txt", "r")
            load_list = f.readlines()
            name = load_list[0][:-1]
            lv = load_list[1][:-1]
            xp = load_list[2][:-1]
            req = load_list[3][:-1]
            min_ATK = load_list[4][:-1]
            max_ATK = load_list[5][:-1]
            max_HP = load_list[6][:-1]
            LUCK_bonus = load_list[7][:-1]
            SPEED_bonus = load_list[8][:-1]
            HOLY_bonus = load_list[9][:-1]
            HP = load_list[10][:-1]
            max_HP = load_list[11][:-1]
            min_ATK = load_list[12][:-1]
            max_ATK = load_list[13][:-1]
            HOLY = load_list[14][:-1]
            LUCK = load_list[15][:-1]
            SPEED = load_list[16][:-1]
            BLOODY_RAG = load_list[17][:-1]
            GOLD = load_list[18][:-1]
            location = load_list[19][:-1]
            clear()
            draw()
            print ('You\'re back ""' + name + '"", finally...')
            print('here are your stats btw, not very impressive just saying')
            print(' -HP:' + HP + '/' + max_HP + '\n -ATK:' + min_ATK + '-' + max_ATK + '\n -LUCK:' + LUCK + '\n -SPEED' + SPEED + '\n -BLOODY RAG:' + BLOODY_RAG + '\n -GOLD:' + GOLD + '\n -LOCATION:' + location)  #there's a syntax error here IDK why though, something to do with the location. ' -LOCATION:' + location)
            draw()
##            input('> Press ENTER to return to begin...')
            menu = False
            play = True

        elif re.match(r'^(3|rule|rules|three|third)$', choice.lower()) != None:
            rules = True

        elif re.match(r'^(4|quit|exit|close|four|fourth)$', choice.lower()) != None:
            quit()


    while play:
        save() #autosave
        clear()
        world(x, y)
