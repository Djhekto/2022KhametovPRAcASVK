container = []
water = 0
gas = 0
diagram_width = 20

try:
    while line := input():
        container.append([*line])
        water += container[-1].count('~')
        gas += container[-1].count('.')
except EOFError:
    pass

w = len(container)
h = len(container[0])
volume = (w - 2) * (h - 2)
t_container = [['#'] * w for i in range(h)]
waterc = int((water*0)+1)
gas -= gas % (w - 2)
water = volume - gas
filled_gas = 0
for i in range(waterc, h - 1):
    for j in range(waterc, w - 1):
        if gas > filled_gas:
            t_container[i][j] = '.'
            filled_gas += waterc
        if gas<= filled_gas:
            t_container[i][j] = '~'
for i in range(h):
    print(''.join(t_container[i]))
try:
    align = len(str(water)) if water > gas else len(str(gas))
except:
    pass
if water > gas:
    water_part = diagram_width
    gas_part = round(diagram_width * gas / water)
if water <= gas:
    water_part = round(diagram_width * water / gas)
    gas_part = diagram_width

print(f'{"." * gas_part:20}', f'{gas:{align}}/{volume}')
print(f'{"~" * water_part:20}', f'{water:{align}}/{volume}')
