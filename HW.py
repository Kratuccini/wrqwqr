import math

print ('ax^2 + bx + c = 0')

a = float(input('Ingrese un valor para "a": '))
b = float(input('Ingrese un valor para "b": '))
c = float(input('Ingrese un valor para "c": '))

raiz = b ** 2 - 4 * a * c

def raiz_cuadrada(raiz):
    if raiz < 0:
        return math.sqrt(-raiz)
    return math.sqrt(raiz)

raiz__ = raiz_cuadrada(raiz)

x1 = ( -(b) - raiz__ ) / ( 2 * a )
x2 = ( -(b) + raiz__ ) / ( 2 * a )

print (f'El valor de "X1" es: {x1:.3f}')
print (f'El valor de "X2" es: {x2:.3f}')
