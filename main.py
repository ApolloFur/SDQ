import random
import character
import rooms
import items

Player = character.Player("placeholder","West Wall",[0,0],100,100,6,6,5,6,6,16,3)
#generate default player inventory
Player.inv = {}
Player.inv["Broadword"] = items.Weapon("Broadword",1,[3,6],2)
Player.inv["Crossbow"] = items.Weapon("Crossbow",1,[4,4],10)
Player.inv["HPotion"] = items.Consumable("HPotion",5,0)
Player.inv["Mpotion"] = items.Consumable("MPotion",5,1)
Player.inv["CONPotion"] = items.Consumable("CONPotion",1,2)

#generate rooms
ROOMS = {}
ROOMS["West Wall"] = rooms.Room("West Wall",[-1, 3],[-11,5],"A large wall that sprawls for miles stands beore you. It's crooked, mossy bricks barely held together feel like they're going to break. Beyond the wall you see what looks like a large castle, something that once might've belonged to a king, but now lays decrepit and dead. But through it you see horrible new life. A large beam of light rises from the center of it all, peircing the heavens with it's demonic glow. This is why you have been sent here with your two fellow mercenaries. Within lies a lich king, a horrible monstrosity capable of reanimating the dead. The king from yonder kingdom is afraid of the lich king's presence, and has hired you to exterminate him with the aid of two other swords-for-hire. You've better get to work.")
ROOMS["North Wall"] = rooms.Room("North Wall",[-5,5],[-2,2],"The wall makes a sharp 90 degree turn and you see a large pile of rubble. At the top, a single door that you couldn't hope of reaching this low.")
ROOMS["Courtyard 1"] = rooms.Room("Courtyard 1",[-12,10],[-5,5],"A large field of dead grass stand before you, as undead creatures patrol around the castle grounds. A tree stand in the middle, along with other small peices of dead shrubbery.")
ROOMS["Courtyard 2"] = rooms.Room("Courtyard 2",[-6,8],[-6,8],"The courtyard continues even further. The dead grass is now punctuated by large rocks jutting out of the lifeless ground.")
ROOMS["Prison Cell 1"] = rooms.Room("Prison Cell 1",[-1,2],[-2,2],"The inside of this prison cell is damp. Puddles strewn across the floor wet your boots. You hope you havn't cause a disease from this disgusting musk.")
ROOMS["Prison Cell 2"] = rooms.Room("Prison Cell 2",[-1,2],[-2,2],"The inside of this prison cell contains little more than bundles of hay on the floor. A chain swings from the roof, but little lays within.")
ROOMS["Prison Cell 3"] = rooms.Room("Prison Cell 3",[-1,2],[-2,2],"There's little within this cell. Only some spiderwebs and the standard cracked bricks that make up this castle.")
ROOMS["Prison Cell 4"] = rooms.Room("Prison Cell 4",[-1,2],[-2,2],"This cell hides a small nest of rats that scitter across the floor as you enter. Their squeaks provide a welcomed sound of life.")
ROOMS["Prison Cell 5"] = rooms.Room("Prison Cell 5",[-1,2],[-2,2],"A skeleton hides within this cell, surprisingly unanimated. A contrast than most other skeeltons here. Perhaps he did something that warranted he not be reanimated?")
ROOMS["Prison Cell 6"] = rooms.Room("Prison Cell 6",[-1,2],[-2,2],"A gaping hole has burned a permanent mark on this prison cell. Sadly, the hole is too small to squeeze through, but something tells you that you didn't want to see what's behind in the first place.")
ROOMS["Prison Hallway 1"] = rooms.Room("Prison Hallway 1",[-2,2],[-9,3],"A dank hallway connect the prison cells among each other, allowing each to be easily accessed.")
ROOMS["Prison Hallway 2"] = rooms.Room("Prison Hallway 2",[-4,4],[-2,1],"A hallway lit by the torches of a room filled with chairs lays before you. Possibly the only source of light in this forsaken tomb.")
ROOMS["Indoors Entrance"] = rooms.Room("Indoors Entrance",[-5,5],[-3,2],"Inside a small room waits before you, with very little beyond a desk or two, a weapon rack, and even more of the standard stench of death you've become accustomed to.")
ROOMS["Break Room"] = rooms.Room("Break Room",[-5,5],[-5,5],"A small room waits here, seemingly a place of rest as a large table stands in the middle of the room, with chairs surrounding it. A few empty goblets sit on the table, lit by a few torches.")
ROOMS["Basement Hallway"] = rooms.Room("Basement Hallway",[-2,3],[-5,6],"Through the door a staircase sits, descending even deeper into the dark pits of this palace. The furthest parts of the starwell seem to contain something evil.")
ROOMS["Basement"] = rooms.Room("Basement",[-4,5],[-3,4],"Entering the door at the end of the stairs you find what looks like sewers, or something connecting to it at least. In the middle of this dark room, a creature of unimaginable horror fills this room with the stench of something truly awful. It smells even worse than death, but rather the intent to kill.")
ROOMS["Castle Entrance"] = rooms.Room("Castle Entrance",[-7,7],[-3,3],"The first splash of color fills this room in the form of a shiny red carpet that crawls across the floor. Many torches line the walls, seeming like a large entrance to something that was once great, but is now filled with terrific evil.")
ROOMS["Castle Hall 1"] = rooms.Room("Castle Hall 1",[-6,7],[-14,14],"Through the large door you see an incredibly large room, easily the largest in this place. Many staircases line this room, aiding it's persuit into the skies. This once great hall is filled with the remains of what little joy might've existed once upon a time. It is now filled with something very different.")
ROOMS["Castle Hall 2"] = rooms.Room("Castle Hall 2",[-6,6],[-6,6],"Yet another room filled with red carpet lies before you, this time housing much more powerful foes. This seems like an attempt to stop you in your tracks, and it does succeed in temporarily intimidating you. But, of course, you must press forward.")
ROOMS["Throne Room"] = rooms.Room("Throne Room",[-9,9],[-7,8],"Beyond the door lies something different. The tattered red carpet has become a much more well-kept golden veil that lines the room. The torches that line along the walls suddenly light, and a throne is revealed. Sitting upon the throne lies the lich king, the being you've been hunting with your acquaintences. He looks at you with pure evil in his eyes, ready to attack.")
ROOMS["Castle Exit"] = rooms.Room("Castle Exit",[-5,5],[-2,2],"Through the door lies the north wall of the castle, at the top of a large pile of rubble. The skies have cleared of their evil, and its beautiful blue once again shines through, and any evil that once resided here has been vanquished. You've completed your job.")
ROOMS["Main Road"] = rooms.Room("Main Road",[-6,6],[-2,2],"As you leave the castle grounds you follow a dirt path, once again illuminated by the purifying light of the heavens. The once dark forest now shines with the light of purity, and you head in the direction of the king who hired you. Time to collect your reward.")
ROOMKEYS = list(ROOMS.keys())

