import string
import random
import re
from graphics import *
global player_atk_buff
player_atk_buff = 0
global player_hp_buff
player_hp_buff = 100
global inventory
inventory = {}
global skills
skills = {}
global spells
spells = {}
global variables
variables = {}
global player_hp
player_hp = 12 + player_hp_buff
global player_xp
player_xp = 0
global player_atk_minimum
player_atk_minimum = 1
global player_atk_maximium
player_atk_maximium = 3
global player_AP_buff
player_AP_buff = 0
global player_run_buff
player_run_buff = 0
global player_magic_buff
player_magic_buff = 0
global skill_1_cooldown
skill_1_cooldown = 0
global skill_2_cooldown
skill_2_cooldown = 0
global player_luck_buff
player_luck_buff = 0
global monster_hp
monster_hp = 0
global monster_xp
monster_xp = 0
global monster_AP
monster_AP = 0
global monster_hit_minimum
monster_hit_minimum = 0
global monster_hit_maximum
monster_hit_maximum = 0
global monster_status_damage
monster_status_damage = 0
global monster_status_duration
monster_status_duration = 0
global initial_monster_status_damage
initial_monster_status_damage = 0
global reset_status_duration
reset_status_duration = 0
global reset_health
reset_health = 0
global monster_name
monster_name = ''
global ability_name
ability_name = ''





monsters = {
    'goblin':    {
        'xp': random.randrange(8, 11),
        'hp': 10,
        'AP': 5,
        'hit':{
            'minimum':1,
            'maximum':3
            }
                },
    'orc':      {
        'xp':random.randrange(16, 20),
        'hp': 20,
        'AP': 7,
        'hit':{
            'minimum':2,
            'maximum':4
            }
                },
    'bokoblin': {
        'xp':random.randrange(4, 8),
        'hp': 5,
        'AP': 3,
        'hit':{
            'minimum': 1,
            'maximum': 3
            }
                },
    'philosraptor':     {
        'xp':random.randrange(40,50),
        'hp': 40,
        'AP': 10,
        'initial ability':{
                        'damage': 5
                        },
        'status':{
                'duration': 3,
                'damage': 4
                },
        'hit':{
            'minimum':6,
            'maximum':8
            }
                        }
}

def combat_intro():
    global monster_name
    global ability_name
    global monster_hp
    global monster_xp
    global monster_AP
    global monster_hit_minimum
    global monster_hit_maximum
    global monster_status_damage
    global monster_status_duration
    global initial_monster_status_damage
    global reset_health
    global reset_status_duration
    monster = random.randrange(1,11)
    if monster == 1 or monster == 2 or monster == 3 or monster == 4 or monster == 5 or monster == 6:
        monster_name = 'goblin'
        reset_health = monsters['goblin']['hp']
        variables ['goblin'] = 1
        monster_hp = monsters['goblin']['hp']
        monster_xp = monsters['goblin']['xp']
        monster_AP = monsters['goblin']['AP']
        monster_hit_minimum = monsters['goblin']['hit']['minimum']
        monster_hit_maximum = monsters['goblin']['hit']['maximum']
    elif monster == 7 or monster == 8 or monster == 9:
        monster_name = 'orc'
        reset_health = monsters['orc']['hp']
        variables ['orc'] = 2
        monster_hp = monsters['orc']['hp']
        monster_xp = monsters['orc']['xp']
        monster_AP = monsters['orc']['AP']
        monster_hit_minimum = monsters['orc']['hit']['minimum']
        monster_hit_maximum = monsters['orc']['hit']['maximum']
    elif monster == 10:
        monster_name = 'philosraptor'
        reset_health = monsters['philosraptor']['hp']
        reset_status_duration = monsters['philosraptor']['status']['duration']
        variables ['philosraptor'] = 3
        variables ['ability starting'] = 4
        variables ['ability'] = 5
        ability_name = 'Green ice'
        monster_hp = monsters['philosraptor']['hp']
        monster_xp = monsters['philosraptor']['xp']
        monster_AP = monsters['philosraptor']['AP']
        monster_hit_minimum = monsters['philosraptor']['hit']['minimum']
        monster_hit_maximum = monsters['philosraptor']['hit']['maximum']
        monster_status_damage = monsters['philosraptor']['status']['damage']
        monster_status_duration = monsters['philosraptor']['status']['duration']
        initial_monster_status_damage = monsters['philosraptor']['initial ability']['damage']
    elif monster == 11 or monster == 12 or monster == 13 or monster == 14 or monster == 15:
        monster_name = 'bokoblin'
        reset_health = monsters['bokoblin']['hp']
        variables ['bokoblin'] = 6
        monster_hp = monsters['bokoblin']['hp']
        monster_xp = monsters['bokoblin']['xp']
        monster_AP = monsters['bokoblin']['AP']
        monster_hit_maximum = monsters['bokoblin']['hit']['minimum']
        monster_hit_maximum = monsters['bokoblin']['hit']['maximum']
    print('<<You Engage Combat With The ({})!>>'.format(monster_name))
    if monster_hp <= 0:
        monster_hp = reset_health
        player_input()
    else:
        player_input()



