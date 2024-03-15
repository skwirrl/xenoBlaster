
from xenoBlasterResources import *

#START VARIABLES
playerHP = 100
alien = squishy
weapon = None
bfgPass = "feelingfancy"

#TITLE
clearScreen()
print(r'''
 __      __       .__                               
/  \    /  \ ____ |  |   ____  ____   _____   ____  
\   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \ 
 \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/ 
  \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >
       \/       \/          \/            \/     \/              
''')
wait(1)
clearScreen()
print(r'''
 __      __       .__                                ___________     
/  \    /  \ ____ |  |   ____  ____   _____   ____   \__    ___/___  
\   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \    |    | /  _ \ 
 \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/    |    |(  <_> )
  \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >   |____| \____/ 
       \/       \/          \/            \/     \/                  
''')
wait(1)
typeThing(r'''
____  ___                  __________.__                   __                
\   \/  /____   ____   ____\______   \  | _____    _______/  |_  ___________ 
 \     // __ \ /    \ /  _ \|    |  _/  | \__  \  /  ___/\   __\/ __ \_  __ \
 /     \  ___/|   |  (  <_> )    |   \  |__/ __ \_\___ \  |  | \  ___/|  | \/
/___/\  \___  >___|  /\____/|______  /____(____  /____  > |__|  \___  >__|   
      \_/   \/     \/              \/          \/     \/            \/        
''', .005)
print()
print()
print()
typeThing('\t\t\tpress any key to continue', .005)
while True:
	wait(.75)
	clearScreen()
	logo()
	wait(.5)
	clearScreen()
	logo()
	print()
	print()
	print()
	print('\t\t\tpress enter to continue')
	if msvcrt.kbhit():
		break
print()
typeThing("\t\t\t\tLet's go!")
wait(1)
input()
clearScreen()

#INTRO
typeThing("You were stationed aboard the Bebop - the famous Class-1 Space Cruiser.\n")
wait(.5)
typeThing("In fact, you had just been assigned there. A promotion, they said.\n")
wait(.5)
typeThing('"Head of Security"\n', 0.15)
wait(.5)
typeThing("But something felt wrong from the start.\n")
wait(.5)
typeThing("The boss had never liked you much - usually sending you to no-name stations to do menial work.\n")
wait(.5)
typeThing("So why this?\n")
wait(.5)
typeThing("And why now?\n", 0.2)
input("Enter to Continue")
for i in range(3):
	clearScreen()
	randomPrint("BANG")
	randomPrint("crrraAASH")
	clearScreen()
	randomPrint("fwooOOOSH")
	clearScreen()
	randomPrint("BANG")
	randomPrint("CRAAAASH")
	randomPrint("feelingfancy")
	wait(.2)
clearScreen()	
typeThing("You awaken to a cacophony of noise...", 0.05)
clearScreen()
for i in range(2):
	print("You awaken to a cacophony of noise...")
	randomPrint("BANG")
	randomPrint("crrraAASH")
	clearScreen()
	print("You awaken to a cacophony of noise...")
	randomPrint("feelingfancy")
	randomPrint("pewpew")
	clearScreen()
	print("You awaken to a cacophony of noise...")
	randomPrint("BANG")
	randomPrint("CRAAAASH")
	randomPrint("fzzzzOOOOOSH")
	clearScreen()
print("You awaken to a cacophony of noise...\n")
wait(1)
typeThing("...which fades to the background as you try to shake off your drowsiness.\n")
typeThing(f'{italicOn}"Goddammit"{italicOff} you think to yourself as you get to your feet and quickly look around the room.\n')

