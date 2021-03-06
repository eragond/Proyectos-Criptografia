# Cruz Torres Francisco Daniel - eragond@ciencias.unam.mx

tabla = [
'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ',
'BCDEFGHIJKLMNÑOPQRSTUVWXYZA',
'CDEFGHIJKLMNÑOPQRSTUVWXYZAB',
'DEFGHIJKLMNÑOPQRSTUVWXYZABC',
'EFGHIJKLMNÑOPQRSTUVWXYZABCD',
'FGHIJKLMNÑOPQRSTUVWXYZABCDE',
'GHIJKLMNÑOPQRSTUVWXYZABCDEF',
'HIJKLMNÑOPQRSTUVWXYZABCDEFG',
'IJKLMNÑOPQRSTUVWXYZABCDEFGH',
'JKLMNÑOPQRSTUVWXYZABCDEFGHI',
'KLMNÑOPQRSTUVWXYZABCDEFGHIJ',
'LMNÑOPQRSTUVWXYZABCDEFGHIJK',
'MNÑOPQRSTUVWXYZABCDEFGHIJKL',
'NÑOPQRSTUVWXYZABCDEFGHIJKLM',
'ÑOPQRSTUVWXYZABCDEFGHIJKLMN',
'OPQRSTUVWXYZABCDEFGHIJKLMNÑ',
'PQRSTUVWXYZABCDEFGHIJKLMNÑO',
'QRSTUVWXYZABCDEFGHIJKLMNÑOP',
'RSTUVWXYZABCDEFGHIJKLMNÑOPS',
'STUVWXYZABCDEFGHIJKLMNÑOPQR',
'TUVWXYZABCDEFGHIJKLMNÑOPQRS',
'UVWXYZABCDEFGHIJKLMNÑOPQRST',
'VWXYZABCDEFGHIJKLMNÑOPQRSTU',
'WXYZABCDEFGHIJKLMNÑOPQRSTUV',
'XYZABCDEFGHIJKLMNÑOPQRSTUVW',
'YZABCDEFGHIJKLMNÑOPQRSTUVWX',
'ZABCDEFGHIJKLMNÑOPQRSTUVWXY',
]

alfabeto = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

# Aplica las acciones de cifrado o descifrado a cada letra del mensaje
def mcifrado(llave, mensaje, aplicacion):
    carmen = ''
    j = 0
    for i in mensaje:
        if(i in alfabeto):
            kc = llave[j % len(llave)]
            carmen += aplicacion(kc, i)
            j += 1 
        else:
            carmen += i

    return carmen

def cifrado(llave, mensaje):
    # cif es lo que pasaria si cifraras un solo caracter de la llave y el mensaje
    cif = lambda kc, mc : tabla[alfabeto.index(kc)][alfabeto.index(mc)]
    return mcifrado(llave, mensaje, cif)

def descifrado(llave, mensaje):
    # cif es lo que pasaria si descifraras un solo caracter de la llave y el mensaje
    cif = lambda kc, mc : tabla[0][tabla[alfabeto.index(kc)].index(mc)]
    return mcifrado(llave, mensaje, cif)


if __name__ == '__main__':
    llave = 'ARRIBA'
    mensaje = 'SI ESTAS LEYENDO ESTO, HAS PERDIDO EL JUEGO'
    print(mensaje)
    cifra = cifrado(llave, mensaje) 
    print(cifra)
    defra = descifrado(llave, cifra)
    print(defra)

