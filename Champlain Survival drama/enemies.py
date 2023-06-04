import string
import random
import re
import copy
import sys
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#Variables that I will be using, things like health and damage. Global becuase I need to change their values in the functions
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#Any variable that has a "$" in it should have the symbole be treated as a plus sign ("+"). These will most often be used to avoid using the word "buff".
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#This dictionary contains buff stats for the player.
global player_buff
player_buff = {
    'atk_min$':0,
    'atk_max$':0,
    'hp$':0,
    'luck$':0,
    'speed$':0,
                }

#This dictionary contains basic stats for the player.
global player_stat
player_stat = {
    'atk_min' :100 + player_buff['atk_min$'],
    'atk_max' :300 + player_buff['atk_max$'],
    'hp' :1000 + player_buff['hp$'],
    'luck' :-30 + player_buff['luck$'],
    'speed' :60 + player_buff['speed$'],
    'karma' :0
               }

#This dictionary contains all the stats for the enemies.

#Wolfe Jameson
WJ = {
    'name': 'Wolfe Jameson',
    'atk_min': 200,
    'atk_max': 300,
    'hp': 4750,
    'luck': 40,
    'speed': 53,
    'karma' :0
     }

#Prochridge Quakers
PQ = {
    'name': 'Prochridge Quakers',
    'atk_min': 250,
    'atk_max': 350,
    'hp': 6000,
    'luck': 30,
    'speed': 40,
    'karma' :0
     }

#Jahseh Von Avon Ayvon
JVA = {
    'name': 'Jahseh Von Avon Ayvon',
    'atk_min': 150,
    'atk_max': 250,
    'hp': 5250,
    'luck': 30,
    'speed': 69,
    'karma' :0
      }

#Smelly Pete
SP = {
    'name': 'Smelly Pete',
    'atk_min': 350,
    'atk_max': 450,
    'hp': 7500,
    'luck': 10,
    'speed': 55,
    'karma' :0
     }

#Sherlock Choochenstein
SC = {
   'name' :'Sherlock Choochenstein',
   'atk_min' :150,
   'atk_max' :250,
   'hp' :9450,
   'luck' :40,
   'speed' :69,
   'karma' :0
    }

#Gustopher J. Joosom
gus = {
    'name' :'Gustopher J. Joosom',
    'atk_min' :250,
    'atk_max' :350,
    'hp' :6700,
    'luck' :20,
    'speed' :44,
    'karma' :0
      }

#Mr. Mihi Yagi
MY = {
    'name' :'Mr. Mihi Yagi',
    'atk_min' :200,
    'atk_max' :300,
    'hp' :5750,
    'luck' :50,
    'speed' :51,
    'karma' :0
     }

#These dictionaries contain all the stats for regular enemies.

#Bear
bear = {
    'name' :'Bear',
    'atk_min' :450,
    'atk_max' :600,
    'hp' :1000,
    'luck' :0,
    'speed' :70,
    'karma' :0
       }

#Iroquoi foot soldier
Ifs = {
    'name' :'Iroquoi foot soldier',
    'atk_min' :350,
    'atk_max' :450,
    'hp' :7500,
    'luck' :50,
    'speed' :60,
    'karma' :-10
      }

#Iroquoi archer
Ia = {
    'name' :'Iroquoi archer',
    'atk_min' :450,
    'atk_max' :600,
    'hp' :5000,
    'luck' :70,
    'speed' :50,
    'karma' :-10
     }

#Iroquoi shaman
Is = {
    'name' :'Iroquoi shaman',
    'atk_min' :7500,
    'atk_max' :1000,
    'hp' :4500,
    'luck' : 60,
    'speed' :40,
    'karma' :-10
}

#wolf
wolf = {
    'name' :'wolf',
    'atk_min' :100,
    'atk_max' :150,
    'hp' :250,
    'luck' :0,
    'speed' :100,
    'karma' :0
}

#beaver
beaver = {
    'name' :'beaver',
    'atk_min' :10,
    'atk_max' :20,
    'hp' :100,
    'luck' :0,
    'speed' :50,
    'karma' :0
}
#This let's me color my text :)
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

#This acts as the dictioanry we'll be using in our applications
mob = {}

#List of dictrionaries that contain enemies
enemies = ['WJ', 'PQ', 'SP', 'JVA', 'SC', 'gus', 'MY', 'bear', 'Ifs', 'Ia', 'Is', 'wolf', 'beaver']

#These lines determine which enemie you will fight

