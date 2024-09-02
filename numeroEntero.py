class numeroEntero:

    def MCD(self, a, b):
        x = abs(a)
        y = abs(b)

        while y != 0:
            remainder = x % y
            x = y
            y = remainder
        return x

    def MCM(self, a, b):
        # MCDM*MCM = a*b
        return a * b / self.MCD(a, b)


if __name__ == '__main__':
    numero1 = int(input("Primer número: "))
    numero2 = int(input("Segundo número: "))

    operacion = numeroEntero()
    print(f"MCD de {numero1} y {numero2} es {operacion.MCD(numero1, numero2)}")
