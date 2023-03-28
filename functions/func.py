def createTable(result: list):
    v = 1

    print(
        "|  Vuelta  |     a     |     b     |    f(a)   |    f(b)   |     x0    |   f(x0)   | f(a)*f(x0)|"
    )
    for i in result:
        vs = ""
        if v < 10:
            vs = " "
        print(
            f'|    {v} {vs}   |{getStr(str(i["a"]))[0]}{i["a"]}{getStr(str(i["a"]))[1]}|{getStr(str(i["b"]))[0]}{i["b"]}{getStr(str(i["b"]))[1]}|{getStr(str(i["fa"]))[0]}{i["fa"]}{getStr(str(i["fa"]))[1]}|{getStr(str(i["fb"]))[0]}{i["fb"]}{getStr(str(i["fb"]))[1]}|{getStr(str(i["xo"]))[0]}{i["xo"]}{getStr(str(i["xo"]))[1]}|{getStr(str(i["fxo"]))[0]}{i["fxo"]}{getStr(str(i["fxo"]))[1]}|{getStr(str(i["rs"]))[0]}{i["rs"]}{getStr(str(i["rs"]))[1]}|'
        )

        v += 1

    print(f'Raiz: {result[v-2]["xo"]}')


def evaluate(ap: float, bp: float, fn: dict):
    fap = round((fn["d"] * (ap * ap)) + (fn["x"] * ap) + (fn["c"]), 5)
    fbp = round((fn["d"] * (bp * bp)) + (fn["x"] * bp) + (fn["c"]), 5)
    xo = round(ap + (((ap - bp) * fap) / (fbp - fap)), 5)
    fxo = round((fn["d"] * (xo * xo)) + (fn["x"] * xo) + (fn["c"]), 5)
    axo = round(fap * fxo, 5)
    return {
        "a": ap,
        "fa": fap,
        "b": bp,
        "fb": fbp,
        "xo": xo,
        "fxo": fxo,
        "rs": axo
    }

def evaluateB(ap: float, bp: float, fn: dict):
    fap = round((fn["d"] * (ap * ap)) + (fn["x"] * ap) + (fn["c"]), 5)
    fbp = round((fn["d"] * (bp * bp)) + (fn["x"] * bp) + (fn["c"]), 5)
    xo = round(((ap) + (bp)) / 2, 5)
    fxo = round((fn["d"] * (xo * xo)) + (fn["x"] * xo) + (fn["c"]), 5)
    axo = round(fap * fxo, 5)
    return {
        "a": ap,
        "fa": fap,
        "b": bp,
        "fb": fbp,
        "xo": xo,
        "fxo": fxo,
        "rs": axo
    }

def getStr(st: str):
    sap = ""
    sat = ""
    if len(st) == 8:
        sap = " "
        sat = "  "
    elif len(st) == 7:
        sap = "  "
        sat = "  "
    elif len(st) == 6:
        sap = "   "
        sat = "  "
    elif len(st) == 5:
        sap = "   "
        sat = "   "
    elif len(st) == 4:
        sap = "    "
        sat = "   "
    elif len(st) == 3:
        sap = "    "
        sat = "    "
    elif len(st) == 2:
        sap = "     "
        sat = "    "
    elif len(st) == 1:
        sap = "     "
        sat = "     "

    return [sap, sat]
