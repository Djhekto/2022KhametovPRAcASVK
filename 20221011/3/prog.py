#Вводится ASCII-art, представляющий прямоугольный контейнер, заполненный жидкостью и/или газом ("#" — стенки, "." — газ, "~" — жидкость)
#Контейнер следует повернуть на 90° и вывести (жидкость и газ перераспределятся):
#На входе слои жидкости заполнены целиком, от края до края. Неполный слой жидкости на выходе дополняется до полного. Например, если в контейнер-ответ налить ещё три капли и повернуть обратно, он окажется полным)
#Также следует вывести горизонтальную диаграмму долей объёма, занимаемых газом и жидкостью:
#строка для газа состоит из символов '.', для жидкости — из символов '~'
#ширина диаграммы (т.е. длина её наибольшей строки) фиксирована и равна 20 символам
#справа от каждой строки выводится в виде x/y исходная доля объёма соответствующей субстанции от объёма контейнера, сокращать дроби не нужно

#дроби должны быть выравнены так, чтобы
#самые правые их символы располагались в одной и той же позиции,
#расстояние между самой длинной строкой и дробью — один пробел
#при расчёте числа симв


container = []
water = 0
gas = 0
diagram_width = 20

#read and calculate count of liquid and gas
while line := input():
    container.append([*line])
    water += container[-1].count('~')
    gas += container[-1].count('.')

#transpose container and calculate its volume
w = len(container)
h = len(container[0])
volume = (w - 2) * (h - 2)
t_container = [['#'] * w for i in range(h)]

#add liquid if a top layer isn't filled
gas -= gas % (w - 2)
water = volume - gas

#fill transposed container
filled_gas = 0
for i in range(1, h - 1):
    for j in range(1, w - 1):
        if gas > filled_gas:
            t_container[i][j] = '.'
            filled_gas += 1
        if gas<= filled_gas:
            t_container[i][j] = '~'

#print transposed container
for i in range(h):
    print(''.join(t_container[i]))

#calculate proportion between liquid and gas
try:
    align = len(str(water)) if water > gas else len(str(gas))
except:
    pass

#print diagram
if water > gas:
    water_part = diagram_width
    gas_part = round(diagram_width * gas / water)
else:
    water_part = round(diagram_width * water / gas)
    gas_part = diagram_width

print(f'{"." * gas_part:20}', f'{gas:{align}}/{volume}')
print(f'{"~" * water_part:20}', f'{water:{align}}/{volume}')
