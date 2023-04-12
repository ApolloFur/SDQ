class Item():
	def __Init(self, name, quantity):
		self.name = name
		self.quan = quantity
	
	def __str__(self):
		rep = f'''Item name: {self.name}
Item Quantity: {self.quan}'''
		return rep

class Potion(Item):
	def __init__(self, name, quantity, type):
		super().__init__(name, quantity)
		self.type = type
	
	def __str__(self):
		rep = super().__str__()
		rep += f"\nPotion type: {self.type}"
	
	def use(self):
		pass


class Weapon(Item):
	def __init__(self, name, quantity, damage, rang):
		super().__init__(name, quantity)
		self.damage = damage
		self.rang = rang
