import math
import json

def gate(gate_no):
    ans = input('Water gate {}: '.format(gate_no))
    if ans == "yes":
        points = gate_dict[gate_no]
        return points
    elif ans == "no":
        points = 0
        return points
    else:
        print(' [-] Wrong answer! ( yes/no )')
        exit()

def total(points):
    if points <= 0:
        x = 3
        return x
    else:
        x = round(points * 1.0204, 3)
        if x > 100:
            x = 100
        return x

gate_dict = {
    1: 21,
    2: 5,
    3: 8,
    4: 16
}

zone_dict = {
    "Z1": 3,
    "Z2": 11,
    "Z3": 19,
    "Z4": 27,
    "Z5": 34,
    "Z6": 41,
    "Z7": 46,
    "Z8": 48,
    "Z9": 25,
    "Z10": 5,
    "central": 50
}

name = input('Name: ')

try:
    rounds = int(input('Round: '))
except ValueError:
    print(' [-] Wrong value! [1-3]')

if not 0 < rounds < 4:
    print(' [-] Wrong value! [1-3]')
    exit()

gate_1 = gate(1)
gate_2 = gate(2)
gate_3 = gate(3)
gate_4 = gate(4)
gate_points = gate_1 + gate_2 + gate_3 + gate_4

zone = input('Landing zone: ')
if zone == "Z1" or zone == "Z2" or zone == "Z3" or zone == "Z4" or zone == "Z5" or zone == "Z6" or zone == "Z7" or \
                                    zone == "Z8" or zone == "Z9" or zone == "Z10" or zone == "central":
    zone_points = zone_dict[zone]
elif not zone:
    zone_points = 0
    gate_points = 0
else:
    print(' [-] Wrong Zone! ( Z[1-10] / central )')
    exit()

stand = input('Stand Up? ')
if stand == "yes":
    stand_points = 0
elif stand == "no":
    stand_points = -10
else:
    print(' [-] Wrong answer! ( yes/no )')
    exit()

# print ('\nGate points: {}'.format(gate_points))
# print ('Zone points: {}'.format(zone_points))
# print ('Stand Up: {}'.format(stand_points))

points = gate_points + zone_points + stand_points
score = total(points)
print('\nOFFICAL SCORE: {}'.format(score))

with open('results_accuracy.txt', 'a') as f:
    f.write('Name: {}, Round: {}, Score: {}\n\tG1: {}\n\tG2: {}\n\tG3: {}\n\tG4: {}\n\tZone: {}\n\tStandUp: {}\n\n'.\
        format(name, rounds, score, "yes" if gate_1 > 0 else "no", "yes" if gate_2 > 0 else "no", "yes" if gate_3 > 0 \
        else "no", "yes" if gate_4 > 0 else "no", zone, stand))