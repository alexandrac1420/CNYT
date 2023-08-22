# Libreria de números complejos
# Alexandra Cortes

import math
def sum_complex(a,b):
    suma_real = a[0]+b[0]
    suma_imag = a[1]+b[1]
    return (suma_real, suma_imag)

def mult_complex(a,b):
    mult_real = (a[0]*b[0])-(a[1]*b[1])
    mult_imag = (a[0]*b[1])+(a[1]*b[0])
    return (mult_real, mult_imag)

def div_complex(a,b):
    divis = ((b[0]**2)+(b[1]**2))
    if divis != 0:
        div_real = ((a[0]*b[0])+(a[1]*b[1]))/ divis
        div_imag = ((b[0]*a[1])-(a[0]*b[1]))/divis
        return (div_real, div_imag)
    else:
        raise Exception ("No es valido, su divisor es igual a 0")

def res_complex(a,b):
    resta_real = a[0] - b[0]
    resta_imag = a[1] - b[1]
    return (resta_real, resta_imag)

def modu_complex(a):
    modulo = ((a[0]**2)+(a[1]**2))**(1/2)
    return modulo

def conju_complex(a):
    conjugado = (a[0],-a[1])
    return conjugado

def cart_to_polar(a):
    modulo = ((a[0]**2)+(a[1]**2))**(1/2)
    fase = math.atan2(a[1],a[0])
    return (modulo, fase)

def polar_to_cart(c):
    a = c[0]*math.cos(c[1])
    b = c[0]*math.sin(c[1])
    return (a,b)

def fase_complex(a):
    fase = math.atan2(a[1], a[0])
    return fase

