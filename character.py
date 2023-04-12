class Character:
	def __init__(self, name, room, pos, HP, MP, SPD, STR, CON, INT, PER):
		self.name = name
		self.room = room
		self.pos = pos
		self.HP = [HP,HP]
		self.MP = [MP,MP]
		self.SPD = [SPD,-SPD]
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

	def Move(self):
		pass

	def Attack(self):
		pass


class Player(Character):
	def __Init__(self, name, room, pos, HP, MP, SPD, STR, CON, INT, PER):
		super().__init__(name, room, pos, HP, MP, SPD, STR, CON, INT, PER)
		self.playerInv = {}
	
	def __str__(self):
		rep = super().__str__()
		rep += f"\nPlayer inventory: {self.playerInv}"
		return rep
