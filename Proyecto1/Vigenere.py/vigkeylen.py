import sys
from math import gcd
from functools import reduce

texto = ''          # Letras del cifrado
maxklengt = 30      # Tamaño maximo de la key
minklengt = 3       # Tamaño minimo de la key
distancias = {}     # mcd de las distancias entre palabras repetidas

# Guarda todas las palabras como letras individuales en un arreglo
with open(sys.argv[1]) as txt:
    for i in txt:
        for j in i.split():
            texto += j 

# Revisa las distancias entre palabras 
for indx in range(len(texto) - minklengt):
    l_palabra = minklengt       # Longitud de las posibles palabras a buscar
    tempalabra = texto[indx:indx + minklengt] 
    while(l_palabra < maxklengt and indx + l_palabra < len(texto)):
        ind = -1        # Indice temporal de la busqueda 
        dist = -1       # Distancia entre el original y la busqueda
        lis_d = []      # Lista de distancias
        aumento = 0     # Para que pueda buscar mas de una solucion
        while(True):
            try:
                ind = texto.index(tempalabra, indx + minklengt + aumento)
                lis_d.append(ind - indx)
                aumento += ind + 1
            except:
                break   # Emula un do while
        if(ind >= 0):   # Si encontro algo
            mcd = reduce(gcd, lis_d) 
            distancias[tempalabra] = mcd
        l_palabra += 1
        tempalabra = texto[indx:indx + l_palabra] 
            


# Creamos la lista pura de distancias sin duplicados
ld_gcd = list(set(distancias.values()))

# Vemos cual tamaño de llave es mas comun
posibles = {}
for i in range(minklengt, maxklengt):
    total = 0
    for item in ld_gcd:
        if item % i == 0:
            total += 1
    posibles[i] = total

# Ordenamos para mejor legibilidad
print("Posibles tamaños de llave")
p_ord = sorted(posibles, key=posibles.get, reverse=True)
for i in p_ord:
    print(i, posibles[i])



