import random
#include name, ID, roomID, position, HP, MP, SPD, STR, CON, INT, initiative
player = ["Player",0,0,[0,0],100,100,[10,-10],6,5,6]
#include name, id, number
playerInv = [["sword",0,1],["crossbow",1,1],["HPotion",2,5],["MPotion",3,5],["bolts",4,30]]
#include name, id, minheight, maxheight, minwidth, maxwidth
ROOMS = (
("testRoom1",0,-10,10,-10,10),
("testRoom2",1,-10,10,-10,10),
("testRoom3",2,-10,10,-10,10)
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
INTERACT = ("interact","2","inter","i")
ENTER = ("enter","3","ent","e")

print("\n\tWelcome to Super Dungeon Quest!")

playing = 1
while playing == 1:
	playerX, playerY = player[3]
	playerSpdMax, playerSpdMin = player[6]
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

	print(f"""\ncurrent position:{playerX},{playerY}
	current room: {ROOMS[player[2]][0]}
	you see:""")
	for n in range(len(availablePortals)):
		if availablePortals[n][1] == player[2]:
			print(f"{availablePortals[n][0]} at {availablePortals[n][3]}")
		if availablePortals[n][2] == player[2]:
			print(f"{availablePortals[n][0]} at {availablePortals[n][4]}")
	for n in range(len(availablePickups)):
		if playerX >= availablePickups[n][4][0]-3 and playerX <= availablePickups[n][4][0]+3 and playerY >= availablePickups[n][4][1]-3 and playerY <= availablePickups[n][4][1]+3:
			print(f"{availablePickups[n][0]} at {availablePickups[n][4]}")
	print("""\nplease pick an option:
	1. move""")
	for n in range(len(availablePickups)):
		if playerX >= availablePickups[n][4][0]-3 and playerX <= availablePickups[n][4][0]+3 and playerY >= availablePickups[n][4][1]-3 and playerY <= availablePickups[n][4][1]+3:
			print("\t2. interact")
			break
	for n in range(len(availablePortals)):
		if (playerX == availablePortals[n][3][0] and playerY == availablePortals[n][3][1]) or (playerX == availablePortals[n][4][0] and playerY == availablePortals[n][4][1]):
			print("\t3. enter")
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
			elif playerX == availablePortals[n][4][0] and playerY == availablePortals[n][4][1]:
				print(f"you have successfully left {ROOMS[player[2]][0]}")
				player[2] = availablePortals[n][1]
				player[3][0] = availablePortals[n][4][0]
				player[3][1] = availablePortals[n][4][1]
				print(f"you are now in {ROOMS[player[2]][0]}")
				break
