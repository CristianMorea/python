#uso de funciones de orden superior: map,   filter, reduce
from math import factorial
from functools import reduce

def calcular_termino(x, n):
    return (x**n) / factorial(n)

def obtener_terminos(num_terminos, x):
    return map(lambda n: calcular_termino(x, n), range(num_terminos))

def sumar_terminos(terminos):
    return reduce(lambda a, b: a + b, terminos)

def main():
    num_terminos = int(input("Ingrese el numero de terminos que desea: "))
    x = float(input("Ingrese el valor de x: "))
    
    terminos = obtener_terminos(num_terminos, x)
    resultado = sumar_terminos(terminos)
    
    print(f"El resultado para e es: {resultado}")
    
main()
