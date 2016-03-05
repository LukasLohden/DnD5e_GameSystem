###################################################################################################
# PROGRAM:     Dungeons and Dragons Fifth Edition Game System                                     #
# MODULE:      CharacterClass.py                                                                       #
# AUTHOR:      Luke Lohden                                                                        #
# CREATED:     2016 • 02 • 15                                                                     #
###################################################################################################

###################################################################################################
"""
DESCRIPTION:
This module defines the character class data structure that stores a character's statistics and
information. It will also contain definitions for the execution of player actions that have an
effect on the character's data. ServerLoop uses this module to store information for a single
character.
"""
###################################################################################################

###################################################################################################
"""
HEADER:
    
    DATA:
    
    Initialization:            ( Details, Persona, Abilities, Skills, spells, inventory)
    
    Details:         namedtuple( player_class, inspiration, armor_class, initiative, speed, 
                                 health, hit_dice, SavingThrows, attacks, proficiencies)
    
    SavingThrows:    namedtuple( strength, dexterity, constitution, intelligence, wisdom, charisma)
    
    Persona:         namedtuple( name, Appearance, features, background, trait, ideal, bond, flaw,
                                 languages, companion, alignment, nature, deity )
                         
    Appearance:      namedtuple( race, height, age, gender, complexion, build, fitness, weight,
                                 hair_color, hair_length, hair_type, facial_hair, body_hair )
    
    Abilities:       namedtuple( strength, dexterity, constitution, intelligence, wisdom, charisma)
    
    Skills:          namedtuple( acrobatics, animal_handling, arcana, athletics, deception, history
                                 insight, intimidation, investigation, medicine, nature, perception
                                 performance, persuasion, religion, sleight of hand, stealth, 
                                 survival )
                                 
    spells:                list( Spell_1, Spell_2, ••• Spell_N )
    
    Spell:           namedtuple( name, level, school, casting_time, ritual, concentration )
    
    inventory:             list( Item_1, Item_2, ••• Item_N )
    
    Item:            namedtuple( type, cost, rarity, damage, weight, properties, armor_class,
                                 strength, stealth, speed, carrying_capacity, size, equipped )
    
    ACTIONS:
    
    gain_XP(xp: int) -> level: int
    
    take_damage(dmg: int) -> health: int
    
    heal_damage(dmg: int) -> health: int
    
    pickup_item(item: Item) -> null
    
    lose_item(item: Item) -> null
    
    equip_item(item: Item) -> null
    
    prepare_spells(spell: Spell) -> null
    
    use_spell(spell: Spell) -> null
    
    QUERIES:
    
    get_Appearance() -> Appearance: namedtuple
    
    get_Details() -> Class: namedtuple
    
    get_Persona() -> Persona: namedtuple
    
    get_Abilities() -> Abilities: namedtuple
    
    get_Spells() -> [Spell]: [namedtuple]
    
    get_Skills() -> Skills: namedtuple
    
    get_Inventory() -> [Item]: [namedtuple]
    
    get_Equipped() -> Equipped: namedtuple
    
"""
###################################################################################################
# IMPORTS                                                                                         #
###################################################################################################

from collections import namedtuple

###################################################################################################
# DATA                                                                                            #
###################################################################################################

Details =      namedtuple('Details',      'player_class inspiration armor_class initiative speed \
                                           health hit_dice SavingThrows attacks proficiencies')

SavingThrows = namedtuple('SavingThrows', 'strength dexterity constitution intelligence wisdom \
                                           charisma')

Persona =      namedtuple('Persona',      'name Appearance features background trait ideal bond\
                                           flaw languages companion alignment nature deity' )

Appearance =   namedtuple('Appearance',   'race height age gender complexion build fitness,\
                                           weight hair_color hair_length hair_type facial_hair\
                                           body_hair')

Abilities =    namedtuple('Abilities',    'strength dexterity constitution intelligence wisdom\
                                           charisma')

Skill =        namedtuple('Skills',       'acrobatics animal_handling arcana athletics deception\
                                           history insight intimidation investigation medicine\
                                           nature perception performance persuasion religion\
                                           sleight_of_hand stealth survival')

Spell =        namedtuple('Spell',        'name level school casting_time ritual concentration')

Item =         namedtuple('Item',         'type cost rarity damage weight properties armor_class\
                                           strength stealth speed carrying_capacity size equipped')

###################################################################################################
# CLASS                                                                                           #
###################################################################################################

class Character:
    
    def __init__(self, Details, SavingThrows, Persona, Appearance, Abilities, Skills, spells, \
                 inventory):
        
        self.Details = Details
        self.SavingThrows = SavingThrows
        self.Persona = Persona
        self.Appearance = Appearance
        self.Abilities = Abilities
        self.Skill = Skill
        self.spells = spells
        
#ACTIONS###########################################################################################
    """
    ACTIONS:
    
    gain_XP(xp: int) -> level: int
    
    take_damage(dmg: int) -> health: int
    
    heal_damage(dmg: int) -> health: int
    
    pickup_item(item: Item) -> null
    
    lose_item(item: Item) -> null
    
    equip_item(item: Item) -> null
    
    prepare_spells(spell: Spell) -> null
    
    use_spell(spell: Spell) -> null
    """
    
    def gain_XP(self, xp: int) -> int:
        pass
   
    def take_damage(self, dmg: int) -> int:
        pass

    def heal_damage(self, dmg: int) -> int:
        pass

    def pickup_item(self, item: Item) -> Item:
        pass
    
    def lose_item(self, item: Item) -> Item:
        pass    

    def equip_item(self, item: Item) -> Item:
        pass

    def prepare_spell(self, spell: Spell) -> Spell:
        pass
    
    def use_spell(self, spell: Spell) -> Spell:
        pass
    
#QUERIES###########################################################################################
    
    """
    QUERIES:
    
    get_Appearance() -> Appearance: namedtuple
    
    get_Details() -> Class: namedtuple
    
    get_Persona() -> Persona: namedtuple
    
    get_Abilities() -> Abilities: namedtuple
    
    get_Spells() -> [Spell]: [namedtuple]
    
    get_Skills() -> Skills: namedtuple
    
    get_Inventory() -> [Item]: [namedtuple]
    
    get_Equipped() -> Equipped: namedtuple
    
    """
    
#DEBUG#############################################################################################
    
    
    
#HELPER############################################################################################

    def _check_details(self, details: Details) -> Details:
        pass
    
    def _check_savingthrows(self, details: SavingThrows) -> SavingThrows:
        pass
    
    def _check_persona(self, details: Persona) -> Persona:
        pass
    
    def _check_appearance(self, details: Appearance) -> Appearance:
        pass
    
    def _check_abilities(self, details: Abilities) -> Abilities:
        pass
    
    def _check_skills(self, details: [Skill]) -> [Skill]:
        pass
    
    def _check_spells(self, details: [Spell]) -> [Spell]:
        pass













###################################################################################################