from numeroEntero import numeroEntero

if __name__ == '__main__':
    numero1 = int(input("Primer numero: "))
    numero2 = int(input("Segundo numero: "))

    operacion = numeroEntero()
    print(f"MCD de {numero1} y {numero2} es {operacion.MCD(numero1,numero2)}")