key = random.randrange(1, len(enemies))
if key == 1:
    mob = WJ.copy()
elif key == 2:
    mob = PQ.copy()
elif key == 3:
    mob = SP.copy()
elif key == 4:
    mob = JVA.copy()
elif key == 5:
    mob = SC.copy()
elif key == 6:
    mob = gus.copy()
elif key == 7:
    mob = MY.copy()
elif key == 8:
    mob = bear.copy()
elif key == 9:
    mob = Ifs.copy()
elif key == 10:
    mob = Ia.copy()
elif key == 11:
    mob = Is.copy()
elif key == 12:
    mob = wolf.copy()
elif key == 13:
    mob = beaver.copy()

#This function introduces the enemie
def intro():
    print(bcolors.WARNING + '<< You Engaged Comabt With ({}), They Have ({}hp)! >>'.format(mob['name'], mob['hp']) + bcolors.ENDC)
    player_stat['karma'] = player_stat['karma'] - mob['karma']
    inputs()

#This function asks for the player's input
def inputs():
    action = input(bcolors.BOLD + bcolors.UNDERLINE + '<< What Do You Want To Do? [Attack]--[Run] >>' + bcolors.ENDC)
    if re.match(r'^(attack|atk|1)$', action.lower()) != None:
        attack()
    elif re.match(r'^(run|2)$', action.lower()) != None:
        run()
    else:
        invalid()
        inputs()

#This function checks for crits for the damage function, for the player
def is_critical():
    crit = random.randrange(1,101)
    if crit <= player_stat['luck']:
        return True
    return False

#This function checks for enemie crits
def enemie_crit():
    crit = random.randrange(1,101)
    if crit <= mob['luck']:
        return True
    return False

#This function deals with whenever the player inputs a response that isn't valid. I'm lazy and don't feel like typing the print function everytime. :3
def invalid():
    print ('\033[1m \033[91m \033[4m' +  "~~~PLEASE INPUT A VALID RESPONSE~~~\n" + '\033[0m')

#This function just reduces repetition, it's has the inputs and the function calls, that simply get repeated a few times, so I want to reduce the amount of lines im using with this function. This is used in the attack function.
def attack_comfirm(hit_chance, is_crit=False):
    comfirmation = input('<< Want To Proceed? [Yes]--[No] >>')
    if re.match(r'^(yes|ye|y|1)$', comfirmation.lower()) != None:
        damage(hit_chance, is_crit)
    elif re.match(r'^(no|n|2)$', comfirmation.lower()) != None:
        inputs()
    else:
        invalid()
        attack_comfirm(hit_chance, is_crit=False)

#This function deals with applying player damage to enemies
def attack():
    is_crit = is_critical()
    hit_chance = (mob['speed']/player_stat['speed'])*100 + (player_stat['luck']/2) - (mob['luck']/2)
    if hit_chance <= 0:
        hit_chance = 1
    if mob['speed'] <= 0:
        hit_chance = 95
    attack_rsp = input('<< Would You Like To See Your Hit Chance? [Yes]--[No] >>')
    if re.match(r'^(yes|ye|y|1)$', attack_rsp.lower()) != None:
        print(bcolors.FAIL + bcolors.UNDERLINE + '<< You Have a' + bcolors.OKCYAN + '({}%)'.format(hit_chance) + bcolors.FAIL + 'Chance To Hit! >>' + bcolors.ENDC)
        attack_comfirm(hit_chance, is_crit)
    elif re.match(r'^(no|n|2)$', attack_rsp.lower()) != None:
        attack_comfirm(hit_chance)
    else:
        invalid()
        attack()

#This function serves the same purpose as attack_comfirm, just lowering the line count.
def run_comfirmation():
    comfirmation = input('<< Want To Proceed? [Yes]--[No] >>')
    if re.match(r'^(yes|ye|y|1)$', comfirmation.lower()) != None:
        run = random.randrange(1,101)
        if run <= run_chance:
            print('<< You Successfully Ran Away! >>')
            escaped()
        else:
            print('<< Your Run Attempt Failed... >>')
            enemie_turn()
    elif re.match(r'^(no|n|2)$', comfirmation.lower()) != None:
        inputs()
    else:
        invalid()
        run_comfirmation()

