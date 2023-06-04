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

#This dictionary has all presently equiped player items
global equiped
equiped = {}

#This dictionary let's me store variables to tell me wether or not the player has completed an event or not
global variable
variable = {}
#This dictionary is the players inventory
global inventory
inventory = {
    'cooked meat' : {
        'healing' : 250,
        'quantity' : 5,
        'value' : 2.5,
        'trait' : 'weapon',
        'discription' : ('Restores 250 hp.')
                    },
    'arrow' : {
        'atk min' : 1,
        'atk max' : 2,
        'atk min y' : 10,
        'atk max y' : 15,
        'stagger' : 20,
        'quantity' : 0,
        'value' : 1,
        'trait' : 'ammo',
        'discription' : ('Has a 20% chance to stagger enemies.')
               },
    'bow' : {
        'atk min' : 1,
        'atk max' : 2,
        'atk min x' : 2,
        'atk max x' : 2.5,
        'quantity' : 0,
        'value' : 15,
        'trait' : 'weapon',
        'discription' : ('Makes arrows hit twice or twice and a half as hard.')
            },
    'bandage' : {
        'healing' : 400,
        'clotting' : 10000,
        'quantity' : 0,
        'value' : 3.5,
        'trait' : 'item',
        'discription' : ('Restores 400 hp, and removes any <<bleeding>> stacks.')
                },
    'war club' : {
        'atk min' : 30,
        'atk max' : 35,
        'blunt' : 2,
        'quantity' : 0,
        'value' : 20,
        'trait' : 'weapon',
        'discription' : ('May cause 2 stacks of <<blunt>>. Blunt reduces enemy attacks by 50%.')
                },
    'tomahawk' : {
        'atk min' : 10,
        'atk max' : 15,
        'bleeding' : 10,
        'quantity' : 0,
        'value' : 12.5,
        'trait' : 'weapon',
        'discription' : ('May cause 10 stacks of <<bleeding>>. Bleeding makes an enemy take 1% of their total health worth of damage per stack. Exceeding 50 stacks causes the enemy to bleedout.')
                },
    'sword' : {
        'atk min' : 40,
        'atk max' : 50,
        'bleeding' : 3,
        'quantity' : 1,
        'value' : 20,
        'trait' : 'weapon',
        'discription' : ('May cause 3 stacks of <<bleeding>>. Bleeding makes an enemy take 1% of their total health worth of damage per stack. Exceeding 50 stacks causes the enemy to bleedout.')
                },
    'shield' : {
        'atk min' : 1,
        'atk max' : 2,
        'block' : 100,
        'quantity': 1,
        'value' : 10,
        'trait' : 'weapon',
        'discription' : ('Has a chance to block 100 units of damage.')
                },
    'meat' : {
        'healing' : 50,
        'quantity' : 0,
        'value' : 3,
        'trait' : 'item',
        'discription' : ('Restores 50hp.')
            },
    'pelt' : {
        'quantity' : 0,
        'value' : 5,
        'trait' : 'misc.',
        'discription' : ('Sells for 5g.')
            },
    'wildlife attractor' : {
        'duration' : 15,
        'effect' : 5,
        'quantity' : 0,
        'value' : 15,
        'trait' : 'item',
        'discription' : ('Quintuples your chances of encounter wildlife. Last for 15 forest trips.')
                            },
    'beaver fur' : {
        'quantity' : 0,
        'value' : 10,
        'trait' : 'misc.',
        'discription' : ('Sells for 10g.')
                    },
    'alex\'s edge' : {
        'atk min' : 70,
        'atk max' : 80,
        'critical strike' : 20,
        'quantity' : 1,
        'value' : 50,
        'trait' : 'weapon',
        'discription' : ('Adds a 20% chance to crits.')
    }
            }


#This variable keeps track of active wildlife attractor effects
global attractor
attractor = 0

#This variable keeps track of experience
global xp
xp = 0


#This variable keeps track of needed experience
global req
req = 10


#This variable keeps track of the player's level
global lv
lv = 1

#This dictionary contains buff stats for the player.
global player_buff
player_buff = {
    'atk_min$':0,
    'atk_max$':0,
    'hp$':0,
    'luck$':0,
    'speed$':0,
    'blunt' :0,
    'bleeding' :0,
    'critical strike' : 0
                }

#This dictionary contains basic stats for the player.
global player_stat
player_stat = {
    'atk_min' :100 + player_buff['atk_min$'],
    'atk_max' :300 + player_buff['atk_max$'],
    'hp': 1000,
    'max hp' :1000 + player_buff['hp$'],
    'luck' :-30 + player_buff['luck$'],
    'speed' :60 + player_buff['speed$'],
    'karma' :0,
    'money' :10,
    'bleeding stacks' : 0,
    'experience' : xp/req,
    'level' : lv
               }

#This function will make the xp requirement go up, reset xp accordingly, and increase player lv.
def lv_up():
    global xp
    global req
    global lv
    while xp >= req:
        lv = lv + 1
        xp = xp - req
        req = req * 2
        player_stat['atk_min'] = player_stat['atk_min']*1.5
        player_stat['atk_max'] = player_stat['atk_max']*1.5
        player_stat['max hp'] = player_stat['max hp']*1.5
        player_stat['speed'] = player_stat['speed']*1.5
        print(bcolors.OKGREEN + 'You <<Leveled Up>>!' + bcolors.ENDC)
        print('({})atk min'.format(player_stat['atk_min']))
        print('({})atk max'.format(player_stat['atk_max']))
        print('({})hp'.format(player_stat['max hp']))
        print('({})speed'.format(player_stat['speed']))
    drop()


#wolf
wolf = {
    'name' :'wolf',
    'atk_min' :100,
    'atk_max' :150,
    'hp' :250,
    'reset hp' : 250,
    'luck' :0,
    'speed' :100,
    'karma' :0,
    'bleeding stacks' : 0,
    'blunt' : 0,
    'experience' : 3,
    'item' : 'pelt',
    'chance': 50
}

#beaver
beaver = {
    'name' :'beaver',
    'atk_min' :10,
    'atk_max' :20,
    'hp' :100,
    'reset hp' : 100,
    'luck' :0,
    'speed' :50,
    'karma' :0,
    'bleeding stacks' : 0,
    'blunt' : 0,
    'experience' : 1,
    'item' : 'beaver fur',
    'chance': 50
}

#Bear
bear = {
    'name' :'Bear',
    'atk_min' :450,
    'atk_max' :600,
    'hp' :1000,
    'reset hp' : 1000,
    'luck' :0,
    'speed' :70,
    'karma' :0,
    'bleeding stacks' : 0,
    'blunt' : 0,
    'experience' : 15,
    'item' : 'meat',
    'chance': 50
       }



#This acts as the dictionary we'll be using in our applications
global mob
mob = {}

#List of dictrionaries that contain enemies
enemies = ['bear','wolf', 'beaver']

#This function lets the player use items
def use(x):
    global attractor
    try:
        if inventory[x]['healing'] > 0:
            player_stat['hp'] = player_stat['hp'] +  inventory[x]['healing']
            inventory[x]['quantity'] = inventory[x]['quantity'] - 1
            print(bcolors.OKGREEN + 'You recovered ({})hp!'.format(inventory[x]['healing']) + bcolors.ENDC)
            if player_stat['hp'] >= player_stat['max hp']:
                player_stat['hp'] = player_stat['max hp']
                inven()
            inven()
    except:
        try:
            if inventory[x]['clotting'] > 0:
                player_stat['bleeding'] = player_stat['bleeding stacks'] -  inventory[x]['clotting']
                inventory[x]['quantity'] = inventory[x]['quantity'] - 1
                print(bcolors.OKGREEN + 'You stopped any bledding!' + bcolors.ENDC)
                if player_stat['bleeding'] < 0:
                    player_stat['bleeding'] = 0
                    inven()
                inven()
        except:
            if inventory[x]['duration'] > 0:
                attractor = attractor + inventory[x]['duration']
                inventory[x]['quantity'] = inventory[x]['quantity'] - 1
                print(bcolors.OKGREEN + 'You added ({}) worth of stacks to your wildlife attractor effect!'.format(inventory[x]['duration']) + bcolors.ENDC)
                inven()

