import random
#include name, ID, roomID, position, HP, MP, SPD, STR, CON, INT, PER, initiative
player = ["Placeholder",0,0,[0,0],[100,100],[100,100],[5,-5],[6,6],[5,5],[6,6],[6,6],0]
#include name, id, number
playerInv = {1: ["sword",1],2: ["crossbow",1],3: ["HPotion",5],4: ["MPotion",5],5: ["STRPotion",0],6: ["CONPotion",1],7: ["INTPotion",0],8: ["bolts",30],9: ["BossKey",0],10: ["ExitKey",0],11: ["PERPotion",0]}
playerSpells = ()
#include name, minheight, maxheight, minwidth, maxwidth, whether it has been entered
ROOMS = {
0: ["WestWall",-11,5,-1,3,0,"A large wall that sprawls for miles stands beore you. It's crooked, mossy bricks barely held together feel like they're going to break. Beyond the wall you see what looks like a large castle, something that once might've belonged to a king, but now lays decrepit and dead. But through it you see horrible new life. A large beam of light rises from the center of it all, peircing the heavens with it's demonic glow. This is why you have been sent here with your two fellow mercenaries. Within lies a lich king, a horrible monstrosity capable of reanimating the dead. The king from yonder kingdom is afraid of the lich king's presence, and has hired you to exterminate him with the aid of two other swords-for-hire. You've better get to work."],
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
("A broken vent cover",0,4,(3,-9),(0,0),(0,0)),
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
#include item id, number, room id, location, whether they have been picked up
pickups = (
[3,1,1,(3,0),0],
[5,1,8,(1,1),0],
[6,1,13,(-1,-4),0],
[8,20,12,(1,-1),0],
[7,2,18,(4,-5),0],
[5,1,20,(-1,-4),0],
[11,1,3,(-1,-4),0]
)

#include ID, name, AI type, location, HP, MP, SPD, STR, CON, INT, PER, initiative, what item it may drop and how much
enemies = {
	1: ["SkeletonGuard1",0,[random.randint(-10,8),random.randint(-4,4)],30,20,(3,-3),5,6,4,5,random.randint(1,20)],
	2: ["SkeletonGuard2",0,[random.randint(-10,8),random.randint(-4,4)],30,20,(3,-3),5,6,4,5,random.randint(1,20)],

	3: ["SkeletonGuard1",0,[random.randint(-5,7),random.randint(-5,7)],30,20,(3,-3),5,6,4,5,random.randint(1,20)],
	4: ["SkeletonGuard2",0,[random.randint(-5,7),random.randint(-5,7)],30,20,(3,-3),5,6,4,5,random.randint(1,20)],
	5: ["SkeletonArcher",1,[random.randint(-5,7),random.randint(-5,7)],20,30,(4,-4),3,6,5,6,random.randint(1,20)],

	6: ["SkeletonGuard",0,[random.randint(-4,4),random.randint(-4,4)],30,20,(3,-3),5,6,4,5,random.randint(1,20)],
	7: ["SkeletonArcher",1,[random.randint(-4,4),random.randint(-4,4)],20,30,(4,-4),3,6,5,6,random.randint(1,20)],
	8: ["Spider",2,[random.randint(-4,4),random.randint(-4,4)],40,0,(2,-2),7,5,1,3,random.randint(1,20)],

	9: ["Spider1",2,[random.randint(-3,4),random.randint(-2,3)],40,0,(2,-2),7,5,1,3,random.randint(1,20)],
	10: ["Spider2",2,[random.randint(-3,4),random.randint(-2,3)],40,0,(2,-2),7,5,1,3,random.randint(1,20)],
	11: ["SkeletonArcher",1,[random.randint(-3,4),random.randint(-2,3)],20,30,(4,-4),3,6,5,6,random.randint(1,20)],
	12: ["GiantZombieBat",3,[0,0],60,30,(5,-5),8,8,4,6,random.randint(1,20)],

	13: ["SkeletonGuard",0,[random.randint(-5,6),random.randint(-13,-2)],30,20,(3,-3),5,6,4,5,random.randint(1,20)],
	14: ["Spider",2,[random.randint(-5,6),random.randint(-13,-2)],40,0,(2,-2),7,5,1,3,random.randint(1,20)],
	15: ["SkeletonArcher1",1,[random.randint(-5,6),random.randint(-13,-2)],20,30,(4,-4),3,6,5,6,random.randint(1,20)],
	16: ["SkeletonArcher2",1,[random.randint(-5,6),random.randint(-13,-2)],20,30,(4,-4),3,6,5,6,random.randint(1,20)],

	17: ["SkeletonArcher1",1,[random.randint(-5,6),random.randint(2,13)],20,30,(4,-4),3,6,5,6,random.randint(1,20)],
	18: ["SkeletonArcher2",1,[random.randint(-5,6),random.randint(2,13)],20,30,(4,-4),3,6,5,6,random.randint(1,20)],
	19: ["PossessedArmor",4,[random.randint(-5,6),random.randint(2,13)],40,40,(3,-3),6,4,6,3,random.randint(1,20)],

	20: ["SkeletonArcher",1,[random.randint(-5,5),random.randint(-5,5)],20,30,(4,-4),3,6,5,6,random.randint(1,20)],
	21: ["SkeletonGuard",0,[random.randint(-5,5),random.randint(-5,5)],30,20,(3,-3),5,6,4,5,random.randint(1,20)],
	22: ["PossessedArmor1",4,[random.randint(-5,5),random.randint(-5,5)],40,40,(3,-3),6,4,6,3,random.randint(1,20)],
	23: ["PossessedArmor2",4,[random.randint(-5,5),random.randint(-5,5)],40,40,(3,-3),6,4,6,3,random.randint(1,20)],

	24: ["PossessedArmor",4,[random.randint(-8,8),random.randint(-6,7)],40,40,(3,-3),6,4,6,3,random.randint(1,20)],
	25: ["EnchantedSword",5,[random.randint(-8,8),random.randint(-6,7)],30,40,(4,-4),5,4,7,4,random.randint(1,20)],
	26: ["LichKing",6,[0,0],80,50,(4,-4),4,7,8,5,random.randint(1,20)]
}

#include ID, roomID, enemyIDs, whether it has been beaten
battles = {
	1: [2,(1,2),0],
	2: [3,(3,4,5),0],
	3: [13,(6,7,8),0],
	4: [16,(9,10,11,12),0],
	5: [18,(13,14,15,16),0],
	6: [18,(17,18,19),0],
	7: [20,(20,21,22,23),0],
	8: [22,(24,25,26),0]
}

def AddEnemiesItem(enemyAI,items):
	for n in range(len(enemies)):
		if enemies[n+1][1] == enemyAI:
			for m in range(len(items)):
				addedItems = []
				if random.randint(1,20) >= items[m][2]:
					addedItems.append(items[m])
			enemies[n+1].append(addedItems)

#enemyAI afectes, followed by item ID, number and chance
AddEnemiesItem(0,((3,random.randint(1,2),10),(5,random.randint(1,2),13),(6,random.randint(1,2),14)))
AddEnemiesItem(1,((3,random.randint(1,2),10),(8,random.randint(1,15),12),(11,random.randint(1,2),14)))
AddEnemiesItem(3,((3,random.randint(1,3),8),(7,random.randint(1,5),10),(9,1,0)))
AddEnemiesItem(4,((3,random.randint(1,2),12),(7,random.randint(1,2),13)))
AddEnemiesItem(6,((10,1,0),(1,0,20)))

def PortalFun(num):
	if PORTALS[n][num] == player[2]:
		availablePortals.append(PORTALS[n])

def AvailablePortalDisplay(num, brea):
	for n in range(len(availablePortals)):
		if availablePortals[n][num] == player[2]:
			print(f"{availablePortals[n][0]} at {availablePortals[n][3]}")
			if brea == 1:
				break


def AvailablePickupDisplay(message, brea):
	for n in range(len(availablePickups)):
		if playerX >= availablePickups[n][3][0]-6 and playerX <= availablePickups[n][3][0]+6 and playerY >= availablePickups[n][3][1]-6 and playerY <= availablePickups[n][3][1]+6:
			print(message)
			if brea == 1:
				break

def PortalMove(num, num2):
	if playerX == availablePortals[n][num2][0] and playerY == availablePortals[n][num2][1]:
		if availablePortals[n][5][0] == 0 or (availablePortals[n][5][0] == 1 and playerInv[availablePortals[n][5][1]] > 0):
			if availablePortals[n][6][0] == 0 or (availablePortals[n][6][0] == 1 and player[2] != availablePortals[n][6][1]):
				print(f"you have successfully left {ROOMS[player[2]][0]}")
				player[2] = availablePortals[n][num]
				player[3][0] = availablePortals[n][num2][0]
				player[3][1] = availablePortals[n][num2][1]
				print(f"you are now in {ROOMS[player[2]][0]}")

def Move(playerDimension, roomMinDim, roomMaxDim):
	if playerDimension < roomMinDim:
		playerDimension = roomMinDim
		player[3][0] = playerDimension
	elif playerDimension > roomMaxDim:
		playerDimension = roomMaxDim
		player[3][0] = playerDimension
	else:
		playerDimension = playerDimension + newPosition
		player[3][0] = playerDimension

MOVE = ("move","1","m")
INTERACT = ("interact","3","inter")
ENTER = ("enter","4","ent","e")
INV = ("inventory","2","inv")
USE = ("use","1","u")
QUIT = ("quit","2","q")
NEW = ("new","n","1")
LOAD = ("load","l","2")
DELETE = ("delete","del","d","3")

running = 1
while running == 1:
	print('''\n\tWelcome to Super Dungeon Quest!
Please select an option:
1. New Game
2. Load Game
3. Delete file
''')
	choice = input("")

	if choice in NEW:
		name = input("\nPlease enter a file name\n")
		player[0] = name
		running = 0
		inGame = 1
	elif choice in LOAD:
		pass
	elif choice in DELETE:
		pass

while inGame == 1:
	if player[2] == 24:
		print(ROOMS[player[2]][6])
		print("\nThank you for playing!")
		inGame == 0
		break
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
		PortalFun(1)
		PortalFun(2)
	availablePickups = []
	for n in range(len(pickups)):
		if pickups[n][2] == player[2]:
			if pickups[n][4] == 0:
				availablePickups.append(pickups[n])

	print(f"""\n\nPlayer: {player[0]}
Your status is:
	HP: {player[4][1]}/{player[4][0]}
	MP: {player[5][1]}/{player[5][0]}
	current position:{playerX},{playerY}
	current room: {ROOMS[player[2]][0]}\n""")
	if ROOMS[player[2]][5] == 0:
		print(ROOMS[player[2]][6])
		ROOMS[player[2]][5] = 1
	print("\nyou see:")

	AvailablePortalDisplay(1, 0)
	AvailablePortalDisplay(2, 0)

	for n in range(len(availablePickups)):
		if playerX >= availablePickups[n][3][0]-6 and playerX <= availablePickups[n][3][0]+6 and playerY >= availablePickups[n][3][1]-6 and playerY <= availablePickups[n][3][1]+6:
			print(f"{playerInv[availablePickups[n][0]][0]} at {availablePickups[n][3]}")
			break

	print("""\nplease pick an option:
	1. move
	2. inventory""")
	AvailablePickupDisplay("\t3. interact", 1)

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
				Move(playerX, ROOMMINW, ROOMMAXW)
				newPosition = int(input(f"how far will you travel along the y axis? (current y: {playerY})\n"))
				if newPosition > playerSpdMax or newPosition < playerSpdMin:
					print(f"that is an invalid number! must be less than {playerSpdMax} and greater than {playerSpdMin}\n!")

				else:
					Move(playerY, ROOMMINH, ROOMMAXH)
					print(f"done! You are now at {playerX},{playerY}")
					playerTurn = 0

	elif chosen in INV:
		inInventory = 1
		while inInventory == 1:
			print("you have:\n[item name, number of item]\n")
			INVKEYS = list(playerInv.keys())
			for n in range(len(playerInv)):
				if playerInv[n+1][1] > 0:
					print(f"{playerInv[n+1]}: Item ID {INVKEYS[n]}")
			print("""what would you like to do?
		1. use
		2. quit""")
			chosen = input("")

			if chosen in USE:
				chosen = input("what would you like to use?\n(type the item ID)\n")
				playerInv[chosen][1] -= 1
			elif chosen in QUIT:
				inInventory = 0
	elif chosen in INTERACT:
		for n in range(len(availablePickups)):
			if playerX >= availablePickups[n][3][0]-6 and playerX <= availablePickups[n][3][0]+6 and playerY >= availablePickups[n][3][1]-6 and playerY <= availablePickups[n][3][1]+6:
				playerInv[availablePickups[n][0]][1] += availablePickups[n][1]
				for m in range(len(pickups)):
					if pickups[m] == availablePickups[n]:
						pickups[m][4] = 1

	elif chosen in ENTER:
		currentRoom = player[2]
		for n in range(len(availablePortals)):
			PortalMove(1,4)
			if currentRoom == player[2]:
				PortalMove(2,3)
			if currentRoom == player[2]:
				PortalMove(1,3)
			if currentRoom == player[2]:
				PortalMove(2,4)
			break