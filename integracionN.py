from sympy import *

x, y, z = symbols("x y z")

ecs = "x**2"
ec = input("Ingresa la integral a evaluar\n")
a = int(input("Ingresa el punto 'a'\n"))
b = int(input("Ingresa el punto 'b'\n"))
n = int(input("Ingresa el numero de vueltas\n"))

dx = (b - a) / n
xi = []
i = 0
while i <= n:
    xi.append(a + (i * dx))
    i += 1

xj = []
i = 1
o = int(input("Selecciona una opcion: \n1-.Rectangulo     2-. Trapecio\n"))

if o == 1:
    while i <= n:
        xj.append((xi[i - 1] + xi[i]) / 2)
        i += 1
    rs = 0
    i = 0
    while i < len(xj):
        rs += sympify(ec).subs(x, xj[i])
        i += 1
    print(f"El resultado por el metodo del rectangulo es: {round(rs*dx, 5)}")
elif o == 2:
    rs = 0
    i = 0
    while i < len(xi):
        if i == 0:
            rs += sympify(ec).subs(x, xi[i])
        elif i == len(xi) - 1:
            rs += sympify(ec).subs(x, xi[i])
        else:
            rs += sympify(ec).subs(x, xi[i]) * 2
        i += 1

    print(f"El resultado por el metodo del rectangulo es: {round(rs*(dx/2), 5)}")
