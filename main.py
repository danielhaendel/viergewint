from obs.SmartFastField import SmartFastField

sff = SmartFastField()

def printAll():
    i = 1
    while i <= sff.fieldY:
        print(buildString(i))
        i += 1


def buildString(y):
   s = f""
   i = 1
   while i <= sff.fieldX:
       s += f"{sff.get(str(i) + str(y))}\t"
       i += 1
   return s

sff.insert("12", 1)
sff.insert("35", 1)

sff.get("36")

printAll()