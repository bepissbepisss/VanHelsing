import string
import random
import re
global player_atk_buff
player_atk_buff = 0
global player_hp_buff
player_hp_buff = 0
global inventory
inventory = {}
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
global skill_1_cooldown
skill_1_cooldown = 0
global skill_2_cooldown
skill_2_cooldown = 0
global player_luck_buff
player_luck_buff = 0
global cooldowns
cooldowns = {}
global variables
variables = {}
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
equipment = {
    'weapons': {
        'sword': 4,
        'rock': 1
    },
    'armour': {
        'shield': 5,
        'stool': 3
    }
}


def equip():
    global player_atk_buff
    global player_hp_buff
    action = input('Choose your equipment or Check your stats!')
    if re.match(r'^(weapons|weapon|1)$', action.lower()) != None:
        action2 = input('What weapon would you like to equip?')
        if re.match(r'^(sword)$', action2.lower()) != None:
            if 'sword' in inventory:
                print('You already have <<sword>> equiped!')
                equip()
            elif 'rock' in inventory:
                action3 = input('<<Sword>> will replace <<Rock>>. Are you sure you want to proceed?')
                if re.match(r'^(yes|proceed|y|yeet|ya)$', action3.lower()) != None:
                    print ('You equiped <<sword>>!')
                    player_atk_buff = 0
                    weapons = equipment['weapons']['sword']
                    player_atk_buff = player_atk_buff + weapons
                    inventory ['sword'] = 1
                    inventory.pop('rock', None)
                    equip()
                elif re.match(r'^(no|nah)$', action3.lower()) != None:
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
        elif re.match(r'^(rock)$', action2.lower()) != None:
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
        elif re.match(r'^(no|nah|back|go back)$', action2.lower()) != None:
            equip()
        else:
            print('Please Input A Valide Answer.')
            equip()
    elif re.match(r'^(armour|2)$', action.lower()) != None:
        action5 = input('What armour would you like to equip?')
        if re.match(r'^(shield)$', action5.lower()) != None:
            if 'shield' in inventory:
                print('You already have <<shield>> equiped!')
                equip()
            elif 'stool' in inventory:
                action6 = input('<<Shield>> will replace <<stool>>. Are you sure you want to proceed?')
                if re.match(r'^(yes|proceed|y|yeet|ya)$', action6.lower()) != None:
                    print('You equiped <<Shield>>!')
                    player_hp_buff = 0
                    armour = equipment['armour']['shield']
                    player_hp_buff = player_hp_buff + armour
                    inventory.pop('stool', None)
                    equip()
                elif re.match(r'^(no|nah)$', action6.lower()) != None:
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
        elif re.match(r'^(stool)$', action5.lower()) != None:
            if 'stool' in inventory:
                print('You already have <<stool>> equiped!')
                equip()
            if 'shield' in inventory:
                action7 = input('<<stool>> will replace <<Shield>>. Are you sure you want to proceed?')
                if re.match(r'^(yes|proceed|y|yeet|ya)$', action7.lower()) != None:
                    print('You equiped <<stool>>!')
                    player_hp_buff = 0
                    armour = equipment['armour']['stool']
                    player_hp_buff = player_hp_buff + armour
                    inventory.pop('shield', None)
                    equip()
                elif re.match(r'^(no|nah)$', action7.lower()) != None:
                    equip()
                else:
                    print('Please Input A Valide Answer.')
                    equip()
            else:
                print('You equiped <<stool>>!')
                armour = equipment['armour']['stool']
                player_hp_buff = player_hp_buff + armour
                inventory ['stool'] = 4
                equip()
        elif re.match(r'^(no|nah|back|go back)$', action5.lower()) != None:
            equip()
    elif re.match(r'^(stat|stats|3)$', action.lower()) != None:
        check_player_stats()
    elif re.match(r'^(remove|unequip|get rid off|discard)$',action.lower()) != None:
        unequip()
    elif re.match(r'^(engage|combat|fight|goblin)$',action.lower()) != None:
        goblin_combat_intro()
    elif re.match(r'^(skill|skill tree|xp|exp|skills)$', action.lower()) != None:
        roam()
    else:
        print('Please Input A Valide Answer.')
        equip()



def check_player_stats():
    action8 = input('Would you like to check your stats?')
    if re.match(r'^(yes|y|ye|yeet|stats)$', action8.lower()) != None:
        print('atk {}|hp{}'.format(player_atk_buff, player_hp_buff))
        equip()
    elif re.match(r'^(no|nah|back|go back)$', action8.lower()) != None:
        equip()
    else:
        print('Please Input A Valide Answer.')
        check()

