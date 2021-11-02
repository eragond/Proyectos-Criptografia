import sys

palabrasr = []
alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

with open(sys.argv[1]) as txt:
    for i in txt:
        for j in i.split():
            palabrasr.append(j)

for p in range(0, len(palabrasr), 2):
    print(palabrasr[p], end=' ')
    print(palabrasr[p+1], end=' ')
    for i in palabrasr[p]:
        print(alfabeto.index(i), end=' ')
    for i in palabrasr[p+1]:
        print(alfabeto.index(i), end=' ')
    print('')
            
