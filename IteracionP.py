import re
import math
from functions.func import createTable, evaluate
print("Introduce tu ecuacion \nFormato: Ax2+Bx+C")
a = input()
cn = re.compile("[+-]")
fn = {}
cu = ["d", "x", "c"]
if a[0] != "-":
    d = list(a)
    d.insert(0, "+")
    a = "".join(d)
op = cn.findall(a)
ts = re.split("[+-]", a)
if a[0] != "-" and len(ts) > 4:
    print("El formato de la ecuacion es incorrfnta")
elif a[0] == "-" and len(ts) <= 4:
    id = 0
    ts.pop(0)
    for i in ts:
        if i[0] == "x":
            i = "1x"
        if i.find("x") != -1:
            i = i[0:i.index("x")]
            fn[cu[id]] = int(f"{op[id]}{i}")
        else:
            if id == 1:
                fn["x"] = int(f"0")
                fn["c"] = int(f"{op[id]}{i}")
                id += 1
            else:
                fn[cu[id]] = int(f"{op[id]}{i}")
        id += 1
    if id == 2:
        fn["c"] = int(f"0")
elif a[0] == "+" and len(ts) <= 4:
    id = 0
    ts.pop(0)
    for i in ts:
        if i[0] == "x":
            i = "1x"
        if i.find("x") != -1:
            i = i[0:i.index("x")]
            fn[cu[id]] = int(f"{op[id]}{i}")
        else:
            if id == 1:
                fn["x"] = int(f"0")
                fn["c"] = int(f"{op[id]}{i}")
                id += 1
            else:
                fn[cu[id]] = int(f"{op[id]}{i}")
        id += 1
    if id == 2:
        fn["c"] = int(f"0")
else:
    print("El formato de la ecuacion es incorrecta")
ers = (fn["x"] * fn["x"]) + (-4 * fn["d"] * fn["c"])
frs = ((-1 * fn["x"]) + (math.sqrt(ers))) / (2 * fn["d"])
srs = ((-1 * fn["x"]) - (math.sqrt(ers))) / (2 * fn["d"])
p = max(round(frs, 5), round(srs, 5))
n = min(round(frs, 5), round(srs, 5))
bp = 0
while bp < p:
    bp += 1
ap = bp - 1
# Evaluacion de la segunda raiz
arp = [{
    "a":
    ap,
    "fa":
    round((fn["d"] * (ap * ap)) + (fn["x"] * ap) + (fn["c"]), 5),
    "b":
    bp,
    "fb":
    round((fn["d"] * (bp * bp)) + (fn["x"] * bp) + (fn["c"]), 5),
    "xo":
    round(
        ap + (((ap - bp) * (round(
            (fn["d"] * (ap * ap)) + (fn["x"] * ap) + (fn["c"]), 5))) / ((round(
                (fn["d"] *
                 (bp * bp)) + (fn["x"] * bp) + (fn["c"]), 5)) - (round(
                     (fn["d"] * (ap * ap)) + (fn["x"] * ap) + (fn["c"]), 5)))),
        5),
    "fxo":
    round((fn["d"] * ((round(
        ap + (((ap - bp) * (round(
            (fn["d"] * (ap * ap)) + (fn["x"] * ap) + (fn["c"]), 5))) / ((round(
                (fn["d"] *
                 (bp * bp)) + (fn["x"] * bp) + (fn["c"]), 5)) - (round(
                     (fn["d"] * (ap * ap)) + (fn["x"] * ap) +
                     (fn["c"]), 5)))), 5)) * (round(
                         ap + (((ap - bp) * (round(
                             (fn["d"] * (ap * ap)) + (fn["x"] * ap) +
                             (fn["c"]), 5))) / ((round(
                                 (fn["d"] * (bp * bp)) + (fn["x"] * bp) +
                                 (fn["c"]), 5)) - (round(
                                     (fn["d"] * (ap * ap)) + (fn["x"] * ap) +
                                     (fn["c"]), 5)))), 5)))) +
          (fn["x"] * (round(
              ap + (((ap - bp) * (round(
                  (fn["d"] * (ap * ap)) + (fn["x"] * ap) + (fn["c"]), 5))) /
                    ((round((fn["d"] * (bp * bp)) + (fn["x"] * bp) +
                            (fn["c"]), 5)) - (round(
                                (fn["d"] * (ap * ap)) + (fn["x"] * ap) +
                                (fn["c"]), 5)))), 5))) + (fn["c"]), 5),
    "rs":
    round((round((fn["d"] * (ap * ap)) + (fn["x"] * ap) + (fn["c"]), 5)) *
          (round((fn["d"] * ((round(
              ap + (((ap - bp) * (round(
                  (fn["d"] *
                   (ap * ap)) + (fn["x"] * ap) + (fn["c"]), 5))) / ((round(
                       (fn["d"] * (bp * bp)) + (fn["x"] * bp) +
                       (fn["c"]), 5)) - (round(
                           (fn["d"] * (ap * ap)) + (fn["x"] * ap) +
                           (fn["c"]), 5)))), 5)) * (round(
                               ap + (((ap - bp) * (round(
                                   (fn["d"] * (ap * ap)) + (fn["x"] * ap) +
                                   (fn["c"]), 5))) / ((round(
                                       (fn["d"] * (bp * bp)) + (fn["x"] * bp) +
                                       (fn["c"]), 5)) - (round(
                                           (fn["d"] *
                                            (ap * ap)) + (fn["x"] * ap) +
                                           (fn["c"]), 5)))), 5)))) +
                 (fn["x"] * (round(
                     ap + (((ap - bp) * (round(
                         (fn["d"] * (ap * ap)) + (fn["x"] * ap) +
                         (fn["c"]), 5))) / ((round(
                             (fn["d"] * (bp * bp)) + (fn["x"] * bp) +
                             (fn["c"]), 5)) - (round(
                                 (fn["d"] * (ap * ap)) + (fn["x"] * ap) +
                                 (fn["c"]), 5)))), 5))) + (fn["c"]), 5)), 5)
}]
ev = evaluate(ap, bp, fn)
arp.append(ev)
while ev["xo"] != p:
    if ev["rs"] > 0:
        ev["a"] = ev["xo"]
    else:
        ev["b"] = ev["xo"]
    ev = evaluate(ev["a"], ev["b"], fn)
    arp.append(ev)
