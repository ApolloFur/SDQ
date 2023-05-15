import random
import math
import time
class Battle:
	def __init__(self, player, enemies, room, message):
		self.player = player
		self.enemies = enemies
		self.characters = [self.player] + self.enemies
		for n in range(len(self.characters)):
			self.characters[n].ini = random.randint(1,20)
			self.characters[n].ini += self.characters[n].SPD[1]
		self.characters = sorted(self.characters, key=lambda c: c.ini)
		self.X = room.X
		self.Y = room.Y
		self.roomName = room.name
		self.message = message
		self.beaten = 0
	
	def __str__(self):
		rep = f'''Battle in room {self.name}
characters included:'''
		for character in self.characters:
			rep += f"\n{character.name} at ({character.pos[0]}, {character.pos[1]}) with HP: {character.HP[0]}/{character.HP[1]} and MP: {character.MP[0]}/{character.MP[1]}"
		return rep
	
	def UpdatePlayer(self):
		for n in range(len(self.characters)):
			if self.characters[n].name == self.player.name:
				self.characters[n] == self.player
	
	def RerollInitiative(self):
		for n in range(len(self.characters)):
			self.characters[n].ini = random.randint(1,20)
			self.characters[n].ini += self.characters[n].SPD[1]
		self.characters = sorted(self.characters, key=lambda c: c.ini)

	def Begin(self):
		print("A battle has begun!")
		while self.beaten == 0:
			if self.End() == 0:
				for turn in range(len(self.characters)):
					if self.End() != 0:
						break
					if self.characters[turn].name == self.player.name:
						self.PlayerTurn()
					else:
						if self.characters[turn].activated == 1:
							self.EnemyTurn(turn)
					self.UpdatePlayer()
			elif self.End() == 1:
				print("You died!")
				break
			elif self.End() == 2:
				print("victory!")
				self.beaten == 1
	
	def PlayerTurn(self):
		QUIT = ('q','quit')
		playerActions = 2
		if self.player.MP[1] > self.player.MP[0]:
			self.player.MP[0] += random.randint(5,15)
			self.UpdatePlayer()
		while playerActions > 0:
			quitted = 0
			MOVE = ("move","m","1")
			INV = ("inventory","i","2")
			ATT = ("attack","a","3")
			print(f'''\n\nYOUR TURN!
Your status is:
	HP: {self.player.HP[0]}/{self.player.HP[1]}
	MP: {self.player.MP[0]}/{self.player.MP[1]}
	Current Position: ({self.player.pos[0]}, {self.player.pos[1]})

	Enemy Positions:''')
			for n in range(len(self.characters)):
				if self.characters[n].name != self.player.name:
					if self.characters[n].activated == 1:
						distance = math.dist(self.player.pos, self.characters[n].pos)
						print(f"\t{self.characters[n].name} at ({self.characters[n].pos[0]}, {self.characters[n].pos[1]}), Distance of {distance:.2f}")
			print('''\nPlease pick an option:
		1. Move
		2. Inventory
		3. Attack
		
	*Remember, type 'q' or 'quit' if you change your mind or want to end the turn!''')
			chosen = input("")

			if chosen in MOVE:
				self.player.PlayerMove()
				self.UpdatePlayer()
				playerActions -= 1

			elif chosen in INV:
				self.player.Inventory()

			elif chosen in ATT:
				SPELL = ('s','spell')
				WEAPON = ('w','weapon')
				choosingSpellWep = 1
				while choosingSpellWep == 1:
					chosen = input("Are you using a spell or a weapon?\n")
					if chosen.lower() in WEAPON:
						choosingSpellWep = 0
						choosingWeapon = 1
						while choosingWeapon == 1:
							print('''\nWhat weapon would you like to use?
	available weapons:''')
							for key in self.player.inv:
								try:
									dmg = self.player.inv[key].damage
								except AttributeError:
									pass
								else:
									print(f"{self.player.inv[key].name}: {self.player.inv[key].damage[0]}d{self.player.inv[key].damage[1]} at {self.player.inv[key].range} range")
							weaponChoice = input("")
							if weaponChoice.lower() in QUIT:
								choosingWeapon = 0
								quitted = 1
								break
							try:
								dmg = self.player.inv[weaponChoice].damage
							except KeyError:
								print("That wasn't a weapon!")
							else:
								choosingWeapon = 0
					elif chosen.lower() in SPELL:
						choosingSpellWep = 0
						choosingSpell = 1
						while choosingSpell == 1:
							print('''\nWhat spell would you like to use?
	available spells:''')
							for key in self.player.spells:
								print(f"{self.player.spells[key].name}: {self.player.spells[key].damage[0]}d{self.player.spells[key].damage[1]} at {self.player.spells[key].range} range")
							spellChoice = input("")
							if spellChoice.lower() in QUIT:
								choosingSpell = 0
								quitted = 1
								break
							try:
								dmg = self.player.spells[spellChoice].damage
							except KeyError:
								print("That wasn't a spell!")
							else:
								choosingSpell = 0
					elif chosen.lower() in QUIT:
						quitted = 1
						break
					else:
						print("That wasn't an option!")
					if quitted == 0 and choosingSpellWep == 0:
						choosingEnemy = 1
						while choosingEnemy == 1:
							print('''\nWhat enemy are you targeting?
(only prints enemies that are in range)
available enemies:''')
							for n in range(len(self.characters)):
								if self.characters[n].name != self.player.name:
									if self.characters[n].activated == 1:
										enemyDis = math.dist(self.player.pos, self.characters[n].pos)
										try:
											if enemyDis <= self.player.inv[weaponChoice].range:
												print(f"{self.characters[n].name} at ({self.characters[n].pos[0]},{self.characters[n].pos[1]}), Distance of {enemyDis:.2f}")
										except UnboundLocalError:
											if enemyDis <= self.player.spells[spellChoice].range:
												print(f"{self.characters[n].name} at ({self.characters[n].pos[0]},{self.characters[n].pos[1]}), Distance of {enemyDis:.2f}")
							enemyChoice = input("")
							if enemyChoice in QUIT:
								choosingEnemy = 0
								quitted = 1
								break
							for n in range(len(self.characters)):
								if self.characters[n].name.lower() == enemyChoice.lower():
									enemyDis = math.dist(self.player.pos, self.characters[n].pos)
									inRange = 1
									try:
										if enemyDis > self.player.inv[weaponChoice].range:
											inRange = 0
									except UnboundLocalError:
										if enemyDis > self.player.spells[spellChoice].range:
											inRange = 0
									if inRange == 1:
										chosenEID = n
										choosingEnemy = 0
										break
									else:
										print("Enemy is out of range!")
						
						if quitted == 0:
							hitRoll = random.randint(0,20)
							hitRoll += self.player.GRT
							if hitRoll > self.characters[chosenEID].EVA:
								damage = 0
								try:
									for n in range(self.player.inv[weaponChoice].damage[0]):
										damage += random.randint(1, self.player.inv[weaponChoice].damage[1])
									if self.player.inv[weaponChoice].range > 3:
										damage += self.player.PER[0]
									elif self.player.inv[weaponChoice].range <= 3:
										damage+= self.player.STR[0]
									self.characters[chosenEID].HP[0] -= damage
									print(f"You hit! You dealt {damage} damage!")
								except UnboundLocalError:
									for n in range(self.player.spells[spellChoice].damage[0]):
										damage += random.randint(1, self.player.spells[spellChoice].damage[1])
									if self.player.spells[spellChoice].range > 3:
										damage += self.player.PER[0]
									elif self.player.spells[spellChoice].range <= 3:
										damage+= self.player.STR[0]
									self.characters[chosenEID].HP[0] -= damage
									print(f"You hit! You dealt {damage} damage!")

								if self.characters[chosenEID].HP[0] <1:
									if self.characters[chosenEID] is not self.player:
										print(f"You have killed {self.characters[chosenEID].name}!")
										self.characters[chosenEID].activated = 0
					else:
						print("The attack missed!")
				if quitted == 0:
					playerActions -= 1
			elif chosen in QUIT:
				playerActions = 0
				print("You ended your turn!")
			else:
				print("That wasn't an option!")
	
	def EnemyTurn(self, enemyID):
		enemyActions = 2
		enemy = self.characters[enemyID]
		while enemyActions > 0:
			MOVE = 0
			ATTACK = 1
			choice, weapon = enemy.EnemyChoice(self.player)
			if choice == MOVE:
				enemy.EnemyMove(self.player)
				print(f"{enemy.name} has moved to ({enemy.pos[0]}, {enemy.pos[1]})")
			elif choice == ATTACK:
				hitRoll = random.randint(1, 20)
				if hitRoll > self.player.EVA:
					damage = 0
					for n in range(weapon.damage[0]):
						damage += random.randint(1, weapon.damage[1])
					try:
						enemy.MP[1] -= weapon.cost
						self.characters[enemyID].MP[1] -= weapon.cost
					except AttributeError:
						pass
					self.player.HP[1] -= damage
					self.UpdatePlayer()
					print(f"{enemy.name} hit! Dealt {damage} damage!")
				else:
					print(f"{enemy.name} missed!")
			enemyActions -= 1

		
	def End(self):
		killed = 0
		for n in range(len(self.characters)):
			try:
				if self.characters[n].activated == 0:
					killed += 1
			except AttributeError:
				pass
			if killed == (len(self.characters) - 1):
				self.beaten = 1
				return 2
		if self.player.HP[1] < 1:
			return 1
		else:
			return 0