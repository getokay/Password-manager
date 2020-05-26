import cifrar_v2
import random

def menu():
    opcion = input("""¿Que desea hacer?
a) Agregar password a la lista.
b) Leer password especifica.
c) Actualizar paasword.
d) Ver lista entera.
e) Generar password random.
Presiones enter para salir.
""")
    return opcion


def agregar(pagina, contrasena):
    texto = open(r"D:\Programas\Pass\contras.txt", "a")
    cifrado = cifrar_v2.bifido("Murcielago", contrasena)
    texto.write(" "+pagina + " " + cifrado + " ")
    texto.close()
    print("Se ha agregado la password %s para la cuenta %s" % (contrasena, pagina))


def leer(pagina):
    archivo = open(r"D:\Programas\Pass\contras.txt")
    texto = archivo.read()
    lista_1 = texto.split()
    contra = 0
    for i in lista_1:
        if i == pagina:
            contra = cifrar_v2.bifido_inv("Murcielago", lista_1[lista_1.index(i) + 1])
            break
    if type(contra) != str:
        print("No se pudo encontrar la password. Revise la lista completa ante una duda.\n")
    else:
        print("Su password es: %s\n" % contra)


def modificar(pagina):
    archivo = open(r"D:\Programas\Pass\contras.txt")
    texto = archivo.read()
    lista_2 = texto.split()
    archivo.close()
    cambio = False
    for i in lista_2:
        if i == pagina:
            lista_2[lista_2.index(i) + 1] = cifrar_v2.bifido("Murcielago", input("Ingrese la nueva password: "))
            cambio = True
            break
    if not cambio:
        print("No se a encontrado la vieja password.")
    archivo = open(r"D:\Programas\Pass\contras.txt", "w")
    archivo.write(" ".join(lista_2))
    archivo.close()


def lista():
    archivo = open(r"D:\Programas\Pass\contras.txt")
    texto = archivo.read()
    lista_3 = texto.split()
    par = []
    conteo = 0
    for i in lista_3:
        par.append(i)
        conteo += 1
        if conteo == 2:
            par[1] = cifrar_v2.bifido_inv("Murcielago", par[1])
            print("   ".join(par))
            par = []
            conteo = 0
    archivo.close()


def generador():
    abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", 'g', "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
           "s", "t", "u", "v",
           "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-", "_"]
    password = ""
    a = ""
    while type(a) != int:
        a = abs(int(input("Ingrese el largo de la password: ")))

    for i in range(a):
        password += random.choice(abc)
    return password


while True:
    b = input("Ingrese la pass global:\t")
    if b == "13121999":
        break
a = " "
while a != "":
    a = menu()
    if a == "a":
        agregar(input("Usuario/pagina: "),input("Contra a usar: "))
    elif a == "b":
        leer(input("Ingrese el usuario/pagina del cual desea leer la password: "))
    elif a == "c":
        modificar(input("Ingrese el usuario/pagina al que desea cambiar la contra"))
    elif a == "d":
        lista()
    elif a == "e":
        print(generador())
