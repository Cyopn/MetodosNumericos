xo = []
a = int(input("Introduce la cantidad de intervalos a ingresar\n"))
if a < 3:
    print("Debes ingresar al menos tres intervalos")
else:
    i = 1
    while i <= a:
        xo.append(int(input(f"Introduce el valor en el intervalo {i}\n")))
        i += 1

    b = int(input("Introduce el intervalo a obtener la razon de cambio\n"))

    if (b + 2) <= a:
        r = ((-3 * xo[b - 1]) + (4 * xo[b]) - (xo[b + 1])) / 2
        print(f"Progresiva: {r}")
    elif (b - 2) > 0:
        r = ((xo[b - 3]) - (4 * xo[b - 2]) + (3 * xo[b - 1])) / 2

        print(f"Regresiva: {r}")
    else:
        print("El intervalo a obtener esta fuera de rango")