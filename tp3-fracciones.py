"""
# Primera version sin __add__

class Fraccion:

    def __init__(self, numerador, denominador):
        self.num = numerador
        self.den = denominador

    def __str__(self):
        return f'{self.num}/{self.den}'
    
    def __add__(self, otro):
        if type(otro) != Fraccion:
            raise ValueError('Solo se puede sumar un Fraccion')


def suma(fr1, fr2):
    if fr1.den != fr2.den:
        nuevoDen = fr1.den * fr2.den
        nuevoNum = fr1.num * fr2.den + fr1.den * fr2.num
    else:
        nuevoNum = fr1.num + fr2.num
        nuevoDen = fr1.den
    return Fraccion(nuevoNum, nuevoDen)

fraccion1 = Fraccion(4,2)
fraccion2 = Fraccion(2,9)
resultado = suma(fraccion1, fraccion2)

print(resultado)
"""
#assert Fraccion(2, 3) + Fraccion(1, 3) == Fraccion(3, 3)
#assert Fraccion(4, 5) + Fraccion(3, 5) == Fraccion(7, 5)
#assert Fraccion(3, 2) + Fraccion(8, 11) == Fraccion(49, 22)
