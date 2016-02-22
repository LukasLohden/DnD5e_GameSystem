####################################################################################################

# Game System Program
# Lukas Lohden, Fall 2014
# Serves to create and store characters; and to create random numbers, loot, and characters

####################################################################################################

# Imports:

from random import randrange
from collections import namedtuple
import random
from random import choice

# MAIN PROGRAM:

def game_system():
    """ Main Program
    """
    print("Welcome to the Game System Program.")
    Characters = Collection_create()
    Characters = handle_commands(Characters)
    print("\n Program closed.")

# MENU:

MENU = """
Game System Program --- Choose one:
  1:  Create a new character
  2:  Remove a character
  3:  Look up information for an existing character
  4:  Print all characters
  5:  Roll die(s)
  6:  Generate a random character
  7:  Generate random loot
  8:  
  9:  
  0:  Quit
"""

# Command Function:

def handle_commands(C: list) -> list:
    """ Displays menu, accepts and processes commands.
    """
    # TEST: Adds Devandaheart to the Character Collection:
    Collection_add(C, ch1)
    while True:
        response = input(MENU)
        if response == '0':
            return C        
        elif response == '1':
            new_char = Character_create()
            C = Collection_add(C, new_char)
        elif response == '2':
            n = input("Enter the name of the character to be removed:     ")
            C = Collection_remove_by_name(C, n)
        elif response == '3':
            n = input("Enter the name of the character to search for:     ")
            search = Collection_search_by_name(C, n)
            for CH in search:
                print(Character_display(CH))
        elif response == '4':
            for CH in C:
                print(Character_display(CH))
        elif response == '5':
            d = input("Enter the type of die to roll (ex: d20 = 20, d8 = 8):     ")
            n = input("Enter the number of times to roll:     ")
            print(Dice_roll_display(Dice_roll(d, n)))
        elif response == '6':
            char_type = input("Enter type of character to be created (NPC, Mob, Elite, or Boss):     ")
            if char_type == 'NPC' or 'npc':
                C = Collection_add(C, Character_create_NPC)
                print(Character_display(C[-1]))
            elif char_type == 'Mob' or 'mob':
                C = Collection_add(C, Character_create_mob)
                print(Character_display(C[-1]))
            elif char_type == 'Elite' or 'elite':
                C = Collection_add(C, Character_create_elite)
                print(Character_display(C[-1]))
            elif char_type == 'Boss' or 'boss':
                C = Collection_add(C, Character_create_boss)
                print(Character_display(C[-1]))
            else: invalid_command(char_type)
        else:
            invalid_command(response)

# Invalid Command Function:

def invalid_command(response):
    """ Prints message for invalid menu command.
    """
    print("(" + response + ") is not a valid command. Try again.")

####################################################################################################

# Character Functions:

####################################################################################################
          
# Create New Character:

Character = namedtuple ('Character', 'name Appearance Statistics abilities inventory')
# Example: ch1 = Character('Devandaheart', ap1, st1, va1, ['Ability1'], ['Item1'])
def Character_create() -> Character:
    """ Prompts user for fields of Character; creates and returns
    """
    print(" \n Character Creation: \n")
    return Character(
        input("Enter the character's name:    "), Appearance_create(), Statistics_create(),
        input("Enter character abililties:     "),
        input("Enter character inventory:     "))

Appearance = namedtuple ('Appearance', 'gender race height weight hair skin')
# Example: ap1 = Appearance('male', 'human', '6ft', 165, 'dirty-blonde', 'tan')
def Appearance_create() -> Appearance:
    """ Prompts user for fields of Appearance; creates and returns
    """
    print(" \n Character's Appearance: \n")
    return Appearance(
        input("Enter gender:     "),
        input("Enter race:     "),
        input("Enter height:     "),
        input("Enter weight:     "),
        input("Enter hair color:     "),
        input("Enter skin tone:     "))

Statistics = namedtuple ('Statistics', 'Attributes Skills Values')
# Example: st1 = Statistics(at1, sk1, va1)
def Statistics_create() -> Statistics:
    """ Prompts user for fields of Statistics; creates and returns
    """
    print(" \n Character's Statistics: \n")
    return Statistics(Attributes_create(), Skills_create(), Values_create())

Values = namedtuple('Values', 'health action_points')
# Example: va1 = Values(145, 79)
def Values_create() -> Values:
    """
    """
    print(" \n Character's Health & Action Points")
    return Values(
        int(input("Enter health value:     ")),
        int(input("Enter action-point value:     ")))

