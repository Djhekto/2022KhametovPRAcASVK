# match case пользовательского класса


class Spell:
	def __init__(self,t,s)
		match t[0]:
			case "l":
				self.type = "lightning"
			case "f":
				self.type = "fireball"
			case _:
				self.type = None
		self.strength = int(s)

while 1:
	try:
		spell = Spell(*input("> ").split())
	except:
		spell = None
	match spell:
		case Spell(type=cast, strength = 0):
			print("0 dmg")
		case Spell(type="lightning", strength = s):
			print("{s} el dmg")		
		case Spell(type="fireball", strength = s):
			print("{s} fi dmg")





#...




