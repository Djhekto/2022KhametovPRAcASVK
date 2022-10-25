def pgen():
	print("start")
	control = yield 1
	print("command",control)
	control = yield 2
	print("command",control)
	control = yield 3
	print("command",control)
	control = yield 4
	print("command",control)

g = pgen()
#next(g)
#res = next(g)
#g.send("idi")