while True:
	weapon = weaponSelection()		
	print("BANG\n")
	wait(1)
	typeThing("...which bursts open as you approach, a small, ugly creature waddles in.\n")
	typeThing("It looks at you, clearly surprised, before letting loose a shrill screech.\n")
	typeThing(f'You ready your {weapon.get("Name").lower()} and...\n')
	wait(2)
	clearScreen()
	if weapon == dagger:
		playerHP = daggerCombatLoop(weapon, alien, playerHP)
	else:
		playerHP = standardCombatLoop(weapon, alien, playerHP)
	if playerHP <= 0:
		restart = input("Would you like to play again? (Y/N)\n")
		if restart.strip().lower() != "y":
			break
		else:
			alien = squishy
			playerHP = 100
			continue
	alien = pokey
	typeThing("Squishy defeated, you make your way into the hall.\n")
	typeThing("You are greeted by the remains of several colleagues.\n")
	typeThing(f'{italicOn}"Unfortunate"{italicOff}\n')
	typeThing("You follow the trail of carnage, a strange clicking sound coming from an unknown location...\n")
	typeThing(f'{italicOn}"Is that.... is that coming from the vents?"{italicOff}\n')
	print("BANG!")
	wait(1)
	typeThing("You look up just in time to dodge as a creature nearly lands on you.\n")
	typeThing("As you turn to face it, you see that the clicking is the result of its many spikes rubbing together.\n")
	typeThing("It lowers itself on its haunches, ready to pounce.\n")
	typeThing(f'You ready your {weapon.get("Name").lower()} and...\n')
	clearScreen()
	if weapon == dagger:
		playerHP = daggerCombatLoop(weapon, alien, playerHP)
	else:
		playerHP = standardCombatLoop(weapon, alien, playerHP)
	if playerHP <= 0:
		restart = input("Would you like to play again? (Y/N)\n")
		if restart.strip().lower() != "y":
			break
		else:
			alien = squishy
			playerHP = 100
			continue
	alien = stabby
	typeThing("Spikey falls to the ground at your feet.\n")
	typeThing(f'{italicOn}"Ugh, this is bad...\n')
	typeThing(f"...I've gotta find the captain...\n")
	typeThing(f'...assuming they made it.{italicOff}"\n')
	typeThing("You make your way towards the bridge, trying to ignore the bodies along the way\n")
	typeThing("As you pass by medbay, your injuries begin to ache.\n")
	heal = input("Enter medbay? (Y/N)\n")
	if heal.strip().lower() != "y":
		typeThing(f"{italicOn}I don't have time!{italicOff} you think and take off down the hall.\n")
	else:
		typeThing(f"You enter cautiously, alert to the possiblility of danger...\n")
		typeThing(f"But medbay appears to be clear. You take a neobandage, wrap your wounds and feel them immediately repair\n")
		playerHP = 100
	typeThing("As you approach the bridge, the door is stuck open and the lights inside are off.\n")
	typeThing("You try your keycard on the light controls and, surprisingly the light flicks on...\n")
	typeThing("Revealing an alien, hunched and hideous, with knives for hands, stabbing repeatedly into what was once your captain...\n")
	typeThing("You start to step backwards just as it turns toward you in a full sprint.\n")
	typeThing(f'You ready your {weapon.get("Name").lower()} and...\n')
	clearScreen()
	if weapon == dagger:
		playerHP = daggerCombatLoop(weapon, alien, playerHP)
	else:
		playerHP = standardCombatLoop(weapon, alien, playerHP)
	if playerHP <= 0:
		restart = input("Would you like to play again? (Y/N)\n")
		if restart.strip().lower() != "y":
			break
		else:
			alien = squishy
			playerHP = 100
			continue
	alien = scary
	typeThing("Stabby defeated, you run to the control console and use it to search for signs of life on the ship...\n")
	typeThing("...but nothing shows....\n")
	typeThing(f'{italicOn}"Shit... I guess its just me, huh?...\n')
	typeThing(f'...escape pod it is then..."{italicOff} you think as you turn on your heels and sprint back into the hall...\n')
	typeThing("Back the way you came, past the medbay...\n") 
	typeThing("...past Stabby...\n")
	typeThing("...past Spikey...\n")
	typeThing("...past your barely familiar room...\n")
	typeThing("You turn the corner - the exit hatch just down the hall.\n")
	typeThing("But you notice a room to your left.\n")
	typeThing('"Authorized Personnel Only", proclaims the panel by the door...\n')
	typeThing(f'{italicOn}"Could be something useful in there..."{italicOff}\n')
	choice = input("Try to enter the room? (Y/N)\n")
	if choice.strip().lower() != "y":
		typeThing(f'{italicOn}"I gotta get out of here..."{italicOff} you think before heading down the hall.\n')
	else:
		choice = "y"
		typeThing("You approach the door, swiping your keycard against the panel.\n")
		typeThing('"Access Denied. Please use password override"\n')
		while True:
			userPass = input("Enter Password:\n")
			if userPass != bfgPass:
				reset = input("Wrong Password. Try again? (Y/N)\n")
				if reset.strip().lower() != "y":
					break
				else:
					continue
			else:
				typeThing("The door slides open, revealing a small room with a massive gun on the wall.\n")
				typeThing('The plaque on the wall below says "Big Fancy Gun"\n')
				typeThing(f'{italicOn}"Big Fancy Gun, eh? Allll miiiine."{italicOff}\n')
				typeThing("You take the gun off the wall. As your skin makes contact with it, it spins to life.\n")
				typeThing(f'{italicOn}"Heres hoping this thing can save my ass..."{italicOff}\n')
				typeThing("You make your way back into the hall and towards the escape pods.\n")
				weapon = bfg
				break
	typeThing("From behind you comes a terrible sound.\n")
	typeThing("A sound like steel nails on a screaming chalkboard...\n")
	turn = input("Turn to look? (Y/N)\n")
	if turn.strip().lower() != "n":
		typeThing("You turn to face the most horrifying thing you've ever seen emerging from the hallway.\n")
		typeThing("Its long spikes scraping against the steel walls as it lopes towards you.\n")
		typeThing("It opens its massive jaw as it approaches...\n")
		typeThing(f'...giving you just enough time to ready your {weapon.get("Name").lower()} and...\n')
		clearScreen()
		if weapon == dagger:
			playerHP = daggerCombatLoop(weapon, alien, playerHP)
		else:
			playerHP = standardCombatLoop(weapon, alien, playerHP)
		if playerHP <= 0:
			restart = input("Would you like to play again? (Y/N)\n")
			if restart.strip().lower() != "y":
				break
			else:
				alien = squishy
				playerHP = 100
				continue
		else:
			typeThing("Scary defeated, you make your way to the escape pods...\n")
			typeThing("...you pick the one closest to you, scan your keycard, and climb in...\n")
			typeThing("...the door slides shut behind you, you hear the boosters activate and...\n")
			typeThing("...finally you can rest.")
			break
	else:
		typeThing("You start sprinting for the escape pods, hearing steel crunching behind you as you do.\n")
		typeThing("You're running as fast as you can but you can still hear it getting closer...\n")
		typeThing("You reach the escape pod bay.\n")
		typeThing("There are two escape pods left, one directly in [F]ront of you and one down to the [R]ight.\n")
		pod = input("Choose a pod! (F/R)\n")
		if pod.strip().lower() != "r":
			typeThing("You press your keycard against the panel in front of you, but the door is too slow...\n")
			typeThing("...it's right behind you...\n")
			print("BANG")
			wait(1)
			typeThing("You manage to dodge just as it slams into the door, stunning itself...\n")
			typeThing(f'...giving you just enough time to ready your {weapon.get("Name").lower()} and...\n')
			clearScreen()
			if weapon == dagger:
				playerHP = daggerCombatLoop(weapon, alien, playerHP)
			else:
				playerHP = standardCombatLoop(weapon, alien, playerHP)
			if playerHP <= 0:
				restart = input("Would you like to play again? (Y/N)\n")
				if restart.strip().lower() != "y":
					break
				else:
					alien = squishy
					playerHP = 100
					continue
			else:
				typeThing("Scary defeated, you make your way into the escape pod to the right...\n")
				typeThing("...the door slides shut behind you, you hear the boosters activate and...\n")
				typeThing("...finally you can rest.\n")
				break
		else:
			typeThing("You run down to the second pod, fervently pressing your keycard into the panel.\n")
			typeThing(f'{italicOn}"HURRY UP"{italicOff} you think to yourself just as -\n')
			print("BANG\n")
			wait(1)
			typeThing("Scary slams into the pod at the entrance, stunning itself...\n")
			typeThing("And giving you just enough time to enter the pod and close the door.\n")
			typeThing("You breathe a sigh of relief as the boosters activate and you feel yourself depart.\n")
			break

print("Thanks for playing XenoBlaster!")
wait(5)
exit()