#this function equipes items
def equipe(x):
    if 'weapon' in equiped:
        equiped.pop('weapon', None)
        player_buff['atk_min$'] = 0
        player_buff['atk_max$'] = 0
        player_buff['critical strike'] = 0
        player_buff['bleeding'] = 0
        player_buff['blunt'] = 0
    try:
        if inventory[x]['block'] >= 0:
            equiped['shield'] = 2
            inven()
    except:
        equiped['weapon'] = 1
        player_buff['atk_min$'] = player_buff['atk_min$'] + inventory[x]['atk min']
        player_buff['atk_max$'] = player_buff['atk_max$'] + inventory[x]['atk max']
        try:
            if inventory[x]['critical strike'] > 0:
                player_buff['critical strike'] = player_buff['critical strike'] + inventory[x]['critical strike']
        except:
            try:
                if inventory[x]['bleeding'] > 0:
                    player_buff['bleeding'] = player_buff['bleeding'] + inventory[x]['bleeding']
            except:
                try:
                    if inventory[x]['blunt'] > 0:
                        player_buff['blunt'] = player_buff['blunt'] + inventory[x]['blunt']
                        inven()
                except:
                    inven()

#This determines whether or not the player encounters an enemy
def check_encounter():
    global attractor
    global mob
    if attractor > 0:
        attractor = attractor - 1
        encounter = 50
        if random.randrange(1, 101) <= encounter:
            key = random.randrange(1, len(enemies)+1)
            if key == 1:
                mob = bear.copy()
            elif key == 2:
                mob = wolf.copy()
            elif key == 3:
                mob = beaver.copy()
            combat_intro()
        else:
            variable['nothing'] = 10
    else:
        encounter = 10
        if random.randrange(1, 101) <= encounter:
            #These lines determine which enemie you will fight
            key = random.randrange(1, len(enemies))
            if key == 1:
                mob = bear.copy()
            elif key == 2:
                mob = wolf.copy()
            elif key == 3:
                mob = beaver.copy()
            combat_intro()
        else:
            variable['nothing'] = 10
            east_forest()

#function which tells the user that the shit they put don't work
def invalid():
    print ('\033[1m \033[91m \033[4m' +  "~~~PLEASE INPUT A VALID RESPONSE~~~\n" + '\033[0m')

#Each function acts as an area, with the function name corresponding to that location.
def beach():
    variable['beach'] = 3
    print(bcolors.OKGREEN + 'This is the <<Beach>>. You can see your crashed ship, the "Santa Maria", on the <<Shore>> from here. There is also a <<Forest>> to your right it seems.' + bcolors.ENDC)
    direction = input(bcolors.OKCYAN + 'Where do you want to go?' + bcolors.ENDC)
    if re.match(r'^(forest|the forest|right|to the forest|go to the forest|the right|to the right|go to the right)$', direction.lower()) != None:
        variable.pop('beach', None)
        east_forest()
    elif re.match(r'^(shore|the shore|to the shore|go to the shore|crash|the crash|to the crash|go to the crash|ship|the ship|to the ship|go to the ship)$', direction.lower()) != None:
        variable.pop('beach', None)
        shore()
    elif re.match(r'^(inventory|bag|sac|my stuff)$', direction.lower()) != None:
        inven()
    else:
        invalid()
        beach()

def shore():
    variable['shore'] = 4
    print(bcolors.OKGREEN + 'You walk to the crash from the <<Beach>>, but there isn\'t much to see. Anything valuabe or even useful seems to have been lost to the sea...' + bcolors.ENDC)
    direction = input(bcolors.OKCYAN + 'Where do you want to go?' + bcolors.ENDC)
    if re.match(r'^(beach|the beach|to the beach|go to the beach|back|go back)$', direction.lower()) != None:
        variable.pop('shore', None)
        beach()
    elif re.match(r'^(inventory|bag|sac|my stuff)$', direction.lower()) != None:
        inven()
    else:
        invalid()
        shore()

def east_forest():
    if 'combat end' in variable:
        variable.pop('combat end', None)
    variable['east forest'] = 5
    if 'combat end' in variable:
        print(bcolors.OKGREEN + 'You enter the <<East Forest>>. Further through the trees, you can see the iroquoienne <<village>>.'  + bcolors.ENDC)
        direction = input(bcolors.OKCYAN + 'Where do you want to go?' + bcolors.ENDC)
        if re.match(r'^(village|the village|to the village|go to the village|iroquoienne village)$', direction.lower()) != None:
            variable.pop('east forest', None)
            village_first()
        elif re.match(r'^(beach|the beach|to the beach|go to the beach|back|go back)$', direction.lower()) != None:
            variable.pop('east forest', None)
            beach()
        elif re.match(r'^(inventory|bag|sac|my stuff)$', direction.lower()) != None:
            inven()
        else:
            invalid()
            east_forest()
    if 'nothing' in variable:
        variable.pop('nothing', None)
    else:
        if 'gans_dialogue' in variable:
            variable.pop('village actions', None)
            variable.pop('east forest', None)#This is probably useless, just added it cause I was trying to fix a bug
            variable.pop('from forest', None)#There are a lot of these useless pops
            check_encounter()
    if 'gans_dialogue' in variable:
        print(bcolors.OKGREEN + 'You enter the <<East Forest>>. Further through the trees, you can see the iroquoienne <<village>>.'  + bcolors.ENDC)
    else:
        print(bcolors.OKGREEN + 'You enter the <<Forest>>. Further through the trees, you can make out a clearing which seems to be have a <<Village>> residing within it.'  + bcolors.ENDC)
    direction = input(bcolors.OKCYAN + 'Where do you want to go?' + bcolors.ENDC)
    if re.match(r'^(village|the village|to the village|go to the village|iroquoienne village)$', direction.lower()) != None:
        variable.pop('east forest', None)
        village_first()
    elif re.match(r'^(beach|the beach|to the beach|go to the beach|back|go back)$', direction.lower()) != None:
        variable.pop('east forest', None)
        beach()
    elif re.match(r'^(inventory|bag|sac|my stuff)$', direction.lower()) != None:
        inven()
    else:
        invalid()
        east_forest()

def village_first():
    if 'gans_dialogue' in variable:
        village()
    variable['village first'] = 6#THIS FUCKING LINE BROKE SHIT FOR THE LONGEST TIME
    print(bcolors.OKGREEN + 'After walking throught the <<Forest>>, You find yourself in the <<Village>>! There\'s a lot of (locals) walking around working and talking.'  + bcolors.ENDC)
    action = input(bcolors.OKCYAN + 'What do you want to do?' + bcolors.ENDC)
    if re.match(r'^(talk|local|locals|talk to local|speak|)$', action.lower()) != None:
        print(bcolors.OKGREEN + 'You approach one of the village locals and attempt at communicating, but they don\'t seem to understand you. The local instead directs you to a certain individuals and ushers you to speak with him.'  + bcolors.ENDC)
        variable.pop('village first', None)
        gansagonas_village()
    elif re.match(r'^(back|go back|forest|the forest|to the forest|go to the forest)$', action.lower()) != None:
        variable.pop('village first', None)
        forest()
    elif re.match(r'^(inventory|bag|sac|my stuff)$', action.lower()) != None:
        inven()
    else:
        invalid()
        village_first()