def unequip():
    action9 = input('Would you like to unequip all equipped items?')
    if re.match(r'^(yes|y|ye|yeet|unequip|remove|get rid of)$', action9.lower()) != None:
        empty_check()
        equip()
    elif re.match(r'^(no|n|negative|nah)$', action9.lower()) != None:
        equip()
    else:
        print('Please Input A Valide Answer.')
        unequip()

def empty_check():
    global player_atk_buff
    if 'no weapon' in variables:
        inventory.pop('no weapon', None)
        empty_check_armour()
    elif 'sword' in inventory:
        inventory.pop('sword', None)
        weapons = equipment['weapons']['sword']
        player_atk_buff = player_atk_buff - weapons
        if player_atk_buff == 0:
            variables ['no weapon'] = 5
            empty_check()
        else:
            empty_check()
    elif 'rock' in inventory:
        inventory.pop('rock', None)
        weapons = equipment['weapons']['rock']
        player_atk_buff = player_atk_buff - weapons
        if player_atk_buff == 0:
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
            inventory ['no armour'] = 6
            empty_check_armour()
        else:
            empty_check_armour()
    elif 'stool' in inventory:
        inventory.pop('stool', None)
        armour = equipment['armour']['stool']
        player_hp_buff = player_hp_buff - armour
        if player_hp_buff ==  0:
            variables ['no armour'] = 6
            empty_check_armour()
        else:
            empty_check_armour()
    else:
        print('All items unequipped!')
        equip()

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
monsters = {
    'goblin': {
        'xp': random.randrange(8, 11),
        'hp': 10,
        'AP': 5,
        'hit':{
            'minimum':1,
            'maximum':3
        }
    },
    'orc': {
        'xp':random.randrange(16, 20),
        'hp': 20,
        'hit':{
            'minimum':2,
            'maximum':4
            }
    },
}
#.///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def skills_check():
            if 'sucker punch' in inventory and 'self esteem' in inventory:
                print('<<You have the skills [Sucker Punch] & [Self Esteem]!>>')
                roam()
            elif 'sucker punch' in inventory:
                print('<<You have the skill [Sucker Punch]!>>')
                roam()
            elif 'self esteem' in inventory:
                print('<<You have the skill [Self Esteem]!>>')
                roam()
            else:
                print('<<You have no skills>>')
                roam()


def xp_check():
    print('{}xp'.format(player_xp))

def check():
    action10 = input('Skills or Xp?')
    if re.match(r'^(skills|skill)$', action10.lower()) != None:
        skills_check()
        roam()
    elif re.match(r'^(xp)$', action10.lower()) != None:
        xp_check()
        roam()
    else:
        print('Please Input A Valide Answer.')
        check()



def roam():
    action11 = input('<<What would you like to do?>>')
    if re.match(r'^(skill|skill tree|xp|exp|skills)$', action11.lower()) != None:
        skill_tree()
    elif re.match(r'^(engage|combat|fight|goblin)$',action11.lower()) != None:
        goblin_combat_intro()
    elif re.match(r'^(check xp|look at xp)$', action11.lower()) != None:
        xp_check()
        roam()
    elif re.match(r'^(check skill|check skills|list|list of skills)$', action11.lower()) != None:
        skills_check()
        roam()
    elif re.match(r'^(check)$', action11.lower()) != None:
        check()
    elif re.match(r'^(equip|equipement|weapons|armour|items)$', action11.lower()) != None:
        equip()
    else:
        print('Please Input A Valide Answer.')
        roam()

def goblin_combat_end():
    global player_xp
    player_xp = player_xp + monsters['goblin']['xp']
    print('<<You Killed The <Goblin>! You Gained {}xp!>>'.format(monsters['goblin']['xp']))
    roam()

def skill_tree():
    global player_xp
    action12 = input('<<You have {}xp to spend. Please choose the following>>            Skills-- (1)[Sucker Punch]~deal 2x more damage <Cost~8xp> / (2)[Self Esteem]~Either take 1 damage or heal 3 <Cost~8xp>'.format(player_xp))
    if re.match(r'^(Sucker Punch|1)$', action12.lower()) != None:
        if 'sucker punch' in inventory:
                print('<<You already have the skill [Sucker Punch]!>>')
        elif player_xp >= 8:
            player_xp = player_xp - 8
            inventory ['sucker punch'] = 8
            print('<<You\'ve Obtained [Sucker Punch]!>>')
            roam()
        else:
            print('<<Sorry, you don\'t have enough \"xp\">> ')
            roam()
    elif re.match(r'^(Self Esteem|2)$', action12.lower()) != None:
        if 'self esteem' in inventory:
            print('<<You already have the skill [Self Esteem]!>>')
        elif player_xp >= 8:
            player_xp = player_xp - 8
            inventory ['self esteem'] = 9
            print('<<You\'ve Obtained [Self Esteem]!>>')
            roam()
        else:
            print('<<Sorry, you don\'t have enough \"xp\">> ')
            roam()
    elif re.match(r'^(back|no|n|cancel|redo|return)$', action12.lower()) != None:
        roam()
    else:
            print('Please Input A Valide Answer.')
            skill_tree()

