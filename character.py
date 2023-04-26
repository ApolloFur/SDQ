class Character:
	def __init__(self, name, room, pos, HP, MP, SPD, STR, CON, INT, PER):
		self.name = name
		self.room = room
		self.pos = pos
		self.HP = [HP,HP]
		self.MP = [MP,MP]
		self.SPD = [-SPD,SPD]
		self.STR = [STR,STR]
		self.CON = [CON,CON]
		self.INT = [INT,INT]
		self.PER = [PER,PER]
		self.ini = 0
	
	def __str__(self):
		rep = f'''Character: {self.name}
Position: room {self.room} at {self.pos}
Health: {self.HP[0]}/{self.HP[1]}
Magic: {self.MP[0]}/{self.MP[1]}
Speed: {self.SPD[0]}/{self.SPD[1]}
Stats:
	STR: {self.STR[0]}/{self.STR[1]}
	CON: {self.CON[0]}/{self.CON[1]}
	INT: {self.INT[0]}/{self.INT[1]}
	PER: {self.PER[0]}/{self.PER[1]}
Current Initiative: {self.ini}'''
		return rep

	def Move(self, X, Y, room):
		self.pos[0] += X
		self.pos[1] += Y

		if self.pos[0] > room.X[1]:
			self.pos[0] = room.X[1]
		elif self.pos[0] < room.X[0]:
			self.pos[0] = room.X[0]

		if self.pos[1] > room.Y[1]:
			self.pos[1] = room.Y[1]
		elif self.pos[1] < room.Y[0]:
			self.pos[1] = room.Y[0]

	def Attack(self):
		pass


class Player(Character):
	def __Init__(self, name, room, pos, HP, MP, SPD, STR, CON, INT, PER):
		super().__init__(name, room, pos, HP, MP, SPD, STR, CON, INT, PER)
		self.inv = {}
	
	def __str__(self):
		rep = super().__str__()
		rep += f"\nPlayer inventory: {self.playerInv}"
		return rep
	
	def PlayerMove(self, room):
		playerMoveX = 1
		playerMoveY = 1
		while playerMoveX == 1:
			try:
				newPositionX = int(input(f"How far will you travel along the X axis? (Current X is {self.pos[0]})\n"))
			except ValueError:
				print("That wasn't a number!")
			else:
				if newPositionX >= self.SPD[0] and newPositionX <= self.SPD[1]:
					while playerMoveY == 1:
						try:
							newPositionY = int(input(f"How far will you travel along the Y axis? (Current Y is {self.pos[1]})\n"))
						except ValueError:
							print("That wasn't a number!")
						else:
							if newPositionY >= self.SPD[0] and newPositionY <= self.SPD[1]:
								super().Move(newPositionX, newPositionY, room)
								print(f"Done! You are now at ({self.pos[0]}, {self.pos[1]})")
								playerMoveX = 0
								playerMoveY = 0
							else:
								print(f"that's too fast! Must be from {self.SPD[0]} - {self.SPD[1]}!")
				else:
					print(f"That's too fast! Must be from {self.SPD[0]} - {self.SPD[1]}!")

	def Pickup(self,item):
		if self.inv.get(item.name, None):
			self.inv[item.name].quan += item.quan
		else:
			self.inv[item.name] = item

	def Enter(self, portal):
		if self.room == portal.roomIn[0]:
			if portal.roomIn[1] == 1:
				self.room = portal.roomOut[0]
				self.pos[0] = portal.posOut[0]
				self.pos[1] = portal.posOut[1]
		elif self.room == portal.roomOut[0]:
			if portal.roomOut[1] == 1:
				self.room = portal.roomIn[0]
				self.pos[0] = portal.posIn[0]
				self.pos[1] = portal.posIn[1]
		else:
			print("uh-oh. Looks like we tried sending you to another room without you being in the right room.")

	def Inventory(self):
		USE = ("u","use","1")
		QUIT = ("q","quit","2")
		inInv = 1
		while inInv == 1:
			invKeys = list(self.inv.keys())
			print("You have:\n")
			for n in range(len(invKeys)):
				invItem = f"{self.inv[invKeys[n]].name}"
				try:
					invItem += f" ({self.inv[invKeys[n]].damage[0]}d{self.inv[invKeys[n]].damage[1]}, range {self.inv[invKeys[n]].range})"
				except AttributeError:
					invItem += f": {self.inv[invKeys[n]].quan}"
				else:
					invItem += f": {self.inv[invKeys[n]].quan}"
				print(invItem)
			choice = input('''What would you like to do?
	1: Use
	2: Quit\n''')
			if choice.lower() in USE:
				pass
			elif choice.lower() in QUIT:
				inInv = 0


class Enemy(Character):
	def __init__(self, name, room, pos, HP, MP, SPD, STR, CON, INT, PER, type):
		super().__init__(name, room, pos, HP, MP, SPD, STR, CON, INT, PER)
		self.ai = type
	
	def __str__(self):
		rep = super().__str__()
		rep += f'\nAI type: {self.ai}'