def gansagonas_village():
    print(bcolors.WARNING + 'Ah, well it would appear that we have a visitor! My name is Gansagonas, the chief of this iroquoienne village. It is to my understanding that you are a French foreigner? What brings you here to our fine land?'  + bcolors.ENDC)
    #This is dialogue with Gansagonas, he's gonna help Champlain and stuff
    #Another thing, I'm trying out dialogue branching here. Kinda sucks ass cause there's so much to FUCKING TYPE!!!!!!! yeah try to keep up with the branches :)
    dialogue = input(bcolors.OKCYAN + '(1) <<My ship crashed>> | (2) <<I\'ve come to steal all your treasure!>> | (3) <<Do I have to answer your question?>>' + bcolors.ENDC)
    #First branch
    if re.match(r'^(1|my ship crashed)$', dialogue.lower()) != None:
        print(bcolors.WARNING + 'Poseidon is a fiddle fellow, in fits of rage many lives and ships may be lost. And unfortunatly my brother, you have also been caught within it. You have my condolences.' + bcolors.ENDC)
        #First deep branch
        dialogue_branch1 = input(bcolors.OKCYAN + '(1) <<How do I get off this island?>> | (2) <<You wouldn\'t happen to know an Amherst would you?>>' + bcolors.ENDC)
        if re.match(r'^(1|how do I get off this island?|how do I get off this island)$', dialogue_branch1.lower()) != None:
            print(bcolors.WARNING + 'Well, there just so happens to be a port on the other side of this island with a fellow named Amherst, but the only way to get there by foot would be going around the mountain that\'s up from the forest here. I would be glad to help you get there, but if I may ask for your name first?' + bcolors.ENDC)
            #First branch DONE variation 1
            last_branch = input(bcolors.OKCYAN + '(1) <<Samuel Champlain>>' + bcolors.ENDC)
            if re.match(r'^(1|samuel champlain|samuel|champlain)$', last_branch.lower()) != None:
                print(bcolors.WARNING + 'Samuel Champlain eh? I look forward to what adventures the future might hold for us, come back once you are stronger, and we will set out for Amherst and his port!' + bcolors.ENDC)
                print(bcolors.OKBLUE + '<<You Gained Geographic Knowledge!>>' + bcolors.ENDC)
                variable['gans_dialogue'] = 1
                variable['exit chief house'] = 8
                village_actions()
            else:
                invalid()
                gansagonas_village()
        elif re.match(r'^(2|You wouldn\'t happen to know an Amherst would you?|You wouldn\'t happen to know an Amherst would you|You wouldnt happen to know an Amherst would you?|You wouldnt happen to know an Amherst would you)$', dialogue_branch1.lower()) != None:
            print(bcolors.WARNING + 'Well, there just so happens to be a port on the other side of this island with a fellow named Amherst, but the only way to get there by foot would be going around the mountain that\'s up from the forest here. I would be glad to help you get there, but if I may ask for your name first?' + bcolors.ENDC)
            #First branch DONE variation 2
            last_branch2 = input(bcolors.OKCYAN + '(1) <<Samuel Champlain>>' + bcolors.ENDC)
            if re.match(r'^(1|samuel champlain|samuel|champlain)$', last_branch2.lower()) != None:
                print(bcolors.WARNING + 'Samuel Champlain eh? I look forward to what adventures the future might hold for us, come back once you are stronger, and we will set out for Amherst and his port!' + bcolors.ENDC)
                print(bcolors.OKBLUE + '<<You Gained Geographic Knowledge!>>' + bcolors.ENDC)
                variable['gans_dialogue'] = 1
                variable['exit chief house'] = 8
                village_actions()
            else:
                invalid()
                gansagonas_village()
        else:
            invalid()
            gansagonas_village()
    #Second branch
    elif re.match(r'^(2|I\'ve come to steal all your treasure!|I\'ve come to steal all your treasure|Ive come to steal all your treasure!|Ive come to steal all your treasure)$', dialogue.lower()) != None:
        print(bcolors.WARNING + 'Well aren\'t you the humorous type! I\'m afraid my friend we have no treasure on our island, unless you are speaking of the ladies, well then you might find a few jems!' + bcolors.ENDC)
        #Second deep branch
        dialogue_branch2 = input(bcolors.OKCYAN + '(1) <<How do I get off this island?>> | (2) <<You wouldn\'t happen to know an Amherst would you?>>' + bcolors.ENDC)
        if re.match(r'^(1|how do I get off this island?|how do I get off this island)$', dialogue_branch2.lower()) != None:
            print(bcolors.WARNING + 'Well, there just so happens to be a port on the other side of this island with a fellow named Amherst, but the only way to get there by foot would be going around the mountain that\'s up from the forest here. I would be glad to help you get there, but if I may ask for your name first?' + bcolors.ENDC)
            #Second branch DONE variation 3
            last_branch3 = input(bcolors.OKCYAN + '(1) <<Samuel Champlain>>' + bcolors.ENDC)
            if re.match(r'^(1|samuel champlain|samuel|champlain)$', last_branch3.lower()) != None:
                print(bcolors.WARNING + 'Samuel Champlain eh? I look forward to what adventures the future might hold for us, come back once you are stronger, and we will set out for Amherst and his port!' + bcolors.ENDC)
                print(bcolors.OKBLUE + '<<You Gained Geographic Knowledge!>>' + bcolors.ENDC)
                variable['gans_dialogue'] = 1
                variable['exit chief house'] = 8
                village_actions()
            else:
                invalid()
                gansagonas_village()
        elif re.match(r'^(2|You wouldn\'t happen to know an Amherst would you?|You wouldn\'t happen to know an Amherst would you|You wouldnt happen to know an Amherst would you?|You wouldnt happen to know an Amherst would you)$', dialogue_branch2.lower()) != None:
            print(bcolors.WARNING + 'Well, there just so happens to be a port on the other side of this island with a fellow named Amherst, but the only way to get there by foot would be going around the mountain that\'s up from the forest here. I would be glad to help you get there, but if I may ask for your name first?' + bcolors.ENDC)
            #Second branch DONE variation 4
            last_branch4 = input(bcolors.OKCYAN + '(1) <<Samuel Champlain>>' + bcolors.ENDC)
            if re.match(r'^(1|samuel champlain|samuel|champlain)$', last_branch4.lower()) != None:
                print(bcolors.WARNING + 'Samuel Champlain eh? I look forward to what adventures the future might hold for us, come back once you are stronger, and we will set out for Amherst and his port!' + bcolors.ENDC)
                print(bcolors.OKBLUE + '<<You Gained Geographic Knowledge!>>' + bcolors.ENDC)
                variable['gans_dialogue'] = 1
                variable['exit chief house'] = 8
                village_actions()
            else:
                invalid()
                gansagonas_village()
        else:
            invalid()
            gansagonas_village()
    #Third branch
    elif re.match(r'^(3|Do I have to answer your question?|Do I have to answer your question)$', dialogue.lower()) != None:
        print(bcolors.WARNING + 'You certainly don\'t, but we won\'t get much done going down that root now will we?' + bcolors.ENDC)
        #Third deep branch
        dialogue_branch3 = input(bcolors.OKCYAN + '(1) <<How do I get off this island?>> | (2) <<You wouldn\'t happen to know an Amherst would you?>>' + bcolors.ENDC)
        if re.match(r'^(1|how do I get off this island?|how do I get off this island)$', dialogue_branch3.lower()) != None:
            print(bcolors.WARNING + 'Well, there just so happens to be a port on the other side of this island with a fellow named Amherst, but the only way to get there by foot would be going around the mountain that\'s up from the forest here. I would be glad to help you get there, but if I may ask for your name first?' + bcolors.ENDC)
            #Second branch DONE variation 3
            last_branch5 = input(bcolors.OKCYAN + '(1) <<Samuel Champlain>>' + bcolors.ENDC)
            if re.match(r'^(1|samuel champlain|samuel|champlain)$', last_branch5.lower()) != None:
                print(bcolors.WARNING + 'Samuel Champlain eh? I look forward to what adventures the future might hold for us, come back once you are stronger, and we will set out for Amherst and his port!' + bcolors.ENDC)
                print(bcolors.OKBLUE + '<<You Gained Geographic Knowledge!>>' + bcolors.ENDC)
                variable['gans_dialogue'] = 1
                variable['exit chief house'] = 8
                village_actions()
            else:
                invalid()
                gansagonas_village()
        elif re.match(r'^(2|You wouldn\'t happen to know an Amherst would you?|You wouldn\'t happen to know an Amherst would you|You wouldnt happen to know an Amherst would you?|You wouldnt happen to know an Amherst would you)$', dialogue_branch3.lower()) != None:
            print(bcolors.WARNING + 'Well, there just so happens to be a port on the other side of this island with a fellow named Amherst, but the only way to get there by foot would be going around the mountain that\'s up from the forest here. I would be glad to help you get there, but if I may ask for your name first?' + bcolors.ENDC)
            last_branch6 = input(bcolors.OKCYAN + '(1) <<Samuel Champlain>>' + bcolors.ENDC)
            if re.match(r'^(1|samuel champlain|samuel|champlain)$', last_branch6.lower()) != None:
                print(bcolors.WARNING + 'Samuel Champlain eh? I look forward to what adventures the future might hold for us, come back once you are stronger, and we will set out for Amherst and his port!' + bcolors.ENDC)
                print(bcolors.OKBLUE + '<<You Gained Geographic Knowledge!>>' + bcolors.ENDC)
                variable['gans_dialogue'] = 1
                variable['exit chief house'] = 8
                village_actions()
            else:
                invalid()
                gansagonas_village()
        else:
            invalid()
            gansagonas_village()
            #Second branch DONE variation 6
    else:
        invalid()
        gansagonas_village()

