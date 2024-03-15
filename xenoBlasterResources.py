#xenoBlasterFunctions

import msvcrt
import os
import sys
import random
import time

#variables
italicOn = '\x1b[3m'

italicOff = '\x1b[0m'

#WEAPONS
weaponChoices = ("d", "p", "s", "f")

dagger = {
    "Name": "Dagger",	
    "Damage": 10,
    "Critical Chance": 30,
    "Accuracy": 90,
    "Defense": 25,
    "Attack": "You slash...",
    "Hit": "...and cut deep!",
    "Miss": "...but you can't manage to hit it!",
    "Dodge": "...but unbelievably you dodge it!",
    "Get Hit": "...aaaaaand nope. Tough to dodge this close up, eh?"
}

pistol = {
    "Name": "Pistol",
    "Critical Chance": 15,
    "Damage": 25,
    "Accuracy": 75,
    "Defense": 50,
    "Attack": "You fire your pistol...",
    "Hit": "...and land your shot!",
    "Miss": "...but you're not sure where you were aiming...",
    "Dodge": "...but you just manage to duck out of the way.",
    "Get Hit": "...and connects cleanly, knocking you back."
}

shotgun = {
    "Name": "Shotgun",	
    "Critical Chance": 10,
    "Damage": 50,
    "Accuracy": 50,
    "Defense": 33,
    "Attack": "You fire your shotgun...",
    "Hit": "...and the spray of pellets hits the mark!",
    "Miss": "...but the pellets only graze it...",
    "Dodge": "...but you deftly escape with a roll.",
    "Get Hit": "...and hits you square in the chest."
}

feather = {
    "Name": "Feather",	
    "Damage": 5,
    "Accuracy": 100,
    "Critical Chance": 15,
    "Defense": 50,
    "Attack": "You rapidly swish your feather back and forth and...",
    "Hit": "...tickle it? Great Job.",
    "Miss": "",
    "Dodge": "...but you feel light as a feather(imsosorry)and easily dodge.",
    "Get Hit": "...and the feather couldn't save you this time."
}

bfg = {
    "Name": "BFG",
    "Damage": random.randint(75, 150),
    "Critical Chance": 40,
    "Accuracy": 98,
    "Defense": 50,
    "Attack": "The barrel spins, emmitting light rapidly...",
    "Hit": "...none of which seems to hit the mark.",
    "Miss": "...which slams into the alien, leaving deep gashes.",
    "Dodge": "... but the light from the gun forms into a shield, deflecting all damage",
    "Get Hit": "...and hits, throwing you backwards.\n You scramble back to your feet.",

}
 
#ALIENS
squishy = {
	"Name": "Squishy",
	"HP": 50,
	"Damage": 5,
	"Attack": "Squishy lunges forward, head down for a vicious headbutt...",
	"Death": "With an ugly cry, Squishy falls to the floor, defeated."
}

pokey = {
    "Name": "Pokey",
    "HP": 100,
    "Damage": 10,
    "Attack": "Pokey's sharp tail darts towards you...",
}

stabby = {
    "Name": "Stabby",
    "HP": 150,
    "Damage": 15,
    "Attack": "Stabby... well he tries to stab you...",
}

scary = {
    "Name": "Scary",
    "HP": 200,
    "Damage": 25,
    "Attack": "Scary lunges forward, its tongue shooting towards you...",
}

#FUNCTIONS
def logo():
	print(r'''
 __      __       .__                                ___________             
/  \    /  \ ____ |  |   ____  ____   _____   ____   \__    ___/___          
\   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \    |    | /  _ \         
 \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/    |    |(  <_> )        
  \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >   |____| \____/         
       \/       \/          \/            \/     \/                  


____  ___                  __________.__                   __                
\   \/  /____   ____   ____\______   \  | _____    _______/  |_  ___________ 
 \     // __ \ /    \ /  _ \|    |  _/  | \__  \  /  ___/\   __\/ __ \_  __ \
 /     \  ___/|   |  (  <_> )    |   \  |__/ __ \_\___ \  |  | \  ___/|  | \/
/___/\  \___  >___|  /\____/|______  /____(____  /____  > |__|  \___  >__|   
      \_/   \/     \/              \/          \/     \/            \/       
''')

def clearScreen():
	os.system('cls')

def wait(waitSecs):
	time.sleep(waitSecs)

def randomChoice(choices):
	choice = random.choice(choices)
	return choice

def randomDelay():
	wait(random.uniform(0.1, 0.5))