def player_input():

    if monster_hp <= 0:
        combat_end()
    elif player_hp <= 0:
        player_death()
    else:
        action15 = input('<<Attack>>  <<Run>>')
        if re.match(r'^(attack|atk|1|hit)$', action15.lower()) != None:
            action14 = input('Magic or Melee?')
            if re.match(r'^(1|hit|melee|physical)$', action14.lower()) != None:
                AP_chance = (20 + player_AP_buff - monster_AP) / 20 * 100
                action16 = input('<<You Have A {}% Chance Of Landing Your Hit. Are You Sure You Want To Proceed?>>'.format(AP_chance))
                if re.match(r'^(no|n|nah|nope)$',action16.lower()) != None:
                    player_input()
                elif re.match(r'^(yes|ya|y|yep|sure|ye)$',action16.lower()) != None:
                    melee()
                else:
                    print('Please Input A Valide Answer')
            elif re.match(r'^(magic|spell|2)$',action14.lower()) != None:
                magic()
            else:
                print('Please Input A Valide Answer.')
                player_input()
        elif re.match(r'^(run|escape|2|leave)$', action15.lower()) != None:
            run_chance = (10 + player_run_buff) / 20 * 100
            action13 = input('<<You Have A {}% Chance Of Running. Are You Sure You Want To Proceed?>>'.format(run_chance))
            if re.match(r'^(run|yes|y|yeet)$', action13.lower()) != None:
                run()
            elif re.match(r'^(no|cancel|negative|nope|nah|n)$', actioon13.lower()) != None:
                player_input()
            else:
                print('Please Input A Valide Answer.')
                player_input()
        else:
            print('Please Input A Valide Answer.')
            player_input()



def melee():
    global monster_hp
    AP_factor = random.randrange(1, 21) + player_AP_buff
    if AP_factor >= 20:
        #critical Hit
        player_atk = random.randrange(player_atk_minimum, player_atk_maximium) + player_atk_buff
        monster_hp = monster_hp - player_atk
        print('<<You Dealt ({}) Critical Damage To ({})! ({}) Health Is Now ({}) And Is Dazed>>'.format(player_atk, monster_name, monster_name, monster_hp))
        if monster_hp < 5:
            print('<<It\'s Almost Dead!>>')
            player_input()
        elif monster_hp <= 0:
            combat_end()
        else:
            player_input()
    elif AP_factor > monster_AP:
        #normal hit
        player_atk = random.randrange(player_atk_minimum, player_atk_maximium) + player_atk_buff
        monster_hp = monster_hp - player_atk
        if monster_hp <= 0:
            combat_end()
        elif monster_hp < 5:
            print('<<You Dealt ({}) Damage To ({})! ({}) Health Is Now ({})>>'.format(player_atk, monster_name, monster_name, monster_hp))
            print('<<It\'s Almost Dead!>>')
            monster_turn()
        else:
            print('<<You Dealt ({}) Damage To ({})! ({}) Health Is Now ({})>>'.format(player_atk, monster_name, monster_name, monster_hp))
            monster_turn()

    else:
        print('<<You Missed!>>')
        monster_turn()



def run():
    action13 = input('?')
    if re.match(r'^(run|yes|y|yeet)$', action13.lower()) != None:
        run_factor = random.randrange(1, 21) + player_run_buff
        if run_factor > 9:
            print('<<You Ran Away!>>')
        else:
            print('<<Your Attempt To Run Failed!>>')
            monster_turn()
    elif  re.match(r'^(no|n|cancel)$', action13.lower()) != None:
        player_input()
    else:
        print('Please Input A Valide Answer.')
        run()



def magic():
    if player_magic_buff > 0:
        action16 = input('')
    else:
        print('You don\'t have any magic!')
        player_input()





def combat_end():
    global player_xp
    player_xp = player_xp + monster_xp
    print('<<You Killed The <{}>! You Gained {}xp!>>'.format(monster_name, monster_xp))



def monster_turn():
    global player_hp
    global monster_status_duration
    # reset ability starting if set
    if 'ability starting' in variables:
        variables.pop('ability starting', None)
        monster_status_duration = 0
    # reduce duration by 1
    if monster_status_duration > 0:
        monster_status_duration = monster_status_duration - 1
    # if duration is 0, remove the ability status from the monster
    if monster_status_duration == 0 and 'status' in variables:
            status = variables.pop('status', None)
            print('monster_turn removing status:{}'.format(status))
    # check if using ability
    if 'ability' in variables and random.randrange(1,5) == 1:
        # apply ability - set duration to start duration
        if monster_status_duration == 0:
            variables['status'] = 7
            monster_status_duration = reset_status_duration
            monster_hit = random.randrange(monster_hit_minimum, monster_hit_maximum)
            monster_hit = monster_hit + initial_monster_status_damage
            player_hp = player_hp - monster_hit
            print('<< ({}) Used ({}) ! It Dealt ({})! Health Is Now ({})! >>'.format(monster_name, ability_name, monster_hit, player_hp))
            player_input()
        else:
            monster_hit = random.randrange(monster_hit_minimum, monster_hit_maximum)
            monster_hit =  monster_hit + monster_status_damage
            player_hp = player_hp - monster_hit
            print(' << ({}) Dealt ({}) Damage! Health Is Now ({})! The ({}) added ({}) of the damage taken>>'.format(monster_name, monster_hit, player_hp, ability_name, monster_status_damage))
            player_input()
    else:
        monster_hit = random.randrange(monster_hit_minimum, monster_hit_maximum)
        if 'status' in variables:
            monster_hit = monster_hit + monster_status_damage
            player_hp = player_hp - monster_hit
            print(' << ({}) Dealt ({}) Damage! Health Is Now ({})! The ({}) added ({}) of the damage taken>>'.format(monster_name, monster_hit, player_hp, ability_name, monster_status_damage))
            player_input()
        else:
            player_hp = player_hp - monster_hit
            print('<< ({}) Dealt ({}) Damage! Health Is Now ({})!>>'.format(monster_name, monster_hit, player_hp))
            player_input()




def player_death():
    print('<<YOU DIED>>')






combat_intro()
# combat_intro()
# TEMP debug monster_turn

#auto pick monster for encounter