#generate portals
PORTALS = {}
PORTALS["West Wall/North Wall"] = rooms.Portal("More of this wall stretches on this side",(3,4),(0,-5),["West Wall",1],["North Wall",1],[0,0])
PORTALS["West Wall/Courtyard 1"] = rooms.Portal("A large entrance to the castle",(3,6),(-12,3),["West Wall",1],["Courtyard 1",1],[0,0])
PORTALS["West Wall/Prison Cell 1"] = rooms.Portal("A broken vent cover",(3,-9),(-1,0),["West Wall",1],["Prison Cell 1",1],[0,0])
PORTALS["Prison Cell 1/Prison Hallway 1"] = rooms.Portal("A third cell door that connects to a hallway on the left",(2,0),(-2,1),["Prison Cell 1",1],["Prison Hallway 1",1],[0,0])
PORTALS["Prison Cell 2/Prison Hallway 1"] = rooms.Portal("A third cell door that connects to a hallway on the right",(-1,0),(2,1),["Prison Cell 2",1],["Prison Hallway 1",1],[0,0])
PORTALS["Prison Cell 3/Prison Hallway 1"] = rooms.Portal("A second cell door that connect to a hallway on the left",(2,0),(-2,-2),["Prison Cell 3",1],["Prison Hallway 1",1],[0,0])
PORTALS["Prison Cell 4/Prison Hallway 1"] = rooms.Portal("A second cell door that connects to a hallway on the right",(-1,0),(2,-2),["Prison Cell 4",1],["Prison Hallway 1",1],[0,0])
PORTALS["Prison Cell 5/Prison Hallway 1"] = rooms.Portal("A cell door that connects to a hallway on the left",(2,0),(-2,5),["Prison Cell 5",1],["Prison Hallway 1",1],[0,0])
PORTALS["Prison Cell 6/Prison Hallway 1"] = rooms.Portal("a cell door that connects to a hallway on the right",(-1,0),(2,-5),["Prison Cell 6",1],["Prison Hallawy 1",1],[0,0])
PORTALS["Prison Hallway 1/Prison Hallway 2"] = rooms.Portal("A turn in the hallway that leads further",(-9,0),(-2,1),["Prison Hallway 1",1],["Prison Hallway 2",1],[0,0])
PORTALS["Prison Hallway 2/Break Room"] = rooms.Portal("A hallway connects to a room with torches and chairs",(4,-1),(-5,-4),["Prison Hallway 2",1],["Break Room",1],[0,0])
PORTALS["Break Room/Indoors Entrance"] = rooms.Portal("A door that connects a break room and the entrace",(5,-3),(-3,-3),["Break Room",1],["Indoors Entrance",1],[0,0])
PORTALS["Indoors Entrance/Courtyard 2"] = rooms.Portal("A door that connects the outside to the inside",(5,-1),(-6,-4),["Indoors Entrance",1],["Courtyard 2",1],[0,0])
PORTALS["Courtyard 2/Courtyard 1"] = rooms.Portal("More courtyard",(-6,2),(10,-2),["Courtyard 2",1],["Courtyard 1",1],[0,0])
PORTALS["Break Room/Basement Hallway"] = rooms.Portal("A door between the break room and the basement",(5,-3),(-2,4),["Break Room",1],["Basement Hallway",1],[0,0])
PORTALS["Basement Hallway/Basement"] = rooms.Portal("A door at the bottom of the stairs that connects the rest of the basement",(-2,-4),(5,-2),["Basement Hallway",1],["Basement",1],[0,0])
PORTALS["Break Room/Castle Entrance"] = rooms.Portal("A door that connects the break room to the castle hall entrance",(5,1),(-7,1),["Break Room",1],["Castle Entrance",1],[0,0])
PORTALS["Castle Entrance/Castle Hall 1"] = rooms.Portal("A large door that connects the castle hall",(7,0),(-6,11),["Castle Entrance",1],["Castle Hall 1",1],[1,"Castle Key"])
PORTALS["Castle Hall 1/Castle Hall 2"] = rooms.Portal("A door that leads to more castle halls",(-6,9),(6,-3),["Castle Hall 1",1],["Castle Hall 2",1],[0,0])
PORTALS["Castle Hall 2/Throne Room"] = rooms.Portal("A door that connects the castle halls to the final room",(-4,6),(4,-7),["Castle Hall 2",1],["Throne Room",1],[0,0])
PORTALS["Throne Room/Castle Exit"] = rooms.Portal("A door that leads to the outside",(-1,-7),(2,2),["Throne Room",1],["Castle Exit",1],[0,0])
PORTALS["Castle Exit/North Wall"] = rooms.Portal("A pile of rubble that leads to the north wall",(-5,0),(4,0),["Castle Exit",1],["North Wall",0],[0,0])
PORTALS["West Wall/Main Road"] = rooms.Portal("A road that leads to the nearby town",(-1,3),(6,0),["West Wall",0],["Main Road",1],[0,0])
PORTALKEYS = list(PORTALS.keys())