def village():
    print(bcolors.OKGREEN + 'After walking throught the <<East Forest>>, You find yourself in the <<Village>>!'  + bcolors.ENDC)
    village_actions()

def village_actions():
    variable['village actions'] = 7
    if 'shop_left' in variable:
        variable.pop('shop_left', None)
        print(bcolors.OKGREEN + 'There\'s a lot of (locals) walking around working and talkingwith the <<East forest>> surrounding them. There is also a <<shop>>!'  + bcolors.ENDC)
        action = input(bcolors.OKCYAN + 'What do you want to do?' + bcolors.ENDC)
        if re.match(r'^(talk|local|locals|talk to local|speak)$', action.lower()) != None:
            print(bcolors.OKGREEN + 'They wave hello and smile at you.' + bcolors.ENDC)
            village_actions()
        elif re.match(r'^(shop|go to shop|the shop|buy|store)$', action.lower()) != None:
            print(bcolors.OKGREEN + 'The shop keeper has a variaty of wares...' + bcolors.ENDC)
            shop()
        elif re.match(r'^(east forest|forest)$', action.lower()) != None:
            variable.pop('village actions', None)
            east_forest()
        elif re.match(r'^(inventory|bag|sac|my stuff)$', action.lower()) != None:
            inven()
        else:
            invalid()
            village_actions()
    if 'exit chief house' in variable:
        variable.pop('exit chief house', None)
        print(bcolors.WARNING + 'BEWARE! You have now been acquainted with the <<Island of Miquelon>>.' + bcolors.ENDC)
        print(bcolors.WARNING + 'Whenever you enter the wilderness, you have a may how a chance encounter with wildlife!' + bcolors.ENDC)
        print(bcolors.WARNING + 'You could try to escape from these battles, but the expeirence and loot you gain from these battles may be worth it!' + bcolors.ENDC)
        print(bcolors.WARNING + 'Everytime you <<LEVEL UP>> your stats will gain a permenant boost! Aren\'t I so kind?' + bcolors.ENDC)
        print(bcolors.WARNING + 'You may also encounter some traveling iroquoienne traders! These people are always friendly and are here to help you on your Adventures!' + bcolors.ENDC)
        print(bcolors.OKGREEN + 'You walk out of Gansagonas\' House.'  + bcolors.ENDC)
    if 'combat end' in variable:
        variable.pop('combat end', None)
        print(bcolors.OKGREEN + 'You wake up in the village in bandages, and Gansagonas is sitting next to you.'  + bcolors.ENDC)
        print(bcolors.WARNING + 'We found you in the forest unconscious... We brough you back to the village but it seems someone had stolen some of you things...' + bcolors.ENDC)
        lost = (player_stat['money']/10)
        player_stat['money'] =  player_stat['money'] - lost
        print(bcolors.FAIL + 'YOU LOST ({})g'.format(lost) + bcolors.ENDC)
    if 'village actions' in variable:
        print(bcolors.OKGREEN + 'There\'s a lot of (locals) walking around working and talking with the <<East forest>> surrounding them. There is also a <<shop>>!'  + bcolors.ENDC)
        action = input(bcolors.OKCYAN + 'What do you want to do?' + bcolors.ENDC)
        if re.match(r'^(talk|local|locals|talk to local|speak|)$', action.lower()) != None:
            print(bcolors.OKGREEN + 'They wave hello and smile at you.' + bcolors.ENDC)
            village_actions()
        elif re.match(r'^(shop|go to shop|the shop|buy|store)$', action.lower()) != None:
            print(bcolors.OKGREEN + 'The shop keeper has a variaty of wares...' + bcolors.ENDC)
            shop()
        elif re.match(r'^(east forest|forest)$', action.lower()) != None:
            variable.pop('village actions', None)
            east_forest()
        elif re.match(r'^(inventory|bag|sac|my stuff)$', action.lower()) != None:
            inven()
        else:
            invalid()
            village_actions()
    action = input(bcolors.OKCYAN + 'What do you want to do?' + bcolors.ENDC)
    if re.match(r'^(talk|local|locals|talk to local|speak)$', action.lower()) != None:
        print(bcolors.OKGREEN + 'They wave hello and smile at you.' + bcolors.ENDC)
        village_actions()
    elif re.match(r'^(shop|go to shop|the shop|buy|store)$', action.lower()) != None:
        print(bcolors.OKGREEN + 'The shop keeper has a variaty of wares...' + bcolors.ENDC)
        shop()
    elif re.match(r'^(east forest|forest)$', action.lower()) != None:
        variable.pop('village actions', None)
        east_forest()
    elif re.match(r'^(inventory|bag|sac|my stuff)$', action.lower()) != None:
        inven()
    else:
        invalid()
        village_actions()