def skills_check_other():
    if 'sucker punch' in inventory:
        print('<<You obtained the skill [Sucker Punch]!>>')
        inventory.pop ('sucker punch', None)
    elif 'self esteem' in inventory:
        print('<<You obtained the skill [Self Esteem]!>>')
        inventory.pop ('self esteem', None)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def goblin_combat_intro():
    print('<<You Engage Combat With The Goblin!>>')
    if monsters['goblin']['hp'] <= 0:
        variables ['dead goblin'] = 7
    if 'dead goblin' in variables:
        variables.pop('dead goblin', None)
        monsters['goblin']['hp'] = 10
    goblin_combat()

def goblin_combat_end():
    global player_xp
    global skill_1_cooldown
    global skill_2_cooldown
    player_xp = player_xp + monsters['goblin']['xp']
    print('<<You Killed The <Goblin>! You Gained {}xp!>>'.format(monsters['goblin']['xp']))
    if skill_1_cooldown < 0:
        skill_1_cooldown = skill_1_cooldown - skill_1_cooldown
        roam()
    if skill_1_cooldown > 0:
        skill_1_cooldown = skill_1_cooldown - skill_1_cooldown
        roam()
    if skill_2_cooldown < 0:
        skill_2_cooldown = skill_2_cooldown - skill_2_cooldown
        roam()
    if skill_2_cooldown > 0:
        skill_2_cooldown = skill_2_cooldown - skill_2_cooldown
        roam()
    else:
        roam()

def goblin_turn():
    global player_hp
    monster_hit = random.randrange(monsters['goblin']['hit']['minimum'], monsters['goblin']['hit']['maximum'])
    player_hp = player_hp - monster_hit
    print('<< <Goblin> Dealt <{}> Damage! Health Is Now {}!>>'.format(monster_hit, player_hp))
    goblin_combat()

def player_death():
    print('<<YOU DIED>>')

def player_turn(critical=False):
    global player_atk_buff
    global skill_1_cooldown
    player_atk = random.randrange(player_atk_minimum, player_atk_maximium) + player_atk_buff
    if 'skill 1' in inventory:
        inventory.pop('skill 1', None)
        player_atk = player_atk * 2
        skill_1_cooldown = skill_1_cooldown + 5
        monsters['goblin']['hp'] = monsters['goblin']['hp'] - player_atk
        print('<<You Dealt <{}> Damage To <Goblin>! <Golbin> Health Is Now {}>>'.format(player_atk, monsters['goblin']['hp']))
    monsters['goblin']['hp'] = monsters['goblin']['hp'] - player_atk
    if critical:
        critical_text='<<You Dealt <{}> Critical Damage To <Goblin>! <Golbin> Health Is Now {} And Is Dazed>>'.format(player_atk, monsters['goblin']['hp'])
        if monsters['goblin']['hp'] < 5:
            print('<<It\'s Almost Dead!>>')
            goblin_combat()
        else:
            goblin_combat()

    elif monsters['goblin']['hp'] <= 0:
        goblin_combat_end()
    elif monsters['goblin']['hp'] < 5:
        print('<<You Dealt <{}> Damage To <Goblin>! <Golbin> Health Is Now {}>>'.format(player_atk, monsters['goblin']['hp']))
        print('<<It\'s Almost Dead!>>')
        goblin_turn()
    else:
        print('<<You Dealt <{}> Damage To <Goblin>! <Golbin> Health Is Now {}>>'.format(player_atk, monsters['goblin']['hp']))
        goblin_turn()

def run():
    action13 = input('?')
    if re.match(r'^(run|yes|y|yeet)$', action13.lower()) != None:
        run_factor = random.randrange(1, 21) + player_run_buff
        if run_factor > 9:
            print('<<You Ran Away!>>')
        else:
            print('<<Your Attempt To Run Failed!>>')
            goblin_turn()
    elif  re.match(r'^(no|n|cancel)$', action13.lower()) != None:
        goblin_combat()
    else:
        print('Please Input A Valide Answer.')
        run()

def attack():
    action14 = input('?')
    AP_factor = random.randrange(1, 21) + player_AP_buff
    if re.match(r'^(hit|atk|attack|yes|y|yeet)$', action14.lower()) != None:
        if AP_factor >= 20:
            player_turn(True)
        elif AP_factor > monsters['goblin']['AP']:
            player_turn()
        else:
            print('<<You Missed!>>')
            goblin_turn()
    elif re.match(r'^(no|n|cancel)$', action14.lower()) != None:
        goblin_combat()
    else:
        print('Please Input A Valide Answer.')
        attack()

