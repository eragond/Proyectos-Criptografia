

alfabeto = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

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

def cifrado(llave, mensaje):
    c = ''
    j = 0
    for i in mensaje:
        if(i in alfabeto):
            c += tabla[alfabeto.index(i)][alfabeto.index(llave[j % len(llave)])]
            j += 1 
        else:
            c+= i

    return c

def descifrado(llave, mensaje):
    c = ''
    j = 0
    for i in mensaje:
        if(i in alfabeto):
            inverso = tabla[alfabeto.index(llave[j % len(llave)])].index(i)
            c += tabla[0][inverso]
            j += 1 
        else:
            c+= i

    return c


if __name__ == '__main__':
    llave = 'ARRIBA'
    mensaje = 'HOLA COMPADRE, QUE WAPO SE VE'
    kk = cifrado(llave, mensaje) 
    print(kk)
    kk = descifrado(llave, kk)
    print(kk)

