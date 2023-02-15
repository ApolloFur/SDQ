import random
#include name, ID, roomID, position, HP, MP, SPD, STR, CON, INT, initiative
player = ["Player",0,0,[0,0],[100,100],[100,100],[4,-4],[6,6],[5,5],[6,6],0]
#include name, id, number
playerInv = [["sword",0,1],["crossbow",1,1],["HPotion",2,5],["MPotion",3,5],["STRPotion",4,0],["CONPotion",5,1],["INTPotion",6,0],["bolts",7,30]]
#include name, id, minheight, maxheight, minwidth, maxwidth, whether it has been entered
ROOMS = (
("WestWall",0,-11,5,-1,3,0),
("NorthWall",1,-2,2,-5,5,0),
("Courtyard1",2,-5,5,-12,10,0),
("Courtyard2",3,-6,8,-6,8,0),
("PrisonCell1",4,-2,2,-1,2,0),
("PrisonCell2",5,-2,2,-1,2,0),
("PrisonCell3",6,-2,2,-1,2,0),
("PrisonCell4",7,-2,2,-1,2,0),
("PrisonCell5",8,-2,2,-1,2,0),
("PrisonCell6",9,-2,2,-1,2,0),
("PrisonHallway1",10,-9,3,-2,2,0),
("PrisonHallway2",11,-10,10,-10,10,0),
("IndoorsEntrance",12,-10,10,-10,10,0),
("BreakRoom",13,-10,10,-10,10,0),
("BasementHallway",14,-10,10,-10,10,0),
("BasementRestRoom",15,-10,10,-10,10,0),
("Basement",16,-10,10,-10,10,0),
("CastleEntrance",17,-10,10,-10,10,0),
("CastleHall1",18,-10,10,-10,10,0),
("CastRestRoom1",19,-10,10,-10,10,0),
("CastleHall2",20,-10,10,-10,10,0),
("CastleRestRoom2",21,-10,10,-10,10,0),
("ThroneRoom",22,-10,10,-10,10,0),
("CastleExit",23,-10,10,-10,10,0),
("MainRoad",24,-10,10,-10,10,0)
)
#include movement text, room id in, room id to, coordinates for room in, coordinates for room to
PORTALS = (
("a corridor between room 1 and room 2",0,1,(10,0),(-10,0)),
("a corridor between room 1 and room 3",0,2,(0,-10),(0,10))
)
#include name, id, number, room id, location, whether they have been picked up
PICKUPS = (
("MPotion",3,1,1,(2,-4),0),
("bolts",4,10,0,(2,1),0)
)

MOVE = ("move","1","m")
INTERACT = ("interact","3","inter")
ENTER = ("enter","4","ent","e")
INV = ("inventory","2","inv")
USE = ("use","1","u")
DROP = ("drop","2","d")
QUIT = ("quit","3","q")

def IncreaseStats(playerStat):
	helpingAmount = random.randrange(8)+1+int(playerConCurrent/2)
	player[playerStat][1] += helpingAmount
	if player[playerStat][1] > player[playerStat][0]:
		player[playerStat][1] = player[playerStat][0]
	playerInv[n][2] -= 1

print("\n\tWelcome to Super Dungeon Quest!")

playing = 1
while playing == 1:
	playerX, playerY = player[3]
	playerSpdMax, playerSpdMin = player[6]
	playerStrMax, playerStrCurrent = player[7]
	playerConMax, playerConCurrent = player[8]
	playerIntMax, playerIntCurrent = player[9]
	ROOMMINH = ROOMS[player[2]][2]
	ROOMMAXH = ROOMS[player[2]][3]
	ROOMMINW = ROOMS[player[2]][4]
	ROOMMAXW = ROOMS[player[2]][5]
	availablePortals = []
	for n in range(len(PORTALS)):
		if PORTALS[n][1] == player[2]:
			availablePortals.append(PORTALS[n])
		if PORTALS[n][2] == player[2]:
			availablePortals.append(PORTALS[n])
	availablePickups = []
	for n in range(len(PICKUPS)):
		if PICKUPS[n][3] == player[2]:
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
		if playerX >= availablePickups[n][4][0]-4 and playerX <= availablePickups[n][4][0]+4 and playerY >= availablePickups[n][4][1]-4 and playerY <= availablePickups[n][4][1]+4:
			print(f"{availablePickups[n][0]} at {availablePickups[n][4]}")
	print("""\nplease pick an option:
	1. move
	2. inventory""")
	for n in range(len(availablePickups)):
		if playerX >= availablePickups[n][4][0]-4 and playerX <= availablePickups[n][4][0]+4 and playerY >= availablePickups[n][4][1]-4 and playerY <= availablePickups[n][4][1]+4:
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
				if playerInv[n][2] > 0:
					print(f"{playerInv[n]}")
			print("""what would you like to do?
		1. use
		2. drop
		3. quit""")
			chosen = input("")

			if chosen in USE:
				chosen = input("what would you like to use?\n(type the item id)\n")
				for n in range(len(playerInv)):
					if playerInv[n][1] == chosen:
						if playerInv[n][2] > 0:
							if playerInv[n][1] <= 1 or playerInv[n][1] == 7:
								print("this cannot be used outside of battle")
							elif playerInv[n][1] == 2:
								IncreaseStats(4)
							elif playerInv[n][1] == 3:
								IncreaseStats(5)
							elif playerInv[n][1] == 4:
								IncreaseStats(7)
							elif playerInv[n][1] == 5:
								IncreaseStats(8)
							elif playerInv[n][1] == 6:
								IncreaseStats(9)
			elif chosen in QUIT:
				inInventory = 0
	elif chosen in INTERACT:
		for n in range(len(availablePickups)):
			if playerX >= availablePickups[n][4][0]-3 and playerX <= availablePickups[n][4][0]+3 and playerY >= availablePickups[n][4][1]-3 and playerY <= availablePickups[n][4][1]+3:
				for m in range(len(playerInv)):
					if playerInv[m][1] == availablePickups[n][1]:
						playerInv[m][1] += availablePickups[n][1]
						availablePickups[n][5] = 0
						print(f"you found {availablePickups[n][3]} {availablePickups[n][0]}!")
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
