import sys

trans = {}
palabras = []


with open(sys.argv[2]) as txt:
    for i in txt:
        trs = i.split()
        trans[trs[0]] = trs[1]

print(trans)

with open(sys.argv[1]) as txt:
    for i in txt:
        for j in i.split():
            palabras.append(j)

print(palabras)

for indx in range(len(palabras)):
    c = ""
    for char in palabras[indx]:
        if(char in trans):
            c += trans[char]
        else:
            c += char
    palabras[indx] = c

for palabra in palabras:
    print(palabra + " ", end = '')

print('')

