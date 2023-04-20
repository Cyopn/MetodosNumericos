import functions.func as f
import re

print("Introduce tus ecuaciones \nFormato: Ax+By+Cz=D")
id = 1
ec = []
while id <= 3:
    print(f"Ecuacion numero {id}")
    a = input()
    ec.append(a)
    id += 1
sm = re.compile("[+-=]")
ig = re.compile("[xyz]")
fe = []
fc = []
gbe = []
for a in ec:
    b = a.split("=")
    fe.append(b[0])
for a in ec:
    b = a.split("=")
    fc.append(int(b[1]))
for a in fe:
    if a[0] != "-":
        d = list(a)
        d.insert(0, "+")
        a = "".join(d)
    im = sm.findall(a)
    ii = ig.findall(a)
    for i in im:
        try:
            b = int(i)
            im.remove(i)
        except Exception as e:
            pass
    i = 0
    j = 0
    sfe = [0, 0, 0]
    while len(ii) > 0:
        if len(a[a.find(im[i]):a.find(ii[i]) + 1]) <= 2:
            if ii[i] == "x":
                sfe[0] = int(f"{im[i]}1")
            elif ii[i] == "y":
                sfe[1] = int(f"{im[i]}1")
            elif ii[i] == "z":
                sfe[2] = int(f"{im[i]}1")
            else:
                sfe[j] = 0
        else:
            if ii[i] == "x":
                sfe[0] = int(a[a.find(im[i]):a.find(ii[i])])
            elif ii[i] == "y":
                sfe[1] = int(a[a.find(im[i]):a.find(ii[i])])
            elif ii[i] == "z":
                sfe[2] = int(a[a.find(im[i]):a.find(ii[i])])
            else:
                sfe[j] = 0
        j += 1
        c = list(a)
        c.remove(im[i])
        im.remove(im[i])
        c.remove(ii[i])
        ii.remove(ii[i])
        a = "".join(c)
    gbe.append(sfe)

r=f.matriz_inversa(gbe, fc)

print("Matriz resultante")
for i in range(len(r[0])):
     print(r[0][i])
     
print("Solucion:")
print(f"x= {r[1][0][0]}")
print(f"y= {r[1][1][0]}")
print(f"z= {r[1][2][0]}")