Attributes = namedtuple ('Attributes', 'strength perception endurance charisma intellect agility luck')
# Example: at1 = Attributes(2, 10, 3, 7, 5, 8, 4)
def Attributes_create() -> Attributes:
    """ Prompts user for fields of Attributes; creates and returns
    """
    print(" \n Character's Attributes: \n")
    return Attributes(
        int(input("Enter strength attribute:     ")),
        int(input("Enter perception attribute:     ")),
        int(input("Enter endurance attribute:     ")),
        int(input("Enter charisma attribute:     ")),
        int(input("Enter intellect attribute:     ")),
        int(input("Enter agility attribute:     ")),
        int(input("Enter luck attribute:     ")))

Skills = namedtuple ('Skills', 'Combat Active Passive')
# Example: sk1 = Skills(co1, ac1, pa1)
def Skills_create() -> Skills:
    """ Prompts user for fields of Skills; creates and returns
    """
    print(" \n Character's Skills: \n")
    return Skills(Combat_create(), Active_create(), Passive_create())

Combat = namedtuple ('Combat', 'small_guns big_guns energy_weapons explosives unarmed melee_weapons throwing')
# Example: co1 = Combat(5, 5, 5, 5, 5, 5, 5)
def Combat_create() -> Combat:
    """ Prompts user for fields of Combat; creates and returns
    """
    print(" \n Character's Combat Skills: \n")
    return Combat(
        int(input("Enter small guns skill:     ")),
        int(input("Enter big guns skill:     ")),
        int(input("Enter energy weapon skill:     ")),
        int(input("Enter explosives skill:     ")),
        int(input("Enter unarmed skill:     ")),
        int(input("Enter melee weapon skill:     ")),
        int(input("Enter throwing skill:     ")))

Active = namedtuple ('Active', 'medicine lockpick repair science sneak')
# Example: ac1 = Active(5, 5, 5, 5, 5)
def Active_create() -> Active:
    """ Prompts user for fields of Active; creates and returns
    """
    print(" \n Character's Active Skills: \n")
    return Active(
        int(input("Enter medicine skill:     ")),
        int(input("Enter lockpick skill:     ")),
        int(input("Enter repair skill:     ")),
        int(input("Enter science skill:     ")),
        int(input("Enter sneak skill:     ")))

Passive = namedtuple ('Passive', 'barter deception gambling survival persuasion pilot speech')
# Example: pa1 = Passive(5, 5, 5, 5, 5, 5, 5)
def Passive_create() -> Passive:
    """ Prompts user for fields of Passive; creates and returns
    """
    print(" \n Character's Passive Skills: \n")
    return Passive(
        int(input("Enter barter skill:     ")),
        int(input("Enter deception skill:     ")),
        int(input("Enter gambling skill:     ")),
        int(input("Enter survival skill:     ")),
        int(input("Enter persuasion skill:     ")),
        int(input("Enter pilot skill:     ")),
        int(input("Enter speech skill:     ")))

####################################################################################################

# Display Character Information:

def Character_display(char: Character) -> str:
    """ Converts Character namedtuple to readable format
    """
    return (
        "Name:     " + str(char.name) + "\n\n" +
        "Inventory:     " + str(char.inventory) + "\n" +
        "Abilities:     " + str(char.abilities) + "\n\n" +
        "Health and Action Points:  \n" +
        Values_display(char.Statistics.Values) +
        "Appearance: \n" +
        Appearance_display(char.Appearance) +
        "Attributes: \n" +
        Attributes_display(char.Statistics.Attributes) +
        "Combat Skills: \n" +
        Combat_display(char.Statistics.Skills.Combat) +
        "Active Skills: \n" +
        Active_display(char.Statistics.Skills.Active) +
        "Passive Skills: \n" + 
        Passive_display(char.Statistics.Skills.Passive))

def Values_display(val: Values) -> str:
    """ Converts Values namedtuple of Character into readable format
    """
    return (
        "Health:     " + str(val.health) + "\n" +
        "Action Points:     " + str(val.action_points) + "\n\n")

def Appearance_display(app: Appearance) -> str:
    """ Converts Appearance namedtuple of Character into readable format
    """
    return (
        "Gender:     " + str(app.gender) + "\n" +
        "Race:     " + str(app.race) + "\n" +
        "Height:     " + str(app.height) + "\n" +
        "Weight:     " + str(app.weight) + "\n" +
        "Hair Color:     " + str(app.hair) + "\n" +
        "Skin Tone:     " + str(app.skin) + "\n\n" )
        
def Attributes_display(att: Attributes) -> str:
    """ Converts Attributes namedtuple of Character into readable format
    """
    return (
        "Strength:     " + str(att.strength) + "\n" +
        "Perception:     " + str(att.perception) + "\n" +
        "Endurance:     " + str(att.endurance) + "\n" +
        "Charisma:    " + str(att.charisma) + "\n" +
        "Intellect:     " + str(att.intellect) + "\n" +
        "Agility:     " + str(att.agility) + "\n" +
        "Luck:     " + str(att.luck) + "\n\n")
        