#generate pickups
pickups = []
for n in range(random.randint(5,10)):
	chosenRoom = ROOMS[ROOMKEYS[random.randint(0,21)]]
	type = random.randint(0,5)
	if type == 0:
		name = "HPotion"
	if type == 1:
		name = "MPotion"
	if type == 2:
		name = "STRPotion"
	if type == 3:
		name = "CONPotion"
	if type == 4:
		name = "INTPotion"
	if type == 5:
		name = "PERPotion"
	#include item, room, location, and if it's activated
	pickups.append([items.Consumable(f"{name}",random.randint(1,2),type),chosenRoom.name,[random.randint(chosenRoom.X[0] + 1,chosenRoom.X[1] - 1),random.randint(chosenRoom.Y[0] + 1,chosenRoom.Y[1] - 1)],1])

MOVE = ("1","m","move")
INVENTORY = ("2","i","inv")
PICKUP = ("3","p","pickup")
ENTER = ("4","e","enter")
SAVE = ("s","save")

inGame = 1
while inGame == 1:
	if Player.room == "Main Road":
		inGame = 0
		print("Thank you for playing!")
		break

	availablePortals = []
	for key in PORTALS:
		if PORTALS[key].roomIn[0] == Player.room:
			portalRoom = 0
		elif PORTALS[key].roomOut[0] == Player.room:
			portalRoom = 1
		else:
			portalRoom = 3

		if portalRoom == 0:
			if PORTALS[key].roomIn[1] == 1:
				availablePortals.append(PORTALS[key])
		elif portalRoom == 1:
			if PORTALS[key].roomOut[1] == 1:
				availablePortals.append(PORTALS[key])

	availablePickups = []
	for n in range(len(pickups)):
		if pickups[n][1] == Player.room:
			if pickups[n][3] == 1:
				availablePickups.append(pickups[n])
	
	print(f'''\n\nPlayer: {Player.name}
Your status is:
	HP: {Player.HP[0]}/{Player.HP[1]}
	MP: {Player.MP[0]}/{Player.MP[1]}
	Current position: ({Player.pos[0]},{Player.pos[1]})
	Current Room: {Player.room}''')

	if ROOMS[Player.room].ent == 0:
		print(f"\n{ROOMS[Player.room].message}")
		ROOMS[Player.room].ent = 1

	print("\nyou see:")
	for n in range(len(availablePortals)):
		portalDisplay = f"{availablePortals[n].name} at "

		if availablePortals[n].roomIn[0] == Player.room:
			portalDisplay += f"{availablePortals[n].posIn}"
		elif availablePortals[n].roomOut[0] == Player.room:
			portalDisplay += f"{availablePortals[n].posOut}"
		
		print(portalDisplay)
	
	for n in range(len(availablePickups)):
		if Player.pos[0] >= availablePickups[n][2][0]-6 and Player.pos[0] <= availablePickups[n][2][0]+6 and Player.pos[1] >= availablePickups[n][2][1]-6 and Player.pos[1] <= availablePickups[n][2][1]+6:
			print(f"{availablePickups[n][0].name} at ({availablePickups[n][2][0]}, {availablePickups[n][2][1]})")
	
	print('''\nPleast pick an option:
	1. Move
	2. Inventory''')
	for n in range(len(availablePickups)):
		if Player.pos[0] >= availablePickups[n][2][0]-6 and Player.pos[0] <= availablePickups[n][2][0]+6 and Player.pos[1] >= availablePickups[n][2][1]-6 and Player.pos[1] <= availablePickups[n][2][1]+6:
			print("\t3. Pickup")
			break
	for n in range(len(availablePortals)):
		if (Player.pos[0] == availablePortals[n].posIn[0] and Player.pos[1] == availablePortals[n].posIn[1]) or (Player.pos[0] == availablePortals[n].posOut[0] and Player.pos[1] == availablePortals[n].posOut[1]):
			print("\t4. Enter")
			break
	
	chosen = input("")

	if chosen.lower() in MOVE:
		Player.PlayerMove()

	elif chosen.lower() in INVENTORY:
		Player.Inventory()

	elif chosen.lower() in PICKUP:
		for n in range(len(availablePickups)):
			if Player.pos[0] >= availablePickups[n][2][0]-6 and Player.pos[0] <= availablePickups[n][2][0]+6 and Player.pos[1] >= availablePickups[n][2][1]-6 and Player.pos[1] <= availablePickups[n][2][1]+6:
				Player.Pickup(availablePickups[n][0])
				availablePickups[n][3] = 0

	elif chosen.lower() in ENTER:
		for n in range(len(availablePortals)):
			if (availablePortals[n].posIn[0] == Player.pos[0] and availablePortals[n].posIn[1] == Player.pos[1]) or (availablePortals[n].posOut[0] == Player.pos[0] and availablePortals[n].posOut[1] == Player.pos[1]):
				Player.Enter(availablePortals[n])