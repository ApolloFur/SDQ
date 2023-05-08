class Item():
	def __init__(self, name, quantity):
		self.name = name
		self.quan = quantity
	
	def __str__(self):
		rep = f'''Item name: {self.name}
Item Quantity: {self.quan}'''
		return rep

class Consumable(Item):
	def __init__(self, name, quantity, type):
		super().__init__(name, quantity)
		self.type = type
	
	def __str__(self):
		rep = super().__str__()
		rep += f"\nConsumable type: {self.type}"
	
	def use(self):
		pass


class Weapon(Item):
	#damage is a list where the first value is the number of rolls, and the second value is the highest value per roll. DnD rules
	def __init__(self, name, quantity, damage, rang):
		super().__init__(name, quantity)
		self.damage = damage
		self.range = rang
	
	def __str__(self):
		rep = super().__str__()
		rep += f'''\nDeals {self.damage} damage at a range of {self.range}'''

class Spell:
	def __init__(self, name, damage, rang, cost):
		self.name = name
		self.damage = damage
		self.range = rang
		self.cost = cost
	
	def __str__(self):
		rep = f'''Spell: {self.name}
Does {self.damage[0]}d{self.damage[1]} damage at a range of {self.range}
Costs {self.cost} MP to cast'''
