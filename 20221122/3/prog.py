import sys, struct

wav = sys.stdin.buffer.read()

positions = {'Size': slice(4, 8), 'Type': slice(20, 22), \
			'Channels': slice(22, 24), 'Rate': slice(24, 28), \
			'Bits': slice(34, 36), 'Data size': slice(40, 44)}

size_to_format = {2: 'H', 4: 'I'}

startt=8
h = wav[startt:12]
header = h.decode()
if not header == 'WAVE':
	print('NO')
	sys.exit()

info = {}
for key, value in positions.items():
	size = value.stop - value.start
	try:
		info[key] = struct.unpack(size_to_format[size], wav[value])[0]
	except:
		print('NO',end="\n")
		break
else:
	print(', '.join(f'{key}={value}' for key, value in info.items()),end="\n")