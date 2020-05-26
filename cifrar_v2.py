import pprint


def matriz_clave(clave):
    for i in clave:
        if clave.count(i) != 1:
            return "La clave no puede tener letras repetidas"
    abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", 'g', "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
           "s", "t", "u", "v",
           "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-", "_"]
    base = []
    n = 0
    m = 0
    letras_faltantes = []
    for i in abc:
        if i not in clave:
            letras_faltantes.append(i)
    for i in range(8):
        fila = []
        for j in range(8):
            if n < len(clave):
                fila.append(clave[n])
                n += 1
            else:
                fila.append(letras_faltantes[m])
                m += 1
        base.append(fila)
    return base


def bifido_paso_1(matriz, cadena):
    numeros = []
    for a in cadena:
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                if a == matriz[i][j]:
                    numeros.append(i)
                    numeros.append(j)
    return numeros


def bifido_paso_2(numeros):
    lista1 = []
    lista2 = []
    for i in range(len(numeros)):
        if i < len(numeros) / 2:
            lista1.append(numeros[i])
        else:
            lista2.append(numeros[i])
    return [lista1, lista2]


def bifido_paso_2_5(lista1, lista2):
    codigo = []
    for i in range(len(lista1)):
        codigo.append([lista1[i], lista2[i]])
    return codigo


def bifido_paso_3(base, codigo):
    palabra = ""
    for i in range(len(codigo)):
        palabra += base[codigo[i][0]][codigo[i][1]]
    return palabra


def bifido(clave, palabra):
    base = matriz_clave(clave)
    if type(base) != list:
        return base
    a = bifido_paso_1(base, palabra)
    b = bifido_paso_2(a)
    b_2 = bifido_paso_2_5(b[0], b[1])
    c = bifido_paso_3(base, b_2)
    return c


def bifido_paso_inv_1(numeros):
    lista1 = []
    lista2 = []
    for i in range(len(numeros)):
        if i % 2 == 0:
            lista1.append(numeros[i])
        else:
            lista2.append(numeros[i])
    codigo = []
    count = 0
    dupla = []
    for i in range(len(lista1)):
        if count == 2:
            codigo.append(dupla)
        if count < 2:
            dupla.append(lista1[i])
            count += 1
        else:
            count = 1
            dupla = [lista1[i]]
    for i in range(len(lista2)):
        if count == 2:
            codigo.append(dupla)
            dupla = []
            count = 0
        if count < 2:
            dupla.append(lista2[i])
            count += 1
        else:
            count = 1
            dupla = [lista2[i]]
        if count == 2 and i == len(lista2) - 1:
            codigo.append(dupla)
    return codigo


def bifido_inv_1(matriz, cadena):
    numeros = []
    for a in cadena:
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                if a == matriz[i][j]:
                    numeros.append(i)
                    numeros.append(j)
    return numeros


def bifido_inv(clave, palabra):
    base = matriz_clave(clave)
    if type(base) != list:
        return base
    a = bifido_inv_1(base, palabra)
    b = bifido_paso_inv_1(a)
    c = bifido_paso_3(base, b)
    return c


