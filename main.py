from obs.SmartFastField import SmartFastField
import bot
sff = SmartFastField()
running = True
isbot = False


def printField():
    i = 1
    while i <= sff.fieldY:
        print(buildString(i))
        i += 1


def buildString(y):
    s = f""
    i = 1
    while i <= sff.fieldX:
        wert = sff.get(str(i) + str(y))
        if wert == 1:
            s += f"O\t"
        elif wert == 2:
            s += f"X\t"
        else:
            s += f"_\t"

        i += 1
    return s


try:
    print("Mit Bot? (True/False)")
    withBot = bool(input())
    isbot = withBot
except:
    print("FEHLER: Spielt startet ohne Bot")

playerValue = 1
while running:
    printField()
    if sff.isWon:
        print("Das Spiel ist zu ende! ")
        break

    if isbot and playerValue == 2:
        if playerValue == 2:
            print("BOT TURN")
            mostLikedField = bot.mostLikedField(sff)
            sff.insert(mostLikedField, playerValue)
            playerValue = 1
    else:
        print("Die Zeile (oder 'exit'):")
        inp = input()
        if inp == "exit":
            running = False
            break
        else:
            row = int(inp)
            bol = sff.insertIntoRow(row, playerValue)

            if (bol):
                if playerValue == 1:
                    playerValue = 2
                elif playerValue == 2:
                    playerValue = 1
                else:
                    print("ERROR")
            else:
                print("Die Zeile ist voll!")