def randomPrint(string):
	"""prints the string in a semi-random location"""
	print('\n' * random.randint(1, 6) + '\t' * random.randint(0, 6 ) + string)
	randomDelay()

def attackRoll(accuracy, critChance):
	"""uses weapon accuracy and critical chance to determine if
	   the player's attack crits, hits, or misses"""
	roll = random.randint(1, 100)
	if roll <= critChance:
		return "Crit"
	if roll <= accuracy:
		return "Hit"
	else:
		return "Miss"

def defenseRoll(defense):
	"""uses weapon defense to determine
	   if a player is hit by the alien"""
	roll = random.randint(1, 100)
	if roll <= defense:
		return "Dodged"
	else:
		return "Hit"

def typeThing(thing, speed = 0.05):
	"""prints a line character by character
		at a default speed of .05characters/second"""
	for i, ch in enumerate(thing):
		if i + 1 == len(thing):
			print(ch)
		else:
			print(ch, end="")
			sys.stdout.flush()
			wait(speed)

def weaponSelection():
	"""loop for weapon selection. takes player input,
	checks if it's valid and resets if not, offers
	information about the weapon's stats and a chance
	to reselect."""
	while True:
		typeThing("You see a [S]hotgun, a [P]istol, a pair of [D]aggers, and... is that a [F]eather?")
		try:
			weapon = input("\nChoose your Weapon: [S/P/D/F]\n")
			if weapon[0].strip().lower() not in weaponChoices:
				typeThing("Please choose one of the listed options.\n")
				continue
			else:
				weapon = weapon[0].strip().lower()
		except:
			typeThing("Please choose one of the listed options.\n")
			continue
		if weapon == 's':
			typeThing("\nYou take the shotgun in your hands, cocking it with a satisfying 'CH-CHUNK'...\n")
			typeThing(f'{italicOn}"This thing can do big damage, but I might have trouble hitting them..."{italicOff}\n')
			try:
				confirm = input("Are you sure? (Y/N)\n")
				if confirm[0].strip().lower() != 'y':
					continue
				else:
					weapon = shotgun
			except:
				continue		
		elif weapon == "p":
			weapon = pistol
			typeThing("\nYou take the pistol, smirking as your hand wraps around its familiar grip.\n")
			typeThing(f'{italicOn}"Not a lot of damage, but this will make dodging easier...{italicOff}\n')
			try:
				confirm = input("Are you sure? (Y/N)\n")
				if confirm[0].strip().lower() != 'y':
					continue
				else:
					weapon = pistol
			except:
				continue
		elif weapon == "d":
			typeThing("\nYou grab the daggers, spinning them in your hands.\n")
			typeThing(f'{italicOn}"Not much damage, too close range to dodge attacks reliably..."\n')
			typeThing(f'"...but fast attacks, and a good chance of hitting a vital spot..."{italicOff}\n')
			try:
				confirm = input("Are you sure? (Y/N)\n")
				if confirm[0].strip().lower() != 'y':
					continue
				else:
					weapon = dagger 
			except:
				continue
		elif weapon == "f":
			typeThing("\n...\n", .3)
			typeThing("Really?\n")
			typeThing("The feather?\n")
			typeThing("Do you have a death wish?\n")
			typeThing("[The feather is super underpowered]")
			try:
				confirm = input("Are you sure? (Y/N)\n")
				if confirm[0].strip().lower() != 'y':
					continue	
				else:
					weapon = feather	
			except:
				continue
		typeThing(f"\n{weapon.get("Name")} in hand, you make your way to the door...\n")	
		return weapon