an = 0
while an > n:
    an -= 1
bn = an + 1
#Evaluacion de la primera raiz
arn = [{
    "a":
    an,
    "fa":
    round((fn["d"] * (an * an)) + (fn["x"] * an) + (fn["c"]), 5),
    "b":
    bn,
    "fb":
    round((fn["d"] * (bn * bn)) + (fn["x"] * bn) + (fn["c"]), 5),
    "xo":
    round(
        an + (((an - bn) * (round(
            (fn["d"] * (an * an)) + (fn["x"] * an) + (fn["c"]), 5))) / ((round(
                (fn["d"] *
                 (bn * bn)) + (fn["x"] * bn) + (fn["c"]), 5)) - (round(
                     (fn["d"] * (an * an)) + (fn["x"] * an) + (fn["c"]), 5)))),
        5),
    "fxo":
    round((fn["d"] * ((round(
        an + (((an - bn) * (round(
            (fn["d"] * (an * an)) + (fn["x"] * an) + (fn["c"]), 5))) / ((round(
                (fn["d"] *
                 (bn * bn)) + (fn["x"] * bn) + (fn["c"]), 5)) - (round(
                     (fn["d"] * (an * an)) + (fn["x"] * an) +
                     (fn["c"]), 5)))), 5)) * (round(
                         an + (((an - bn) * (round(
                             (fn["d"] * (an * an)) + (fn["x"] * an) +
                             (fn["c"]), 5))) / ((round(
                                 (fn["d"] * (bn * bn)) + (fn["x"] * bn) +
                                 (fn["c"]), 5)) - (round(
                                     (fn["d"] * (an * an)) + (fn["x"] * an) +
                                     (fn["c"]), 5)))), 5)))) +
          (fn["x"] * (round(
              an + (((an - bn) * (round(
                  (fn["d"] * (an * an)) + (fn["x"] * an) + (fn["c"]), 5))) /
                    ((round((fn["d"] * (bn * bn)) + (fn["x"] * bn) +
                            (fn["c"]), 5)) - (round(
                                (fn["d"] * (an * an)) + (fn["x"] * an) +
                                (fn["c"]), 5)))), 5))) + (fn["c"]), 5),
    "rs":
    round((round((fn["d"] * (an * an)) + (fn["x"] * an) + (fn["c"]), 5)) *
          (round((fn["d"] * ((round(
              an + (((an - bn) * (round(
                  (fn["d"] *
                   (an * an)) + (fn["x"] * an) + (fn["c"]), 5))) / ((round(
                       (fn["d"] * (bn * bn)) + (fn["x"] * bn) +
                       (fn["c"]), 5)) - (round(
                           (fn["d"] * (an * an)) + (fn["x"] * an) +
                           (fn["c"]), 5)))), 5)) * (round(
                               an + (((an - bn) * (round(
                                   (fn["d"] * (an * an)) + (fn["x"] * an) +
                                   (fn["c"]), 5))) / ((round(
                                       (fn["d"] * (bn * bn)) + (fn["x"] * bn) +
                                       (fn["c"]), 5)) - (round(
                                           (fn["d"] *
                                            (an * an)) + (fn["x"] * an) +
                                           (fn["c"]), 5)))), 5)))) +
                 (fn["x"] * (round(
                     an + (((an - bn) * (round(
                         (fn["d"] * (an * an)) + (fn["x"] * an) +
                         (fn["c"]), 5))) / ((round(
                             (fn["d"] * (bn * bn)) + (fn["x"] * bn) +
                             (fn["c"]), 5)) - (round(
                                 (fn["d"] * (an * an)) + (fn["x"] * an) +
                                 (fn["c"]), 5)))), 5))) + (fn["c"]), 5)), 5)
}]
evn = evaluate(an, bn, fn)
arn.append(evn)
while evn["xo"] != n:
    if evn["rs"] > 0:
        evn["a"] = evn["xo"]
    else:
        evn["b"] = evn["xo"]
    evn = evaluate(evn["a"], evn["b"], fn)
    arn.append(evn)
print("Primera raiz")
createTable(arn)
print("Segunda raiz")
createTable(arp)