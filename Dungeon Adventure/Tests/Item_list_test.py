global player_atk_buff
player_atk_buff = 0
global player_hp_buff
player_hp_buff = 0
global player_magic_buff
player_magic_buff = 0
import re
global inventory
inventory = {}
global variables
variables = {}
global spells
spells = {}
global skills
skills = {}




equipment = {
    'weapons':     {
        'sword': 4,
        'rock': 1,
        'PP rod':     {
                'damage': 1,
                'magic': 5
                    }
                },
    'armour':    {
        'shield': 5,
        'plank': 3
                }
}




def equip():
    action = input('Choose your equipment or Check your stats!')
    if re.match(r'^(weapons|weapon|1)$', action.lower()) != None:
        weapons()
    elif re.match(r'^(armour|2)$', action.lower()) != None:
        armour()
    elif re.match(r'^(stat|stats|3)$', action.lower()) != None:
        check()
    elif re.match(r'^(remove|unequip|get rid off|discard)$',action.lower()) != None:
        unequip()
    else:
        print('Please Input A Valide Answer.')
        equip()


def weapons():
    action2 = input('What weapon would you like to equip?')
    if re.match(r'^(sword)$', action2.lower()) != None:
        sword()
    elif re.match(r'^(rock)$', action2.lower()) != None:
        rock()
    elif re.match(r'^(pp rod|pprod)$', action2.lower()) != None:
        PP_rod()
    elif re.match(r'^(no|nah|back|go back)$', action2.lower()) != None:
        equip()
    else:
        print('Please Input A Valide Answer.')
        equip()



def armour():
    action3 = input('What armour would you like to equip?')
    if re.match(r'^(shield)$', action3.lower()) != None:
        shield()
    elif re.match(r'^(plank)$', action3.lower()) != None:
        plank()
    elif re.match(r'^(no|nah|back|go back)$', action2.lower()) != None:
        equip()


def sword():
    global player_atk_buff
    if 'sword' in inventory:
        print('You already have <<sword>> equiped!')
        equip()
    elif 'rock' in inventory:
        action5 = input('<<Sword>> will replace <<Rock>>. Are you sure you want to proceed?')
        if re.match(r'^(yes|proceed|y|yeet|ya)$', action5.lower()) != None:
            print ('You equiped <<sword>>!')
            player_atk_buff = 0
            weapons = equipment['weapons']['sword']
            player_atk_buff = player_atk_buff + weapons
            inventory ['sword'] = 1
            inventory.pop('rock', None)
            equip()
        elif re.match(r'^(no|nah)$', action4.lower()) != None:
            equip()
        else:
            print('Please Input A Valide Answer.')
            equip()
    else:
        print ('You equiped <<sword>>!')
        weapons = equipment['weapons']['sword']
        player_atk_buff = player_atk_buff + weapons
        inventory ['sword'] = 1
        equip()


def rock():
    global player_atk_buff
    if 'rock' in inventory:
        print('You already have <<rock>> equiped!')
        equip()
    elif 'sword' in inventory:
        action4 = input('<<Rock>> will replace <<Sword>>. Are you sure you want to proceed?')
        if re.match(r'^(yes|proceed|y|yeet|ya)$', action4.lower()) != None:
            print('You equiped <<rock>>!')
            player_atk_buff = 0
            weapons = equipment['weapons']['rock']
            player_atk_buff = player_atk_buff + weapons
            inventory.pop('sword', None)
            inventory ['rock'] = 2
            equip()
        elif re.match(r'^(no|nah)$', action4.lower()) != None:
            equip()
        else:
            print('Please Input A Valide Answer.')
            equip()
    else:
        print('You equiped <<rock>>!')
        weapons = equipment['weapons']['rock']
        player_atk_buff = player_atk_buff + weapons
        inventory ['rock'] = 2
        equip()


def PP_rod():
    global player_atk_buff
    global player_magic_buff
    if 'PP_rod' in inventory:
        print('You already have <<PP Rod>> equiped!')
        equip()
    elif 'sword' in inventory:
        action4 = input('<<PP Rod>> will replace <<Sword>>. Are you sure you want to proceed?')
        if re.match(r'^(yes|proceed|y|yeet|ya)$', action4.lower()) != None:
            print('You equiped <<PP Rod>>!')
            player_atk_buff = 0
            weapons = equipment['weapons']['PP rod']['damage']
            magic = equipment['weapons']['PP rod']['magic']
            player_atk_buff = player_atk_buff + weapons
            player_magic_buff = player_magic_buff + magic
            inventory.pop('sword', None)
            inventory ['PP_rod'] = 2 and spells ['waifu'] = 1
            equip()
    elif 'rock' in inventory:
        action4 = input('<<PP Rod>> will replace <<rock>>. Are you sure you want to proceed?')
        if re.match(r'^(yes|proceed|y|yeet|ya)$', action4.lower()) != None:
            print('You equiped <<PP Rod>>!')
            player_atk_buff = 0
            weapons = equipment['weapons']['PP rod']
            magic = equipment['weapons']['PP rod']['magic']
            player_atk_buff = player_atk_buff + weapons
            player_magic_buff = player_magic_buff + magic
            inventory.pop('rock', None)
            inventory ['PP_rod'] = 2 and spells ['waifu'] = 1
            equip()
        elif re.match(r'^(no|nah)$', action4.lower()) != None:
            equip()
        else:
            print('Please Input A Valide Answer.')
            equip()
    else:
        print('You equiped <<PP Rod>>!')
        weapons = equipment['weapons']['PP rod']['damage']
        magic = equipment['weapons']['PP rod']['magic']
        player_atk_buff = player_atk_buff + weapons
        player_magic_buff = player_magic_buff + magic
        inventory ['PP_rod'] = 2 and spells ['waifu'] = 1
        equip()