#This function performs the running action
def run():
    run_chance = (mob['speed']/(player_stat['speed']/2))*100 + (player_stat['luck']/2) - (mob['luck']/2)
    escape = input('<< Would You Like To See Your Run Chance? [Yes]--[No] >>')
    if re.match(r'^(yes|ye|y|1)$', escape.lower()) != None:
        print('<< You Have a ({}%) Chance To Hit! >>'.format(run_chance))
        run_comfirmation()
    elif re.match(r'^(no|n|2)$', escape.lower()) != None:
        run_comfirmation()
    else:
        invalid()
        run()

#This function processes the enemies turn + the critical gives the monster more damage output
def enemie_turn(critical = False):
    hit_chance = (player_stat['speed']/mob['speed'])*100 - (player_stat['luck']/2) + (mob['luck']/2)

#This function also for lower line count, man im doing a lot of these eh?
def almost_ded():
    if mob['hp'] <= mob['hp']/3:
        print('<< It\'s Almost Dead! >>')
    else:
        enemie_turn()

#This function does the damage calculations for the player's turn + the critical skips the monster's turn.
def damage(hit_chance, is_crit=False):
    damage = random.randrange(player_stat['atk_min'], (player_stat['atk_max'] + 1))
    if hit_chance >= random.randrange(1,101):
        if is_crit:
            damage = damage * 1.5
            mob['hp'] = mob['hp'] - damage
            print(bcolors.OKGREEN + bcolors.UNDERLINE + '<< You Dealt' + bcolors.OKCYAN + '({})'.format(damage) + bcolors.OKGREEN + 'Critical Damage To ({})! ({}) Health Is Now'.format(mob['name'], mob['name']) + bcolors.OKCYAN + '({}hp)'.format(mob['hp']) + bcolors.OKGREEN + '! >>' + bcolors.ENDC)
            check_death()
            almost_ded()
        if is_crit == False:
            mob['hp'] = mob['hp'] - damage
            print(bcolors.OKGREEN + '<< You Dealt' + bcolors.OKCYAN + '({})'.format(damage) + bcolors.OKGREEN + 'Damage To ({})! ({}) Health Is Now'.format(mob['name'], mob['name']) + bcolors.OKCYAN + '({}hp)'.format(mob['hp']) + bcolors.OKGREEN + '>>' + bcolors.ENDC)
            check_death()
            almost_ded()
    else:
        print(bcolors.WARNING + '<< You Didn\'t Land Your Hit... >>' + bcolors.ENDC)
        enemie_turn()

def enemie_turn():
    hit_chance = (player_stat['speed']/mob['speed'])*100 - (player_stat['luck']/2) + (mob['luck']/2)
    damage = random.randrange(mob['atk_min'], (mob['atk_max'] + 1))
    is_crit = enemie_crit()
    if hit_chance >= random.randrange(1,101):
        player_stat['hp'] = player_stat['hp'] - damage
        print(bcolors.FAIL + '<< ({}) Dealt'.format(mob['name']) + bcolors.WARNING + '({})'.format(damage) + bcolors.FAIL + 'Damage! Your Health Is Now' + bcolors.WARNING + '({}hp)'.format(player_stat['hp']) + bcolors.FAIL + '>>' + bcolors.ENDC)
        check_death()
        inputs()
    if is_crit:
        damage = damage * 1.5
        player_stat['hp'] = player_stat['hp'] - damage
        print(bcolors.FAIL + bcolors.UNDERLINE + '<< ({}) Dealt'.format(mob['name'])  + bcolors.WARNING + '({})'.format(damage) + bcolors.FAIL +  'Critical Damage! Your Health Is Now' + bcolors.WARNING + '({}hp)'.format(player_stat['hp']) + bcolors.FAIL + '>>'.format(mob['name'], damage, player_stat['hp']) + bcolors.ENDC)
        check_death()
        inputs()
    else:
        print(bcolors.OKGREEN + '<< ({}) Didn\'t Land It\'s Hit... >>'.format(mob['name']) + bcolors.ENDC)
        inputs()

def check_death():
    if player_stat['hp'] <= 0:
        print (bcolors.UNDERLINE + bcolors.WARNING + '~~~' + bcolors.FAIL +  "YOU DIED" + bcolors.WARNING + '~~~' + bcolors.ENDC)
        sys.exit()
    if mob['hp'] <= 0:
        print(bcolors.OKGREEN + '<< You Killed ({})!'.format(mob['name']) + bcolors.ENDC)
        if mob['karma'] == 0 - 10:
            print(bcolors.WARNING + 'Victory is yours, but was it worth the cost of innocent blood?' + bcolors.ENDC)
        sys.exit()
    return False

intro()
