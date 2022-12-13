NAME = "MUD"
VESION = 0.01
DEVELOPERS="JBDKASBJKD"
import datetime
import readline #istoriya input

def move1(direct, name):
	match direct:
		case DIR.LEFT:
			print("moved l")
		case DIR.RIGHT:
			print("moved r")
		case _:
			print("kuda")

class DIR:
	LEFT = "left"
	RIGHT = "right"

while 1:
	s = input("> ")
	match s.split():
		case ["about"]:
			print(f"{NAME}  {VESION}")
		case ["credits"]:
			print(f"Copyright © {DEVELOPERS}")
		case ["credits", "--year"]:
			print(f"Copyright © {DEVELOPERS} {datetime.date.today().year}")
		case ["move"]:
			print("kuda")		
		case ["move", direction]:
			move1(direction, "move")
		case ["travel", *directions]:
			if directions:
				for direct in directions:
					#match direct:
					#move1()
					pass	
			else:
				print("kuda")
		case ["quit"]:
			break
		case _:
			print("cant parse")
			