def goblin_combat():
    global skill_1_cooldown
    global skill_2_cooldown
    if monsters['goblin']['hp'] <= 0:
        variables ['dead goblin'] = 7
        goblin_combat_end()
    elif player_hp <= 0:
        player_death()
    else:
        action15 = input('<<Attack>>  <<Run>>  <<Skill>>')
        if 'cooldown_1' in inventory:
            cooldowns.pop('cooldown_1', None)
        elif skill_1_cooldown > 0:
            skill_1_cooldown = skill_1_cooldown - 1
        if 'cooldown_2' in inventory:
            cooldowns.pop('cooldown_2', None)
        elif skill_2_cooldown > 0:
            skill_2_cooldown = skill_2_cooldown - 1
        if re.match(r'^(attack|atk|1|hit)$', action15.lower()) != None:
            AP_chance = (10 + player_AP_buff) / 20 * 100
            print('<<You Have A {}% Chance Of Landing Your Hit. Are You Sure You Want To Proceed?>>'.format(AP_chance))
            attack()
        elif re.match(r'^(run|escape|2|leave)$', action15.lower()) != None:
            run_chance = (10 + player_run_buff) / 20 * 100
            print('<<You Have A {}% Chance Of Running. Are You Sure You Want To Proceed?>>'.format(run_chance))
            run()
            print('Please Input A Valide Answer.')
        elif re.match(r'^(skills|skill|ability|abilities)$',action15.lower()) != None:
            if 'sucker punch' in inventory and 'self esteem' in inventory:
                print('<<You have the skills [Sucker Punch] & [Self Esteem]!>>')
                action16 = input('Which skill do you want to use?')
                if re.match(r'^(sucker punch|suckerpunch|1|first)$',action16.lower()) != None:
                    if skill_1_cooldown <= 0:
                        inventory['skill 1'] = 10
                        player_turn()
                    else:
                        print('<<You have a {} turn cooldown for this skill>>'.format(skill_1_cooldown))
                        cooldowns['cooldown_1'] = 12
                        goblin_combat()
                elif re.match(r'^(self esteem|selfesteem|2|second)$',action16.lower()) != None:
                    if skill_2_cooldown <= 0:
                        inventory ['skill 2'] = 11
                        selfesteem()
                    else:
                        print('<<You have a {} turn cooldown for this skill>>'.format(skill_2_cooldown))
                        cooldowns['cooldown_2'] = 13
                        goblin_combat()
                else:
                    print('Please Input A Valide Answer')
            elif 'sucker punch' in inventory:
                print('<<You have the skill [Sucker Punch]!>>')
                action17 = input('Do you want to use this skill?')
                if re.match(r'^(y|yes|sure)$',action17.lower()) != None:
                    if skill_1_cooldown <= 0:
                        inventory ['skill 1'] = 10
                        player_turn()
                    else:
                        print('<<You have a {} turn cooldown for this skill>>'.format(skill_1_cooldown))
                        cooldowns['cooldown_1'] = 12
                        goblin_combat()
                else:
                    print('Please Input A Valide Answer.')
                    goblin_combat()
            elif 'self esteem' in inventory:
                print('<<You have the skill [Self Esteem]!>>')
                action17 = input('Do you want to use this skill?')
                if re.match(r'^(y|yes|sure)$',action17.lower()) != None:
                    if skill_2_cooldown <= 0:
                        inventory ['skill 2'] = 11
                        selfesteem()
                    else:
                        print('<<You have a {} turn cooldown for this skill>>'.format(skill_2_cooldown))
                        cooldowns['cooldown_2'] = 13
                        goblin_combat()
                else:
                    print('Please Input A Valide Answer.')
                    goblin_combat()
            else:
                print('<<You have no skills>>')
                goblin_combat()

        else:
            print('Please Input A Valide Answer.')
            goblin_combat()

def selfesteem():
    global player_hp
    global skill_2_cooldown
    if 'skill 2' in cooldowns:
        cooldowns.pop('skill 2', None)
        chance = random.randrange(1, 4) + player_luck_buff
        skill_2_cooldown = skill_2_cooldown + 3
        if chance >= 2:
            player_hp = player_hp + 3
            print('<<You Rocovered <3> Vitality! Your Health Is Now <{}>! (good at game) >>'.format(player_hp))
            goblin_turn()
        else:
            player_hp = player_hp - 1
            print('<<You Took <1> Self Damage! Your Health Is Now <{}>! (bad at game)>>'.format(player_hp))
            goblin_turn()

# starting {X}
# load monster {x}
# load player
# player attacks
# is monster dead
#   y - get xp
# monster attacks
#add hit or miss factor
#Random monster picker, Make a list from which the program can randomly pick a monster, Variables are already held withine the dictionary
#Added Return function
#Get the skills to work in Combat!!!




equip()
