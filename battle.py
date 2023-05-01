import random
import math
class Battle:
	def __init__(self, player, enemies, room):
		self.player = player
		self.enemies = enemies
		self.characters = [self.player] + self.enemies
		for character in self.characters:
			self.characters[character].ini = random.randint(0,20)
			self.characters[character].ini += character.SPD[1]
		self.characters = sorted(self.characters, key=lambda c: c.ini)
		self.X = room.X
		self.Y = room.Y
		self.roomName = room.name
	
	def __str__(self):
		rep = f'''Battle in room {self.name}
characters included:'''
		for character in self.characters:
			rep += f"\n{character.name} at ({character.pos[0]}, {character.pos[1]}) with HP: {character.HP[0]}/{character.HP[1]} and MP: {character.MP[0]}/{character.MP[1]}"
		return rep
	
	def Begin(self):
		if self.End() == 0:
			for n in range(len(self.characters)):
				if self.characters[n] is self.player:
					self.PlayerTurn()
				else:
					self.EnemyTurn(n)
	
	def PlayerTurn(self):
		MOVE = ("move","m","1")
		INV = ("inventory","i","2")
		ATT = ("attack","a","3")
		print(f'''\n\nYOUR TURN!
Your status is:
	HP: {self.player.HP[0]}/{self.player.HP[1]}
	MP: {self.player.MP[0]}/{self.player.MP[1]}
	Current Position: ({self.player.pos[0]}, {self.player.pos[1]})

Enemy Positions:''')
		for character in self.characters:
			if character is not self.player:
				print(f"\t{character.name} at ({character.pos[0]}, {character.pos[1]})")
		print('''\nPlease pcik an option:
	1. Move
	2. Inventory
	3. Attack''')
		chosen = input("")

		if chosen in MOVE:
			self.player.PlayerMove()
			for character in self.characters:
				if character is self.player:
					character.pos = self.player.pos

		elif chosen in INV:
			self.player.Inventory()

		elif chosen in ATT:
			choosingWeapon = 1

			while choosingWeapon == 1:
				print('''\nWhat weapon would you like to use?
	available weapons:''')
				for n in range(len(self.player.inv)):
					try:
						dmg = self.player.inv[n].damage
					except ValueError:
						pass
					else:
						print(f"{self.player.inv[n].name}: {self.player.inv[n].damage[0]}d{self.player.inv[n].damage[1]} at {self.player.inv[n].range} range")
				weaponChoice = input("")
				try:
					dmg = self.player.inv[weaponChoice].damage
				except ValueError:
					print("That wasn't a weapon!")
				else:
					choosingWeapon = 0
					choosingEnemy = 1

					while choosingEnemy == 1:
						print('''\nWhat enemy are you targeting?
		available enemies:''')
						for character in self.characters:
							if character is not self.player:
								enemyXDis = abs((self.characters[character].pos[0] - self.player.pos[0])^2)
								enemyYDis = abs((self.characters[character].pos[1] - self.player.pos[1])^2)
								enemyDis = math.sqrt(enemyXDis + enemyYDis)
								if enemyDis <= self.player.inv[weaponChoice].range:
									print(f"{self.characters[character].name} at ({self.characters[character].pos[0]},{self.characters[character].pos[1]})")
						enemyChoice = input("")
						for n in range(len(self.characters)):
							if self.characters[n].name == enemyChoice:
								chosenEID = n
								choosingEnemy = 0
								break
							else:
								print("Enemy not found! Please try again")
					
					hitRoll = random.randint(0,20)
					hitRoll += self.player.GRT
					if hitRoll > self.characters[chosenEID].EVA:
						damage = 0
						for n in range(self.player.inv[weaponChoice].damage[0]):
							damage += random.randint(1, self.player.inv[weaponChoice].damage[1])
						if self.player.inv[weaponChoice].range > 3:
							damage += self.player.PER
						elif self.player.inv[weaponChoice].range <= 3:
							damage+= self.player.STR
						self.characters[chosenEID].HP -= damage

						if self.characters[chosenEID].HP <1:
							if self.characters[chosenEID] is not self.player:
								killed = self.characters[chosenEID].pop()
								print(f"You have killed {killed.name}!")
	
	def EnemyTurn(self, enemyID):
		MOVE = 0
		ATTACK = 1
		choice = random.randint(0,1)
		if choice in MOVE:
			if self.player.pos[0] > self.characters[enemyID].pos[0]:
				XAmount = self.characters[enemyID].SPD[1] - random.randint(0, 2)
			else:
				XAmount = self.characters[enemyID].SPD[0] + random.randint(0, 2)
			
			if self.player.pos[1] > self.characters[enemyID].pos[1]:
				YAmount = self.characters[enemyID].SPD[1] - random.randint(0, 2)
			else:
				YAmount = self.characters[enemyID].SPD[1] + random.randint(0, 2)
			
			if XAmount > self.room.X[1]:
				XAmount = self.room.X[1]
			elif XAmount < self.room.X[0]:
				XAmount = self.room.x[0]
			
			if YAmount > self.room.Y[1]:
				YAmount = self.room.Y[1]
			elif YAmount < self.room.Y[0]:
				YAmount = self.room.Y[0]
			
			self.characters[enemyID].Move(XAmount, YAmount)
		elif choice in ATTACK:
			pass
		
	def End(self):
		if self.player.HP[1] < 1:
			print("you died!")
			return 1
		elif len(self.characters) == 1 and self.characters[0] is self.player:
			print("victory!")
			return 1
		else:
			return 0