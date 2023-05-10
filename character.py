import random
import math
class Character:
	def __init__(self, name, room, pos, HP, MP, SPD, STR, CON, INT, PER, EVA, GRT):
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
		self.EVA = EVA
		self.GRT = GRT
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

	def Move(self, X, Y):
		self.pos[0] += X
		self.pos[1] += Y


class Player(Character):
	def __Init__(self, name, room, pos, HP, MP, SPD, STR, CON, INT, PER, AC, Grit):
		super().__init__(name, room, pos, HP, MP, SPD, STR, CON, INT, PER, AC, Grit)
		self.inv = {}
		self.spells = {}
	
	def __str__(self):
		rep = super().__str__()
		rep += f"\nPlayer inventory: {self.playerInv}"
		return rep
	
	def PlayerMove(self):
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
								super().Move(newPositionX, newPositionY)
								print(f"Done! You are now at ({self.pos[0]}, {self.pos[1]})")
								playerMoveX = 0
								playerMoveY = 0
							else:
								print(f"that's too fast! Must be from {self.SPD[0]}-{self.SPD[1]}!")
				else:
					print(f"That's too fast! Must be from {self.SPD[0]}-{self.SPD[1]}!")

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
	def __init__(self, name, room, pos, HP, MP, SPD, STR, CON, INT, PER, AC, grit, type, weapons, spells):
		super().__init__(name, room, pos, HP, MP, SPD, STR, CON, INT, PER, AC, grit)
		self.type = type
		self.weapons = weapons
		self.spells = spells
	
	def __str__(self):
		rep = super().__str__()
		rep += f'\nAI type: {self.ai}'
	
	def EnemyMove(self, player):
		#The skeleton guard flails in a rough direction at the player
		if self.type == 0:
			if player.pos[0] > self.pos[0]:
				XAmount = self.SPD[1]
				XAmount += random.randint(-2,2)
			elif player.pos[0] < self.pos[0]:
				XAmount = self.SPD[0]
				XAmount += random.randint(-2,2)
			else:
				XAmount = random.randint(-1,1)
			
			if player.pos[1] > self.pos[1]:
				YAmount = self.SPD[1]
				YAmount += random.randint(-2,2)
			elif player.pos[1] < self.pos[1]:
				YAmount = self.SPD[0]
				YAmount += random.randint(-2,2)
			else:
				YAmount = random.randint(-1,1)
			
			if XAmount > self.room.X[1]:
				XAmount = self.room.X[1]
			elif XAmount < self.room.X[0]:
				XAmount = self.room.X[0]
			if YAmount > self.room.Y[1]:
				YAmount = self.room.Y[1]
			elif YAmount < self.room.Y[0]:
				YAmount = self.room.Y[0]
		#The skeleton archer wants to remain at a rough distance from the player (not done yet)
		elif self.type == 1:
			IDEALDISTANCE = 7
			XAmount = 0
			YAmount = 0
			XDifference = self.pos[0] - player.pos[0]
			YDifference = self.pos[1] - player.pos[1]

		#The spider makes a beeline to the player
		elif self.type == 2:
			XAmount = player.pos[0] - self.pos[0]
			YAmount = player.pos[1] - self.pos[1]
			if XAmount > self.SPD[1]:
				XAmount = self.SPD[1]
			elif XAmount < self.SPD[0]:
				XAmount = self.SPD[0]
			if YAmount > self.SPD[1]:
				YAmount = self.SPD[1]
			elif YAmount < self.SPD[0]:
				YAmount = self.SPD[0]
		#Don't know what to do with the zombie bat yet
		elif self.type == 3:
			XAmount = random.randint(self.SPD[0],self.SPD[1])
			YAmount = random.randint(self.SPD[0],self.SPD[1])

			if XAmount > self.room.X[1]:
				XAmount = self.room.X[1]
			elif XAmount < self.room.X[0]:
				XAmount = self.room.X[0]
			if YAmount > self.room.Y[1]:
				YAmount = self.room.Y[1]
			elif YAmount < self.room.Y[0]:
				YAmount = self.room.Y[0]
		
		#the possessed armor will circle the player
		elif self.type == 4:
			pass

		#the enchanted sword will also make a beeline to the player
		elif self.type == 5:
			XAmount = player.pos[0] - self.pos[0]
			YAmount = player.pos[1] - self.pos[1]
			if XAmount > self.SPD[1]:
				XAmount = self.SPD[1]
			elif XAmount < self.SPD[0]:
				XAmount = self.SPD[0]
			if YAmount > self.SPD[1]:
				YAmount = self.SPD[1]
			elif YAmount < self.SPD[0]:
				YAmount = self.SPD[0]
		
		#The lich king will have the most complicated movement
		elif self.type == 6:
			pass

		self.Move(XAmount, YAmount)
	
	def EnemyChoice(self, player):
		XDifference = self.pos[0] - player.pos[0]
		YDifference = self.pos[1] - player.pos[1]
		Distance = (XDifference)^2 +(YDifference)^2
		Distance = math.sqrt(abs(Distance))
		#The Skeleton Guard simply waits to be in range to attack
		if self.type == 0:
			if Distance <= self.weapons[0].range:
				return 1, self.weapons[0]
			else:
				return 0, 0
		#The skeleton Archer will first attack with the dagger, otherwise it'll either move or attack with a bow
		elif self.type == 1:
			if Distance <= self.weapons[1].range:
				return 1, self.weapons[1]
			else:
				choice = random.randint(0,1)
				if choice == 1:
					return 1, self.weapons[0]
				else:
					return 0, 0
		
		elif self.type == 2:
			if Distance <= self.weapons[0].range:
				return 1, self.weapons[0]
			else:
				return 0,0

		elif self.type == 3:
			if Distance <= self.weapons[0].range:
				return 1, self.weapons[0]
			else:
				return 0,0
		
		elif self.type == 4:
			if Distance <= self.weapons[0].range:
				return 1, self.weapons[0]
			else:
				return 0,0
		#the enchanted sword swipes in to kill before backing off to fire a single beam. Then it resumes
		elif self.type == 5:
			if hasAttacked == 1:
				if Distance <= self.weapons[0].range:
					hasAttacked = 1
					return 1, self.weapons[0]
				else:
					return 0,0
			else:
				if self.MP[1] <= 10:
					if Distance <= self.weapons[0].range:
						hasAttacked = 0
						return 1, self.weapons[0]
					else:
						return 0,0
				else:
					if Distance <= 5:
						return 0,0
					else:
						hasAttacked == 0
						return 1, self.spells[0]
		
		elif self.type == 6:
			if self.MP[1] > 30:
				pass