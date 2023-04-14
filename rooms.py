class Room:
	def __init__(self, name, X, Y, message):
		self.name = name
		self.X = X
		self.Y = Y
		self.message = message
		self.ent = 0
	
	def __str__(self):
		rep = f'Room: {self.name}'
		if self.ent == 0:
			rep += '\nThis room has not been entered yet'
		else:
			rep += '\nThis room has been entered'

		rep += f'''\nEntrance text:
	{self.message}
Room Dimensions:
	X: {self.X[0]}-{self.X[1]}
	Y: {self.Y[0]}-{self.Y[1]}'''
		return rep

class Portal:
	#roomIn, roomOut both small lists, with a 1 or 0 if that way is functional. Allows one-way doors. Locked is a list with a 1-0 as first value, followed by the key
	def __init__(self, name, posIn, posOut, roomIn, roomOut, locked):
		self.name = name
		self.posIn = posIn
		self.posOut = posOut
		self.roomIn = roomIn
		self.roomOut = roomOut
		self.locked = locked
	
	def __str__(self):
		rep = f'''Portal: {self.name}
Positions:
	in: {self.posIn} in Room {self.roomIn[0].name}
	out: {self.posOut} in Room {self.roomOut[0].name}'''
		if self.locked[0] == 0:
			rep += '\nPortal is not locked'
		if self.locked[0] == 1:
			rep += f'\nPortal is locked with key {self.locked[1]}'
		return rep