def shop():
    cooked_meat = 5
    arrow = 2
    bow = 30
    bandage = 7
    war_club = 40
    tomahawk = 25
    wildlife_attractor = 30
    alexs_edge = 100
    print(bcolors.OKCYAN + ' (1) <<cooked meat [5g]>> ' + bcolors.ENDC)
    print(bcolors.OKCYAN + ' (2) <<arrow [2g]>> ' + bcolors.ENDC)
    print(bcolors.OKCYAN + ' (3) <<bow [30g]>> ' + bcolors.ENDC)
    print(bcolors.OKCYAN + ' (4) <<bandage [7g]>> ' + bcolors.ENDC)
    print(bcolors.OKCYAN + ' (5) <<war club [40g]>> ' + bcolors.ENDC)
    print(bcolors.OKCYAN + ' (6) <<tomahawk [25g]>> ' + bcolors.ENDC)
    print(bcolors.OKCYAN + ' (7) <<wildlife attractor [30g]>> ' + bcolors.ENDC)
    print(bcolors.OKCYAN + ' (8) <<alex\'s edge [100g]>> ' + bcolors.ENDC)
    print(bcolors.OKCYAN + ' (9) <<SELL>> ' + bcolors.ENDC)
    stock = input(bcolors.OKCYAN + ' (10) <<EXIT>>' + bcolors.ENDC)
    if re.match(r'^(1|cooked meat)$', stock.lower()) != None:
        amount(cooked_meat, 'cooked meat')
    elif re.match(r'^(2|arrow|arrows)$', stock.lower()) != None:
        amount(arrow, 'arrow')
    elif re.match(r'^(3|bow)$', stock.lower()) != None:
        amount(bow, 'bow')
    elif re.match(r'^(4|bandage)$', stock.lower()) != None:
        amount(bandage, 'bandage')
    elif re.match(r'^(5|war club)$', stock.lower()) != None:
        amount(war_club, 'war_club')
    elif re.match(r'^(6|tomahawk)$', stock.lower()) != None:
        amount(tomahawk, 'tomahawk')
    elif re.match(r'^(7|wildlife attractor)$', stock.lower()) != None:
        amount(wildlife_attractor, 'wildlife attractor')
    elif re.match(r'^(8|alex\'s edge)$', stock.lower()) != None:
        amount(alexs_edge, 'alex\'s edge')
    elif re.match(r'^(9|sell)$', stock.lower()) != None:
        sell()# sell option for the player
    elif re.match(r'^(10|exit|leave|back|go back|stop|finish|terminate)$', stock.lower()) != None:
        print(bcolors.OKGREEN + 'You leave the shop' + bcolors.ENDC)
        variable['shop_left'] = 2
        village_actions()
    else:
        invalid()
        shop()

def amount(x, y):
    pay_for = input(bcolors.OKCYAN + 'How many do you want to buy?' + bcolors.ENDC)
    try:
        isinstance(int(pay_for), int)
    except Exception: #when the player don't type the good, send him to the invalid, very nice
        invalid()
        amount(x, y)
    if isinstance(int(pay_for), int) == True: #Nvrm, got it to work now. just had to make the whole thing a try block, then I put the exception after.
        cost = int(pay_for) * x
        print('It will cost ({})g'.format(cost))
        print('You have ({})g'.format(player_stat['money']))
        confirmation = input(bcolors.OKCYAN + 'Proceed with transaction?' + bcolors.ENDC)
        if re.match(r'^(yes|y|ye|ya|yep|buy|proceed|complete|yeah|aqcuire|purchase)$', confirmation.lower()) != None:
            if player_stat['money'] < cost:
                print(bcolors.FAIL + '<<YOU DON\'T HAVE ENOUGH MONEY>>')
                shop()
            else:
                player_stat['money'] = player_stat['money'] - cost
                inventory[y]['quantity'] = inventory[y]['quantity'] + int(pay_for)
                print(bcolors.OKBLUE + 'You Gained ({}) <<{}>>!'.format(int(pay_for), y) + bcolors.ENDC)
                shop()
        elif re.match(r'^(no|n|cancel|stop|don\'t|don\'t buy|back|discontinue)$', confirmation.lower()) != None:
            shop()
        else:
            invalid()
            amount(x, y)

def inven():
    global xp
    global req
    global lv
    if 'from forest' in variable:
        variable.pop('from forest', None)
    print(bcolors.OKGREEN + 'What would You like to View?' +  bcolors.ENDC)
    action = input(bcolors.OKCYAN + '(1) <<Health>> | (2) <<Money>> | (3) <<Overall stats>> | (4) <<Inventory>> | (5) <<Experience>> | (6) <<EXIT>>' +  bcolors.ENDC)
    if re.match(r'^(1|health)$', action.lower()) != None:
        print(player_stat['hp'])
        inven()
    elif re.match(r'^(2|money)$', action.lower()) != None:
        print(player_stat['money'])
        inven()
    elif re.match(r'^(3|overall stats|stats)$', action.lower()) != None:
        print(player_stat)
        inven()
    elif re.match(r'^(5|experience)$', action.lower()) != None:
        print('({})xp'.format(xp))
        print('({})req xp'.format(req))
        print('({})lv'.format(lv))
        inven()
    elif re.match(r'^(4|inventory)$', action.lower()) != None:
        print(bcolors.OKGREEN + 'Which Item do You wish to Look at?' +  bcolors.ENDC)
        print(bcolors.OKCYAN + '(1) <<Cooked meat>>' +  bcolors.ENDC)
        print(bcolors.OKCYAN + '(2) <<Arrow>>' +  bcolors.ENDC)
        print(bcolors.OKCYAN + '(3) <Bow>>' +  bcolors.ENDC)
        print(bcolors.OKCYAN + '(4) <<Bandage>>' +  bcolors.ENDC)
        print(bcolors.OKCYAN + '(5) <<War club>>' +  bcolors.ENDC)
        print(bcolors.OKCYAN + '(6) <<Tomahawk>>' +  bcolors.ENDC)
        print(bcolors.OKCYAN + '(7) <<Sword>>' +  bcolors.ENDC)
        print(bcolors.OKCYAN + '(8) <<shield>>' +  bcolors.ENDC)
        print(bcolors.OKCYAN + '(9) <<meat>>' +  bcolors.ENDC)
        print(bcolors.OKCYAN + '(10) <<pelt>>' +  bcolors.ENDC)
        print(bcolors.OKCYAN + '(11) <<wildlife attractor>>' +  bcolors.ENDC)
        print(bcolors.OKCYAN + '(12) <<alex\'s edge>>' +  bcolors.ENDC)
        print(bcolors.OKCYAN + '(13) <<beaver fur>>' +  bcolors.ENDC)
        specification = input(bcolors.OKCYAN + '(14) <<EXIT>>' +  bcolors.ENDC)
        if re.match(r'^(1|cooked meat)$', specification.lower()) != None:
            print(inventory['cooked meat'])
            if inventory['cooked meat']['quantity'] > 0:
                ask = input(bcolors.OKGREEN + 'Would you like to use this item?' +  bcolors.ENDC)
                if re.match(r'^(yes|y|yeah|sure|use|yep)$', ask.lower()) != None:
                    use('cooked meat')
                elif re.match(r'^(no|nope|nah|n|exit|cancel|leave)$', ask.lower()) != None:
                    inven()
                else:
                    invalid()
                    inven()
            else:
                inven()
        elif re.match(r'^(2|arrow)$', specification.lower()) != None:
            print(inventory['arrow'])
            inven()
        elif re.match(r'^(3|bow)$', specification.lower()) != None:
            print(inventory['bow'])
            inven()
        elif re.match(r'^(4|bandage)$', specification.lower()) != None:
            print(inventory['bandage'])
            if inventory['bandage']['quantity'] > 0:
                ask2 = input(bcolors.OKGREEN + 'Would you like to use this item?' +  bcolors.ENDC)
                if re.match(r'^(yes|y|yeah|sure|use|yep)$', ask2.lower()) != None:
                    use('bandage')
                elif re.match(r'^(no|nope|nah|n|exit|cancel|leave)$', ask2.lower()) != None:
                    inven()
                else:
                    invalid()
                    inven()
            else:
                inven()
        elif re.match(r'^(5|war club)$', specification.lower()) != None:
            print(inventory['war club'])
            if inventory['war club']['quantity'] > 0:
                ask = input(bcolors.OKGREEN + 'Would you like to equip this item?' +  bcolors.ENDC)
                if re.match(r'^(yes|y|yeah|sure|use|yep)$', ask.lower()) != None:
                    equipe('war club')
                elif re.match(r'^(no|nope|nah|n|exit|cancel|leave)$', ask.lower()) != None:
                    inven()
                else:
                    invalid()
                    inven()
            else:
                inven()
        elif re.match(r'^(6|tomahawk)$', specification.lower()) != None:
            print(inventory['tomahawk'])
            if inventory['tomahawk']['quantity'] > 0:
                ask = input(bcolors.OKGREEN + 'Would you like to equip this item?' +  bcolors.ENDC)
                if re.match(r'^(yes|y|yeah|sure|use|yep)$', ask.lower()) != None:
                    equipe('tomahawk')
                elif re.match(r'^(no|nope|nah|n|exit|cancel|leave)$', ask.lower()) != None:
                    inven()
                else:
                    invalid()
                    inven()
            else:
                inven()
        elif re.match(r'^(7|sword)$', specification.lower()) != None:
            print(inventory['sword'])
            if inventory['sword']['quantity'] > 0:
                ask = input(bcolors.OKGREEN + 'Would you like to equip this item?' +  bcolors.ENDC)
                if re.match(r'^(yes|y|yeah|sure|use|yep)$', ask.lower()) != None:
                    equipe('sword')
                elif re.match(r'^(no|nope|nah|n|exit|cancel|leave)$', ask.lower()) != None:
                    inven()
                else:
                    invalid()
                    inven()
            else:
                inven()
        elif re.match(r'^(8|shield)$', specification.lower()) != None:
            print(inventory['shield'])
            if inventory['shield']['quantity'] > 0:
                ask = input(bcolors.OKGREEN + 'Would you like to equip this item?' +  bcolors.ENDC)
                if re.match(r'^(yes|y|yeah|sure|use|yep)$', ask.lower()) != None:
                    equipe('shield')
                elif re.match(r'^(no|nope|nah|n|exit|cancel|leave)$', ask.lower()) != None:
                    inven()
                else:
                    invalid()
                    inven()
        elif re.match(r'^(9|meat)$', specification.lower()) != None:
            print(inventory['meat'])
            if inventory['meat']['quantity'] > 0:
                ask3 = input(bcolors.OKGREEN + 'Would you like to use this item?' +  bcolors.ENDC)
                if re.match(r'^(yes|y|yeah|sure|use|yep)$', ask3.lower()) != None:
                    use('meat')
                elif re.match(r'^(no|nope|nah|n|exit|cancel|leave)$', ask3.lower()) != None:
                    inven()
                else:
                    invalid()
                    inven()
            else:
                inven()
        elif re.match(r'^(10|pelt)$', specification.lower()) != None:
            print(inventory['pelt'])
            inven()
        elif re.match(r'^(11|wildlife attractor)$', specification.lower()) != None:
            print(inventory['wildlife attractor'])
            if inventory['wildlife attractor']['quantity'] > 0:
                ask4 = input(bcolors.OKGREEN + 'Would you like to use this item?' +  bcolors.ENDC)
                if re.match(r'^(yes|y|yeah|sure|use|yep)$', ask4.lower()) != None:
                    use('wildlife attractor')
                elif re.match(r'^(no|nope|nah|n|exit|cancel|leave)$', ask4.lower()) != None:
                    inven()
                else:
                    invalid()
                    inven()
            else:
                inven()
        elif re.match(r'^(12|alex\'s edge)$', specification.lower()) != None:
            print(inventory['alex\'s edge'])
            if inventory['alex\'s edge']['quantity'] > 0:
                ask = input(bcolors.OKGREEN + 'Would you like to equip this item?' +  bcolors.ENDC)
                if re.match(r'^(yes|y|yeah|sure|use|yep)$', ask.lower()) != None:
                    equipe('alex\'s edge')
                elif re.match(r'^(no|nope|nah|n|exit|cancel|leave)$', ask.lower()) != None:
                    inven()
                else:
                    invalid()
                    inven()
            else:
                inven()
        elif re.match(r'^(13|beaver fur)$', specification.lower()) != None:
            print(inventory['beaver fur'])
            inven()
        elif re.match(r'^(14|exit|leave|cancel|stop)$', specification.lower()) != None:
            inven()
        else:
            invalid()
            inven()
    elif re.match(r'^(6|exit|leave|cancel|stop)$', action.lower()) != None:
        if 'beach' in variable:
            beach()
        elif 'shore' in variable:
            shore()
        elif 'east forest' in variable:
            east_forest()
        elif 'village first' in variable:
            village_first()
        elif 'village actions' in variable:
            variable.pop('village actions', None)
            village_actions()
        elif 'combat' in variable:
            inputs()
    else:
        invalid()
        inven()

