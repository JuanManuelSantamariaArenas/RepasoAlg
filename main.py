#REPASO DE CLASE

def repaso_1():
    import random

    print("Punto #1")
    print("Hi World :P")

    print("Punto #2")
    n = int(input("Ingrese un número entero: "))
    print(f" El numero ingresado fue {n}")

    print("Punto #3")
    n1 = random.randrange(0, 10, 1)
    n2 = random.randrange(0, 10, 1)
    suma = n1 + n2
    print(f"#1 = {n1} y #2 = {n2}, las suma de los dos numero es {suma}")

    print("Punto #4")
    nu1 = float(input("Ingrese un número real: "))
    nu2 = float(input("Ingrese otro número real: "))
    multi = nu1 * nu2
    print(f"La multiplicacion de los numeros ingresados fue {multi}")

    print("Punto #5")
    num1 = random.random()
    num2 = random.random()
    multip = num1 * num2
    print(f"La multiplicación de los numeros generados fue {multip}")

    print("Punto #6")

    print("Punto #12")

repaso_1()