def Combat_display(com: Combat) -> str:
    """ Converts Combat namedtuple of Character into readable format
    """
    return (
        "Small Guns Skill:     " + str(com.small_guns) + "\n" +
        "Big Guns Skill:     " + str(com.big_guns) + "\n" +
        "Energy Weapons Skill     " + str(com.energy_weapons) + "\n" +
        "Explosives Skill:     " + str(com.explosives) + "\n" +
        "Unarmed Skill:     " + str(com.unarmed) + "\n" +
        "Melee Weapons Skill:     " + str(com.melee_weapons) + "\n" +
        "Throwing Skill:     " + str(com.throwing) + "\n\n" )

def Active_display(act: Active) -> str:
    """ Converts Active namedtuple of Character into readable format
    """
    return (
        "Medicine Skill:     " + str(act.medicine) + "\n" +
        "Lockpick Skill:     " + str(act.lockpick) + "\n" +
        "Repair Skill:     " + str(act.repair) + "\n" +
        "Science Skill:     " + str(act.science) + "\n" +
        "Sneak Skill:     " + str(act.sneak) + "\n\n" )

def Passive_display(pas: Passive) -> str:
    """ Converts Passive namedtuple of Character into readable format
    """
    return (
        "Barter Skill:     " + str(pas.barter) + "\n" +
        "Deception Skill:     " + str(pas.deception) + "\n" +
        "Gambling Skill:     " + str(pas.gambling) + "\n" +
        "Survival Skill:     " + str(pas.survival) + "\n" +
        "Persuasion Skill:     " + str(pas.persuasion) + "\n" +
        "Pilot Skill:     " + str(pas.pilot) + "\n" +
        "Speech Skill:     " + str(pas.speech) + "\n\n" )

####################################################################################################

# Random Generation Functions:
        
####################################################################################################

# Dice Rolling:

def Dice_roll(die: int, number: int) -> list:
    """ Generates a list of input length of random numbers according to input die type 
    """
    rolls = []
    for i in range(0, int(number)):
        rolls.append(randrange(1, int(die) + 1))
    return rolls

def Dice_roll_display(Dice_roll: list) -> str:
    """ Converts the list from Dice_roll into readable format to be returned to the user
    """
    display = []
    display_string = ''
    for r in range(len(Dice_roll)):
        display.append("Roll " + str(r+1) + ": " + str(Dice_roll[r]))
    for d in display:
        display_string += d + "\n"
    result = "Result of dice rolls: \n\n" + display_string
    return result

# Create Random Characters:

def Character_create_NPC(gender: str) -> Character:
    """ Creates a Character for the purpose of player non-combat interaction
    """
    gender = gender.lower()
    new_NPC = Character_create_random(gender)
    return new_NPC
    
def Character_create_mob(gender: str) -> Character:
    """ Creates a weak Character for the purpose of player combat interaction
    """
    gender = gender.lower()
    new_mob = Character_create_random(gender)
    return new_mob

def Character_create_elite(gender: str) -> Character:
    """ Creates an experienced Character for the purpose of player combat interaction
    """
    gender = gender.lower()
    new_elite = Character_create_random(gender)
    return new_elite
    
def Character_create_boss(gender: str) -> Character:
    """ Creates a powerful Character for the purpose of player combat interaction
    """
    gender = gender.lower()
    new_boss = Character_create_random(gender)
    return new_boss

# Create Random Character Details:

def Character_create_random(gender: str) -> Character:
    """ Creates a randomly generated Character
    """
    return Character(Name_create_random(gender), Appearance_create_random(gender), Statistics_create_random(),
                     Abilities_create_random(), Inventory_create_random())

def remove_non_letters(line: str) -> str:
    """ Removes punctuation from given string 
    """
    word = ''
    for c in line:
        if c.isalpha() == True:
            word += c
    return word

def Name_create_random(gender: str) -> str:
    """ Creates a random name for a random Character of random gender
    """
    last_name = ''
    first_name = ''
    name = ''
    
    infile = open('surnames.txt', 'r')
    surnames = infile.readlines()
    infile.close()
    last_name += random.choice(surnames)

    if gender == 'male':
        infile = open('malenames.txt', 'r')
        malenames = infile.readlines()
        infile.close()
        first_name += random.choice(malenames)

    if gender == 'female':
        infile = open('femalenames.txt', 'r')
        femalenames = infile.readlines()
        infile.close()
        first_name += random.choice(femalenames)

    last_name = remove_non_letters(last_name)
    first_name = remove_non_letters(first_name)

    name += first_name
    name += ' '
    name += last_name
    
    return name