def sell():
    print('Which Item do You want to Sell?')
    print(bcolors.OKCYAN + '(1) <<EXIT>>' +  bcolors.ENDC)
    print(bcolors.OKCYAN + '(2) <<Cooked meat>>' +  bcolors.ENDC)
    print(bcolors.OKCYAN + '(3) <<Arrow>>' +  bcolors.ENDC)
    print(bcolors.OKCYAN + '(4) <Bow>>' +  bcolors.ENDC)
    print(bcolors.OKCYAN + '(5) <<Bandage>>' +  bcolors.ENDC)
    print(bcolors.OKCYAN + '(6) <<War club>>' +  bcolors.ENDC)
    print(bcolors.OKCYAN + '(7) <<Tomahawk>>' +  bcolors.ENDC)
    print(bcolors.OKCYAN + '(8) <<Sword>>' +  bcolors.ENDC)
    print(bcolors.OKCYAN + '(9) <<shield>>' +  bcolors.ENDC)
    print(bcolors.OKCYAN + '(10) <<meat>>' +  bcolors.ENDC)
    print(bcolors.OKCYAN + '(11) <<pelt>>' +  bcolors.ENDC)
    print(bcolors.OKCYAN + '(12) <<wildlife attractor>>' +  bcolors.ENDC)
    print(bcolors.OKCYAN + '(13) <<Alex\'s Edge>>' +  bcolors.ENDC)
    specification = input(bcolors.OKCYAN + '(14) <<beaver fur>>' +  bcolors.ENDC)
    if re.match(r'^(2|cooked meat)$', specification.lower()) != None:
        print('You have ({}) of these! Each is Worth ({})'.format(inventory['cooked meat']['quantity'], inventory['cooked meat']['value']))
        give(inventory['cooked meat']['value'], 'cooked meat')
    elif re.match(r'^(3|arrow)$', specification.lower()) != None:
        print('You have ({}) of these! Each is Worth ({})'.format(inventory['arrow']['quantity'], inventory['arrow']['value']))
        give(inventory['arrow']['value'], 'arrow')
    elif re.match(r'^(4|bow)$', specification.lower()) != None:
        print('You have ({}) of these! Each is Worth ({})'.format(inventory['bow']['quantity'], inventory['bow']['value']))
        give(inventory['bow']['value'], 'bow')
    elif re.match(r'^(5|bandage)$', specification.lower()) != None:
        print('You have ({}) of these! Each is Worth ({})'.format(inventory['bandage']['quantity'], inventory['bandage']['value']))
        give(inventory['bandage']['value'], 'bandage')
    elif re.match(r'^(6|war club)$', specification.lower()) != None:
        print('You have ({}) of these! Each is Worth ({})'.format(inventory['war club']['quantity'], inventory['war club']['value']))
        give(inventory['war club']['value'], 'war club')
    elif re.match(r'^(7|tomahawk)$', specification.lower()) != None:
        print('You have ({}) of these! Each is Worth ({})'.format(inventory['tomahawk']['quantity'], inventory['tomahawk']['value']))
        give(inventory['tomahawk']['value'], 'tomahawk')
    elif re.match(r'^(8|sword)$', specification.lower()) != None:
        print('You have ({}) of these! Each is Worth ({})'.format(inventory['sword']['quantity'], inventory['sword']['value']))
        give(inventory['sword']['value'], 'sword')
    elif re.match(r'^(9|shield)$', specification.lower()) != None:
        print('You have ({}) of these! Each is Worth ({})'.format(inventory['shield']['quantity'], inventory['shield']['value']))
        give(inventory['shield']['value'], 'shield')
    elif re.match(r'^(10|meat)$', specification.lower()) != None:
        print('You have ({}) of these! Each is Worth ({})'.format(inventory['meat']['quantity'], inventory['meat']['value']))
        give(inventory['meat']['value'], 'meat')
    elif re.match(r'^(11|pelt)$', specification.lower()) != None:
        print('You have ({}) of these! Each is Worth ({})'.format(inventory['pelt']['quantity'], inventory['pelt']['value']))
        give(inventory['pelt']['value'], 'pelt')
    elif re.match(r'^(12|wildlife attractor)$', specification.lower()) != None:
        print('You have ({}) of these! Each is Worth ({})'.format(inventory['wildlife attractor']['quantity'], inventory['wildlife attractor']['value']))
        give(inventory['wildlife attractor']['value'], 'wildlife attractor')
    elif re.match(r'^(13|alex\'s edge)$', specification.lower()) != None:
        print('You have ({}) of these! Each is Worth ({})'.format(inventory['alex\'s edge']['quantity'], inventory['alex\'s edge']['value']))
        give(inventory['alex\'s edge']['value'], 'alex\'s edge')
    elif re.match(r'^(14|beaver fur)$', specification.lower()) != None:
        print('You have ({}) of these! Each is Worth ({})'.format(inventory['beaver fur']['quantity'], inventory['beaver fur']['value']))
        give(inventory['beaver fur']['value'], 'beaver fur')
    elif re.match(r'^(1|no|n|cancel|stop|don\'t|don\'t buy|back|discontinue|exit)$', specification.lower()) != None:
        shop()
    else:
        invalid()
        sell()


