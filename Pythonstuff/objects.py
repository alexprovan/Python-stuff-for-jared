#stats are health,mana,stamina add up to 40 at the start
#skill are attack,defense,Agility,Magic,Weaponry add up to 5 at the start
import random
races = {
    'Human': {'skill':(1,1,1,1,1), 'stat':(15,15,10), 'ability':'bonusperk'}, 
    'Elf': {'skill':(1,0,2,2,0), 'stat':(10,20,10), 'ability':'fortifymagic'},
    'Dark_Elf': {'skill':(2,0,1,2,0), 'stat':(10,20,10), 'ability':'fortifyattack'},
    'Orc': {'skill':(2,1,0,0,2), 'stat':(15,10,15), 'ability':'fortifyweaponry'},
    'Dwarf': {'skill':(0,2,2,0,1), 'stat':(20,10,10), 'ability':'fortifydefense'},
    'Halfling': {'skill':(0,1,2,2,0), 'stat':(10,10,20), 'ability':'fortifyagility'}}

chclasses = {
        'Mage': {'skill':(2,0,1,3,0), 'stat':(0,30,0)},
	'Rogue': {'skill':(0,0,0,0,0), 'stat':(30,0,0)},
	'Thief': {'skill':(0,0,0,0,0), 'stat':(0,0,30)},
	'Warrior': {'skill':(0,0,0,0,0), 'stat':(30,0,0)},
	'Battlemage': {'skill':(3,1,0,2,0), 'stat':(30,0,0)},
	'Spellsword': {'skill':(2,0,0,3,1), 'stat':(0,30,0)},
	'Ranger': {'skill':(1,0,2,0,3), 'stat':(0,0,30)},
	'Monk': {'skill':(0,3,2,1,0), 'stat':(30,0,0)}}

enemies = {
    'level1': {
        'Bonewalker': {'eclass':'undead', 'skill':(1,2,1,1,1), 'stat':(15,15,10), 'ability':'bonusperk'},
        'Novice': {'eclass':'mage', 'skill':(1,1,1,2,1), 'stat':(15,15,10), 'ability':'bonusperk'},
        'Imp': {'eclass':'monster', 'skill':(1,1,1,1,2), 'stat':(15,15,10), 'ability':'bonusperk'},
        'Unicorn': {'eclass':'boss', 'skill':(2,3,1,1,1), 'stat':(15,15,10), 'ability':'bonusperk'}},
    'level2': {
        'Zombie': {'eclass':'undead', 'skill':(2,3,1,1,1), 'stat':(20,20,15), 'ability':'bonusperk'},
        'Apprentice': {'eclass':'mage', 'skill':(2,1,1,3,1), 'stat':(20,20,15), 'ability':'bonusperk'},
        'Goblin': {'eclass':'monster', 'skill':(2,1,1,1,3), 'stat':(20,20,15), 'ability':'bonusperk'},
        'Giant': {'eclass':'boss', 'skill':(2,2,2,2,3), 'stat':(20,20,15), 'ability':'bonusperk'}},
    'level3': {
        'Vampire': {'eclass':'undead', 'skill':(3,4,2,2,2), 'stat':(25,25,20), 'ability':'bonusperk'},
        'Adept': {'eclass':'mage', 'skill':(3,2,2,4,2), 'stat':(25,25,20), 'ability':'bonusperk'},
        'Troll': {'eclass':'monster', 'skill':(3,2,2,2,4), 'stat':(25,25,20), 'ability':'bonusperk'},
        'Grey': {'eclass':'boss', 'skill':(3,3,4,4,3), 'stat':(25,25,20), 'ability':'bonusperk'}},
    'level4': {
        'Ghost': {'eclass':'undead', 'skill':(4,5,3,3,3), 'stat':(30,30,25), 'ability':'bonusperk'},
        'Expert': {'eclass':'mage', 'skill':(4,3,3,5,3), 'stat':(30,30,25), 'ability':'bonusperk'},
        'Cockatrice': {'eclass':'monster', 'skill':(4,3,3,3,5), 'stat':(30,30,25), 'ability':'bonusperk'},
        'Doppelganger': {'eclass':'boss', 'skill':(4,4,5,5,5), 'stat':(30,30,30), 'ability':'bonusperk'}},
    'level5': {
        'Ghoul': {'eclass':'undead', 'skill':(5,6,4,4,4), 'stat':(35,35,30), 'ability':'bonusperk'},
        'Master': {'eclass':'mage', 'skill':(5,4,4,6,4), 'stat':(35,35,30), 'ability':'bonusperk'},
        'Cerebrus': {'eclass':'monster', 'skill':(5,4,4,4,6), 'stat':(35,35,30), 'ability':'bonusperk'},
        'Minotaur': {'eclass':'boss', 'skill':(6,7,6,6,6), 'stat':(35,35,30), 'ability':'bonusperk'}},
    'level6': {
        'Necromancer': {'eclass':'undead', 'skill':(7,6,6,8,6), 'stat':(45,45,40), 'ability':'bonusperk'},
        'Exceptional': {'eclass':'mage', 'skill':(6,7,6,8,6), 'stat':(45,45,40), 'ability':'bonusperk'},
        'Banshee': {'eclass':'monster', 'skill':(7,6,8,6,6), 'stat':(45,45,40), 'ability':'bonusperk'},
        'Golem': {'eclass':'boss', 'skill':(9,7,7,7,8), 'stat':(45,45,40), 'ability':'bonusperk'}},
    'level7': {
        'Litche': {'eclass':'undead', 'skill':(9,10,8,8,8), 'stat':(55,55,50), 'ability':'raiseundead'},
        'Legendary': {'eclass':'mage', 'skill':(9,8,8,10,8), 'stat':(55,55,50), 'ability':'bonusperk'},
        'Dragon': {'eclass':'monster', 'skill':(9,8,10,8,8), 'stat':(55,55,50), 'ability':'bonusperk'},
        'Grimmer': {'eclass':'boss', 'skill':(10,10,9,10,9), 'stat':(55,55,50), 'ability':'bonusperk'}}} 
        