def Appearance_create_random(gender: str) -> Appearance:
    """ Creates a randomly generated Appearance for a Character
    """
    # PLACEHOLDER: Appearance files required before implementation
    return Appearance(gender, 'human', '6ft', '165', 'brown', 'caucasian')

def Abilities_create_random() -> list:
    """ 
    """
    # PLACEHOLDER: Abilities file required before implementation
    return []

def Inventory_create_random() -> list:
    """ 
    """
    # PLACEHOLDER: Inventory file required before implementation
    return []

def Statistics_create_random() -> Statistics:
    """ Creates randomly generated Statistics for a Character
    """
    return Statistics(Attributes_create_random, Skills_create_random, Values_create_random)
    
def Values_create_random() -> Values:
    """ Creates randomly generated Values for a Character
    """
    return Values(randrange(10, 40), randrange(40, 60))

def Attributes_create_random() -> Attributes:
    """ Creates randomly generated Attributes for Statistics
    """
    return Attributes(randrange(1, 10), randrange(1, 10), randrange(1, 10), randrange(1, 10),
                      randrange(1, 10), randrange(1, 10), randrange(1, 10))

def Skills_create_random() -> Skills:
    """ Creates randomly generated Skills for Statistics
    """
    return Skills(Combat_create_random, Active_create_random, Passive_create_random)

def Combat_create_random() -> Combat:
    """ Creates randomly generated Combat Skills
    """
    return Combat(randrange(1,50), randrange(1,50), randrange(1,50), randrange(1,50),
                  randrange(1,50), randrange(1,50), randrange(1,50))

def Active_create_random() -> Active:
    """ Creates randomly generated Active Skills
    """
    return Active(randrange(1,50), randrange(1,50), randrange(1,50), randrange(1,50),
                  randrange(1,50))

def Passive_create_random() -> Passive:
    """ Creates randomly generated Passive Skills
    """
    return Passive(randrange(1,50), randrange(1,50), randrange(1,50), randrange(1,50),
                  randrange(1,50), randrange(1,50), randrange(1,50))

####################################################################################################

# Loot Table Functions

####################################################################################################

####################################################################################################

# Character Collection Functions:

####################################################################################################

# Create a Collection of Characters:

def Collection_create() -> list:
    """ Return a new, empty collection
    """
    return [ ]

# Add a Character to the Collection:

def Collection_add(C: list, CH: Character) -> list:
    """ Return list of Characters with input Character added at end.
    """
    C.append(CH)
    return C

# Remove a Character from the Collection:

def Collection_remove_by_name(C: list, name: str) -> list:
    """ Given name, remove all Characters with that name from collection.
    """
    result = [ ]
    for CH in C:
        if CH.name != name:
            result.append(r)
    return result

# Search the Collection for a Character:

def Collection_search_by_name(C: list, name: str) -> list:
    """ Return list of Characters in input list whose name matches input string.
    """
    result = [ ]
    for CH in C:
        if CH.name == name:
            result.append(CH)
    return result

####################################################################################################

# Tests

####################################################################################################

print("System Tests: \n")

# Creates Test Character 'Devandaheart':

pa1 = Passive(5, 5, 5, 5, 5, 5, 5)
ac1 = Active(5, 5, 5, 5, 5)
co1 = Combat(5, 5, 5, 5, 5, 5, 5)
sk1 = Skills(co1, ac1, pa1)
at1 = Attributes(2, 10, 3, 7, 5, 8, 4)
va1 = Values(145, 79)
st1 = Statistics(at1, sk1, va1)
ap1 = Appearance('male', 'human', '6ft', 165, 'dirty-blonde', 'tan')
ab1 = ['Cloak'] # TBD - Namedtuple for abilties?
in1 = ['3x Syringes', 'Hammer', "3x Nails"] # TBD - Namedtuple for inventory?
ch1 = Character('Devandaheart', ap1, st1, ab1, in1)
print(ch1)

print()

# Tests Character Display Function:

print(Character_display(ch1))

print()

# Dice Roll Test:

print(Dice_roll_display(Dice_roll(8, 3)))

# Run the Program:

game_system()

####################################################################################################

# To-Do:

####################################################################################################

# Format Character display function

# Implement 'Quiz' section to determine character skills

# Complete Random Characters funtions

# Create loot table and loot drop functions

# Create file system to save characters & loot

# Create a tkinter function that creates a likeness of a character

# Create a character display sheet in a file that is filled in with character info and likeness

# Create a namedtuple for Abilities and Inventory

# Add a skill check system that rolls a check for a character's skill in specified area

####################################################################################################
