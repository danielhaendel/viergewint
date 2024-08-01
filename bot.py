from obs import SmartFastField
from obs import star


def getPlayableFields(sff):
    columnCount = sff.fieldX
    playableFields = []

    while columnCount >= 1:
        rowCount = sff.fieldY
        while rowCount >= 1:
            key = (str(columnCount) + str(rowCount))
            if sff.get(key) == 0:
                playableFields.append(key)
                break
            else:
                rowCount -= 1

        columnCount -= 1

    return playableFields

def generateStarList(sff, fields):
    stars = []
    for field in fields:
        sta = star.Star(sff, field, star.get(sff, field))
        stars.append(sta)
    return stars


def mostLikedField(sff):
    pointsList = {}
    myValue = 2
    gegnerValue = 1
    stars = generateStarList(sff, getPlayableFields(sff))
    for bigStar in stars:  # Geht alle Möglichen Felder durch
        key = bigStar.key
        star = bigStar.star

        points = 0
        for name, ar in star.items():  # Geht alle Felder in Umgebung durch
            # Möglicher Sieg
            if ar[0] == myValue and ar[1] == myValue and ar[2] == myValue:
                points += 15

            # Generischer möglicher Sieg
            if ar[0] == gegnerValue and ar[1] == gegnerValue and ar[2] == gegnerValue:
                points += 13


            # Gegner Blockt feld mit 2
            if (ar[0] == gegnerValue and ar[1] == gegnerValue) or (ar[1] == gegnerValue and ar[2] == gegnerValue):
                points -= 4
            elif ar[0] == gegnerValue or ar[1] == gegnerValue or ar[2] == gegnerValue: # Gegner Blockt feld mit 1
                points -= 2


            # 2 Steine in Folge # MAX 5
            if (ar[0] == myValue and ar[1] == myValue) or (ar[1] == myValue and ar[2] == myValue):
                points += 5
            elif ar[0] == myValue or ar[1] == myValue or ar[2] == myValue:     # 1 Stein in Folge
                points += 4

            # Alles leer
            if ar[0] == 0 or ar[1] == 0 or ar[2] == 0: # MAX 3 min 0
                if ar[0] == 0:
                    points += 1
                if ar[1] == 0:
                    points += 1
                if ar[2] == 0:
                    points += 1

            print()

        pointsList[key] = points

    mostLikedKey = ""
    points = 0
    for key, p in pointsList.items():
        if mostLikedKey == "":
            mostLikedKey = key
            points = p
        else:
            if points < p:
                mostLikedKey = key
                points = p

    return mostLikedKey
