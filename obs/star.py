sff = None


def get(sff, key):
    stern = {
        "UP": returnArray(sff, key, False, True, -1),
        "DOWN": returnArray(sff, key, False, True, 1),

        "LEFT": returnArray(sff, key, True, False, -1),
        "RIGHT": returnArray(sff, key, True, False, 1),

        "UP-RIGHT": returnArrayQuer(sff, key, True, 1, True, -1),
        "UP-LEFT": returnArrayQuer(sff, key, True, -1, True, -1),

        "DOWN-RIGHT": returnArrayQuer(sff, key, True, 1, True, 1),
        "DOWN-LEFT": returnArrayQuer(sff, key, True, -1, True, 1)
    }
    return stern


# Key Middle Position
# moveX ob x Verschoben werden soll - bol
# moveY ob Y Verschoben werden soll - bol
# pos Ob Positiv oder Negativ gerechnet werden soll. - bol -> true positiv
def returnArray(sff, key, moveX, moveY, pos):
    x = int(key[0])
    y = int(key[1])

    ar = []
    index = 2
    while index >= 0:
        if moveX:
            x += pos
        if moveY:
            y += pos

        ar.append(sff.get(str(x) + str(y)))
        index -= 1
    return ar


def returnArrayQuer(sff, key, moveX, posX, moveY, posY):
    x = int(key[0])
    y = int(key[1])

    ar = []
    index = 2
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
