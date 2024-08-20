sff = None


def get(sff, key):
    centralUP = returnArray(sff, key, False, True, -1, 1)
    centralUP.append(returnSingle(sff, key, False, True, 1))

    centralDOWN = returnArray(sff, key, False, True, 1, 1)
    centralDOWN.append(returnSingle(sff, key, False, True, -1))

    centralLEFT = returnArray(sff, key, True, False, -1, 1)
    centralLEFT.append(returnSingle(sff, key, True, False, 1))

    centralRIGHT = returnArray(sff, key, True, False, 1, 1)
    centralRIGHT.append(returnSingle(sff, key, True, False, -1))

    centralUPRIGHT = returnArrayQuer(sff, key, True, 1, True, -1, 1)
    centralUPRIGHT.append(returnQuerSingle(sff, key, True, -1, True, 1))

    centralUPLEFT = returnArrayQuer(sff, key, True, -1, True, -1, 1)
    centralUPLEFT.append(returnQuerSingle(sff, key, True, 1, True, 1))

    centralDOWNRIGHT = returnArrayQuer(sff, key, True, 1, True, 1, 1)
    centralDOWNRIGHT.append(returnQuerSingle(sff, key, True, -1, True, -1))

    centralDOWNLEFT = returnArrayQuer(sff, key, True, -1, True, 1, 1)
    centralDOWNLEFT.append(returnQuerSingle(sff, key, True, 1, True, -1))
    stern = {
        "UP": returnArray(sff, key, False, True, -1),
        "DOWN": returnArray(sff, key, False, True, 1),

        "LEFT": returnArray(sff, key, True, False, -1),
        "RIGHT": returnArray(sff, key, True, False, 1),

        "UP-RIGHT": returnArrayQuer(sff, key, True, 1, True, -1),
        "UP-LEFT": returnArrayQuer(sff, key, True, -1, True, -1),

        "DOWN-RIGHT": returnArrayQuer(sff, key, True, 1, True, 1),
        "DOWN-LEFT": returnArrayQuer(sff, key, True, -1, True, 1),

        "CENTRAL-UP": centralUP,
        "CENTRAL-DOWN": centralDOWN,

        "CENTRAL-LEFT": centralLEFT,
        "CENTRAL-RIGHT": centralRIGHT,

        "CENTRAL-UP-RIGHT": centralUPRIGHT,
        "CENTRAL-UP-LEFT": centralUPLEFT,

        "CENTRAL-DOWN-RIGHT": centralDOWNRIGHT,
        "CENTRAL-DOWN-LEFT": centralDOWNLEFT


    }
    return stern




def returnSingle(sff, key, moveX, moveY, pos):
    x = int(key[0])
    y = int(key[1])

    if moveX:
        x += pos
    if moveY:
        y += pos

    return sff.get(str(x) + str(y))

def returnQuerSingle(sff, key, moveX, posX, moveY, posY):
    x = int(key[0])
    y = int(key[1])

    if moveX:
        x += posX
    if moveY:
        y += posY

    return sff.get(str(x) + str(y))

# Key Middle Position
# moveX ob x Verschoben werden soll - bol
# moveY ob Y Verschoben werden soll - bol
# pos Ob Positiv oder Negativ gerechnet werden soll. - bol -> true positiv
def returnArray(sff, key, moveX, moveY, pos, index=2):
    x = int(key[0])
    y = int(key[1])

    ar = []
    while index >= 0:
        if moveX:
            x += pos
        if moveY:
            y += pos

        ar.append(sff.get(str(x) + str(y)))
        index -= 1
    return ar


def returnArrayQuer(sff, key, moveX, posX, moveY, posY, index=2):
    x = int(key[0])
    y = int(key[1])

    ar = []
    while index >= 0:
        if moveX:
            x += posX
        if moveY:
            y += posY

        ar.append(sff.get(str(x) + str(y)))
        index -= 1
    return ar


class Star:
    def __init__(self, sff, key, star):
        self.sff = sff
        self.key = key
        self.star = star