def give(x, y):
    sell_for = input(bcolors.OKGREEN + 'How many do you want to sell?' + bcolors.ENDC)
    try:
        isinstance(int(sell_for), int)
    except Exception: #when the player don't type the good, send him to the invalid, very nice
        invalid()
        give(x, y)
    if isinstance(int(sell_for), int) == True: #Nvrm, got it to work now. just had to make the whole thing a try block, then I put the exception after.
        cost = int(sell_for) * x
        print('You will get ({})g'.format(cost))
        confirmation = input(bcolors.OKCYAN + 'Proceed with transaction?' + bcolors.ENDC)
        if re.match(r'^(yes|y|ye|ya|yep|buy|proceed|complete|yeah|aqcuire|purchase)$', confirmation.lower()) != None:
            if inventory[y]['quantity'] < int(sell_for):
                print(bcolors.FAIL + '<<YOU ARE SELLING TOO MUCH>>' + bcolors.ENDC)
                sell()
            else:
                player_stat['money'] = player_stat['money'] + cost
                inventory[y]['quantity'] = inventory[y]['quantity'] - int(sell_for)
                print(bcolors.OKBLUE + 'You Sold ({}) <<{}>> and Gained ({})g !'.format(int(sell_for), y, cost) + bcolors.ENDC)
                shop()
        elif re.match(r'^(no|n|cancel|stop|don\'t|don\'t buy|back|discontinue)$', confirmation.lower()) != None:
            shop()
        else:
            invalid()
            give(x, y)
def intro():
    print(bcolors.OKGREEN + 'Anything between <<>> and () are actions and places you can interact with.' + bcolors.ENDC)
    print(bcolors.OKGREEN + 'Also, to access your <<Inventory>>, simply write the following,' + bcolors.ENDC)
    print(bcolors.OKCYAN + '<<inventory>>' + bcolors.ENDC)
    print(bcolors.OKCYAN + '<<bag>>' + bcolors.ENDC)
    print(bcolors.OKCYAN + '<<sac>>' + bcolors.ENDC)
    print(bcolors.OKCYAN + '<<my stuff>>' + bcolors.ENDC)
    print(bcolors.OKGREEN + 'Finally, don\'t worry about capitalization, it won\'t result in any issues ;3' + bcolors.ENDC)
    print(bcolors.WARNING + '<<I Hope You Enjoy the Game!>>' + bcolors.ENDC)
    beach()


#This function introduces the enemie
def combat_intro():
    global mob
    print(bcolors.WARNING + '<< You Engaged Comabt With ({}), They Have ({}hp)! >>'.format(mob['name'], mob['hp']) + bcolors.ENDC)
    player_stat['karma'] = player_stat['karma'] - mob['karma']
    inputs()

#This function determines whether or not the pplayer parries
def is_parry():
    parry = (player_stat['speed']/mob['speed'])/2*100 + (player_stat['luck']/2) - (mob['luck']/2)
    if parry <= random.randrange(1, 101):
        return True
    return False
#This function is for blocking
def parry():
    global mob
    parry = is_parry()
    is_crit = is_critical()
    hit_chance = (player_stat['speed']/mob['speed'])/2*100 + (player_stat['luck']/2) - (mob['luck']/2)
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
#This function asks for the player's input
def inputs():
    global mob
    variable['combat'] = 13
    if mob['bleeding stacks'] > 0:
        mob['hp'] = mob['hp'] - (mob['hp']/100*player_buff['bleeding'])
        damage = (mob['hp']/100*player_buff['bleeding'])
        print(bcolors.OKGREEN + bcolors.UNDERLINE + 'The ({}) took ({}) damage from bleeding!'.format(mob['name'], damage,) + bcolors.ENDC)
    action = input(bcolors.BOLD + bcolors.UNDERLINE + '<< What Do You Want To Do? [Attack]--[Run]--[Parry]--[Inventory] >>' + bcolors.ENDC)
    if re.match(r'^(attack|atk|1)$', action.lower()) != None:
        variable.pop('combat', None)
        attack()
    elif re.match(r'^(run|2)$', action.lower()) != None:
        variable.pop('combat', None)
        run()
    elif re.match(r'^(parry|3)$', action.lower()) != None:
        if 'shield' in equiped:
            variable.pop('combat', None)
            parry()
        else:
            print(bcolors.FAIL + 'YOU DON"T HAVE A SHIELD EQUIPED' + bcolors.ENDC)
            inputs()
    elif re.match(r'^(inventory|bag|sac|my stuff|4)$', action.lower()) != None:
        inven()
    else:
        invalid()
        inputs()

#This function checks for crits for the damage function, for the player
def is_critical():
    crit = random.randrange(1,101)
    if crit <= player_stat['luck'] + player_buff['critical strike'] :
        return True
    return False

#This function checks for enemie crits
def enemie_crit():
    global mob
    crit = random.randrange(1,101)
    if crit <= mob['luck']:
        return True
    return False


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
    global mob
    is_crit = is_critical()
    hit_chance = (player_stat['speed']/mob['speed'])*100 + (player_stat['luck']/2) - (mob['luck']/2)
    if hit_chance <= 0:
        hit_chance = 1
    if mob['speed'] <= 0:
        hit_chance = 95
    attack_rsp = input('<< Would You Like To See Your Hit Chance? [Yes]--[No] >>')
    if re.match(r'^(yes|ye|y|1)$', attack_rsp.lower()) != None:
        print(bcolors.FAIL + bcolors.UNDERLINE + '<< You Have a' + bcolors.OKCYAN + '({}%)'.format(hit_chance) + bcolors.FAIL + 'Chance To Hit! >>' + bcolors.ENDC)
        attack_comfirm(hit_chance, is_crit)
    elif re.match(r'^(no|n|2)$', attack_rsp.lower()) != None:
        attack_comfirm(hit_chance, is_crit)
    else:
        invalid()
        attack()

