global player_xp
player_xp = 0
global skills
skills = {}
global variables
variables = {}
import string
import random
import re



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





def skills_check():
            if 'sucker punch' in skills and 'self esteem' in skills:
                print('<<You have the skills [Sucker Punch] & [Self Esteem]!>>')
                roam()
            elif 'sucker punch' in skills:
                print('<<You have the skill [Sucker Punch]!>>')
                roam()
            elif 'self esteem' in skills:
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
        if 'sucker punch' in skills:
                print('<<You already have the skill [Sucker Punch]!>>')
        elif player_xp >= 8:
            player_xp = player_xp - 8
            skills ['sucker punch'] = 8
            print('<<You\'ve Obtained [Sucker Punch]!>>')
            roam()
        else:
            print('<<Sorry, you don\'t have enough \"xp\">> ')
            roam()
    elif re.match(r'^(Self Esteem|2)$', action12.lower()) != None:
        if 'self esteem' in skills:
            print('<<You already have the skill [Self Esteem]!>>')
        elif player_xp >= 8:
            player_xp = player_xp - 8
            skills ['self esteem'] = 9
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
    if 'sucker punch' in skills:
        print('<<You obtained the skill [Sucker Punch]!>>')
        skills.pop ('sucker punch', None)
    elif 'self esteem' in skills:
        print('<<You obtained the skill [Self Esteem]!>>')
        skills.pop ('self esteem', None)



goblin_combat_end()
