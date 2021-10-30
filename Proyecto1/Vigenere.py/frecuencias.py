import sys

def ana_letras(palabras):
    letras = {}
    ord_letras = {}
    total = 0
    # Inicializa diccionarios
    for i in palabras:
        for j in i:
            letras[j] = {}
            letras[j]['v'] = 0
            total += 1

    # Cuenta numero de apariciones
    for i in palabras:
        for j in i:
            letras[j]['v'] += 1

    # Cuenta frecuencias
    for j in letras:
        letras[j]['f'] = round(letras[j]['v'] / total * 100, 3)

    # Ordena y regresa
    n_letras = sorted(letras, key = (lambda i : letras.get(i)['f']), reverse = True)
    for i in n_letras:
        ord_letras[i] = letras[i] 

    return ord_letras

if __name__ == '__main__':
    palabrasr = []

    with open(sys.argv[1]) as txt:
        for i in txt:
            for j in i.split():
                palabrasr.append(j)
                
    x = ana_letras(palabrasr)
    for i in x:
        print(i, x[i])

