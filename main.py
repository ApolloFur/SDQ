import random
#include name, ID, roomID, position, HP, MP, SPD, STR, CON, INT, initiative
player = ["Player",0,0,[0,0],[100,100],[100,100],[4,-4],[6,6],[5,5],[6,6],0]
#include name, id, number
playerInv = {1: ["sword",1],2: ["crossbow",1],3: ["HPotion",5],4: ["MPotion",5],5: ["STRPotion",0],6: ["CONPotion",1],7: ["INTPotion",0],8: ["bolts",30],9: ["BossKey",0],10: ["ExitKey",0]}
#include name, minheight, maxheight, minwidth, maxwidth, whether it has been entered
ROOMS = {
0: ["WestWall",-11,5,-1,3,0,"A large wall that sprawl for miles stands beore you. It's crooked, mossy bricks barely holding together feel like they're going to break. Beyond the wall you see what looks like a large castle, something that once might've belonged to a king, but now lays decrepit and dead. But through it you see horrible new life. A large beam of light rises from the center of it all, peircing the heavens with it's demonic glow. This is why you have been sent here with your two fellow mercenaries. Within lies a lich king, a horrible monstrosity capable of reanimating the dead. The king from yonder kingdom is afraid of the lich king's presence, and has hired you to exterminate him with the aid of two other swords-for-hire. You've better get to work."],
1: ["NorthWall",-2,2,-5,5,0,"The wall makes a sharp 90 degree turn and you see a large pile of rubble. At the top, a single door that you couldn't hope of reaching this low."],
2: ["Courtyard1",-5,5,-12,10,0,"A large field of dead grass stand before you, as undead creatures patrol around the castle grounds. A tree stand in the middle, along with other small peices of dead shrubbery."],
3: ["Courtyard2",-6,8,-6,8,0,"The courtyard continues even further. It looks identical to the previous field."],
4: ["PrisonCell1",-2,2,-1,2,0,"The inside of this prison cell is damp and musty. Puddles strewn across the floor wet your boots. You hope you havn't cause a disease from this disgusting musk."],
5: ["PrisonCell2",-2,2,-1,2,0,"The inside of this prison cell contains little more than bundles of hay on the floor. A chain swings from the roof, but little lays within."],
6: ["PrisonCell3",-2,2,-1,2,0,"There's little within this cell. Only some spiderwebs and the standard cracked bricks that make up this castle."],
7: ["PrisonCell4",-2,2,-1,2,0,"This cell hides a small nest of rats that scitter across the floor as you enter. Their squeaks provide a welcoming sound of life."],
8: ["PrisonCell5",-2,2,-1,2,0,"A skeleton hides within this cell, surprisingly unanimated. A contrast than most other skeeltons here. Perhaps he did something that warranted he not be reanimated?"],
9: ["PrisonCell6",-2,2,-1,2,0,"A gaping hole has burned a permanent mark on this prison cell. Sadly, the hole is too small to squeeze through, but something tells you that you didn't want to see what's behind in the first place."],
10: ["PrisonHallway1",-9,3,-2,2,0,"A dank hallway connect the prison cells among each other, allowing each to be easily accessed."],
11: ["PrisonHallway2",-2,1,-4,4,0,"A hallway lit by the torches of a room filled with chairs lays before you. Possibly the only source of light in this forsaken tomb."],
12: ["IndoorsEntrance",-3,2,-5,5,0,"Inside a small room waits before you, with very little beyond a desk or two, a weapon rack, and even more of the standard stench of death you've become accustomed to."],
13: ["BreakRoom",-5,5,-5,5,0,"A small room waits here, seemingly a place of rest as a large table stands in the middle of the room, with chairs surrounding it. A few empty goblets sit on the table, lit by a few torches."],
14: ["BasementHallway",-5,6,-2,3,0,"Through the door a staircase sits, descending even deeper into the dark pits of this palace. The furthest parts of the starwell seem to contain something evil."],
15: ["BasementRestRoom",-2,2,-2,2,0,"This room contains the only bit of security that you've found in this entire castle. A bench sits on the furthest end of the room, lit by a torch that seems more alive than any other source of light in this place. For a moment the dread of this dungeon seems to dissipate."],
16: ["Basement",-3,4,-4,5,0,"Entering the door at the end of the stairs you find what looks like sewers, or something connecting to it at least. In the middle of this dark room, a creature of unimaginable horror fills this room with the stench of something truly awful. It smells even worse than death, but rather the intent to kill."],
17: ["CastleEntrance",-3,3,-7,7,0,"The first splash of color fills this room in the form of a shiny red carpet that crawls across the floor. Many torches line the walls, seeming like a large entrance to something that was once great, but is now filled with terrific evil."],
18: ["CastleHall1",-14,14,-6,7,0,"Through the large door you see an incredibly large room, easily the largest in this place. Many staircases line this room, aiding it's persuit into the skies. This once great hall is filled with the remains of what little joy might've existed once upon a time. It is now filled with something very different."],
19: ["CastleRestRoom1",-2,2,-2,2,0,"Here at the top of the hall is a small room that provides an amount of safety. From how far you've come, this point feels like a place of temporary comfort. You don't know what horrors lie beyond this room with a bench, but it mustn't be good."],
20: ["CastleHall2",-6,6,-6,6,0,"Yet another room filled with red carpet lies before you, this time housing much more powerful foes. This seems like an attempt to stop you in your tracks, and it does succeed in temporarily intimidating you. But, of course, you must press forward."],
21: ["CastleRestRoom2",-2,2,-3,4,0,"This is the final opportunity to rest before whatever lies within the room beyond. Whatever is behind this door mustn't be good. After all, not many benches are placed in the middle of two locations, rather than off to the side."],
22: ["ThroneRoom",-7,8,-9,9,0,"Beyond the door lies something different. The tattered red carpet has become a much more well-kept golden veil that lines the room. The torches that line along the walls suddenly light, and a throne is revealed. Sitting upon the throne lies the lich king, the being you've been hunting with your acquaintences. He looks at you with pure evil in his eyes, ready to attack."],
23: ["CastleExit",-2,2,-5,5,0,"Through the door lies the north wall of the castle, at the top of a large pile of rubble. The skies have cleared of their evil, and its beautiful blue once again shines through, and any evil that once resided here has been vanquished. You've completed your job."],
24: ["MainRoad",-2,2,-6,6,0,"As you leave the castle grounds you follow a dirt path, once again illuminated by the purifying light of the heavens. The once dark forest now shines with the light of purity, and you head in the direction of the king who hired you. Time to collect your reward."]
}
#include movement text, room id in, room id to, coordinates for room in, coordinates for room to, whether it is locked and what item id goes to it if it is and if it's one-way and which side is one-way.
PORTALS = (
("More of this wall stretches on this side",0,1,(3,4),(0,-5),(0,0),(0,0)),
("A large entrance to the castle",0,2,(3,6),(-12,3),(0,0),(0,0)),
("A broken cover",0,4,(3,-9),(0,0),(0,0)),
("A third cell door that connects to a hallway on the left",4,10,(2,0),(-2,1),(0,0),(0,0)),
("A third cell door that connects to a hallway on the right",5,10,(-1,0),(2,1),(0,0),(0,0)),
("A second cell door that connect to a hallway on the left",6,10,(2,0),(-2,-2),(0,0),(0,0)),
("A second cell door that connects to a hallway on the right",7,10,(-1,0),(2,-2),(0,0),(0,0)),
("A cell door that connects to a hallway on the left",8,10,(2,0),(-2,-5),(0,0),(0,0)),
("a cell door that connects to a hallway on the right",9,10,(-1,0),(2,-5),(0,0),(0,0)),
("A turn in the hallway that leads further",10,11,(-9,0),(-2,1),(0,0),(0,0)),
("A hallway connects to a room with torches and chairs",11,13,(4,-1),(-5,-4),(0,0),(0,0)),
("A door that connects a break room and the entrace",13,12,(5,-3),(-3,-3),(0,0),(0,0)),
("A door that connects the outside to the inside",12,3,(5,-1),(-6,-4),(0,0),(0,0)),
("More courtyard",3,2,(-6,2),(10,-2),(0,0),(0,0)),
("A door between the break room and the basement",13,14,(5,-3),(-2,4),(0,0),(0,0)),
("A door that connects the basement hallway to a bench room",14,15,(3,4),(-2,0),(0,0),(0,0)),
("A door at the bottom of the stairs that connects the rest of the basement",14,16,(-2,-4),(5,-2),(0,0),(0,0)),
("A door that connects the break room to the castle hall entrance",13,17,(5,1),(-7,1),(0,0),(0,0)),
("A large door that connects the castle hall",17,18,(7,0),(-6,11),(1,9),(0,0)),
("A small alcove containing a bench",18,19,(5,14),(0,-2),(0,0),(0,0)),
("A door that leads to more castle halls",18,20,(-6,9),(6,-3),(0,0),(0,0)),
("A door that connects the castle hall to a bench room",20,21,(-6,-5),(4,-1),(0,0),(0,0)),
("A door that connects the bench room to the final room",21,22,(0,2),(4,-7),(0,0),(0,0)),
("A door that leads to the outside",22,23,(-1,-7),(2,2),(1,10),(0,0)),
("A pile of rubble that leads to the north wall",23,1,(-5,0),(5,0),(0,0),(1,1)),
("A road that leads to the nearby town",0,24,(-1,3),(6,0),(1,10),(1,0))
)
#include id, number, room id, location, whether they have been picked up
PICKUPS = (
[3,1,1,(3,0),0]
)

