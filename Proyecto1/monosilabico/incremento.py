
alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
texto = "JGYUSNUIG"

for j in range(len(alfabeto)):
    c = ""
    for i in (texto):
        c += alfabeto[(alfabeto.index(i)+j) % len(alfabeto)]
    print(c)