def shield():
    global player_hp_buff
    if 'shield' in inventory:
        print('You already have <<shield>> equiped!')
        equip()
    elif 'plank' in inventory:
        action4 = input('<<Shield>> will replace <<Plank>>. Are you sure you want to proceed?')
        if re.match(r'^(yes|proceed|y|yeet|ya)$', action4.lower()) != None:
            print('You equiped <<Shield>>!')
            player_hp_buff = 0
            armour = equipment['armour']['shield']
            player_hp_buff = player_hp_buff + armour
            inventory.pop('plank', None)
            equip()
        elif re.match(r'^(no|nah)$', action4.lower()) != None:
            equip()
        else:
            print('Please Input A Valide Answer.')
            equip()
    else:
        print('You equiped <<shield>>!')
        armour = equipment['armour']['shield']
        player_hp_buff = player_hp_buff + armour
        inventory ['shield'] = 3
        equip()


def plank():
    global player_hp_buff
    if 'plank' in inventory:
        print('You already have <<plank>> equiped!')
        equip()
    if 'shield' in inventory:
        action4 = input('<<Plank>> will replace <<Shield>>. Are you sure you want to proceed?')
        if re.match(r'^(yes|proceed|y|yeet|ya)$', action4.lower()) != None:
            print('You equiped <<Plank>>!')
            player_hp_buff = 0
            armour = equipment['armour']['plank']
            player_hp_buff = player_hp_buff + armour
            inventory.pop('shield', None)
            equip()
        elif re.match(r'^(no|nah)$', action4.lower()) != None:
            equip()
        else:
            print('Please Input A Valide Answer.')
            equip()
    else:
        print('You equiped <<plank>>!')
        armour = equipment['armour']['plank']
        player_hp_buff = player_hp_buff + armour
        inventory ['plank'] = 4
        equip()



def check():
    action = input('Would you like to check your stats?')
    if re.match(r'^(yes|y|ye|yeet|stats)$', action.lower()) != None:
        print('atk {}|hp{}'.format(player_atk_buff, player_hp_buff))
        equip()
    elif re.match(r'^(no|nah|back|go back)$', action.lower()) != None:
        equip()
    else:
        print('Please Input A Valide Answer.')
        check()

def unequip():
    action = input('Would you like to unequip all equipped items?')
    if re.match(r'^(yes|y|ye|yeet|unequip|remove|get rid of)$', action.lower()) != None:
        empty_check()
        equip()
    elif re.match(r'^(no|n|negative|nah)$', action.lower()) != None:
        equip()
    else:
        print('Please Input A Valide Answer.')
        unequip()

def empty_check():
    global player_atk_buff
    global player_magic_buff
    if 'no weapon' in variables:
        variables.pop('no weapon', None)
        empty_check_armour()
    elif 'sword' in inventory:
        inventory.pop('sword', None)
        weapons = equipment['weapons']['sword']
        player_atk_buff = player_atk_buff - weapons
        if player_atk_buff == 0 and player_magic_buff == 0:
            variables ['no weapon'] = 5
            empty_check()
        else:
            empty_check()
    elif 'rock' in inventory:
        inventory.pop('rock', None)
        weapons = equipment['weapons']['rock']
        player_atk_buff = player_atk_buff - weapons
        if player_atk_buff == 0 and player_magic_buff == 0:
            variables ['no weapon'] = 5
            empty_check()
        else:
            empty_check()
    elif 'PP_rod' in inventory:
        inventory.pop('PP_rod', None)
        weapons = equipment['weapons']['PP rod']['damage']
        magic = equipment['weapons']['PP rod']['magic']
        player_atk_buff = player_atk_buff - weapons
        player_magic_buff = player_magic_buff - magic
        if player_atk_buff == 0 and player_magic_buff == 0:
            variables ['no weapon'] = 5
            empty_check()
        else:
            empty_check()
    else:
        empty_check_armour()

def empty_check_armour():
    global player_hp_buff
    if 'no armour' in variables:
        variables.pop('no armour', None)
        print('All items unequipped!')
        equip()
    elif 'shield' in inventory:
        inventory.pop('shield', None)
        armour = equipment['armour']['shield']
        player_hp_buff = player_hp_buff - armour
        if player_hp_buff == 0:
            variables ['no armour'] = 6
            empty_check_armour()
        else:
            empty_check_armour()
    elif 'plank' in inventory:
        inventory.pop('plank', None)
        armour = equipment['armour']['plank']
        player_hp_buff = player_hp_buff - armour
        if player_hp_buff ==  0:
            variables ['no armour'] = 6
            empty_check_armour()
        else:
            empty_check_armour()
    else:
        print('All items unequipped!')
        equip()
