import sys
from frecuencias import ana_letras


texto = ''      # El texto a tratar
keylen = 9      # Longitud de la llave
maxnum = 4      # Maximo numero de las mejoes letras que esperamos

# Guarda todas las palabras como letras individuales en un arreglo
with open(sys.argv[1]) as txt:
    for i in txt:
        for j in i.split():
            texto += j 

# Particiones donde se debe hacer analisis monoalfabetico
part = ['']*keylen 

# Llenamos con el texto que les corresponde
for i in range(len(texto)):
    part[i % keylen] += texto[i]

# Hacemos analisis de frecuencias a cada particion
for cad in part:
    x = ana_letras([cad])
    # Imprimimos las mejores 5 de cada analisis
    for indx, itm in enumerate(x):
        if(indx < maxnum):
            print(itm, ' ', end='')
    print('\n')