def standardCombatLoop(weapon, alien, playerHP):
	"""loop for combat. takes players weapon choice and hp,
	   along with the current alien and assigns relevant variables,
	   uses attack roll to check for crits, hits, and misses,  
	   applies damage, then uses defense roll to determine if 
	   alien hits or misses"""
	weaponDamage = weapon.get("Damage")
	attackMSG = weapon.get("Attack")
	hitMSG = weapon.get("Hit")
	missMSG = weapon.get("Miss")
	dodgeMSG = weapon.get("Dodge")
	alienHP = alien.get("HP")
	alienDMG = alien.get("Damage")
	alienAtkMSG = alien.get("Attack")
	alienHitMSG = weapon.get("Get Hit")
	while True:
		print("==============================")
		print(f"You: {playerHP}hp  VS  {alien.get("Name")}: {alienHP}hp")
		print("==============================\n")
		wait(1)
		typeThing(attackMSG)
		hitCheck = attackRoll(weapon.get("Accuracy"), weapon.get("Critical Chance"))
		wait(1)
		if hitCheck == "Crit":
			if weapon == feather:
				alienHP -= alienHP
				typeThing("...and the creature makes a horrid croaking sound...\n")
				typeThing(f"{italicOn}Is...\n")
				typeThing(f'Is that this things laugh???"{italicOff}\n')
				typeThing(f"As the croaking gets louder, the creature expands until...\n")
				print("POP\n")
				typeThing("...it explodes\n")
				typeThing(f"{italicOn}I can't believe that worked.{italicOff}\n")
				clearScreen()
				return playerHP
			damage = weaponDamage * 1.5
			alienHP -= damage
			typeThing(hitMSG)
			typeThing(f"Critical Hit! You deal {damage} damage!\n")
		elif hitCheck == "Hit":
			damage = weaponDamage
			alienHP -= damage
			typeThing(hitMSG)
			typeThing(f"You deal {damage} damage!\n")
		elif hitCheck == "Miss":
			typeThing(missMSG)
			typeThing(f"You deal... well... 0 damage.\n")
		if alienHP <= 0:
			print("You killed it!")
			clearScreen()
			return playerHP
		typeThing(alienAtkMSG)
		dodgeCheck = defenseRoll(weapon.get("Defense"))
		if dodgeCheck == "Hit":
			playerHP -= alienDMG
			typeThing(alienHitMSG)
			typeThing(f"You take {alienDMG} damage!\n")
		else:
			typeThing(dodgeMSG)
			typeThing("You avoid all damage!\n")
		if playerHP <= 0:
			typeThing("You Died", .2)
			clearScreen()
			return playerHP

def daggerCombatLoop(weapon, alien, playerHP):
	weaponDamage = weapon.get("Damage")
	attackMSG = weapon.get("Attack")
	hitMSG = weapon.get("Hit")
	missMSG = weapon.get("Miss")
	dodgeMSG = weapon.get("Dodge")
	alienHP = alien.get("HP")
	alienDMG = alien.get("Damage")
	alienAtkMSG = alien.get("Attack")
	alienHitMSG = weapon.get("Get Hit")
	while True:
		print("==============================")
		print(f"You: {playerHP}hp  VS  {alien.get("Name")}: {alienHP}hp")
		print("==============================\n")
		wait(1)
		typeThing(attackMSG)
		hitCheck = attackRoll(weapon.get("Accuracy"), weapon.get("Critical Chance"))
		wait(1)
		if hitCheck == "Crit":
			damage = weaponDamage * 1.5
			alienHP -= damage
			typeThing(hitMSG)
			typeThing(f"Critical Hit! You deal {damage} damage!\n")
		elif hitCheck == "Hit":
			damage = weaponDamage
			alienHP -= damage
			typeThing(hitMSG)
			typeThing(f"You deal {damage} damage!\n")
		elif hitCheck == "Miss":
			typeThing(missMSG)
			typeThing(f"You deal... well... 0 damage.\n")
		if alienHP <= 0:
			print("You killed it!")
			clearScreen()
			return playerHP
		typeThing(attackMSG)
		hitCheck = attackRoll(weapon.get("Accuracy"), weapon.get("Critical Chance"))
		wait(1)
		if hitCheck == "Crit":
			damage = weaponDamage * 1.5
			alienHP -= damage
			typeThing(hitMSG)
			typeThing(f"Critical Hit! You deal {damage} damage!\n")
		elif hitCheck == "Hit":
			damage = weaponDamage
			alienHP -= damage
			typeThing(hitMSG)
			typeThing(f"You deal {damage} damage!\n")
		elif hitCheck == "Miss":
			typeThing(missMSG)
			typeThing(f"You deal... well... 0 damage.\n")
		if alienHP <= 0:
			print("You killed it!")
			clearScreen()
			return playerHP
		typeThing(alienAtkMSG)
		dodgeCheck = defenseRoll(weapon.get("Defense"))
		if dodgeCheck == "Hit":
			playerHP -= alienDMG
			typeThing(alienHitMSG)
			typeThing(f"You take {alienDMG} damage!\n")
		else:
			typeThing(dodgeMSG)
			typeThing("You avoid all damage!\n")
		if playerHP <= 0:
			typeThing("You Died", .2)
			clearScreen()
			return playerHP
	pass



