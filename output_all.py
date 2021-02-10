from draftmaster import *
import draftmaster as dm

# print(f'HP-GL instructions ({len(dm._instructions[0])}):')
# for inst, desc in dm._instructions[0].items():
#     print(f'{inst}, {desc}')
# 
# print(f'\nDevice-control instructions ({len(dm._instructions[1])}):')
# for inst, desc in dm._instructions[1].items():
#     print(f'{inst}, {desc}')
# print()

open('/dev/tty.usbserial-A700CYY0')
ESC_A()
print(f'ESC.A: {read()}')

ESC_B()
print(f'ESC.B: {read()}')

ESC_E()
print(f'ESC.E: {read()}')

ESC_L()
print(f'ESC.L: {read()}')

ESC_O()
print(f'ESC.O: {read()}')

for n in range(7):
    ESC_S(n)
    print(f'ESC.S{n}: {read()}')

IN()

OA()
print(f'OA: {read()}')

OC()
print(f'OC: {read()}')

OE()
print(f'OE: {read()}')

OF()
print(f'OF: {read()}')

OG()
print(f'OG: {read()}')

OI()
print(f'OI: {read()}')

OL()
print(f'OL: {read()}')

OO()
print(f'OO: {read()}')

OS()
print(f'OS: {read()}')

OT()
print(f'OT: {read()}')

OH()
print(f'OH: {read()}')

OP()
print(f'OP: {read()}')

OW()
print(f'OW: {read()}')

OK()
print(f'OK: {read()}')

OD()
print(f'OD: {read()}')

close()