MOVE = ("move","1","m")
INTERACT = ("interact","3","inter")
ENTER = ("enter","4","ent","e")
INV = ("inventory","2","inv")
USE = ("use","1","u")
DROP = ("drop","2","d")
QUIT = ("quit","3","q")

print("\n\tWelcome to Super Dungeon Quest!")

inGame = 1
while inGame == 1:
	playerX, playerY = player[3]
	playerSpdMax, playerSpdMin = player[6]
	playerStrMax, playerStrCurrent = player[7]
	playerConMax, playerConCurrent = player[8]
	playerIntMax, playerIntCurrent = player[9]
	ROOMMINH = ROOMS[player[2]][1]
	ROOMMAXH = ROOMS[player[2]][2]
	ROOMMINW = ROOMS[player[2]][3]
	ROOMMAXW = ROOMS[player[2]][4]
	availablePortals = []
	for n in range(len(PORTALS)):
		if PORTALS[n][1] == player[2]:
			availablePortals.append(PORTALS[n])
		if PORTALS[n][2] == player[2]:
			availablePortals.append(PORTALS[n])
	availablePickups = []
	for n in range(len(PICKUPS)):
		if PICKUPS[n][2] == player[2]:
			availablePickups.append(PICKUPS[n])

	print(f"""\n\n{player[0]}
Your status is:
	HP: {player[4][1]}/{player[4][0]}
	MP: {player[5][1]}/{player[5][0]}

	current position:{playerX},{playerY}
	current room: {ROOMS[player[2]][0]}
	you see:""")
	for n in range(len(availablePortals)):
		if availablePortals[n][1] == player[2]:
			print(f"{availablePortals[n][0]} at {availablePortals[n][3]}")
		if availablePortals[n][2] == player[2]:
			print(f"{availablePortals[n][0]} at {availablePortals[n][4]}")
	for n in range(len(availablePickups)):
		if playerX >= availablePickups[n][3][0]-4 and playerX <= availablePickups[n][3][0]+4 and playerY >= availablePickups[n][3][1]-4 and playerY <= availablePickups[n][3][1]+4:
			print(f"{playerInv[n][0]} at {availablePickups[n][3]}")
	print("""\nplease pick an option:
	1. move
	2. inventory""")
	for n in range(len(availablePickups)):
		if playerX >= availablePickups[n][3][0]-4 and playerX <= availablePickups[n][3][0]+4 and playerY >= availablePickups[n][3][1]-4 and playerY <= availablePickups[n][3][1]+4:
			print("\t3. interact")
			break
	for n in range(len(availablePortals)):
		if (playerX == availablePortals[n][3][0] and playerY == availablePortals[n][3][1]) or (playerX == availablePortals[n][4][0] and playerY == availablePortals[n][4][1]):
			print("\t4. enter")
			break

	chosen = input("")
	
	if chosen in MOVE:
		playerTurn = 1
		while playerTurn == 1:
			newPosition = int(input(f"how far will you travel along the X axis? (current x: {playerX})\n"))
			if newPosition > playerSpdMax or newPosition < playerSpdMin:
				print(f"that is an invalid number! must be less than {playerSpdMax} and greater than {playerSpdMin}!\n")
			else:
				if playerX < ROOMMINW:
					playerX = ROOMMINW
					player[3][0] = playerX
				elif playerX > ROOMMAXW:
					playerX = ROOMMAXW
					player[3][0] = playerX
				else:
					playerX = playerX + newPosition
					player[3][0] = playerX
				newPosition = int(input(f"how far will you travel along the y axis? (current y: {playerY})\n"))
				if newPosition > playerSpdMax or newPosition < playerSpdMin:
					print(f"that is an invalid number! must be less than {playerSpdMax} and greater than {playerSpdMin}\n!")

				else:
					if playerY < ROOMMINH:
						playerY = ROOMMINH
						player[3][1] = playerY
					elif playerY > ROOMMAXH:
						playerY = ROOMMAXH
						player[3][1] = playerY
					else:
						playerY = playerY + newPosition
						player[3][1] = playerY
					print(f"done! You are now at {playerX},{playerY}")
					playerTurn = 0
	elif chosen in INV:
		inInventory = 1
		while inInventory == 1:
			print("you have:\n[item name, item ID, number of item]")
			for n in range(len(playerInv)):
				if playerInv[n][1] > 0:
					print(f"{playerInv[n]}")
			print("""what would you like to do?
		1. use
		2. drop
		3. quit""")
			chosen = input("")

			if chosen in USE:
				chosen = input("what would you like to use?\n(type the item id)\n")
				playerInv[chosen][1] -= 1
			elif chosen in QUIT:
				inInventory = 0
	elif chosen in INTERACT:
		for n in range(len(availablePickups)):
			if playerX >= availablePickups[n][3][0]-3 and playerX <= availablePickups[n][3][0]+3 and playerY >= availablePickups[n][3][1]-3 and playerY <= availablePickups[n][3][1]+3:
				playerInv[availablePickups[0]][1] += availablePickups[1]
	elif chosen in ENTER:
		for n in range(len(availablePortals)):
			if playerX == availablePortals[n][3][0] and playerY == availablePortals[n][3][1]:
				print(f"you have successfully left {ROOMS[player[2]][0]}")
				player[2] = availablePortals[n][2]
				player[3][0] = availablePortals[n][4][0]
				player[3][1] = availablePortals[n][4][1]
				print(f"you are now in {ROOMS[player[2]][0]}")
				break
			elif playerX == availablePortals[n][3][0] and playerY == availablePortals[n][3][1]:
				print(f"you have successfully left {ROOMS[player[2]][0]}")
				player[2] = availablePortals[n][1]
				player[3][0] = availablePortals[n][4][0]
				player[3][1] = availablePortals[n][4][1]
				print(f"you are now in {ROOMS[player[2]][0]}")
				break