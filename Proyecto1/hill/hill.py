import numpy as np
import math

alfabeto = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

# A partir de una matriz llave y el mensaje en texto transforma multiplica
# el texto por la matriz
def multexto(llave, mensaje):
    carmen = ''
    dim = len(llave)
    vec = []
    for i in range(0, len(mensaje), dim):
        for j in range(dim):
            vec.append(alfabeto.index(mensaje[i + j]))
        vec = np.array(vec)
        res = np.matmul(llave, vec)
        res %= len(alfabeto)
        for x in np.nditer(res):
            carmen += alfabeto[x]
        vec = []
                
    return carmen

# Calcula la matriz inversa modulo n de manera medio tramposa
def inv_mod(mat):
    det = int(np.linalg.det(mat))
    inv = np.linalg.inv(mat)    # Obtenemos la inversa comun
    inv *= det                  # La multiplicamos por el determinante para tener la adjunta
    inv = inv * pow(det, -1, len(alfabeto)) # La multiplicamos por el inverso del determinante
    inv = np.rint(inv).astype(int) # Redondeamos a enteros
    inv %= len(alfabeto)        # Aplicamos modulo
    return inv

# Revisa que la llave sea valida y regresa su representacion matricial
def revisa_key(llave):
    # Verificamos que la dimension sea correcta
    if(len(llave) != 4 and len(llave) != 9):
        raise Exception('La dimension de la lave debe ser 2 o 3')
    dim = int(math.sqrt(len(llave))) # Dimension de la llave
    m_key = [[] for i in range(dim)] # Matriz de la llave
    for i, k in enumerate(llave):    # Poblamos la matriz con la llave
        m_key[i % dim].append(alfabeto.index(k))

    m_key = np.matrix(m_key)        # Transformamos a una matriz de numpy
    det = np.linalg.det(m_key)      # Determinante de la matriz

    # Tiramos excepcion si la matriz no es invertible
    if(det == 0 or math.gcd(int(det), len(alfabeto)) != 1):
        raise Exception('La matriz de la llave no es invertible en z27')

    return m_key

def cifrado(llave, mensaje):
    m_key = revisa_key(llave) 
    # Agregamos un padding para que el mensaje tenga un tamaño correcto
    while(len(mensaje) % len(llave) != 0):
        mensaje += 'A'
    
    return multexto(m_key, mensaje)

def descifrado(llave, mensaje):
    m_key = revisa_key(llave)
    # Si el mensaje no tiene el tamaño correcto sacamos error
    if(len(mensaje) % len(m_key) != 0):
        raise Exception('El mensaje no tiene el tamaño correcto')
    
    inv = inv_mod(m_key)            # Obtenemos la inversa
    m_key %= len(alfabeto)          # Pasamos la matriz inversa bajo el modulo 27

    return multexto(inv, mensaje)


if __name__ == '__main__':
    llave = 'ASFG'
    llave = 'AFBSJDFBJ'
    mensaje = 'SEÑORASYSEÑORESHEMOSLOGRADOTANTOYNOHEMOSLOGRADONADAEFE'
    print(mensaje)
    cifra = cifrado(llave, mensaje) 
    print(cifra)
    defra = descifrado(llave, cifra)
    print(defra)

