import random
import os


palabras = ["IMPRESORA", "LÁPIZ", "PARAGUAS", "JIRAFA", "TELEVISIÓN",
        "COMPUTADORA", "EXPLORADOR", "PERIÓDICO", "BICICLETA", "ZAPATILLA",
        "HORNO", "PLATILLO", "HELICÓPTERO","CUADERNO", "JUGUETE",
        "CAMIÓN", "GUITARRA", "MALETA", "ELEFANTE", "VENTILADOR"] 

palabra = list(random.choice(palabras))

horca = ["             !========|",
        "                      |",
        "                      |",
        "                      |",
        "                      |",
        "                      |",
        "                      |",
        "                      |",
        "           ___________|"]

ahorcado = ["             !========|",
            "             o        |",
            "           / | \      |",
            "           \ | /      |",
            "             |        |",
            "            / \       |",
            "          _/   \_     |",
            "                      |",
            "           ___________|"]

letras_todas = []              # Todas las letras dichas
fallos = 1                     # Contador de fallos

resultado = []                 # Lista con guiones a sustituir por letras acertadas

for i in range(len(palabra)):
    resultado.append("_")

 # Bucle principal del juego
    
while True:
    os.system("cls")

    print("***   EL JUEGO DEL AHORCADO   ***")
    print("*********************************")

    for i in range(fallos):
        print(ahorcado[i])
    for i in range(len(horca)-fallos):
        print(horca[i + fallos])

    print()

    # Mostramos el resultado que se va obteniendo

    print("    ", end = " ")
    for i in resultado:
        print(i, end = " ")

    print()
    print()

    # Comprobamos si se ha acertado la palabra o se han terminado los intentos

    if resultado == palabra:
        print(' "HAS GANADO ANASHE" ')
        break
    
    if fallos > 6:
        print("La palabra era", "".join(palabra))
        print("HAS PERDIDO BRO nt")
        break

    # Bucle para que el usuario elija una letra

    while True:
        letra_usuario_sinformato = input("Dime una letra: ")
        letra_usuario = letra_usuario_sinformato.upper()
        if len(letra_usuario) != 1:
            print("Introduce una letra")
        elif letra_usuario in letras_todas:
            print("Esa letra ya la has dicho :/")
        elif letra_usuario not in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ":
            print("Introduce una letra")
        else:
            letras_todas.append(letra_usuario)
            break

    # Comprobamos si la letra está en la palabra, si está la sustituimos por el guión.
   
    for i in range(len(palabra)):
        if palabra[i] == letra_usuario:
            resultado[i] = letra_usuario

    if letra_usuario not in palabra:
        fallos += 1

    print()
    print()