#This function serves the same purpose as attack_comfirm, just lowering the line count.
def run_comfirmation(run_chance):
    comfirmation = input('<< Want To Proceed? [Yes]--[No] >>')
    if re.match(r'^(yes|ye|y|1)$', comfirmation.lower()) != None:
        run = random.randrange(1,101)
        if run <= run_chance:
            print('<< You Successfully Ran Away! >>')
            east_forest()
        else:
            print('<< Your Run Attempt Failed... >>')
            enemie_turn()
    elif re.match(r'^(no|n|2)$', comfirmation.lower()) != None:
        inputs()
    else:
        invalid()
        run_comfirmation(run_chance)

#This function performs the running action
def run():
    global mob
    run_chance = ((player_stat['speed']/mob['speed']/2))*100 + (player_stat['luck']/2) - (mob['luck']/2)
    escape = input('<< Would You Like To See Your Run Chance? [Yes]--[No] >>')
    if re.match(r'^(yes|ye|y|1)$', escape.lower()) != None:
        print('<< You Have a ({}%) Chance To Hit! >>'.format(run_chance))
        run_comfirmation(run_chance)
    elif re.match(r'^(no|n|2)$', escape.lower()) != None:
        run_comfirmation(run_chance)
    else:
        invalid()
        run()

#This function processes the enemies turn + the critical gives the monster more damage output
def enemie_turn(critical = False):
    global mob
    hit_chance = (mob['speed']/player_stat['speed'])*100 - (player_stat['luck']/2) + (mob['luck']/2)

#This function also for lower line count, man im doing a lot of these eh?
def almost_ded(x):
    global mob
    if mob['hp'] <= mob['hp']/3:
        print('<< It\'s Almost Dead! >>')
    if x == True:
        inputs()
    else:
        enemie_turn()

#This function does the damage calculations for the player's turn + the critical skips the monster's turn.
def damage(hit_chance, parry=False, is_crit=False):
    global mob
    damage = random.randrange(player_stat['atk_min'], (player_stat['atk_max'] + 1))
    if hit_chance >= random.randrange(1,101):
        if player_buff['bleeding'] > 0:
            print(bcolors.OKGREEN + bcolors.UNDERLINE + 'You applied ({}) bleeding stacks!'.format(player_buff['bleeding']) + bcolors.ENDC)
            mob['bleeding stacks'] = mob['bleeding stacks'] + player_buff['bleeding']
            print(bcolors.OKGREEN + bcolors.UNDERLINE + 'Total active bleeding stacks ({})'.format(mob['bleeding stacks']) + bcolors.ENDC)
        if mob['bleeding stacks'] >= 50:
            print(bcolors.OKGREEN + bcolors.UNDERLINE + 'The ({}) Bled out! '.format(mob['name']) + bcolors.ENDC)
            mob['hp'] = 0
            check_death()
        if player_buff['blunt'] > 0:
            print(bcolors.OKGREEN + bcolors.UNDERLINE + 'You applied ({}) blunt stacks!'.format(player_buff['blunt']) + bcolors.ENDC)
            mob['blunt'] = mob['blunt'] + player_buff['blunt']
            print(bcolors.OKGREEN + bcolors.UNDERLINE + 'Total active blunt stacks ({})'.format(mob['blunt']) + bcolors.ENDC)
        if is_crit:
            damage = damage * 1.5
            mob['hp'] = mob['hp'] - damage
            print(bcolors.OKGREEN + bcolors.UNDERLINE + '<< You Dealt' + bcolors.OKCYAN + '({})'.format(damage) + bcolors.OKGREEN + 'Critical Damage To ({})! ({}) Health Is Now'.format(mob['name'], mob['name']) + bcolors.OKCYAN + '({}hp)'.format(mob['hp']) + bcolors.OKGREEN + '! >>' + bcolors.ENDC)
            check_death()
            almost_ded(parry)
        if is_crit == False:
            mob['hp'] = mob['hp'] - damage
            print(bcolors.OKGREEN + '<< You Dealt' + bcolors.OKCYAN + '({})'.format(damage) + bcolors.OKGREEN + 'Damage To ({})! ({}) Health Is Now'.format(mob['name'], mob['name']) + bcolors.OKCYAN + '({}hp)'.format(mob['hp']) + bcolors.OKGREEN + '>>' + bcolors.ENDC)
            check_death()
            almost_ded(parry)
        if is_crit and parry:
            damage = damage * 1.5
            mob['hp'] = mob['hp'] - damage
            print(bcolors.OKGREEN + bcolors.UNDERLINE + '<< You Parried the Attack and Dealt' + bcolors.OKCYAN + '({})'.format(damage) + bcolors.OKGREEN + 'Critical Damage To ({})! ({}) Health Is Now'.format(mob['name'], mob['name']) + bcolors.OKCYAN + '({}hp)'.format(mob['hp']) + bcolors.OKGREEN + '! >>' + bcolors.ENDC)
            check_death()
            almost_ded(parry)
        if parry:
            mob['hp'] = mob['hp'] - damage
            print(bcolors.OKGREEN + '<< You Parried the Attack and Dealt' + bcolors.OKCYAN + '({})'.format(damage) + bcolors.OKGREEN + 'Damage To ({})! ({}) Health Is Now'.format(mob['name'], mob['name']) + bcolors.OKCYAN + '({}hp)'.format(mob['hp']) + bcolors.OKGREEN + '>>' + bcolors.ENDC)
            check_death()
            almost_ded(parry)
    else:
        print(bcolors.WARNING + '<< You Didn\'t Land Your Hit... >>' + bcolors.ENDC)
        enemie_turn()

def enemie_turn():
    global mob
    hit_chance = (mob['speed']/player_stat['speed'])*100 - (player_stat['luck']/2) + (mob['luck']/2)
    damage = random.randrange(mob['atk_min'], (mob['atk_max'] + 1))
    if mob['blunt'] > 0:
        mob['blunt'] = mob['blunt'] - 1
        damage = damage/2
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
    global mob
    global xp
    if player_stat['hp'] <= 0:
        print (bcolors.UNDERLINE + bcolors.WARNING + '~~~' + bcolors.FAIL +  "YOU DIED" + bcolors.WARNING + '~~~' + bcolors.ENDC)
        variable['combat end'] = 9
        player_stat['hp'] = player_stat['max hp']
        village_actions()
    if mob['hp'] <= 0:
        print(bcolors.OKGREEN + '<< You Killed ({}) and Gained ({})xp! >>'.format(mob['name'], mob['experience']) + bcolors.ENDC)
        xp = xp + mob['experience']
        mob['hp'] = mob['hp'] + mob['reset hp']
        lv_up()
        if mob['karma'] == 0 - 10:
            print(bcolors.WARNING + 'Victory is yours, but was it worth the cost of innocent blood?' + bcolors.ENDC)
        variable['combat end'] = 9
        east_forest()
    return False

def drop():
    try:
        if mob['item'] == 'pelt':
            if mob['chance'] <= random.randrange(1,101):
                print(bcolors.OKGREEN + 'You Gained (1) <<pelt>> and (1) <<meat>> !' + bcolors.ENDC)
                inventory['pelt']['quantity'] = inventory['pelt']['quantity'] + 1
                inventory['meat']['quantity'] = inventory['meat']['quantity'] + 1
                variable['combat end'] = 9
                east_forest()
    except:
        try:
            if mob['item'] == 'meat':
                if mob['chance'] <= random.randrange(1,101):
                    print(bcolors.OKGREEN + 'You Gained (5) <<meat>> !' + bcolors.ENDC)
                    inventory['meat']['quantity'] = inventory['meat']['quantity'] + 5
                    variable['combat end'] = 9
                    east_forest()
        except:
                if mob['item'] == 'beaver fur':
                    if mob['chance'] <= random.randrange(1,101):
                        print(bcolors.OKGREEN + 'You Gained (1) <<beaver fur>> !' + bcolors.ENDC)
                        inventory['beaver']['quantity'] = inventory['beaver']['quantity'] + 1
                        variable['combat end'] = 9
                        east_forest()

intro()
