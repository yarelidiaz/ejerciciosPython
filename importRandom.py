import random

def adivina_el_numero(x):
    print("====================================================================")
    print("Bienvenido al juego")
    print("====================================================================")

    print("tu meta es adivinar el numero generado por la computadora.")

    numero_aleatorio = random.randint(1,x)

    prediccion = 0
    while prediccion != numero_aleatorio:
    #el usuario ingresa un numero entre 1 y [x]:"))#f-string
        if prediccion> numero_aleatorio:
            print("intenta otra vezz.este numero es muy pequeño.")

        elif prediccion> numero_aleatorio:
            print("intenta otra vez. este numero es muy grande.")
            print(f"¡felicitaciones adivinaste el numero)[numero_aleatorio]correctamente!")

adivina_el_numero(100)