class Fraccion:

    def __init__(self, numerador, denominador):
        self.num = numerador
        self.den = denominador

    def __str__(self):
        return f'{self.num}/{self.den}'
    
    def __add__(self, otro):
        if type(otro) != Fraccion:
            raise ValueError('Solo se puede sumar una Fraccion')
        if self.den == 0 or otro.den == 0:
            raise ValueError('El denominador de la fraccion no debe ser 0')
        return self.sumar_fraccion(otro)
    

    def sumar_fraccion(self, otro):
        if self.den != otro.den:
            nuevoDen = self.den * otro.den
            nuevoNum = self.num * otro.den + self.den * otro.num
        else:
            nuevoNum = self.num + otro.num
            nuevoDen = self.den
        return Fraccion(nuevoNum, nuevoDen)


print(Fraccion(3,5) + Fraccion(4,3))
print(Fraccion(29,15))

assert Fraccion(3, 5) + Fraccion(4, 3) == Fraccion(29, 15)
assert Fraccion(1, 2) + Fraccion(1, 4) == Fraccion(6, 8)
assert Fraccion(1, 3) + Fraccion(2, 4) == Fraccion(10, 12)

print("Todo Ok!")